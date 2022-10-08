import cv2

print("Package Imported")


def read_image():
    img = cv2.imread("Resources/Landscape.jpg")  # reads image
    print(img)
    cv2.imshow("Output", img)
    cv2.waitKey(0)  # infinite delay to view image


def read_video():
    cap = cv2.VideoCapture("")
    while True:  # videos are a sequence of images : this goes through that sequence
        success, img = cap.read()
        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def read_webcam():
    cap = cv2.VideoCapture(0)  # 0 uses the default webcame
    cap.set(3, 640)  # width &
    cap.set(4, 480)  # height
    cap.set(10, 100)  # changing brightness

    while True:  # videos are a sequence of images : this goes through that sequence
        success, img = cap.read()
        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # stops when you press q
            break


def image_processing():
    img = cv2.imread("Resources/Landscape.jpg")  # reads image
    # changes your image to different color spaces
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray Image", imgGray)
    imgCanny = cv2.Canny(img, 100, 100) #determine the parameters and what they define
    cv2.imshow("Canny Image", imgCanny)  # detects the edges
    cv2.waitKey(0)


image_processing()
