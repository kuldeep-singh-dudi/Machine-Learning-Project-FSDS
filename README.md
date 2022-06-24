## Machine-Learning-Project-FSDS

Kuldeep Singh Dudi


### Software and account Requirement.
Github Account
Heroku Account
VS Code IDE
GIT cli
Github Documentation
Creating conda environment

conda create -p venv python==3.7 -y
conda activate venv/
OR

conda activate venv
pip install -r requirements.txt
To Add files to git

git add .
OR

git add <file_name>
Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status

git status
To check all version maintained by git

git log
To create version/commit all changes by git

git commit -m "message"
To send version/changes to github

git push origin main
To check remote url

git remote -v
To setup CI/CD pipeline in heroku we need 3 information

HEROKU_EMAIL
HEROKU_API_KEY
HEROKU_APP_NAME
BUILD the DOCKER IMAGE

docker build -t <image_name>:<tagname> .
Note: Image name for docker must be lowercase

To list docker image

docker images
Run Docker Image

docker run -p 5000:5000 -e PORT=5000 <image_id>
To check running in docker

docker ps
To stop docker container

docker stop <container_id>
To install requirements.txt

 python setup.py install
Project Structure
|-- Project
    |-- housing (Project folder)
        |-- __init__.py
        |-- component (pipeline stages)
            |-- __init__.py
            |-- data_ingestion.py
            |-- data_validation.py
            |-- data_transformation.py
            |-- model_trainer.py
            |-- model_evaluation.py
            |-- model_pusher.py
        |-- config
            |-- __init__.py
        |-- entity (artifacts)
            |-- __init__.py
        |-- exception
            |-- __init__.py
        |-- logger
            |-- __init__.py
        |-- pipeline
            |-- __init__.py
            |-- pipeline.py
    |-- .github (Continuous Delivery/Deployment)
        |-- workflows
            |-- main.yaml    
    |-- Dockerfile
    |-- .dockerignore
    |-- .gitignore
    |-- app.py (Entry Point)
    |-- requirements.txt
    |-- setup.py
    |-- LICENSE
    |-- README.md



    
4d07c9ba-9d67-438e-bf6a-f812fe53d795