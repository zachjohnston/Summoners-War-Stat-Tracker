from PIL import Image
import os 
import numpy as np
import pytesseract as pt

def read_and_process_images(directory):
    images = []
    for file in os.listdir(directory):
        filename = os.fsdecode(directory) + os.fsdecode(file)
        image = Image.open(filename)
        processed_image = crop_image(image)
        images.append(processed_image)
    return images

def crop_image(image):
    w, h = image.size
    left = w - 800
    bottom = h - 245
    top = 50
    image = image.crop((left,top,w,bottom))
    return image

def imgtostring(images, verbose):
    textlist = []
    notread = 0
    for image in images:
        image_array = np.array(image)
        text = pt.image_to_string(image_array)
        text = text.split()
        if len(text) > 20:
            textlist.append(text)
        else:
            notread+=1
        if verbose:
            print(text)
    return textlist, notread

