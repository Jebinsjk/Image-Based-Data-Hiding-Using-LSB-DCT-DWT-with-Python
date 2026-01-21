# 🖼️ Image Watermarking with LSB & DCT

This project demonstrates **digital watermarking** techniques using **Least Significant Bit (LSB)** and **Discrete Cosine Transform (DCT)** methods.  
It allows you to **encode** hidden data into an image, **decode** it back, and **compare** the effects of both watermarking methods visually and statistically.

---

## 📌 Features
- **LSB Encoding & Decoding**: Embed hidden messages into the least significant bits of an image without noticeable visual change.
- **DCT Encoding & Decoding**: Use frequency-domain transformations for more robust watermarking.
- **Comparison Tool**: Evaluate images using MSE (Mean Square Error) and PSNR (Peak Signal-to-Noise Ratio).
- **Side-by-Side Visualization**: View original, LSB, and DCT images together for quick visual analysis.

---

## 📂 Project Structure
watermarking/
│── Original_image/         # Stores original input images
│── Encoded_image/          # Stores watermarked images
│── Decoded_image/          # Stores decoded output
│── Comparison_result/      # Stores MSE & PSNR results (.xls)
│── watermarking.py         # Main script (encode, decode, compare)
│── compare_images.py       # Script to create comparison visuals

---

## 🚀 How to Run

### **1. Clone the repository**
```bash
git clone https://github.com/yourusername/image-watermarking.git
cd image-watermarking

install dependencies
pip install opencv-python numpy matplotlib xlwt

run the main program:
python3 watermarking.py

Follow the prompts:
	•	1 → Encode
	•	2 → Decode
	•	3 → Compare

🧪 Technologies Used
	•	Python 3
	•	OpenCV – Image processing
	•	NumPy – Numerical operations
	•	Matplotlib – Visualization
	•	xlwt – Excel report generation

📖 Background

Digital watermarking is a technique for embedding information into a digital signal in a way that is imperceptible but can be later extracted or detected.
This project focuses on spatial-domain (LSB) and frequency-domain (DCT) methods to explore the trade-off between imperceptibility and robustness.

⸻

Made with 🧠 by Megh Mehta# steganography
