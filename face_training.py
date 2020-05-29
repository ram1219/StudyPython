import cv2
import numpy as np
from PIL import Image
import os

# 얼굴 데이터셋 경로
path = 'facedetection/dataset'
recognizer = cv2.face.createLBPHFaceRecognizer()
detector = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')

# 이미지들을 가져오고 데이터 라벨링하는 함수
def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    ids = []
    for imagePath in  imagePaths:
        PIL_img = Image.open(imagePath).convert('L')     # 회색톤으로 변환
        img_numpy = np.array(PIL_img, 'uint8')
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)
        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h, x:x+w])
            ids.append(id)
    return faceSamples, ids

print("\n [INFO] TRAINING FACES. It will take a few seconds. Wait...")
faces, ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))

recognizer.save('trainer.yml')

print("\n [INFO] {0} FACES TRANED. Exiting Program".format(len(np.unique(ids))))
