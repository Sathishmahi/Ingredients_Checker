import os
from pathlib import Path
from Ingredients_Checker.utils import read_yaml,make_dirs
from Ingredients_Checker.constant import (ArtifactConstant,
IngredientsPickerConstant,
UpsamplingConstant,
TextExtractorConstant)
from Ingredients_Checker.entity import IngredientsPickerConfig,UpsamplingConfig,TextExtractorConfig

class Configuration:
    def __init__(self):
        self.con=self.config_content=read_yaml()
        self.artifacts_dir_name=self.con.get(ArtifactConstant.ARTIFACT_ROOT_KEY).get(ArtifactConstant.ARTIFACT_ROOT_DIR_KEY)
        _=self.get_ingredients_picker_config()
        _=self.get_upsampling_config()
        _=self.get_text_extractor_config()



    def get_text_extractor_config(self)->TextExtractorConfig:

        text_extractor_content=self.config_content.get(TextExtractorConstant.TEXTEXTRACTOR_ROOT_KEY)
        
        root_dir=os.path.join(
            self.artifacts_dir_name,
            text_extractor_content.get(TextExtractorConstant.TEXTEXTRACTOR_ROOT_DIR_KEY)
        )

        ingredient_txt_file_name=os.path.join(
            root_dir,
            text_extractor_content.get(TextExtractorConstant.TEXTEXTRACTOR_TXT_FILE_NAME_KEY)
            )
        
        prediction_image_file_path=None

        if len(os.listdir(self.upsample_image_dir_name))>0:
            prediction_image_file_path=os.path.join(self.upsample_image_dir_name,
            os.listdir(self.upsample_image_dir_name)[0])
        
        make_dirs(dirs_list=[root_dir])
        model_lan=text_extractor_content.get(TextExtractorConstant.TEXTEXTRACTOR_MODEL_LAN_KEY)
        txt_extractor_config=TextExtractorConfig(root_dir, ingredient_txt_file_name, 
        prediction_image_file_path,model_lan)
        return txt_extractor_config
    
    def get_upsampling_config(self)->UpsamplingConfig:


        upsampling_content=self.config_content.get(UpsamplingConstant.UPSAMPLING_ROOT_KEY)
        root_dir=os.path.join(self.artifacts_dir_name,upsampling_content.get(UpsamplingConstant.UPSAMPLING_ROOT_DIR_KEY))
        model_path=upsampling_content.get(UpsamplingConstant.UPSAMPLING_MODEL_PATH_KEY)
        self.upsample_image_dir_name=os.path.join(
            root_dir,
            upsampling_content.get(UpsamplingConstant.UPSAMPLING_IMAGE_DIR_NAME_KEY))

        upsample_image_file_name=os.path.join(
            self.upsample_image_dir_name,
            upsampling_content.get(UpsamplingConstant.UPSAMPLING_IMAGE_NAME_KEY)
        )

        upsampling_config=UpsamplingConfig(root_dir, model_path, self.upsample_image_dir_name, 
        upsample_image_file_name,self.save_image_dir_name)
        make_dirs(dirs_list=[root_dir,Path(self.upsample_image_dir_name)])
        return upsampling_config

    def get_ingredients_picker_config(self)->IngredientsPickerConfig:
        

        ingredient_picker_content=self.config_content.get(IngredientsPickerConstant.IngredientsPicker_ROOT_KEY)
        root_dir=os.path.join(
            self.artifacts_dir_name,ingredient_picker_content.get(IngredientsPickerConstant.IngredientsPicker_ROOT_DIR_KEY)
        )
        no_of_classes=ingredient_picker_content.get(IngredientsPickerConstant.IngredientsPicker_NO_CLASSES_KEY)
        trained_model_path=ingredient_picker_content.get(IngredientsPickerConstant.IngredientsPicker_TRAINED_MODEL_PATH_KEY)
        self.save_image_dir_name=os.path.join(root_dir,ingredient_picker_content.get(IngredientsPickerConstant.IngredientsPicker_SAVE_DIR_KEY))
        save_image_file_name=os.path.join(
            self.save_image_dir_name,
            ingredient_picker_content.get(IngredientsPickerConstant.IngredientsPicker_SAVE_IMAGE_FILE_NAME_KEY))
        yolo_model_name=ingredient_picker_content.get(IngredientsPickerConstant.IngredientsPicker_YOLO_MODEL_NAME_KEY)

        make_dirs(dirs_list=[root_dir,self.save_image_dir_name])
        ingredients_picker_config=IngredientsPickerConfig(root_dir,no_of_classes, trained_model_path, 
        self.save_image_dir_name, save_image_file_name,yolo_model_name)

        return ingredients_picker_config
