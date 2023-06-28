import logging
from Ingredients_Checker.constant import LOG_FILE_PATH

format_str=f"[  %(asctime)s  %(filename)s  %(funcName)s  %(lineno)d   ]   [   %(message)s  ]"
logging.basicConfig(

    filename=LOG_FILE_PATH,
    format=format_str,
    level=logging.INFO
    
)