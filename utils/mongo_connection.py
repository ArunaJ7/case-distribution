from pymongo import MongoClient
from utils.core_utils import get_config
import logging

class MongoConnection:
    def __init__(self):
        self.logger = None
        try:
            from utils.logger import SingletonLogger
            self.logger = SingletonLogger.get_logger("appLogger")
        except Exception:
            self.logger = logging.getLogger("fallback_logger")
            if not self.logger.handlers:
                logging.basicConfig(level=logging.INFO)

    def get_database(self):
        try:
            cfg = get_config()
            mongo_uri = cfg["mongo_uri"]
            mongo_db = cfg["mongo_db"]

            self.logger.debug("Connecting to MongoDB...")
            self.logger.debug("Mongo URI: %s", mongo_uri)
            self.logger.debug("Mongo DB: %s", mongo_db)

            client = MongoClient(mongo_uri)
            db = client[mongo_db]

            self.logger.debug("Successfully connected to MongoDB.")
            return db

        except Exception as e:
            self.logger.error("Failed to connect to MongoDB: %s", str(e), exc_info=True)
            raise
