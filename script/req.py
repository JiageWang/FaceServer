import requests

#
# files={'2.jpg',open('2.jpg','rb'),'image/png'}
files = {'img': ('1.jpg', open('1.jpg', 'rb'), 'image/png')}
r = requests.request("POST", url='http://127.0.0.1:5002/face', files=files,
                     data={'name': 'jiage', 'number': '2180702', 'device':3})
# r = requests.request("GET",url='http://127.0.0.1:5001/data/record?time=20190616_20190619&device=1')

print(r.text)

# from hyperlpr import *
# import cv2
#
# img = cv2.imread('2.JPG')
# r = HyperLPR_PlateRecogntion(img)
