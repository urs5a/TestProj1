#STEP 3 cont
import ResearchOS as ros

class Subject(ros.DataObject):
    prefix: str = "SJ" # Needs to start with "SJ" for "Subject", and be unique within the project.

class Trial(ros.DataObject):
    prefix: str = "TR" # Needs to start with "TR" for "Trial", and be unique within the project.