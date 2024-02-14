## Current Functionalities
- main.py will read through any images placed in the "images" folder
- It will read all of the stats and put them into a Python pandas dataframe
- The dataframe is turned into an excel spreadsheet that can be saved by the user
- Running main.py will also overwrite any existing data in data.xlsx

## To Do List:
- [X] Image recognition to extract the text
- [X] Organization of the text
- [ ] Have it read the screen data
- [X] Put the data into a spreadsheet
- [ ] Create an application

## Current Issues
- Certain data points are read incorrectly, specifically names. Example: L's read as t's, q's read as g's. Especially problematic when a title is read incorrectly. Example: Def read as Dag.
- Fixed by addressing all the cases I've run into
- Need a way to fix it properly

