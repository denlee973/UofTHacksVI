# first attempt at using azure custom vision

from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
import os

PROJECT_NAME = "asl"
ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com"
trainingEndpoint = "https://southcentralus.api.cognitive.microsoft.com/customvision/v2.2/Training/"
predictionEndpoint = "https://southcentralus.api.cognitive.microsoft.com/customvision/v2.0/Prediction/"
trainingKey = "14d7fcd72d514522a575e23ac3492a4f"
predictionKey = "d1783dfe45454e2b9520f2fd65ef641c"

# fetch project object from Custom Vision Service (customvision.ai)
def fetch_project():
    try:
        print "Get trainer"
        trainer = CustomVisionTrainingClient(trainingKey, endpoint=ENDPOINT)

        print "Get project"
        for proj in trainer.get_projects():
            if (proj.name == PROJECT_NAME):
                return proj
    except Exception as e:
        print str(e)

print("Set path for folder containign image to predict")
IMAGES_FOLDER = os.path.dirname(os.path.realpath(__file__))

# Get predictor and project objects
print "Get predictor"
predictor = CustomVisionPredictionClient(predictionKey, endpoint=ENDPOINT)
project = fetch_project()

print("Make prediction")
# try:
# with open("one.jpg") as test_data:
with open(os.path.join(IMAGES_FOLDER, "test", "one.jpg"), mode="rb") as test_data:
    results = predictor.predict_image(project.id, test_data.read())
# except Exception as e:
#     print(str(e))
#     input()

# Display the results
for prediction in results.predictions:
    print(prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100))
    input()