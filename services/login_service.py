import json

import pyrebase

import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate('firebase-config.json')
firebase = firebase_admin.initialize_app(cred)
pb = pyrebase.initialize_app(
    {
    'apiKey': "AIzaSyCk21RBJJA3m-G3HdmunoTsFNpy_LQVC3c",
    'authDomain': "todolist-ff2a4.firebaseapp.com",
    'databaseURL': "https://todolist-ff2a4.firebaseio.com",
    'projectId': "todolist-ff2a4",
    'storageBucket': "todolist-ff2a4.appspot.com",
    'messagingSenderId': "900316837100",
    'appId': "1:900316837100:web:6919a6d7eb571d2b3c61c9",
    'measurementId': "G-YSVNBMLY9J"
  }
)

# auth = firebase.auth()

def register_user(email, password):
    try:
        user = auth.create_user(email=email, password=password)
        print(user)
        return True, user
    except Exception as e:
        print(str(e))
        return False, str(e)

def login_user(email, password):
    try:
        user = pb.auth().sign_in_with_email_and_password(email, password)
        # print(user)
        return True, user
    except Exception as e:
        return False, e

def verify_id_token(token):
    return auth.verify_id_token(token)

if __name__ == "__main__":
    # login_user('diplavsingh@gmail.com', 'myPassword')
    register_user('dipavsingh@gmail.com', 'myPassword')