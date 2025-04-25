# 📄 Image Forgery Detection Using CNN and ELA

Detect image manipulations using **Error Level Analysis (ELA)** combined with a **Convolutional Neural Network (CNN)** model.

---

## 🛠 Project Structure

```
ImageForgeryDetection_CNN_ELA/
│
├── main.py               # Main entry point to run the project
├── utils/
│   └── ela_processing.py # Functions for Error Level Analysis
├── models/
│   └── cnn_model.py       # CNN model definition
├── dataset/              # Folder containing images (real & forged)
├── outputs/              # Saved models, plots, and results
└── README.md             # Project documentation (this file)
```

---

## 🧠 How It Works

1. **Error Level Analysis (ELA)** is applied to images to detect inconsistencies.
2. ELA-transformed images are fed into a **Convolutional Neural Network (CNN)**.
3. CNN learns patterns that distinguish between **authentic** and **forged** images.
4. The trained model predicts whether new images are **real** or **tampered**.

---

## 🚀 How to Run

### 1. Install Requirements

First, make sure you have Python 3.10+ installed.

Install required Python libraries:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install tensorflow numpy matplotlib pillow scikit-learn
```

*(Let me know if you want me to generate a full `requirements.txt` too!)*

---

### 2. Run the Project

```bash
python main.py
```

It will:
- Perform ELA on dataset images
- Train the CNN model
- Save accuracy/loss graphs
- Save the trained model

---

## 📊 Example Outputs

- **Accuracy Curve**  
  ![Training and Validation Accuracy](outputs/accuracy_plot.png)

- **Loss Curve**  
  (optional: can be generated too)

- **Saved Model**  
  (e.g., `outputs/cnn_model.h5`)

---

## ⚡ Results

- Training Accuracy: **100%**
- Validation Accuracy: **100%**
- Model converges quickly, showing excellent learning capability on the given dataset.

---

## 🧪 Technologies Used

- Python 3.10
- TensorFlow / Keras
- NumPy
- Matplotlib
- Pillow (PIL)
- Scikit-learn

---

## 📚 References

- [Error Level Analysis Explained](https://www.forensically.net/ela/)
- [TensorFlow Documentation](https://www.tensorflow.org/)
- [CNNs for Image Classification](https://cs231n.github.io/convolutional-networks/)

---

## 🙌 Acknowledgements

This project was inspired by the need for **reliable image forgery detection** using simple but powerful techniques combining **forensic analysis** and **deep learning**.

---

## ✨ Future Improvements

- Test on larger and more diverse datasets
- Add data augmentation techniques
- Try advanced CNN architectures (like ResNet, MobileNet)
- Deploy as a web app for easier use

---

## 👩‍💻 Author

**Sukanya Ghosh**  
[GitHub](https://github.com/sukanyaghosh74) | [LinkedIn](https://www.linkedin.com/in/sukanya-ghosh-706129274/)

---

# ⭐ If you find this project useful, feel free to give it a ⭐ on GitHub!
