import requests
#
# files={'IMG_00000005.jpg',open('IMG_00000005.jpg','rb'),'image/png'}
files={'img':('IMG_00000005.jpg',open('IMG_00000005.jpg','rb'),'image/png')}
r = requests.request("POST",url='http://127.0.0.1:5001/face' , files=files, data={'device':1})
# r = requests.request("GET",url='http://127.0.0.1:5001/data/record?time=20190616_20190619&device=1')

print(r.text)


# from hyperlpr import *
# import cv2
#
# img = cv2.imread('2.JPG')
# r = HyperLPR_PlateRecogntion(img)
