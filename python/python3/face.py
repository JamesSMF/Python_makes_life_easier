from PIL import Image, ImageDraw
from IPython.display import display
import face_recognition

image = face_recognition.load_image_file("/Users/liguangyao/Downloads/IMG_2719.JPG")
face_landmarks_list = face_recognition.face_landmarks(image)
display(face_landmarks_list)
