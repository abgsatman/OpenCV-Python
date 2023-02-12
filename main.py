import cv2
import keyboard

def version():
    print("OpenCV Version is:", cv2.__version__)

def showImage():
    img = cv2.imread("src/images/logo.png")
    size = (500, 500)

    resize =cv2.resize(img, size, img,interpolation = cv2.INTER_AREA)
    cv2.imshow("resize", resize)

    cv2.waitKey(0)

version()
showImage()
#while True:
#    if keyboard.read_key() == "q":
#        quit()



