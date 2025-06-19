from utils.logger import SingletonLogger
from utils.mongo_connection import get_mongo_db

class CaseDistributor:
    def __init__(self):
        self.logger = SingletonLogger.get_logger("appLogger")

    def run(self):
        self.logger.info("CaseDistributor started processing.")

        try:
            db = get_mongo_db()
            
            # Example logic
            count = db['Case_details'].count_documents({})
            self.logger.info(f"Total documents in 'your_collection': {count}")

            # Your actual business logic here
            self.logger.debug("Running main case distribution logic.")

        except Exception as e:
            self.logger.error(f"An error occurred: {e}", exc_info=True)

        self.logger.info("CaseDistributor finished processing.")
