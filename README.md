# US_visa_approval_classifier
ML project

- Install VSCODE https://code.visualstudio.com/

- Install ANACONDA https://www.anaconda.com/

- Install GIT BASH https://git-scm.com/downloads

- MLOPs Tool: https://www.evidentlyai.com/

- Mongodb https://account.mongodb.com/account/login

- dataset https://www.kaggle.com/datasets/moro23/easyvisa-dataset

- Virtual environment creation
   ```python -m venv us_visa```

- To create the folders
   ```python template```

- Install all the requirements
   ``` pip install -r requirements.txt```

- Run application without container in local
   ```python app.py```
- Run the application in docker container
   ```docker run Dockerfile```
   
- Summary

Created a end to end machine learning using visa approval project which is having following components:-

1. Data ingestion : which will extract the data from mongodb database and convert it into csv file.

2. Data validation: validate data that test and train dataset is of same distribution using evidently ai library.

3. Data transformation: transform the features like numerical and categorical in this way
-For numerical feature dont have normal distribution, convert them into normal distribution using yeo jonshon method.
- for categorical features having categories less than 3 is using ordinal encoding and features having more than 3 categories using one hot encoding.
above tranformation is used to create preprocessing.pkl object to tranform the train and test data.

4. Data training: train the all the mentioned models in the model.yaml file and choose the best one having accuracy either more than 60 % or greater the model in the production.
note:- production model os stored in s3 bucket.
if it has accuracy more than production model accuray than it replaces the production model.

5. fast api is created to perform prediction and training on new dataset.




