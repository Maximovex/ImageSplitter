import tkinter as tk
from tkinter import filedialog
from split_image import split_image
from PIL import Image
from PyQt6.QtCore import Qt,QSize
from PyQt6.QtWidgets import QLineEdit,QApplication, QWidget,QLabel,QPushButton,QHBoxLayout,QVBoxLayout
from PyQt6.QtGui import QPixmap
import os


hsize=800
file_path=""
im_name=""

#QtGUI shell initialisation
app=QApplication([])
main_window=QWidget()
main_window.setWindowTitle("Image Splitter")
main_window.resize(500,500)

#creating all app objects
title=QLabel("Split image by specifying rows and columns")
cols=QLineEdit("1")
rows=QLineEdit("5")
res_width=QLineEdit("1416")
btn_open=QPushButton("Open Image")
btn_cut=QPushButton("Cut IT")
btn_resize=QPushButton("Resize")
sel_image=QLabel()


#Design objects
master_layout=QVBoxLayout()
row_descriptions=QHBoxLayout()
row_colrows=QHBoxLayout()
row_view=QHBoxLayout()
row_commands=QHBoxLayout()

row_descriptions.addWidget(title,alignment=Qt.AlignmentFlag.AlignHCenter)
row_colrows.addWidget(cols,alignment=Qt.AlignmentFlag.AlignHCenter)
row_colrows.addWidget(rows,alignment=Qt.AlignmentFlag.AlignHCenter)
row_colrows.addWidget(res_width,alignment=Qt.AlignmentFlag.AlignHCenter)

row_view.addWidget(sel_image,alignment=Qt.AlignmentFlag.AlignHCenter)
row_commands.addWidget(btn_open)
row_commands.addWidget(btn_resize)
row_commands.addWidget(btn_cut)


master_layout.addLayout(row_descriptions)
master_layout.addLayout(row_colrows)
master_layout.addLayout(row_view)
master_layout.addLayout(row_commands)
main_window.setLayout(master_layout)


base_width=int(res_width.text())
num_cols=int(cols.text())
num_rows=int(rows.text())

def get_image(file_path):



    im = Image.open(file_path)
    return im

#openning big image
def get_file():

    global hsize
    global file_path
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()

    im = get_image(file_path)
    width, height = im.size
    hsize=height*base_width/width
    pixmap = QPixmap(file_path)
    scaled_pixmap=pixmap.scaled(QSize(300,300),Qt.AspectRatioMode.KeepAspectRatio)
    sel_image.setPixmap(scaled_pixmap)

    btn_open.setText("Clicked")

#adding image to the app window

def resize():
    global im_name
    im = get_image(file_path)
    im = im.resize((base_width, int(hsize)), Image.Resampling.BICUBIC)
    im_name = os.path.basename(file_path).split('.')[0]
    im.save(im_name + str(base_width)+'.png', 'PNG', quality=100)

def splitting():

    global hsize

    im = get_image(file_path)

    im_name = os.path.basename(file_path).split('.')[0]
    #rows = int(hsize // 708 + 1)
    split_image(im_name+"_"+str(base_width)+'.png', num_rows, num_cols, False, False,output_dir=os.path.dirname(file_path))

#events
btn_open.clicked.connect(get_file)
btn_resize.clicked.connect(resize)
btn_cut.clicked.connect(splitting)

#Showing window
main_window.show()
app.exec()