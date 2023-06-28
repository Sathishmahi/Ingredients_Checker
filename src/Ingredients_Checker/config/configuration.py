import os
from pathlib import Path
from Ingredients_Checker.utils import read_yaml,make_dirs
from Ingredients_Checker.constant import ArtifactConstant,IngredientsPickerConstant
from Ingredients_Checker.entity import IngredientsPickerConfig

class Configuration:
    def __init__(self):
        self.con=self.config_content=read_yaml()
        self.artifacts_dir_name=self.con.get(ArtifactConstant.ARTIFACT_ROOT_KEY).get(ArtifactConstant.ARTIFACT_ROOT_DIR_KEY)
        
    def get_ingredients_picker_config(self)->IngredientsPickerConfig:
        
        ingredient_picker_content=self.config_content.get(IngredientsPickerConstant.IngredientsPicker_ROOT_KEY)
        no_of_classes=ingredient_picker_content.get(IngredientsPickerConstant.IngredientsPicker_NO_CLASSES_KEY)
        trained_model_path=ingredient_picker_content.get(IngredientsPickerConstant.IngredientsPicker_TRAINED_MODEL_PATH_KEY)

        ingredients_picker_config=IngredientsPickerConfig(no_of_classes, trained_model_path)

        return ingredients_picker_config
