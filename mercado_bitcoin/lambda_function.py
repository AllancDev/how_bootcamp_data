import datetime

from ingestors import AwsDaySummaryIngestor
from writers import S3Writter

import logging

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)

def lambda_handler(event, context):
    logger.info(f"{event}")
    logger.info(f"{context}")

    AwsDaySummaryIngestor(
        writer=S3Writter,
        coins=["BTC", "ETH", "LTC", "BCH"],
        default_start_date=datetime.date(2022, 12, 1),
    ).ingest()