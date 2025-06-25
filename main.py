from utils.logger import SingletonLogger
from app.get_case_list import CaseDistributor
from utils.mongo_connection import MongoConnection


def main():
    SingletonLogger.configure()
    mongo_conn = MongoConnection()
    db = mongo_conn.get_database() # Ensure MongoDB connection is established
    if db is None:
        raise Exception("Failed to connect to MongoDB. Exiting application.")   
    
    
     
    distributor = CaseDistributor()
    distributor.run()

if __name__ == "__main__":
    main()





