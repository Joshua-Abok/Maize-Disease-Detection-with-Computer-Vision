import tensorflow as tf
from pathlib import Path
import mlflow
import mlflow.keras
from urllib.parse import urlparse

from src.maizeDiseaseDetection.entity.config_entity import EvaluationConfig
from src.maizeDiseaseDetection.utils.common import save_json



class Evaluation: 
    def __init__(self, config: EvaluationConfig):
        self.config = config

    
    def _valid_generator(self):
        
        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.30
        )

        dataflow_kwargs = dict(
            target_size = self.config.params_image_size[:-1], 
            batch_size=self.config.params_batch_size, 
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )


        self._valid_generator =  valid_datagenerator.flow_from_directory(
            directory=self.config.training_data, 
            subset="validation", 
            shuffle=False, 
            **dataflow_kwargs
        )



    # staticmethod decorator to load the model
    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    

    #after loading the model, now evaluate the model
    def evaluation(self): 
        self.model = self.load_model(self.config.path_of_model)
        self._valid_generator()   #generate validation dataset
        self.score = self.model.evaluate(self._valid_generator)   # evaluate model, as taking the valid_generator
                                                            # and determine some score. set the score
        self.save_score()   # calling the save_score method

    # save the score 
    def save_score(self): 
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)   # saving scores in json file


    # mlflow integration
    def log_into_mlflow(self): 
        mlflow.set_registry_uri(self.config.mlflow_uri) # uri track the server, will take the lin
        tracking_uri_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():    # start tracking the experiment
            mlflow.log_params(self.config.all_params)  # log the params from config file
            mlflow.log_metrics(
                {"loss": self.score[0], "accuracy": self.score[1]}  # log metrics loss, accuracy
            )

            # Model registry does not work with file store 
            if tracking_uri_type_store != "file":
                # Register the model 
                # There are other ways to use the Model Registry, which depends on the use case, 
                # please refer to the doc for more information: 
                mlflow.keras.log_model(self.model, "model", registered_model_name="VGG16Model")
            else: 
                mlflow.keras.log_model(self.model, "model")


                                            
