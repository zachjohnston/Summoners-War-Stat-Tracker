from PIL import Image
import pytesseract as pt
import numpy as np
import pandas as pd
import os
import xlsxwriter

directory = os.fsencode("images/")
unit_list = [] #list

for file in os.listdir(directory):
    filename = os.fsdecode(directory) + os.fsdecode(file)
    full_image = Image.open(filename)
    #crop image
    w, h = full_image.size
    #take off the left two thirds
    left = w - 800 
    #keep the upper  5/6
    bottom = h - 245
    #take off the top 1/8
    top = 50


    cropped_image = full_image.crop((left, top, w, bottom))
    # cropped_image.show()

    image_array = np.array(cropped_image)
    #get the text out of the image
    text = pt.image_to_string(image_array)

    #split up all the text in the file
    textlist = text.split()
    print(textlist)


    #put information in a tuple
    unitstats = ()
    looping = True
    errorchecker = 0
    #unitstats = unitstats + (textlist[0],) #name
    while looping:
        for i in range(len(textlist)):
            if ("@" in textlist[i] or "©" in textlist[i] or "B"  in textlist[i] or "®"  in textlist[i]) and len(unitstats) == 0: 
                unitstats = unitstats + (textlist[i+1].capitalize(),)
            match textlist[i]:
                case "Level" if len(unitstats) == 1:
                    print(textlist[i])
                    print(textlist[i+1])
                    try:
                        int(textlist[i+1]) #checks if it's 40 (int) or 40/40 (str)
                    except: #read the value wrong
                        print("value read wrong")
                        lvl = textlist[i+1].split('/') 
                        unitstats = unitstats + (lvl[0],)
                        unitstats = unitstats + (lvl[1],)
                        unitstats = unitstats + (textlist[i+2],) 
                    else: #read the value correctly   
                        unitstats = unitstats + (textlist[i+1],) #current level
                        unitstats = unitstats + (textlist[i+3],) #max level
                        unitstats = unitstats + (textlist[i+4],) #type
                case "HP" if len(unitstats) == 4:
                    unitstats = unitstats + (textlist[i+1],) #hp
                    unitstats = unitstats + (textlist[i+2].strip('+'),) #+hp
                case "ATK" if len(unitstats) == 6:
                    unitstats = unitstats + (textlist[i+1],) #atk
                    unitstats = unitstats + (textlist[i+2].strip('+'),) #+atk
                case "DEF" if len(unitstats) == 8:
                    unitstats = unitstats + (textlist[i+1],) #def
                    unitstats = unitstats + (textlist[i+2].strip('+'),) #+def
#---------------ERROR CASE---------------------------
                case "Dag" if len(unitstats) == 8:
                    unitstats = unitstats + (textlist[i+1],) #def
                    unitstats = unitstats + (textlist[i+2].strip('+'),) #+def                    
#----------------------------------------------------                
                case "SPD" if len(unitstats) == 10:
                    unitstats = unitstats + (textlist[i+1],) #spd
                    unitstats = unitstats + (textlist[i+2].strip('+'),) #+spd
                case "CRI" if len(unitstats) == 12 or len(unitstats) == 13:
                    if textlist[i+1] == "Rate":
                        unitstats = unitstats + (textlist[i+2],) #cri rate
                    elif textlist[i+1] == "Dmg":
                        unitstats = unitstats + (textlist[i+2],) #cri dmg
                case "Resistance" if len(unitstats) == 14:
                    unitstats = unitstats + (textlist[i+1],) #resistance
                case "Accuracy" if len(unitstats) == 15:
                    unitstats = unitstats + (textlist[i+1],) #accuracy
                    looping = False 
                    unit_list.append(unitstats)      
        #add unit to full list
        print(unitstats)
        

#titles of the columns in sheet 1
title_list_1 = [
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

#titles of the columns in sheet 2
title_list_2 = [
    "Name",
    "Total HP"#,
#    "Total ATK",
#    "Total DEF",
#    "Total SPD",
#    "Total CRI Rate",
#    "Total CRI Dmg",
#    "Effective HP"
]

#print out the info
# for i in range(len(unit_list)):
#     print("-----------------")
#     for j in range(len(unit_list[i])):
#         print(str(title_list[j]) + ": " + str(unit_list[i][j]))

final_data_1 = pd.DataFrame.from_records(unit_list,columns=title_list_1)
print(final_data_1)

#check if the file exists and delete it
if os.path.exists("data.xlsx"):
    os.remove("data.xlsx")
final_data_1.to_excel("data.xlsx",index=False)

#want another sheet that has total hp, atk, def, spd, cri dmg, EHP with towers factored in

