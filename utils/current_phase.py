from datetime import datetime
from utils.mongo_connection import get_mongo_db
from utils.timezones import colombo_tz

mongo_db = get_mongo_db()

async def get_phase(case_status: str) -> str:
    """
    Returns the current active case phase for a given case_status.
    Filters where end_dtm is None or less than current datetime.
    """
    query = {
        "case_status": case_status,
        "$or": [
            {"end_dtm": None},
            {"end_dtm": {"$lt": datetime.now(colombo_tz)}}
        ]
    }

    doc = await mongo_db["Case_Phases"].find_one(query)

    if doc and "case_phase" in doc:
        return doc["case_phase"]
    else:
        return "Unknown"
