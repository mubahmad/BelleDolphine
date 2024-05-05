import cv2
import pyqrcode

Hadidi = cv2.imread("Mosaissa.png")
Ali=cv2.QRCodeDetector()
val,pts,code = Ali.detectAndDecode(Hadidi)
print(val)
