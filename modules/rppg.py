import numpy as np
from modules.face_detection import detect_face


def extract_rppg_signal(frame):

    face_box = detect_face(frame)

    if face_box is None:
        return None, None

    x, y, w, h = face_box

    # select forehead region (top 40%)
    roi = frame[y:int(y + h * 0.4), x:x + w]

    if roi.size == 0:
        return None, None

    # green channel gives best pulse signal
    green_channel = roi[:, :, 1]

    signal_value = np.mean(green_channel)

    return signal_value, face_box