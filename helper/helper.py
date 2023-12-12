import os

def helper():
    osEnv = {
        "FIREBASE_APIKEY": os.getenv("FIREBASE_APIKEY"),
        "FIREBASE_AUTHDOMAIN": os.getenv("FIREBASE_AUTHDOMAIN"),
        "FIREBASE_PROJECTID": os.getenv("FIREBASE_PROJECTID"),
        "FIREBASE_STORAGEBUCKET": os.getenv("FIREBASE_STORAGEBUCKET"),
        "FIREBASE_MESSAGINGSENDERID": os.getenv("FIREBASE_MESSAGINGSENDERID"),
        "FIREBASE_APPID": os.getenv("FIREBASE_APPID"),
        "FIREBASE_MEASUREMENTID": os.getenv("FIREBASE_MEASUREMENTID"),
    }
    
    return osEnv