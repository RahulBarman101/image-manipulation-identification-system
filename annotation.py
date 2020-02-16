#imports for saving the xml files
import os
import matplotlib.pyplot as plt
import cv2
from matplotlib.widgets import RectangleSelector
from generate_xml import write_xml

img = None
tl_list = []
br_list = []
object_list = []

image_folder = 'E:/miniproject/dataset/images'
savedir = 'annotations'
obj = 'photoshoped'

def line_select_callback(clk, rls):
    global tl_list
    global br_list
    #global object_list
    #gets the click event and saves the coordinates of topleft and bottom right corner in lists
    tl_list.append((int(clk.xdata), int(clk.ydata)))
    br_list.append((int(rls.xdata), int(rls.ydata)))
    #object_list.append(obj)

def toggle_selector(event):
    toggle_selector.RS.set_active(True)

def onkeypress(event):       #function for saving the topleft and bottom right corner of the bounding box

    global tl_list
    global br_list
    global object_list
    global img
    if event.key == 'q':
        #print(tl_list,br_list)
        #function for writing the data into xml files
        write_xml(image_folder,img,object_list,tl_list,br_list,savedir)
        tl_list = []
        br_list = []
        #object_list = []
        img = None
        plt.close()



if __name__ == '__main__':
    #Scans the folder for images and displays it using matplotlib
    for n, imfile in enumerate(os.scandir(image_folder)):
        img = imfile
        fig,ax = plt.subplots(1)
        image = cv2.imread(imfile.path)
        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        ax.imshow(image)
        #Uses RectangleSelector for drawing bounding boxes
        toggle_selector.RS = RectangleSelector(
                                                ax,line_select_callback,drawtype='box',
                                                useblit=True,button=[1],minspanx=5,
                                                minspany=5,spancoords='pixels',interactive=True
                                                )
        bbox = plt.connect('key_press_event',toggle_selector)
        key = plt.connect('key_press_event',onkeypress)
        plt.show()
