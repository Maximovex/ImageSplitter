import tkinter as tk
from tkinter import filedialog
from split_image import split_image
from PIL import Image
import os

root = tk.Tk()
root.withdraw()
base_width=1416


file_path = filedialog.askopenfilename()
im = Image.open(file_path)
width, height = im.size
hsize=height*base_width/width

im = im.resize((base_width, int(hsize)), Image.Resampling.BICUBIC)

im_name=os.path.basename(file_path).split('.')[0]
im.save(im_name+'_1440.png','PNG',quality=100)
rows=int(hsize//708+1)


split_image(im_name+'_1440.png', rows, 1, False, False,output_dir=os.path.dirname(file_path))