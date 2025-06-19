import configparser
import os
import logging
from dotenv import load_dotenv
from urllib.parse import quote_plus

_config = None

# Load environment variables from .env
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

def load_config():
    # Setup logger
    try:
        from utils.logger import SingletonLogger
        logger = SingletonLogger.get_logger("appLogger")
    except Exception:
        logger = logging.getLogger("fallback_logger")
        if not logger.handlers:
            logging.basicConfig(level=logging.INFO)

    # Load .ini configuration
    config = configparser.RawConfigParser()
    ini_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'core_config.ini')
    config.read(ini_path)

    # Get environment from .env
    env = os.getenv("ENV", "development").strip().lower()

    def env_key(base):
        return f"{base.upper()}_{env.upper()}"

    mongo_user = quote_plus(os.getenv(env_key("MONGO_USERNAME")))
    mongo_pass = quote_plus(os.getenv(env_key("MONGO_PASSWORD")))
    mongo_hosts = os.getenv(env_key("MONGO_HOSTS"))
    mongo_replica = os.getenv(env_key("REPLICA_SET"), "rs0")
    mongo_db = os.getenv(env_key("DB_NAME"))

    mongo_uri = (
        f"mongodb://{mongo_user}:{mongo_pass}@{mongo_hosts}/"
        f"{mongo_db}?replicaSet={mongo_replica}&authSource=admin"
    )

    # Server config fallback
    server_section = f"server_{env}"
    host = config.get(server_section, "host", fallback="127.0.0.1")
    port = config.getint(server_section, "port", fallback=8000)

    logger_section = f"logger_path_{env}"
    log_dir = config.get(logger_section, "log_dir", fallback="/tmp/logs")

    logger.info(f"Environment loaded: {env}")

    return {
        "env": env,
        "mongo_uri": mongo_uri,
        "mongo_db": mongo_db,
        "host": host,
        "port": port,
        "log_dir": log_dir
    }

def get_config():
    global _config
    if _config is None:
        _config = load_config()
    return _config
