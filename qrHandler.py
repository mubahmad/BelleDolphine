from picamera2.picamera2 import Picamera2
import cv2
import numpy as np
import RPi.GPIO as GPIO
from movement import move
from time import sleep

def getInRoom():
    move('w',20)
    sleep(0.5)
    move('a',10)
    sleep(0.5)
    move('d',10)
    sleep(0.5)
    move('a',50)
    sleep(0.5)
    move('w',20)
    sleep(2)
    move('d',50)
    sleep(0.3)
    return 6





def ratio_and_center_of_quadrilateral_area_to_image(image):
    """
    Calculate the ratio of the area of a quadrilateral detected in an image to the total area of the image,
    and find the center of the quadrilateral.
    
    Parameters:
    image_path (str): Path to the image file.
    
    Returns:
    tuple: (retval, ratio, center) where:
        - retval (bool): Whether a quadrilateral was detected.
        - ratio (float or None): Ratio of the quadrilateral area to the image area (None if not detected).
        - center (tuple or None): (x, y) coordinates of the quadrilateral's center (None if not detected).
    """
    def calculate_area_of_quadrilateral(points):
        """
        Calculate the area of a quadrilateral given four points using the Shoelace formula.
        
        Parameters:
        points (list of tuples): List of four (x, y) tuples representing the vertices of the quadrilateral.
        
        Returns:
        float: Area of the quadrilateral.
        """
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        x4, y4 = points[3]
        
        # Shoelace formula
        area = 0.5 * abs(x1*y2 + x2*y3 + x3*y4 + x4*y1 - y1*x2 - y2*x3 - y3*x4 - y4*x1)
        return area
    
    def calculate_center_of_quadrilateral(points,imageWidth):
        """
        Calculate the center (centroid) of a quadrilateral given four points.
        
        Parameters:
        points (list of tuples): List of four (x, y) tuples representing the vertices of the quadrilateral.
        
        Returns:
        tuple: (x, y) coordinates of the quadrilateral's center.
        """
        x_coords = [p[0] for p in points]
    
        # Calculate the average x-coordinate
        avg_x = sum(x_coords) / 4
        
        
        center = (avg_x / image_width) * 2 - 1
        

        return center
    
        
    # Check if the image was successfully loaded
    if image is None:
        raise ValueError("Image not found or unable to load.")
    
    # Get image dimensions
    image_height, image_width = image.shape
    image_area = image_height * image_width
    
    # Create a QRCode detector
    detector = cv2.QRCodeDetector()
    
    # Detect and decode the QR code
    retval, points, straight_qrcode = detector.detectAndDecode(image)
    
    # Check if a QR code was detected
    if retval and points is not None:
        points = points[0]  # Get the first set of points if multiple are detected
        
        # Calculate the area of the quadrilateral
        quadrilateral_area = calculate_area_of_quadrilateral(points)
        
        # Calculate the ratio
        ratio = quadrilateral_area / image_area
        
        # Calculate the center of the quadrilateral
        center = calculate_center_of_quadrilateral(points,image_width)
        
        return retval, ratio, center
    else:
        return retval, None, None

# Example usage


# camera = Picamera2()
# camera.start()

# print("starting")

# i = 0 
# while True:
#     print('got one')
#     frame = camera.capture_array()
#     frame =cv2.flip(frame, 0)
#     retval, ratio, center = ratio_and_center_of_quadrilateral_area_to_image(frame)

#     if retval:
#         print(f"Ratio of quadrilateral area to image area: {ratio:.4f}")
#         print(f"Center of quadrilateral: {center}")
#         print(f"qrcode: {retval}")
#         break
#     else:
#         print("No quadrilateral detected.")
#         cv2.imwrite(f"img{i}.png", frame)
#         if cv2.waitKey(10) == ord("q"):
#             break


