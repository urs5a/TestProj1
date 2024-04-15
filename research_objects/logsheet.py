import ResearchOS as ros
#NOTE need to ADD two lines below:
from research_objects.data_objects import * 
import research_objects.variables as vr

logsheet = ros.Logsheet(id = "LG1") # Needs to start with "LG" for "Logsheet", and be unique within the project.
logsheet.path = "C:\\Users\\14156\\Desktop\\Stevens\\UrsulaFolderResearchOS\\TestProj1\\dummy_data.csv"
# how is this path different from the data path?
# i'm assuming this path goes to this .py file while data goes to oour dummy data?
# add a note about needing the double slash
# add a note to give a warning if it doesn't end with .csv
logsheet.num_header_rows = 1

#fixing step 6 errors: we swapped the order so that logsheet.class_column_names comes AFTER logsheet.headers
logsheet.headers = [
    ("Subject", str, Subject, vr.subject_name),
    ("Trial", int, Trial, vr.trial_name),
    ("Value", int, Trial, vr.value)
]
logsheet.class_column_names = {
    "Subject": Subject,
    "Trial": Trial
}