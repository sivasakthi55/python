import qrcode
img=qrcode.make("hello")
img.save("siva1.jpg")


#pip install opencv-python
import cv2
qr_img=cv2.imread("siva1.jpg")
qr_det=cv2.QRCodeDetector()
val,pts,st_code=qr_det.detectAndDecode(qr_img)
print("information:",val)