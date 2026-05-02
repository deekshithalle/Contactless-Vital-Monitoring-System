import streamlit as st
import cv2
import numpy as np
import time

from modules.camera import start_camera, get_frame, stop_camera
from modules.rppg import extract_rppg_signal
from modules.signal_processing import process_signal
from modules.face_detection import draw_face_box


st.title("📷 Capture & Analysis")

st.write("Position your face inside the frame")

FRAME_WINDOW = st.empty()

capture_button = st.button("▶ Start Capture")

# capture duration in seconds (fast demo)
CAPTURE_TIME = 8


if capture_button:

    cap = start_camera()

    signal_buffer = []

    start_time = time.time()

    st.info("Capturing signal... please stay still")

    while True:

        frame = get_frame(cap)

        if frame is None:
            st.error("Camera not working")
            break

        signal_value, face_box = extract_rppg_signal(frame)

        if face_box is not None:

            frame = draw_face_box(frame, face_box)

            if signal_value is not None:
                signal_buffer.append(signal_value)

        # convert BGR → RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        FRAME_WINDOW.image(frame)

        # stop after capture time
        if time.time() - start_time > CAPTURE_TIME:
            break

    stop_camera(cap)

    if len(signal_buffer) < 30:

        st.warning("⚠ Unable to detect signal. Try better lighting")

    else:

        bpm, rr, signal = process_signal(signal_buffer)

        # store in session
        st.session_state["bpm"] = round(bpm)
        st.session_state["rr"] = round(rr)
        st.session_state["signal"] = signal.tolist()

        st.success("Analysis complete")

        # auto move to results page
        st.switch_page("pages/4_Results.py")