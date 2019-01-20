# first attempt at using azure custom vision

from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
import os
#import cv2


PROJECT_NAME = "asl"
ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com"
trainingEndpoint = "https://southcentralus.api.cognitive.microsoft.com/customvision/v2.2/Training/"
predictionEndpoint = "https://southcentralus.api.cognitive.microsoft.com/customvision/v2.0/Prediction/"
trainingKey = "14d7fcd72d514522a575e23ac3492a4f"
predictionKey = "d1783dfe45454e2b9520f2fd65ef641c"

# fetch project object from Custom Vision Service (customvision.ai)
def fetch_project():
    try:
       # print "Get trainer"
        trainer = CustomVisionTrainingClient(trainingKey, endpoint=ENDPOINT)

       # print "Get project"
        for proj in trainer.get_projects():
            if (proj.name == PROJECT_NAME):
                return proj
    except Exception as e:
        print str(e)

#print("Set path for folder containign image to predict")
IMAGES_FOLDER = os.path.dirname(os.path.realpath(__file__))

# Get predictor and project objects
#print "Get predictor"
predictor = CustomVisionPredictionClient(predictionKey, endpoint=ENDPOINT)
project = fetch_project()

#print("Make prediction")
# try:
#     with open(os.path.join(IMAGES_FOLDER, "test", "one.jpg"), mode="rb") as test_data:
#         results = predictor.predict_image(project.id, test_data.read())
# except Exception as e:
#     print(str(e))
#     input()
#
# # Display the results
# for prediction in results.predictions:
#     print(prediction.tag_name)
#     input()
#
#


#
# cv2.namedWindow("preview")
# vc = cv2.VideoCapture(0)
#
# if vc.isOpened(): # try to get the first frame
#     rval, frame = vc.read()
# else:
#     rval = False
#
# x = 0
# while x != 27:
#     cv2.namedWindow("preview")
#     vc = cv2.VideoCapture(0)
#
#     if vc.isOpened():  # try to get the first frame
#         rval, frame = vc.read()
#     else:
#         rval = False
#     cv2.imshow("preview", frame)
#     rval, frame = vc.read()
#     key = cv2.waitKey(20)
#     if key == 27: # exit on ESC
#         x = 27
#         break
#     elif key == 32:
#         out = cv2.imwrite('capture.jpg', frame)
#         try:
#             with open("capture.jpg", mode="rb") as test_data:
#                 results = predictor.predict_image(project.id, test_data.read())
#         except Exception as e:
#             print(str(e))
#             input()
#
#         # Display the results
#        # x = 0
#        # preds = None
#         for prediction in results.predictions:
#            # if x == 0:
#             print prediction.tag_name
#             break
#                # x += 1
#             # if (prediction.probability*100) >= x:
#             #     preds = prediction.tag_name
#             #print(prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100))
#         #print(preds)
#         #
#
#
#
#         ###

#cv2.destroyWindow("preview")


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.properties import ListProperty
from kivy.config import Config
from kivy.uix.image import Image
from kivy.core.window import Window

Window.size = (450, 750)

import time

Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    lbl1: bleh
    
   
    
    
    # Label:
    # 
    #     size_hint_y: None
    #     color: 1,1,1,1
    #     height: '150dp'
    #     text: ""
    #     bcolor: 1, 1, 1, 1
    #     canvas.before:
    #         Color:
    #             rgba: self.bcolor
    #         Rectangle:
    #             center: self.parent.center
    #             size: self.size
    #             source: 'diallogueLogo.png'
    #             
    #         
    
    Image:
        source: 'diallogueLogo.png'
        size_hint: 1.5, 1
        allow_stretch: True
        keep_ratio: True
        pos_hint: {'center_x': 0.5, 'center_y': 0.75}
                

        
    
    Camera:
        id: camera
        resolution: (640, 480)
        play: True
    # ToggleButton:
    #     text: 'Play'
    #     on_press: camera.play = not camera.play
    #     size_hint_y: None
    #     height: '48dp'
          
    Button:
        text: 'Translate'
        size_hint_y: None
        size: sp(100), sp(100)
        height: '48dp'
        on_press: root.capture()
        width: '48dp'
        background_normal: ''
        background_color: 0.996, 0.196, 0.024, 1
        
    Label:
        id: bleh
        size_hint_y: None
        color: 0,0,0,1
        height: '100dp'
        text: ""
        bcolor: 1, 1, 1, 1
        canvas.before:
            Color:
                rgba: self.bcolor
            Rectangle:
                pos: self.pos
                size: self.size
                
    Button:
        text: 'Clear'
        size_hint_y: None
        height: '32dp'
        on_press: root.clear()
        background_normal: ''
        background_color: 0.996, 0.196, 0.024, 1

        
        

''')


class LabelB(Label):
    bcolor = ListProperty([1,1,1,1])

class LabelC(Button):
    ccolor = ListProperty([254, 50, 102, 1])

class CameraClick(BoxLayout):


    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("capture.jpg")
        try:
            with open("capture.jpg", mode="rb") as test_data:
                results = predictor.predict_image(project.id, test_data.read())
        except Exception as e:
            print(str(e))
            input()

        # Display the results
       # x = 0
       # preds = None
        for prediction in results.predictions:
           # if x == 0:

            self.lbl1.text = self.lbl1.text + " " + prediction.tag_name



           # print prediction.tag_name
            break
               # x += 1
            # if (prediction.probability*100) >= x:
            #     preds = prediction.tag_name
            #print(prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100))
        #print(preds)
        #
       # print("Captured")
    def clear(self):
        self.lbl1.text = ""




class TestCamera(App):

    def build(self):
        return CameraClick()

TestCamera().run()



