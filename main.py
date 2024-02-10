from PIL import Image
import pytesseract as pt
import numpy as np
import pandas as pd

filelocation = "images/kaki.jpg", "images/icaru.jpg"
unit_list = []

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

    unitstats = (j,)

    #put information in a tuple

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
    "Number",       #0
    "Name",         #1          
    "Current Level",#2
    "Max Level",    #3
    "Type",         #4
    "HP",           #5
    "HP+",          #6
    "ATK",          #7
    "ATK+",         #8
    "DEF",          #9
    "DEF+",         #10
    "SPD",          #11
    "SPD+",         #12
    "CRI Rate",     #13
    "CRI Dmg",      #14
    "Resistance",   #15
    "Accuracy"      #16
]


print(unit_list)


for i in range(len(unit_list)):
    print("-----------------")
    for j in range(len(unit_list[i])):
        print(str(title_list[j]) + ": " + str(unit_list[i][j]))

    # for i in range(len(stat_list[j])):
    #     print(title_list[i] + ": " + stat_list[j][i])

    # df = pd.DataFrame(stat_dict, index=[0])

    # print(df)
