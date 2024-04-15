#STEP 3 cont
import ResearchOS as ros
from research_objects.data_objects import Subject, Trial

#am I supposed to change the DS1 name?
dataset = ros.Dataset(id = "DS1") # Needs to start with "DS" for "Dataset", and be unique within the project.
dataset.schema = [
    [ros.Dataset, Subject],
    [Subject, Trial]
]
dataset.dataset_path = "C:\\Users\\14156\\Desktop\\Stevens\\UrsulaFolderResearchOS\\TestProj1\\Data" 
#is this just the path to our dummy_data? if the dummy data is already in the Testproj1 folder do I need a path?