"""
Data ingestion pipeline for GridMind.
"""

from datetime import datetime, timedelta
import os

from ingestion.entsoe_client import ENTSOEClient


def run_entsoe_ingestion():
    api_key = os.getenv("ENTSOE_API_KEY")
    client = ENTSOEClient(api_key=api_key)

    end = datetime.utcnow()
    start = end - timedelta(days=1)

    df = client.fetch_load(start=start, end=end)

    output_path = "data/raw/entsoe_load.csv"
    df.to_csv(output_path, index=False)

    print(f"ENTSO-E load data saved to {output_path}")


if __name__ == "__main__":
    run_entsoe_ingestion()
