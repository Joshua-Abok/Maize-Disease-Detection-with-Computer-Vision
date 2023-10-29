from src.maizeDiseaseDetection.config.configuration import ConfigurationManager
from src.maizeDiseaseDetection.components.model_training import Training
from src.maizeDiseaseDetection import logger


# initialize stage name 
STAGE_NAME = "Model Training"


class ModelTrainingPipeline: 
    def __init__(self) -> None:
        pass

    def main(self): 
        config = ConfigurationManager() #passing training config in the training
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()

if __name__ == "__main__":
    try: 
        logger.info(f"***********************")
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed  <<<<<<<\n\nx=============x")
    except Exception as e: 
        logger.exception(e)
        raise e