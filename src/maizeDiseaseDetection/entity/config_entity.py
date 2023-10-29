# entity -> written type of any function 
#            written type of data ingestion function 

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True) #decorator assigned on top of any python class so as to consider as entity
class DataIngestionConfig: 
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path                       # everything written in config.yaml file


# update entity on part 2: prepare_base_model
@dataclass(frozen=True)    # frozen=True -> don't want any changes
class PrepareBaseModelConfig: 
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool 
    params_weights: str
    params_classes: int