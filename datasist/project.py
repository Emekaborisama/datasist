import os
import argparse  
import json

def start_project(project_name=None):
    '''
    Creates a standard data science project directory. This helps in
    easy team collaboration, rapid prototyping, easy reproducibility and fast iteration. 
    
    The directory structure is by no means a globally recognized standard, but was inspired by
    the folder structure created by the Azure team (https://docs.microsoft.com/en-us/azure/machine-learning/team-data-science-process/overview)
    and Edward Ma (https://makcedward.github.io/) of OOCL.
    
    ### PROJECT STRUCTURE:

            ├── data
            │   ├── processed
            │   └── raw
            ├── models
            ├── notebooks
            │   ├── eda
            │   └── modeling
            ├── scripts
            │   ├── modeling
            │   ├── preparation
            │   └── processing
            ├── test

            DETAILS:

            data: Stores data used for the experiments, including raw and intermediate processed data.
                processed: stores all processed data files after cleaning, analysis, feature creation etc.
                raw: Stores all raw data obtained from databases, file storages, etc.

            models: Stores trained binary model files. This are models saved after training and evaluation for later use.

            notebooks: stores jupyter notebooks for exploration, modeling, evaluation, etc.
                eda: Stores notebook of exploratory data analysis.
                modeling: Stores notebook for modeling and evaluation of different models.

            scripts: Stores all code scripts usually in Python/R format. This is usually refactored from the notebooks.
                modeling: Stores all scripts and code relating to model building, evaluation and saving.
                preparation: Stores all scripts used for data preparation and cleaning.
                processing: Stores all scripts used for reading in data from different sources like databases or file storage.

            test: Stores all test files for code in scripts.
    
    
    Parameters:
    -------------
    project_name: String, Filepath
            Name of filepath of the directory to initialize and create folders.
    
    Returns:
    -------------
    None
    
    '''
    if project_name is None:
        raise ValueError("project_name: Expecting a string or filepath, got 'None'")

    
    basepath = os.path.join(os.getcwd(), project_name)
    datapath = os.path.join(basepath, 'data')
    modelpath = os.path.join(basepath, 'models')
    outputpath = os.path.join(basepath, 'outputs')

    
    os.makedirs(datapath, exist_ok=True)
    os.makedirs(os.path.join(datapath, 'raw'), exist_ok=True)
    os.makedirs(os.path.join(datapath, 'processed'), exist_ok=True)

    os.makedirs(os.path.join(basepath, 'notebooks'), exist_ok=True)
    os.makedirs(os.path.join(basepath, 'notebooks', 'eda'), exist_ok=True)
    os.makedirs(os.path.join(basepath, 'notebooks', 'modeling'), exist_ok=True)

    os.makedirs(os.path.join(basepath, 'scripts'), exist_ok=True)
    os.makedirs(os.path.join(basepath, 'scripts', 'modeling'), exist_ok=True)
    os.makedirs(os.path.join(basepath, 'scripts', 'preparation'), exist_ok=True)
    os.makedirs(os.path.join(basepath, 'scripts', 'processing'), exist_ok=True)

    os.makedirs(modelpath, exist_ok=True)
    os.makedirs(outputpath, exist_ok=True)

    os.makedirs(os.path.join(basepath, 'test'), exist_ok=True)
    
    desc = '''
            ### PROJECT STRUCTURE:

            ├── data
            │   ├── processed
            │   └── raw
            ├── models
            ├── notebooks
            │   ├── eda
            │   └── modeling
            ├── scripts
            │   ├── modeling
            │   ├── preparation
            │   └── processing
            ├── test

            DETAILS:

            data: Stores data used for the experiments, including raw and intermediate processed data.
                processed: stores all processed data files after cleaning, analysis, feature creation etc.
                raw: Stores all raw data obtained from databases, file storages, etc.

            models: Stores trained binary model files. This are models saved after training and evaluation for later use.

            notebooks: stores jupyter notebooks for exploration, modeling, evaluation, etc.
                eda: Stores notebook of exploratory data analysis.
                modeling: Stores notebook for modeling and evaluation of different models.

            scripts: Stores all code scripts usually in Python/R format. This is usually refactored from the notebooks.
                modeling: Stores all scripts and code relating to model building, evaluation and saving.
                preparation: Stores all scripts used for data preparation and cleaning.
                processing: Stores all scripts used for reading in data from different sources like databases or file storage.

            test: Stores all test files for code in scripts.

            ''' 
    #project configuration settings
    json_config = {"description": "This file holds all confguration settings for the current project",
                    "basepath": basepath,
                    "datapath" : datapath,
                    "outputpath": outputpath,
                    "modelpath": modelpath}
    
    #create a readme.txt file to explain the folder structure
    with open(os.path.join(basepath, "README.txt"), 'w') as readme:
        readme.write(desc)
    
    with open(os.path.join(basepath, "config.txt"), 'w') as configfile:
        json.dump(json_config, configfile)
    
    print("Project Initialized successfully in {}".format(basepath))
    print("Check folder description in ReadMe.txt")





if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--project_name", help="Name of the parent directory to initialize folders")
    args = parser.parse_args()

    start_project(args.project_name)