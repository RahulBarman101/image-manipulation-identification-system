import os
from flask import Flask, render_template, redirect, flash, request, url_for
import cv2
#import sys
import tensorflow as tf
import numpy as np
#sys.path.append("..")

from utils import label_map_util
from utils import visualization_utils as vis_util
app = Flask(__name__, template_folder='templates')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/signup/")
def signup():
    return render_template('signup.html')

@app.route("/predict/" , methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        return redirect(url_for('home'))
    return render_template('predict.html')

@app.route("/upload")
def index():
    return render_template('upload.html')
@app.route('/display')
def display():
    return render_template('display.html')

@app.route("/upload/pred",methods=['Post'])
def upload():
    target = os.path.join(APP_ROOT,'images')
    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        filename = file.filename
        destination = '/'.join([target,filename])
        file.save(destination)
        #path names and file names initialization
        MODEL_NAME = 'inference_graph'
        IMAGES = os.listdir('C:/Users/MY PC/Desktop/FlaskApp/images')
        IMAGE_NAME = IMAGES[0]
        IMAGE_PATH = 'C:/Users/MY PC/Desktop/FlaskApp/images'

        CWD_PATH = 'E:/miniproject'

        PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph.pb')

        PATH_TO_LABELS = os.path.join(CWD_PATH,'training','labelmap.pbtxt')

        PATH_TO_IMAGE = os.path.join(IMAGE_PATH,IMAGE_NAME)

        NUM_CLASSES = 1
        #label_map : objects to be detected in the image i.e photoshop
        label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
        categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
        category_index = label_map_util.create_category_index(categories)

        #initialize the frozen graph
        detection_graph = tf.Graph()
        with detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')

            sess = tf.Session(graph=detection_graph)

        image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

        #create the bounding boxes
        detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

        detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
        detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

        num_detections = detection_graph.get_tensor_by_name('num_detections:0')

        #take the image and perform object detection
        image = cv2.imread(PATH_TO_IMAGE)
        image_expanded = np.expand_dims(image, axis=0)

        (boxes, scores, classes, num) = sess.run(
            [detection_boxes, detection_scores, detection_classes, num_detections],
            feed_dict={image_tensor: image_expanded})

        vis_util.visualize_boxes_and_labels_on_image_array(
            image,
            np.squeeze(boxes),
            np.squeeze(classes).astype(np.int32),
            np.squeeze(scores),
            category_index,
            use_normalized_coordinates=True,
            line_thickness=4,
            min_score_thresh=0.65)

        #cv2.imshow('Object detector', image)

        cv2.imwrite('C:/Users/MY PC/Desktop/FlaskApp/static/images/prediction/new_img.png',image)

        #cv2.waitKey(0)

        #cv2.destroyAllWindows()
        os.remove(PATH_TO_IMAGE)
    return render_template('display.html')


if __name__ == "__main__":
    app.run(debug=True)
