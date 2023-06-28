from super_gradients.training import models
from Ingredients_Checker.entity import IngredientsPickerConfig
from Ingredients_Checker.config import Configuration
from pathlib import Path
import cv2


def get_bounding_box(test_image,to_store_image_path:Path)->None:

    ingredients_picker_config=Configuration().get_ingredients_picker_config()

    no_of_classes=ingredients_picker_config.no_of_classes
    trained_model_path=ingredients_picker_config.trained_model_path
    best_model = models.get('yolo_nas_m',
                            num_classes=no_of_classes,
                            checkpoint_path=trained_model_path)

    result=best_model.predict(test_image)
    rgb_crop_img_arr=result.image
    bgr_img=cv2.cvtColor(a.image, cv2.COLOR_BGR2RGB)
    save_or_not=cv2.imwrite(f'{to_store_image_path}',bgr_img)

    if save_or_not:
        return to_store_image_path
    raise Exception(f'somthing went wrong please check the file path or other')
