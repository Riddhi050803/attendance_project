import cv2
import os

def register_user(roll_no, name, max_images=20):
    """
    Registers a user by capturing images with their face using a webcam.
    The images are saved in a directory named after the user's roll number and name.
    
    Parameters:
    roll_no (str): The roll number of the user.
    name (str): The name of the user.
    max_images (int): Maximum number of images to capture. Defaults to 20.
    """
    
    # Load the Haar cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
    
    # Open the camera (webcam)
    cam = cv2.VideoCapture(0)
    
    if not cam.isOpened():
        print("Error: Could not open webcam.")
        return
    
    # Create a directory for storing user images
    user_dir = f"data/{roll_no}_{name}"
    os.makedirs(user_dir, exist_ok=True)
    
    print(f"Capturing images for {name} (Roll No: {roll_no}). Press 'q' to stop.")
    
    img_count = 0  # Initialize image count
    
    while True:
        ret, frame = cam.read()  # Capture frame from camera
        if not ret:
            print("Failed to grab frame. Exiting.")
            break
        
        # Convert the frame to grayscale (necessary for face detection)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the grayscale image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
        
        # Draw rectangles around detected faces and save face images
        for (x, y, w, h) in faces:
            img_count += 1
            face_img = frame[y:y+h, x:x+w]
            img_path = os.path.join(user_dir, f"{name}_{img_count}.jpg")
            cv2.imwrite(img_path, face_img)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Display the frame with rectangles around detected faces
        cv2.imshow("Register User - Press 'q' to Quit", frame)
        
        # Stop capturing after the specified number of images
        if img_count >= max_images:
            print(f"Captured {max_images} images. Stopping.")
            break
        
        # Exit loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release camera and close windows
    cam.release()
    cv2.destroyAllWindows()
    
    print(f"User '{name}' registered with {img_count} images.")

# Example usage: register user with Roll No. '12345' and Name 'John Doe'
# register_user('12345', 'John Doe')
