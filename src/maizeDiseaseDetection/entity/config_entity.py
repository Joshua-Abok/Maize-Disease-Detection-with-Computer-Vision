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