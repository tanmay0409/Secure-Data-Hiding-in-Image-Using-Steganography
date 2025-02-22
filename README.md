# 🛠 StegoCrypt-Image-Steganography-Tool

### 🎯 **What is this?**  
This is a simple tool that lets you hide a secret message inside an image and later retrieve it. The encryption and decryption are done using Python and OpenCV, and the image format used is **PNG** to avoid data loss.  

---

## 🔧 **Setup & Installation**  

### 1️⃣ Install Python  
First, download and install **Python 3.x** from [python.org](https://www.python.org/downloads/).  
**Important:** **While installing, check the box that says "Add Python to PATH"**—this will save you from a lot of headaches later!  

### 2️⃣ Check if Python and pip are installed  
Open **Command Prompt (cmd)** and run these:  
```sh
python --version
pip --version
```
If both show a version number, you’re good to go. If not, Python might not be installed correctly, or it’s missing from PATH.  

### 3️⃣ Install Required Libraries  
Once Python is installed, you need **OpenCV** to work with images. Run this in **Command Prompt (cmd)**:  
```sh
pip install opencv-python
```

### 4️⃣ Fix Common Issues (if needed)  
If you get an error like **"pip is not recognized"**, try running these commands **one by one in Command Prompt**:  
```sh
python -m ensurepip
python -m pip install --upgrade pip
```
This will make sure pip is installed and updated properly.  

---

## 🔐 **How to Use**  

### 🔹 Encrypt (Hide a Message)  
1️⃣ Place your **image file (PNG format)** in the same folder as `encrypt.py`.  
2️⃣ Open **Command Prompt**, navigate to the folder where the script is located, and run:  
   ```sh
   python encrypt.py
   ```
3️⃣ Enter your **secret message** and a **passcode** when asked.  
4️⃣ A new image called `encryptedImage.png` will be created with your hidden message inside.  

### 🔹 Decrypt (Retrieve the Message)  
1️⃣ Open **Command Prompt** in the same folder as the encrypted image and run:  
   ```sh
   python decrypt.py
   ```
2️⃣ Enter the **passcode** you used during encryption.  
3️⃣ The hidden message will be revealed!  

---

## ❗ **Troubleshooting**  

### 🛑 **"pip is not recognized" error**  
✔️ Make sure you installed Python **and** added it to **PATH** during installation.  
✔️ If the error persists, run these commands in **Command Prompt**:  
   ```sh
   python -m ensurepip
   python -m pip install --upgrade pip
   ```

### 🛑 **"Error: Image not found!"**  
✔️ Double-check that the image file is **in the same folder as the script**.  
✔️ Make sure the image is **PNG format**—JPG compression can mess up the data.  

---

## 📜 License  
This project is open-source and free to use.  

💬 **If you run into any issues, feel free to ask!** 🚀  

---

