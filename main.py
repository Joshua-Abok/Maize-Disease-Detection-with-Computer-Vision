from src.maizeDiseaseDetection import logger

# logger.info("Welcome to our custom log 2")

from src.maizeDiseaseDetection.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.maizeDiseaseDetection.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.maizeDiseaseDetection.pipeline.stage_03_model_training import ModelTrainingPipeline


STAGE_NAME = "Data Ingestion stage"

try: 
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=========x")
except Exception as e: 
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model"

try: 
    logger.info(f"***********************")
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed  <<<<<<<\n\nx=============x")
except Exception as e: 
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training"

try: 
    logger.info(f"***********************")
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started")
    model_training = ModelTrainingPipeline()
    model_training.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed  <<<<<<<\n\nx=============x")
except Exception as e: 
    logger.exception(e)
    raise e