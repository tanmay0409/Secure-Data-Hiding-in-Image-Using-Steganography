
# 🛠 **Secure Data Hiding in Image Using Steganography**  

### 🎯 **What is this?**  
This project allows you to **hide a secret message** inside an image and later **retrieve it**. The encryption and decryption process is done using **Python and OpenCV**, with **PNG** images for better quality and lossless data hiding.  

---

## 🔧 **Setup & Installation**  

### ✅ **Step 1: Install Python**  
1. Download and install **Python 3.x** from [python.org](https://www.python.org/downloads/).  
2. **Important:** While installing, **check the box** that says **"Add Python to PATH"** (this prevents errors later).  

### ✅ **Step 2: Check if Python and pip are installed**  
Open **Command Prompt (cmd)** and run these commands:  

```sh
python --version
pip --version
```  
✔️ If both show a version number, you're good to go.  
❌ If you see an error, Python might **not be installed correctly** or **missing from PATH**.  

### ✅ **Step 3: Install Required Libraries**  
Run the following command in **Command Prompt**:  

```sh
pip install opencv-python
```  

This installs **OpenCV**, which is used for image processing.  

### 🛠 **Fix Common Issues (if needed)**  
If you see **"pip is not recognized"**, try running:  

```sh
python -m ensurepip
python -m pip install --upgrade pip
```  
This ensures **pip** is installed and updated.  

---

## 🔐 **How to Use**  

### 🔹 **Encrypt (Hide a Message in an Image)**  
1️⃣ Place your **image file (PNG format)** in the same folder as `encrypt.py`.  
2️⃣ Open **Command Prompt**, navigate to the script’s folder, and run:  

```sh
python encrypt.py
```  

3️⃣ Enter your **secret message** and a **passcode** when asked.  
4️⃣ A new **encrypted image** (`encryptedImage.png`) will be created, containing your hidden message.  

### 🔹 **Decrypt (Retrieve the Hidden Message)**  
1️⃣ Open **Command Prompt** in the same folder as the encrypted image and run:  

```sh
python decrypt.py
```  

2️⃣ Enter the **same passcode** you used during encryption.  
3️⃣ Your hidden message will be **revealed**!  

---

## ❗ **Troubleshooting**  

### 🛑 **Issue: "pip is not recognized"**  
✔️ Ensure Python is installed and **added to PATH**.  
✔️ If the issue persists, run these:  

```sh
python -m ensurepip
python -m pip install --upgrade pip
```  

### 🛑 **Issue: "Error: Image not found!"**  
✔️ Make sure the image file is **in the same folder as the script**.  
✔️ **Use PNG format** (JPG can distort hidden data).  

---

## 📸 Screenshot

![Code Image](https://raw.githubusercontent.com/tanmay0409/StegoCrypt-Image-Steganography-Tool/main/code_image.png)

---

### 🚀 **Enjoyed this project?**  
If you found this useful, **give it a ⭐ on GitHub!** 😊  

---

###  **🚨 Disclaimer**  

This project is for educational and ethical purposes only. The author is not responsible for any misuse, illegal activities, or harm caused by using this code. This project is intended for learning purposes only. The creator is not liable for any unintended consequences arising from the use of this code. Use it ethically and responsibly.

---
