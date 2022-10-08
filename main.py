import cv2
print("Package Imported")

def read_image():
    img = cv2.imread("Resources/Landscape.jpg") #reads image
    print(img)
    cv2.imshow("Output", img)
    cv2.waitKey(0) #infinite delay to view image

def read_video():
    cap = cv2.VideoCapture("")
    while True:   #videos are a sequence of images : this goes through that sequence
        success, img = cap.read()
        cv2.imshow("Video" , img)
        if cv2.waitKey(1)  & 0xFF ==ord('q'):
            break

