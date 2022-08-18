import cv2
import numpy as np
import mtcnn
from architecture import *
from train_v2 import normalize,l2_normalizer
from scipy.spatial.distance import cosine
from tensorflow.keras.models import load_model
import pickle
from playsound import playsound
from threading import Thread


confidence_t=0.99
recognition_t=0.5
required_size = (160,160)

def get_face(img, box):
    x1, y1, width, height = box
    x1, y1 = abs(x1), abs(y1)
    x2, y2 = x1 + width, y1 + height
    face = img[y1:y2, x1:x2]
    return face, (x1, y1), (x2, y2)

def get_encode(face_encoder, face, size):
    face = normalize(face)
    face = cv2.resize(face, size)
    encode = face_encoder.predict(np.expand_dims(face, axis=0))[0]
    return encode


def load_pickle(path):
    with open(path, 'rb') as f:
        encoding_dict = pickle.load(f)
    return encoding_dict

def detect(img, detector, encoder, encoding_dict):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = detector.detect_faces(img_rgb)
    name = 'nao amigo'

    for res in results:
        if res['confidence'] < confidence_t:
            continue
        face, pt_1, pt_2 = get_face(img_rgb, res['box'])
        encode = get_encode(encoder, face, required_size)
        encode = l2_normalizer.transform(encode.reshape(1, -1))[0]

        distance = float("inf")
        for db_name, db_encode in encoding_dict.items():
            dist = cosine(db_encode, encode)
            if dist < recognition_t and dist < distance:
                name = db_name
                distance = dist

        if name == 'nao amigo':
            cv2.rectangle(img, pt_1, pt_2, (0, 0, 255), 2)
            cv2.putText(img, "Nao amigo", pt_1, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)
        else:
            name = "amigo"
            cv2.rectangle(img, pt_1, pt_2, (0, 255, 0), 2)
            cv2.putText(img, "amigo", (pt_1[0], pt_1[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 200, 200), 2)
    return img, name


def latir(nome):
    if nome == "nao amigo":
        playsound('Barks/notfriendly.mp3')
    elif nome == "amigo":
        playsound('Barks/friendly.mp3')


if __name__ == "__main__":
    print("iniciando")
    required_shape = (160,160)
    face_encoder = InceptionResNetV2()
    path_m = "facenet_keras_weights.h5"

    print("carregando pesos")
    face_encoder.load_weights(path_m)
    encodings_path = 'encodings/encodings.pkl'

    print("iniciando face detector")
    face_detector = mtcnn.MTCNN()
    encoding_dict = load_pickle(encodings_path)

    print('iniciando camera')
    cap = cv2.VideoCapture(0)
    nome = "nao amigo"
    nomeanterior = nome

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("CAM NOT OPEND")
            break

        frame, nome = detect(frame, face_detector, face_encoder, encoding_dict)
        cv2.imshow('camera', frame)
        if nome != nomeanterior:
            nomeanterior = nome
            Thread(target=latir, args=(nome,)).start()


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
