import cv2
import paramiko
import numpy as np

def capturecamera_feed():
    cap = cv2.VideoCapture(0)  # Use 0 for the default camera
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Display the frame locally
        cv2.imshow('Camera Feed', frame)

        # Send the frame over SSH
        send_frame_over_ssh(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def send_frame_over_ssh(frame):
    # Initialize SSH connection
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('your_ssh_host', username='your_username', password='your_password')

    # Encode the frame as JPEG before sending
    , buffer = cv2.imencode('.jpg', frame)
    jpgastext = buffer.tobytes()

    # Send the frame data
    sftp = ssh.opensftp()
    with sftp.file('/path/to/save/frame.jpg', 'wb') as f:
        f.write(jpgas_text)

    # Close SSH connection
    ssh.close()

if __name == "__main":
    capture_camera_feed()