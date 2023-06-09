from super_gradients.training import models
from Ingredients_Checker.entity import IngredientsPickerConfig
from Ingredients_Checker.config import Configuration
from pathlib import Path
from Ingredients_Checker.utils import make_dirs
import cv2


def get_bounding_box(test_image)->None:

    ingredients_picker_config=Configuration().get_ingredients_picker_config()

    no_of_classes=ingredients_picker_config.no_of_classes
    trained_model_path=ingredients_picker_config.trained_model_path
    save_image_dir_name=ingredients_picker_config.save_image_dir_name
    save_image_file_path=ingredients_picker_config.save_image_file_name
    yolo_model_name=ingredients_picker_config.yolo_model_name

    best_model = models.get(yolo_model_name,
                            num_classes=no_of_classes,
                            checkpoint_path=trained_model_path)

    result=best_model.predict(test_image)
    rgb_crop_img_arr=list(result)[0].image
    bgr_img=cv2.cvtColor(rgb_crop_img_arr, cv2.COLOR_BGR2RGB)
    save_or_not=cv2.imwrite(f'{save_image_file_path}',bgr_img)

    if save_or_not:
        return save_or_not
    raise Exception(f'somthing went wrong please check the file path or other')


if __name__=="__main__":
    get_bounding_box("/config/workspace/src/1f783016-fc7c-11ed-b2b0-0242ac1c000c.jpg")