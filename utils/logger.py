import os
import sys
import logging
import logging.config
import configparser
from datetime import datetime

class MaxLevelFilter(logging.Filter):
    def __init__(self, level):
        super().__init__()
        self.level = self._check_level(level)

    def filter(self, record):
        return record.levelno <= self.level

    def _check_level(self, level):
        return logging.getLevelName(level.upper()) if isinstance(level, str) else level

class MinLevelFilter(logging.Filter):
    def __init__(self, level):
        super().__init__()
        self.level = self._check_level(level)

    def filter(self, record):
        return record.levelno >= self.level

    def _check_level(self, level):
        return logging.getLevelName(level.upper()) if isinstance(level, str) else level

class SingletonLogger:
    _configured = False

    @classmethod
    def configure(cls, config_file='config/logger.ini', env_file='config/core_config.ini'):
        if cls._configured:
            return

        env_config = configparser.ConfigParser()
        env_config.read(env_file)

        current_env = env_config.get('environment', 'current')
        log_dir = env_config.get(f'logger_path_{current_env}', 'log_dir')

        os.makedirs(log_dir, exist_ok=True)

        today = datetime.now().strftime('%Y-%m-%d')
        logfilename_info = os.path.join(log_dir, f'case_info_{today}.log')
        logfilename_error = os.path.join(log_dir, f'case_error_{today}.log')

        logging_config = configparser.ConfigParser()
        with open(config_file, 'r') as f:
            logging_config.read_file(f)

        defaults = {
            'logfilename_info': logfilename_info,
            'logfilename_error': logfilename_error
        }

        logging.config.fileConfig(config_file, defaults=defaults, disable_existing_loggers=False)
        cls._configured = True

    @staticmethod
    def get_logger(name):
        return logging.getLogger(name)
