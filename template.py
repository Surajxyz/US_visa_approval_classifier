import os
from pathlib import Path

folder="src"

list_of_files = [

    f"{folder}/__init__.py",
    f"{folder}/components/__init__.py",
    f"{folder}/components/data_ingestion.py",  
    f"{folder}/components/data_validation.py",
    f"{folder}/components/data_transformation.py",
    f"{folder}/components/model_trainer.py",
    f"{folder}/components/model_evaluation.py",
    f"{folder}/components/model_pusher.py",
    f"{folder}/configuration/__init__.py",
    f"{folder}/constants/__init__.py",
    f"{folder}/entity/__init__.py",
    f"{folder}/entity/config_entity.py",
    f"{folder}/entity/artifact_entity.py",
    f"{folder}/exception/__init__.py",
    f"{folder}/logger/__init__.py",
    f"{folder}/pipline/__init__.py",
    f"{folder}/pipline/training_pipeline.py",
    f"{folder}/pipline/prediction_pipeline.py",
    f"{folder}/utils/__init__.py",
    f"{folder}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")