from PIL import Image
import warnings
import numpy as np
import os

def loadFromFolder(folder_path):
    if folder_path[-1] != '/':
        folder_path = folder_path+'/'
    imgs=[]
    for filename in os.listdir(folder_path):
        try:
            img = np.array(Image.open(folder_path +filename))
            imgs.append(img)
        except OSError:
            warnings.warn('\nCan not load \"' + folder_path + filename + '\"')
    return imgs
    
    
if __name__ == '__main__':
    print('Image processing api.')