from utils.mongo_connection import get_mongo_db
from utils.logger import SingletonLogger


class CaseDistributor:
    def __init__(self):
        self.logger = SingletonLogger.get_logger("appLogger")
        self.drc_rtom_mapping = self.load_drc_rtom_mapping()

    def load_drc_rtom_mapping(self):
        mapping = {}
        try:
            db = get_mongo_db()
            if db is None:
                self.logger.error("Failed to connect to MongoDB for drc_rtom_mapping.")
                return {}

            collection = db["drc_rtom_mappings"]
            cursor = collection.find({})

            for doc in cursor:
                drc_code = doc.get("drc_code")
                rtoms = doc.get("rtoms", [])
                if drc_code:
                    mapping[drc_code] = rtoms

            self.logger.debug(f"Loaded DRC-RTOM mapping: {mapping}")
        except Exception as e:
            self.logger.error(f"Error loading DRC-RTOM mapping: {e}", exc_info=True)

        return mapping

    def run(self):
        self.logger.info("CaseDistributor started processing.")
        # Now self.drc_rtom_mapping is dynamically loaded from DB
        # Use it in your logic

        try:
            self.logger.debug("Running main case distribution logic.")
            # For example
            self.logger.info(f"RTOM mapping: {self.drc_rtom_mapping}")
        except Exception as e:
            self.logger.error(f"An error occurred: {e}", exc_info=True)

        self.logger.info("CaseDistributor finished processing.")