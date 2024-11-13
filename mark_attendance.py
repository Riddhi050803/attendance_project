import cv2
import os
import numpy as np
from datetime import datetime, timedelta

# Dictionary to store the last attendance time for each user
last_attendance_time = {}

def mark_attendance(name):
    """Mark attendance in a file if 50 seconds have passed since the last mark for the same user."""
    now = datetime.now()
    
    # Check if the user has marked attendance within the last 50 seconds
    if name in last_attendance_time:
        elapsed_time = now - last_attendance_time[name]
        if elapsed_time < timedelta(seconds=150):
            print(f"Attendance for {name} already marked recently. Try again after {50 - elapsed_time.seconds} seconds.")
            return False  # Return False if attendance is not marked
    
    # Update last attendance time and mark attendance
    last_attendance_time[name] = now
    with open("attendance.txt", "a") as file:
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{name},{dt_string}\n")
    print(f"Attendance marked for {name}")
    return True  # Return True if attendance is successfully marked

def recognize_user():
    face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
    cam = cv2.VideoCapture(0)
    
    if not cam.isOpened():
        print("Error: Could not open webcam.")
        return
    
    # Load registered images and preprocess them
    known_faces = {}
    for folder in os.listdir("data"):
        path = os.path.join("data", folder)
        if os.path.isdir(path):
            images = []
            for img_name in os.listdir(path):
                img_path = os.path.join(path, img_name)
                img = cv2.imread(img_path, 0)  # Read in grayscale
                if img is not None:
                    images.append(img)
            known_faces[folder] = images
    
    print("Ready to recognize faces and mark attendance.")
    
    while True:
        ret, frame = cam.read()  # Capture frame
        if not ret:
            print("Failed to grab frame. Exiting.")
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)  # Detect faces

        for (x, y, w, h) in faces:
            face_img = gray[y:y+h, x:x+w]  # Extract the face from the image
            matched_name = None

            # Compare the captured face with known faces using template matching
            for name, images in known_faces.items():
                for img in images:
                    result = cv2.matchTemplate(face_img, img, cv2.TM_CCOEFF_NORMED)
                    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
                    if max_val > 0.6:  # Match threshold
                        matched_name = name
                        break
                if matched_name:
                    break
            
            if matched_name:
                # Mark attendance if user is matched
                if mark_attendance(matched_name):
                    # Exit the loop if attendance is marked
                    print("Attendance successfully marked. Exiting.")
                    cam.release()
                    cv2.destroyAllWindows()
                    return
                cv2.putText(frame, f"Attendance: {matched_name}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            else:
                cv2.putText(frame, "Unknown", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            
            # Draw a rectangle around the face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow("Mark Attendance - Press 'q' to Quit", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

# Example usage: To start face recognition and mark attendance
recognize_user()
