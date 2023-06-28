from paddleocr import PaddleOCR,draw_ocr
from pathlib import Path
from Ingredients_Checker.config import Configuration
from Ingredients_Checker.utils import to_write_txt
import os

def to_return_ingredients_list(prediction_image_file_path:Path,lan_model:str,ingre_txt_file_path:Path,
                                to_write_ingre_list:bool=True)->list[str]:

    if not os.path.isfile(prediction_image_file_path):
        raise FileNotFoundError(f" prediction file not found {prediction_image_file_path} ")
    ocr=PaddleOCR(use_angle_cls=True,lang=lan_model)
    result=ocr.ocr(prediction_image_file_path)
    all_ingre_name=[i[1][0] for i in result[0]]
    ingredient_list=sum(list(map(lambda ing: ing.split(',') if ',' in ing else [ing],all_ingre_name)),[])
    if to_write_ingre_list:
        to_write_txt(file_path=ingre_txt_file_path, content=ingredient_list)
    return ingredient_list

if __name__=="__main__":
    text_extractor_config=Configuration().get_text_extractor_config()
    ingre_txt_file_name=text_extractor_config.ingredient_txt_file_name
    prediction_img_path=text_extractor_config.prediction_image_file_path
    model_lan=text_extractor_config.model_lan
    ing_li=to_return_ingredients_list("/config/workspace/src/1f783016-fc7c-11ed-b2b0-0242ac1c000c.jpg"
                                    ,model_lan,ingre_txt_file_name)