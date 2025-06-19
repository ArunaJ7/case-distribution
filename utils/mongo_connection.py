from pymongo import MongoClient
from utils.core_utils import get_config
import logging

def get_mongo_db():
    logger = None
    try:
        try:
            from utils.logger import SingletonLogger
            logger = SingletonLogger.get_logger("appLogger")
        except Exception:
            logger = logging.getLogger("fallback_logger")
            if not logger.handlers:
                logging.basicConfig(level=logging.INFO)

        cfg = get_config()
        mongo_uri = cfg["mongo_uri"]
        mongo_db = cfg["mongo_db"]

        logger.debug("Connecting to MongoDB...")
        logger.debug("Mongo URI: %s", mongo_uri)
        logger.debug("Mongo DB: %s", mongo_db)

        client = MongoClient(mongo_uri)
        db = client[mongo_db]

        logger.debug("Successfully connected to MongoDB.")
        return db

    except Exception as e:
        if logger:
            logger.error("Failed to connect to MongoDB: %s", str(e), exc_info=True)
        else:
            print(f"Failed to connect to MongoDB: {e}")
        raise
