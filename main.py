from utils.logger import SingletonLogger
from app.distribution import CaseDistributor

def main():
    SingletonLogger.configure()
    distributor = CaseDistributor()
    distributor.run()

if __name__ == "__main__":
    main()
