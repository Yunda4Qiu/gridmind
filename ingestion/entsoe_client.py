"""
ENTSO-E data client for GridMind.

This module handles:
- Data retrieval (API or local fallback)
- Basic validation
- Normalized output format
"""


import pandas as pd
import requests
from typing import Optional
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

class ENTSOEClient:
    """
    Lightweight ENTSO-E client focused on load time-series data.
    """

    BASE_URL = "https://web-api.tp.entsoe.eu/api"

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key

    def fetch_load(
        self,
        start: datetime,
        end: datetime,
        country_code: str = "NL"
    ) -> pd.DataFrame:
        """
        Fetch actual load data for a given country and time range.

        Returns a DataFrame with:
        - timestamp (UTC)
        - load_mw
        """

        if self.api_key is None:
            raise RuntimeError(
                "ENTSO-E API key not provided. "
                "Set it via environment variable or config."
            )

        params = {
            "securityToken": self.api_key,
            "documentType": "A65",  # Actual total load
            "processType": "A16",
            "outBiddingZone_Domain": country_code,
            "periodStart": start.strftime("%Y%m%d%H%M"),
            "periodEnd": end.strftime("%Y%m%d%H%M"),
        }

        response = requests.get(self.BASE_URL, params=params, timeout=30)
        response.raise_for_status()

        return self._parse_xml_response(response.text)

    def _parse_xml_response(self, xml_text: str) -> pd.DataFrame:
        """
        Parse ENTSO-E XML response into a normalized DataFrame.

        Output schema:
        - timestamp (UTC)
        - load_mw
        """

        root = ET.fromstring(xml_text)

        records = []

        # ENTSO-E XML uses namespaces
        ns = {"ns": root.tag.split("}")[0].strip("{")}

        for ts in root.findall("ns:TimeSeries", ns):
            period = ts.find("ns:Period", ns)
            if period is None:
                continue

            time_interval = period.find("ns:timeInterval", ns)
            start_str = time_interval.find("ns:start", ns).text

            start_time = datetime.strptime(start_str, "%Y%m%d%H%M")

            resolution = period.find("ns:resolution", ns).text
            if resolution != "PT15M":
                raise ValueError(f"Unsupported resolution: {resolution}")

            for point in period.findall("ns:Point", ns):
                position = int(point.find("ns:position", ns).text)
                quantity = float(point.find("ns:quantity", ns).text)

                timestamp = start_time + timedelta(minutes=15 * (position - 1))

                records.append(
                    {
                        "timestamp": timestamp,
                        "load_mw": quantity,
                    }
                )

        df = pd.DataFrame(records)
        df.sort_values("timestamp", inplace=True)
        df.reset_index(drop=True, inplace=True)

        return df
