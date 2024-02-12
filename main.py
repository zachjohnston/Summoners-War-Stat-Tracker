from PIL import Image
import pytesseract as pt
import numpy as np
import pandas as pd

filelocation = "images/kaki.jpg", "images/icaru.jpg"
unit_list = [] #list

for j in range(len(filelocation)):
    full_image =Image.open(filelocation[j])
    #crop image
    w, h = full_image.size
    #take off the left two thirds
    left = w * 2/3 - 50
    #keep the upper  5/6
    bottom = h * 5/6
    #take off the top 1/8
    top = h * 1/8

    cropped_image = full_image.crop((left, top, w, bottom))
    #cropped_image.show()

    file = np.array(cropped_image)
    #get the text out of the image
    text = pt.image_to_string(file)

    #split up all the text in the file
    textlist = text.split()
    print("text list")
    print(textlist)

    #remove first element, thinks element is a symbol
    del textlist[0]

    #put information in a tuple
    unitstats = ()
    unitstats = unitstats + (textlist[0],)
    for i in range(len(textlist)):
        match textlist[i]:
            case "Level":
                unitstats = unitstats + (textlist[i+1],)
                unitstats = unitstats + (textlist[i+3],)
                unitstats = unitstats + (textlist[i+4],)
            case "HP":
                unitstats = unitstats + (textlist[i+1],)
                unitstats = unitstats + (textlist[i+2].strip('+'),)
            case "ATK":
                unitstats = unitstats + (textlist[i+1],)
                unitstats = unitstats + (textlist[i+2].strip('+'),)
            case "DEF":
                unitstats = unitstats + (textlist[i+1],)
                unitstats = unitstats + (textlist[i+2].strip('+'),)
            case "SPD":
                unitstats = unitstats + (textlist[i+1],)
                unitstats = unitstats + (textlist[i+2].strip('+'),)
            case "CRI":
                if textlist[i+1] == "Rate":
                    unitstats = unitstats + (textlist[i+2],)
                elif textlist[i+1] == "Dmg":
                    unitstats = unitstats + (textlist[i+2],)
                else: #probably default to cri dmg as it seems to have issues
                    unitstats = unitstats + (textlist[i+1],)
            case "Resistance":
                unitstats = unitstats + (textlist[i+1],)
            case "Accuracy":
                unitstats = unitstats + (textlist[i+1],)
    #add unit to full list
    unit_list.append(unitstats)

title_list = [
    "Name",         #0          
    "Current Level",#1
    "Max Level",    #2
    "Type",         #3
    "HP",           #4
    "HP+",          #5
    "ATK",          #6
    "ATK+",         #7
    "DEF",          #8
    "DEF+",         #9
    "SPD",          #10
    "SPD+",         #11
    "CRI Rate",     #12
    "CRI Dmg",      #13
    "Resistance",   #14
    "Accuracy"      #15
]

print(unit_list)

#print out the info
for i in range(len(unit_list)):
    print("-----------------")
    for j in range(len(unit_list[i])):
        print(str(title_list[j]) + ": " + str(unit_list[i][j]))

final_data = pd.DataFrame.from_records(unit_list,columns=title_list)
print(final_data)

final_data.to_csv("data.csv", index=False)