import cv2
import numpy as np
import pyautogui
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# Global variables
recording = False
paused = False
out = None
prev_mouse_pos = None  # Initialize prev_mouse_pos here

def toggle_recording():
    global recording, out
    if recording:
        # Stop recording
        stop_recording()
        # Update button text
        record_button.config(text="Start Recording")
    else:
        # Start recording
        start_recording()
        # Update button text
        record_button.config(text="Stop Recording")

def start_recording():
    global recording, out
    if recording:
        messagebox.showwarning("Warning", "Already recording!")
        return
    
    codec = cv2.VideoWriter_fourcc(*"XVID")
    today_date = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    output_filename = f'recorded_screen_{today_date}.avi'
    fps = 10.0
    resolution = pyautogui.size()  # Get the resolution of the screen
    out = cv2.VideoWriter(output_filename, codec, fps, resolution)
    recording = True

def stop_recording():
    global recording, out
    if not recording:
        messagebox.showwarning("Warning", "Not recording!")
        return
    
    recording = False
    out.release()

def pause_recording():
    global paused
    paused = not paused

def update_gui():
    global prev_mouse_pos  # Declare prev_mouse_pos as global
    if recording and not paused:
        # Take screenshot using pyautogui
        img = pyautogui.screenshot()

        # Convert the screenshot to a numpy array
        frame = np.array(img)

        # Convert RGB to BGR (OpenCV uses BGR)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Get current mouse position
        mouse_x, mouse_y = pyautogui.position()

        # Draw a circle at the current mouse position
        cv2.circle(frame, (mouse_x, mouse_y), 5, (0, 0, 255), -1)

        # Draw a line to indicate movement from previous position
        if prev_mouse_pos:
            cv2.line(frame, prev_mouse_pos, (mouse_x, mouse_y), (0, 255, 0), thickness=2)

        # Update previous mouse position
        prev_mouse_pos = (mouse_x, mouse_y)

        # Write the frame to the video file
        out.write(frame)

        # Display the recording in real-time (optional)
        # This part is omitted for simplicity, as displaying in tkinter can be complex.
        # You may choose to show frames using a label or another mechanism.

    # Schedule the next update after 10 milliseconds
    root.after(10, update_gui)

# Create tkinter GUI
root = tk.Tk()
root.title("Screen Recorder")

# Single function button for recording
record_button = tk.Button(root, text="Start Recording", command=toggle_recording, width=20, height=2)
record_button.pack(pady=10)

pause_button = tk.Button(root, text="Pause/Resume", command=pause_recording, width=20, height=2)
pause_button.pack(pady=10)

# Start GUI update loop
update_gui()

# Start the tkinter main loop
root.mainloop()

# Release the VideoWriter and close all windows when tkinter exits
if out:
    out.release()
cv2.destroyAllWindows()
