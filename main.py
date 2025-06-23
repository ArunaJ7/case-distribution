from utils.logger import SingletonLogger
from app.get_case_list import CaseDistributor


def main():
    SingletonLogger.configure()
    distributor = CaseDistributor()
    distributor.run()

if __name__ == "__main__":
    main()
