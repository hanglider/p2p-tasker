import cv2

def open_image(crop):
    image = cv2.imread("negr.jpg")
    croped = image[crop]
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
