import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format = '[%(asctime)s - %(message)s]')

projectName = "mlApp1"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{projectName}/__init__.py",
    f"src/{projectName}/components/__init__.py",
    f"src/{projectName}/utils/__init__.py",
    f"src/{projectName}/utils/common.py",
    f"src/{projectName}/config/__init__.py",
    f"src/{projectName}/config/configuration.py",
    f"src/{projectName}/pipeline/__init__.py",
    f"src/{projectName}/entity/__init__.py",
    f"src/{projectName}/entity/config_entity.py",
    f"src/{projectName}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/research.ipynb",
    "template/index.html"    
]

for file in list_of_files:
    filePath = Path(file)
    fileDir, filePathVal = os.path.split(filePath)
    
    if (fileDir != ""):
        os.makedirs(fileDir, exist_ok=True)
        logging.info(f"{fileDir} created. For creating {filePathVal} this file")
        
    # print(os.path.getsize(filePathVal))
    if (not os.path.exists(filePath) or os.path.getsize(filePath) == 0):
        with open(filePath, "w") as f:
            pass
        
        logging.info(f"{filePathVal} file created inside the {fileDir} directory")
        
    else:
        logging.info(f"{filePathVal} file already exsited")