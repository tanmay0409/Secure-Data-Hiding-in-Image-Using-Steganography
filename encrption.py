import cv2
import os

img = cv2.imread("mypic.png")  # Use PNG instead of JPG to avoid compression issues
if img is None:
    print("Error: Image not found!")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Store message length
msg_length = len(msg)
img[0, 0, 0] = msg_length // 256  # High byte
img[0, 0, 1] = msg_length % 256   # Low byte

m, n, z = 1, 0, 2  # Start encoding from pixel (0,1)

for char in msg:
    img[n, m, z] = ord(char)
    m += 1
    if m >= img.shape[1]:  # Move to next row
        m = 0
        n += 1

cv2.imwrite("encryptedImage.png", img)  # Save as PNG
os.system("start encryptedImage.png")
print("Encryption Done! Image saved as encryptedImage.png")
