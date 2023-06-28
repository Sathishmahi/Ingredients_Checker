import os
from pathlib import Path
from Ingredients_Checker.log import logging
from Ingredients_Checker.constant import CONFIG_FILE_PATH
import yaml
from typing import Any



def to_write_txt(file_path:Path,content:Any,append=False)->None:
    
    out_str=content
    if isinstance(content, list | tuple ):
        out_str="\n".join(content)
    mode="a" if os.path.isfile(file_path) else "w"
    with open(file_path,mode=mode) as f:
        f.write(out_str)
    

def read_yaml(yaml_file_path:Path=CONFIG_FILE_PATH)->dict:
    
    if not os.path.exists(yaml_file_path):
        e=FileNotFoundError(f'yaml file not found {yaml_file_path}')
        logging.exception(e)
        raise e
    try:
        with open(yaml_file_path) as yaml_file:
            con=yaml.safe_load(yaml_file)
        return con
    except Exception as e:
        raise e
    
def make_dirs(dirs_list:Path,log=True)->None:
    try:
        if not dirs_list:
            raise Exception(f'dir list is empty')
        for dir in dirs_list:
            os.makedirs(name=dir,exist_ok=True)
            if log:logging.info(msg=f"folder created {dir}")
    except Exception as e:
        logging.exception(msg=e)
        raise e
