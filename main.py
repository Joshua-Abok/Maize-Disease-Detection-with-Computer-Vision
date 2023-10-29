from src.maizeDiseaseDetection import logger

# logger.info("Welcome to our custom log 2")

from src.maizeDiseaseDetection.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion stage"

try: 
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=========x")
except Exception as e: 
    logger.exception(e)
    raise e