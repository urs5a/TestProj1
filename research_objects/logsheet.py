import ResearchOS as ros

logsheet = ros.Logsheet(id = "LG1") # Needs to start with "LG" for "Logsheet", and be unique within the project.
logsheet.path = "your_project_folder/dummy_logsheet.csv" #how much of the path should I put here
logsheet.num_header_rows = 1
logsheet.class_column_names = {
    "Subject": Subject,
    "Trial": Trial
}
logsheet.headers = [
    ("Subject", str, Subject, vr.subject_name),
    ("Trial", int, Trial, vr.trial_name),
    ("Value", int, Trial, vr.value)
]