# Windows Screen Recorder

A lightweight and easy-to-use **Windows Screen Recorder** built with Python. This application records your screen and saves it as a video file. It can be run directly as a Python script during development or packaged into a standalone Windows executable (`.exe`) for distribution.

## Features

* Record the entire screen
* Save recordings as video files
* Lightweight and easy to use
* Pure Python implementation
* Can be packaged as a standalone Windows executable

---

# Requirements

* Windows 10/11
* Python 3.9 or newer (recommended)

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/sherz12r/screen_video_recorder_windows.git
cd screen_video_recorder_windows
```

## 2. Create a virtual environment (Optional)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

Run the application using:

```bash
python recorder.py
```

Replace `recorder.py` with your actual Python filename if different.

---

# Building a Windows Executable (.exe)

Install PyInstaller:

```bash
pip install pyinstaller
```

Build the executable:

```bash
py -m pyinstaller --onefile --noconsole recorder.py
```

The generated executable will be located in:

```
dist/
```

Run:

```
dist/recorder.exe
```

---

# Project Structure

```
screen_video_recorder_windows/
│
├── recorder.py
├── requirements.txt
├── README.md
└── dist/
```

---

# Installing New Dependencies

Whenever a new package is installed, regenerate the requirements file:

```bash
pip freeze > requirements.txt
```

---

# License

This project is provided for educational and personal use. Modify and distribute it according to your project's license.
