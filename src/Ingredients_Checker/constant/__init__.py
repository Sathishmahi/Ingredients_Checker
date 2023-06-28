import time
import os
from pathlib import Path
from dataclasses import dataclass

TIME_STAMP=time.strftime(f"%Y_%m_%d_%H_%M_%S")
LOGS_DIR_NAME="running_logs"


os.makedirs(name=LOGS_DIR_NAME,exist_ok=True)
FILE_NAME=f"{TIME_STAMP}.log"
LOG_FILE_PATH=os.path.join(

    LOGS_DIR_NAME,
    FILE_NAME
    
)

CONFIG_FILE_PATH=Path('config/config.yaml')

@dataclass
class IngredientsPickerConstant:
    
    IngredientsPicker_ROOT_KEY:str="ingredient_picker"
    IngredientsPicker_NO_CLASSES_KEY:str="no_of_classes"
    IngredientsPicker_TRAINED_MODEL_PATH_KEY:str="trained_model_path"


@dataclass
class ArtifactConstant:

    ARTIFACT_ROOT_KEY:str="artifacts"
    ARTIFACT_ROOT_DIR_KEY:str="root_dir"

    