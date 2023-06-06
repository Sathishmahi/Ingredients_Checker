import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,filename='loginfo.log',format='[%(asctime)s]  [%(message)s]')

package_name='Package_name'
REQUIREMENTS_TXT_NAME="requirements.txt"

list_of_files=[
'.github/workflows/.gitkeep',
f'src/{package_name}/__init__.py',
f'src/{package_name}/components/__init__.py',
f'src/{package_name}/config/__init__.py',
f'src/{package_name}/utils/__init__.py',
f'src/{package_name}/constant/__init__.py',
f'src/{package_name}/pipeline/__init__.py',
f'src/{package_name}/entity/__init__.py',
f'src/{package_name}/__init__.py',
'config/config.yaml',
'params.yaml',
'dvc.yaml',
'init_setup.sh',
REQUIREMENTS_TXT_NAME,
'setup.py',
]


###

for file_path in list_of_files:
    file_path=Path(file_path)
    file_splits=os.path.split(file_path)
    if file_splits[0]=='':
        if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
            with open(file_path,'w') as f:pass
            logging.info(msg=f'file created file name is {file_path}')
    else:
        os.makedirs(file_splits[0],exist_ok=True)
        if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
            with open(file_path,'w') as f:pass
            logging.info(msg=f'file created file name is {file_path}')


BASIC_REQUIREMENTS_LIST=[
    f"dvc\n",
    f"mkdocs-material\n"]

with open(REQUIREMENTS_TXT_NAME,'w') as require_file:
    [require_file.write(package) for package in BASIC_REQUIREMENTS_LIST]