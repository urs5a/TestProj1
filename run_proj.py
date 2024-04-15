#STEP 1 below
#pasted from website
import ResearchOS as ros #TYPO, originally was researchos

ros.DBInitializer() 

#STEP 1 DONE
#all worked

#STEP 2
# should specify HOW we are creating dummy_data.csv
# I'm left wondering if it matters how I make it, do I just make my own excel doc?
# might seem obvious but I would say something like "you can make this csv file using excel or what ever you normally use"
# how do I get it into the project? do I just drag it into the project folder? 
# if uploading the dummy data is an another step I would also say something like "this step is just to create the data, we will connect it to our test projet in the next step"

# i liked the text the end explaining what the fake data means, again seems obvious but it makes it easier to follow along

#i made my dummy_data by saving excel as a CSV (comma deliminated)

#STEP 3
#should specify to create dataset.py inside of new research_objects folder

#TYPO, Data Objects are custom defined IN each project

#should also specify that data_objects is different than dataset and 
#it is just a little strange bc we made a new file (dataset.py) but then we need another new file (data_objects.py) to paste the new code into
#I'm assuming I paste the new code into data_objects but thats also not specified

# NOTE "# Needs to start with "SJ" for "Subject", and be unique within the project." is inaccurate
# check naming instructions for DS aswell, note that its a singleton
#code & comments in research_objects/data_objects

#how you did "Type the following into research_objects/datasets.py:" is really helpful

#STEP 4
# i like how simple it was

#STEP 5
# also very simple, code still works
# question: to test this, I'm just running this (run_proj.py) file, does that work? should I also be running a different file?
# TYPO, said to make "logsheets.py", should be "logsheet.py"

#STEP 6 below
from research_objects import logsheet as lg
from research_objects import dataset as ds

lg.logsheet.read_logsheet()
#right now, logsheet doesn't work due to class column names 
#SO... in error message, make sure to add the type of error (ex: validation) on which object (ex: logsheet), attribute name, and what the actual eror is
# that way you know where the error is and what type it is
