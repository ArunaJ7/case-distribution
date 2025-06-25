# from pymongo import MongoClient

# def extract_case_id_and_billing_centre(case_ids):
#     client = MongoClient("mongodb://localhost:27017")  # Update with your URI
#     db = client["your_database_name"]                 # Replace with your DB name
#     collection = db["your_collection_name"]           # Replace with your collection name

#     result = []
#     for case_id in case_ids:
#         doc = collection.find_one({"case_id": case_id})
#         if doc:
#             billing_centre = None
#             accounts = doc.get("ref_customer_account_permanent", [])
#             if accounts and isinstance(accounts, list):
#                 billing_centre = accounts[0].get("billing_centre")
#             result.append((case_id, billing_centre))
#         else:
#             result.append((case_id, None))  # In case not found

#     client.close()
#     return result


from utils.logger import SingletonLogger
from utils.mongo_connection import MongoConnection

db = MongoConnection().get_database()



class CaseDistributor:
    def __init__(self):
        self.logger = SingletonLogger.get_logger("appLogger")

    def run(self):
        self.logger.info("CaseDistributor started processing.")


    def extract_case_id_and_billing_centre(case_ids):
        db = MongoConnection().get_database()

        collection = db["Case_Details"]  #db name 

        result = []
        for case_id in case_ids:
            doc = collection.find_one({"case_id": case_id})
            if doc:
                billing_centre = None
                accounts = doc.get("ref_customer_account_permanent", [])
                if accounts and isinstance(accounts, list):
                    billing_centre = accounts[0].get("billing_centre")
                result.append((case_id, billing_centre))
            else:
                result.append((case_id, None))
        return result
