from src.maizeDiseaseDetection.config.configuration import ConfigurationManager
from src.maizeDiseaseDetection.components.model_evaluation_mlflow import Evaluation
from src.maizeDiseaseDetection import logger


# give stage name
STAGE_NAME = "model evaluation with mlflow"

class ModelEvaluationPipeline: 
    def __init__(self) -> None:
        pass

    def main(self): 
         
        config = ConfigurationManager()   #passing training config in the training
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(config=eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()   # logging experiment to mlflow
    

if __name__ == '__main__':
    try: 
        logger.info(f"***********************")
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed  <<<<<<<\n\nx=============x")
    except Exception as e: 
        logger.exception(e)
        raise e