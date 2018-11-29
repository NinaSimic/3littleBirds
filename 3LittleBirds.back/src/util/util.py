'''
Created on Nov 28, 2018

@author: Petar
'''

import os

from PIL import Image
import requests 


def verifyFaces(face1, face2):
    faceId1 = getFaceId(face1)
    faceId2 = getFaceId(face2)
    
    verifyFaceIDs(faceId1, faceId2)

def verifyFaceIDs(id1, id2):    
    # defining the api-endpoint  
    API_ENDPOINT = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/verify"
      
    # your API key here 
    API_KEY = "0bca6c3c510e489ea9c4c11682cad5cb"
    
    headers = {'Ocp-Apim-Subscription-Key': API_KEY, 'Content-Type':'application/json'}
    
    data = {'faceId1': id1, 'faceId2': id2}
    
    r = requests.post(API_ENDPOINT, json=data, headers=headers)
    
    print r.json()

def getFaceId(image):
    # defining the api-endpoint  
    API_ENDPOINT = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=false"
      
    # your API key here 
    API_KEY = "0bca6c3c510e489ea9c4c11682cad5cb"
    
    headers = {'Ocp-Apim-Subscription-Key': API_KEY, 'Content-Type': 'application/octet-stream', 'Content-Length':str(os.path.getsize(image))}
      
    # your source code here 
    
    #img2 = change_contrast(Image.open(image), 50)
    img2 = Image.open(image)
    
    
    img2.save("tmp.jpg")
    
    data = open("tmp.jpg", 'rb').read()
    
    r = requests.post(API_ENDPOINT, data=data, headers=headers)
    
    print r.json()
    
    return r.json()[0]['faceId']


def prepareIdFace(idCard):
    API_KEY = "AIzaSyC0v9PGDcx_p1ynLqqBYKenCrbTpjJ8JQc"
    
    API_ENDPOINT =  "https://vision.googleapis.com/v1/images:annotate?key="+API_KEY


def change_contrast(img, level):
    factor = (259 * (level + 255)) / (255 * (259 - level))
    def contrast(c):
        return 128 + factor * (c - 128)
    return img.point(contrast)    

if __name__ == '__main__':
    #getFaceId("faca5.jpg")
    verifyFaces('faca4.jpg','faca2.jpg')
    

