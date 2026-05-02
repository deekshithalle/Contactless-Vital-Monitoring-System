import cv2


def start_camera():

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise Exception("Camera not accessible")

    return cap


def get_frame(cap):

    ret, frame = cap.read()

    if not ret:
        return None

    return frame


def stop_camera(cap):

    cap.release()