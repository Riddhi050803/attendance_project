**Face Recognition Attendance System**
Overview
This is a face recognition-based attendance system that uses OpenCV and Python. The system captures images from the webcam, detects faces, and matches them with registered faces stored locally. If a match is found, the attendance is marked for that user, and the system ensures that attendance can only be marked once within 50 seconds. Once the attendance is successfully marked, the program automatically closes.

Features
Face Detection: Detects faces in real-time using OpenCV's Haar Cascade Classifier.
Face Recognition: Matches detected faces with known registered faces stored in a local directory.
Attendance Marking: Records attendance in a text file with a timestamp.
50-second Limit: Prevents multiple attendance marks within 50 seconds for the same person.
Automatic Exit: Automatically closes the program once attendance is successfully marked for a recognized user.
User-Friendly: Displays the name of the recognized user on the webcam feed.
Requirements
Python 3.x
OpenCV
Numpy
Install dependencies
To install the necessary Python libraries, run the following command:
pip install opencv-python numpy


**Directory Structure**
project_directory/
├── data/                         # Directory for storing registered users' images (one folder per user)
│   ├── user1/
│   │   ├── img1.jpg
│   │   ├── img2.jpg
│   └── user2/
│       ├── img1.jpg
│       ├── img2.jpg
├── haarcascade/
│   ├── haarcascade_frontalface_default.xml  # Haar cascade for face detection
├── attendance.txt                # Attendance file storing name and timestamp
├── face_recognition_attendance.py  # Main script
└── README.md                     # This file

data/ Directory
Place user images in the data/ directory, where each user has their own folder with multiple images for better face recognition accuracy.
Image files should be named any way you prefer (e.g., img1.jpg, img2.jpg).
haarcascade_frontalface_default.xml
This file is required for the face detection algorithm. You can download it from here.

Usage
Register User Images: Place the images of the users you want to recognize in the data/ folder. Each user should have their own folder with at least one image.

Run the Program:

Run the following command to start the program:

python app.py

The program will open the webcam feed and start detecting faces. When a recognized face is detected, the system will mark attendance and print the message Attendance marked for <user_name> in the terminal. The program will then automatically exit.

Attendance File: Attendance will be recorded in the attendance.txt file in the format:

<user_name>,<timestamp>

Exit the Program Manually: You can also exit the program at any time by pressing q on the keyboard.

