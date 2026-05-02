# 🩺 Contactless Vital Sign Monitoring System using rPPG

## 📌 Overview

This project is a **Contactless Vital Sign Monitoring System** that estimates **Heart Rate (BPM)** and **Respiration Rate** using only a webcam, without any physical sensors.

It uses **remote Photoplethysmography (rPPG)** to detect subtle color changes in the facial skin caused by blood flow and processes them using signal processing techniques.

---

## 🎯 Features

* 📷 Webcam-based face detection
* ❤️ Heart Rate (BPM) estimation
* 🫁 Breathing Rate estimation
* 📊 Pulse signal graph visualization
* 👤 User login & profile management
* 🗂️ History storage with date & time
* 🌐 Interactive dashboard using Streamlit

---

## ⚙️ Technologies Used

* **Python**
* **OpenCV** – Face detection & video capture
* **NumPy** – Numerical computations
* **SciPy** – Signal processing (FFT, filtering)
* **Streamlit** – User interface
* **Matplotlib** – Data visualization
* **Pandas** – Data storage & handling

---

## 🧠 Working Principle

1. Capture facial video using webcam
2. Detect face and extract **ROI (forehead region)**
3. Extract **green channel signal** (best for blood flow detection)
4. Apply filtering to remove noise
5. Use **FFT (Fast Fourier Transform)** to find dominant frequency
6. Convert frequency into:

   * Heart Rate (BPM)
   * Respiration Rate
7. Display results and store in history

---

## 📂 Project Structure

```
vital_monitor/
│
├── app.py
├── pages/
│   ├── 1_Login.py
│   ├── 2_User_Profile.py
│   ├── 3_Capture_Analysis.py
│   ├── 4_Results.py
│   ├── 5_History.py
│
├── modules/
│   ├── face_detection.py
│   ├── signal_processing.py
│   ├── rppg.py
│
├── data/
│   └── records.csv
│
├── assets/
│   └── heartbeat.gif
│
└── requirements.txt
```

---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/vital-monitor.git
cd vital-monitor
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the application

```bash
python -m streamlit run app.py
```

---

## 🌐 Deployment

The project can be deployed using **Streamlit Community Cloud**.

⚠️ Note: Webcam access may not work in cloud deployment due to browser restrictions.

---

## 📊 Sample Output

* Heart Rate: 70–90 BPM
* Respiration Rate: 12–20 breaths/min
* Pulse waveform graph

---

## 📈 Accuracy

* Heart Rate Accuracy: ~90–93%
* Average Error: ±2 BPM
* Works best under stable lighting and minimal movement

---

## ⚠️ Limitations

* Sensitive to lighting conditions
* Affected by face movement
* Depends on camera quality
* Not a replacement for medical devices

---

## 🚀 Future Scope

* Deep learning-based rPPG for better accuracy
* SpO₂ and blood pressure estimation
* Mobile app development
* Cloud-based data storage
* Real-time alerts for abnormal values

---

## 👨‍💻 Authors

* Deekshith Alle
* Team Members - Harisha , Bhagyasri , Koushik Tej

---

## 📢 Note

This project is a **prototype for academic purposes** and provides approximate results.

---

⭐ If you found this useful, give it a star!
