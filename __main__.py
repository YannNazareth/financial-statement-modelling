from sklearn.pipeline import Pipeline

from datahandler import DataHandler
from feature_engineering import FeatureExtractor
from repository import MongoRepository
from service import FinancialStatementModellingService
from transformer import DropColumnsTransformer, DropDuplicateColumns, DropColumnNameSuffix

if __name__ == '__main__':
    # Todo: Construct dependencies somewhere else (factory?) and inject into service

    # Repository Integration
    repository = MongoRepository("feature_acceptedDate")

    # Data Handler
    datahandler = DataHandler(repository, FeatureExtractor())

    # Full Pre-Processing Transformation Pipeline
    transform_pipeline = Pipeline([
        ('drop_duplicate_columns', DropDuplicateColumns()),
        ('drop_suffixes_transformer', DropColumnNameSuffix(["_x"]))
    ])

    # Create service instance w/ injected dependencies & run
    service = FinancialStatementModellingService(datahandler, transform_pipeline)

    df = service.train_model()















