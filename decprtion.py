import cv2

img = cv2.imread("encryptedImage.png")  # Use PNG format
if img is None:
    print("Error: Encrypted image not found!")
    exit()

password = input("Enter passcode for Decryption: ")

msg_length = int(img[0, 0, 0]) * 256 + int(img[0, 0, 1])  # Read stored message length

m, n, z = 1, 0, 2  # Start reading from pixel (0,1)

message = ""
for _ in range(msg_length):
    char = chr(int(img[n, m, z]))  # Ensure we read the correct pixel value
    message += char
    m += 1
    if m >= img.shape[1]:  # Move to next row
        m = 0
        n += 1

print("Decryption message:", message)
