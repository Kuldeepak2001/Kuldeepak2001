import time
import camera
import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime
import logging
import pickle
from cv2 import *

path = './ImagesAttendance/'


def get_images_name_list(path):
    images = []
    classNames = []
    mylist = os.listdir(path)
    for cl in mylist:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    return images, classNames


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encoded_face = face_recognition.face_encodings(img)[0]
        encodeList.append(encoded_face)
    return encodeList


def markAttendance(name):
    with open('./AttendanceDataset/Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            time = now.strftime('%I:%M:%S:%p')
            date = now.strftime('%d-%B-%Y')
            f.writelines(f'{name}, {time}, {date},')


def capture_image(webcam, frame, name):
    cv2_filename = f'./ImagesAttendance/{name}.jpg'
    cv2.imshow("Capturing", frame)
    cv2.imwrite(filename=cv2_filename, img=frame)
    print("Image saved!")
    webcam.release()
    markAttendance(name)


def main():
    images, classNames = get_images_name_list(path)
    encoded_face_train = findEncodings(images)
    print("Encoding Finished!")
    # take pictures from webcam
    WebCam = cv2.VideoCapture(0)

    while True:
        success, img = WebCam.read()
        try:
            imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
            faces_in_frame = face_recognition.face_locations(imgS)
            encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)

            for encode_face, faceloc in zip(encoded_faces,faces_in_frame):
                matches = face_recognition.compare_faces(encoded_face_train, encode_face)
                faceDist = face_recognition.face_distance(encoded_face_train, encode_face)
                matchIndex = np.argmin(faceDist)
                if matches[matchIndex]:
                    name = classNames[matchIndex].upper().lower()
                    y1, x2, y2, x1 = faceloc
                    y1, x2, y2, x1 = y1 * 2, x2 * 5, y2 * 5, x1 * 3
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, name, (x1 + 6, y2 - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    markAttendance(name)
                else:
                    y1, x2, y2, x1 = faceloc
                    y1, x2, y2, x1 = y1 * 2, x2 * 5, y2 * 5, x1 * 3
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
                    cv2.rectangle(img, (x1, y2 - 25), (x2, y2), (0, 0, 255), cv2.FILLED)
                    cv2.putText(img, 'UNKNOWN', (x1 + 6, y2 - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
        except Exception:
            logging.info("cv2.error: Resize issue.")

        cv2.imshow('webcam', img)
        if cv2.waitKey(3) & 0xFF == ord('s'):
            name = input('Enter the Unknown Person\'s Name: ')
            capture_image(WebCam, img, name)
            WebCam.release()
            cv2.destroyAllWindows()
            os.system("python C:/Users/anmol.r/PycharmProjects/FaceRecognition/face_recog.py")
        elif cv2.waitKey(3) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    main()
    exit()