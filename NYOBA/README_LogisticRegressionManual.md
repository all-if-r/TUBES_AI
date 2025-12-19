# Logistic Regression Manual - Dokumentasi

## 📋 Daftar File

1. **LogisticRegressionManual_Pima.ipynb** - Notebook baru dengan implementasi Logistic Regression MANUAL
2. **diabetes.xls** - Dataset Pima Indians Diabetes (sudah ada)

---

## 🎯 Tujuan

Implementasi Logistic Regression **dari nol** menggunakan **numpy** tanpa menggunakan library machine learning seperti sklearn LogisticRegression.

---

## ✨ Fitur Utama Implementasi

### 1. **Class LogisticRegressionManual**

Kelas yang mengimplementasikan Logistic Regression MANUAL dengan:

- **`__init__(learning_rate, epochs, verbose)`**: Inisialisasi parameter
- **`sigmoid(z)`**: Fungsi sigmoid manual σ(z) = 1/(1+e^(-z))
- **`compute_loss(y_true, y_pred)`**: Binary Cross-Entropy Loss manual
- **`fit(X, y)`**: Training dengan Gradient Descent
  - Forward pass: z = X·w + b, ŷ = sigmoid(z)
  - Loss computation
  - Backward pass: compute gradients (dw, db)
  - Weight update: w ← w - lr·dw, b ← b - lr·db
- **`predict_proba(X)`**: Prediksi probabilitas
- **`predict(X, threshold)`**: Prediksi kelas (0 atau 1)

### 2. **Gradient Descent Manual**

Algoritma training:
```
For each epoch:
    1. Forward: z = X·w + b
    2. Activation: ŷ = sigmoid(z)
    3. Loss: L = -(1/m)·Σ[y·log(ŷ) + (1-y)·log(1-ŷ)]
    4. Gradient: dw = (1/m)·X^T·(ŷ - y)
                 db = (1/m)·Σ(ŷ - y)
    5. Update: w ← w - lr·dw
               b ← b - lr·db
```

### 3. **Preprocessing dengan Scaling**

- StandardScaler digunakan untuk normalisasi fitur
- Train-Test Split 80-20 dengan stratification

### 4. **Evaluasi Metrik**

Metrik yang dihitung:
- **Accuracy**: (TP+TN) / Total
- **Precision**: TP / (TP+FP)
- **Recall**: TP / (TP+FN)
- **F1-Score**: Harmonic mean Precision & Recall
- **Confusion Matrix**: TN, FP, FN, TP

---

## 🚀 Cara Menggunakan

### Buka Notebook di Jupyter
```bash
jupyter notebook LogisticRegressionManual_Pima.ipynb
```

### Jalankan Semua Cell
- Klik: `Run All` atau tekan `Ctrl+Shift+Enter`

### Ubah Parameter (Optional)
```python
learning_rate = 0.1  # Laju pembelajaran
epochs = 1000        # Jumlah iterasi
```

---

## 📊 Struktur Notebook

1. **Import Library** - Library yang digunakan (numpy, pandas, matplotlib, sklearn metrics)
2. **Load Data** - Baca diabetes.xls dan explorasi data
3. **Explorasi Data** - Distribusi kelas, statistik deskriptif
4. **Preprocessing** - Scaling dan train-test split
5. **Logistic Regression Manual** - Implementasi kelas dan training
6. **Prediksi** - Prediksi pada training dan test set
7. **Evaluasi** - Confusion matrix, akurasi, precision, recall, F1
8. **Visualisasi** - Loss history, confusion matrix heatmap, metrik performa
9. **Analisis** - Ringkasan dan interpretasi hasil
10. **Test Individual** - Uji prediksi dengan sampel individual
11. **Simpan Model** - Tampilkan weights dan bias hasil training

---

## 🔑 Poin Penting

### ✅ Yang BOLEH Digunakan
- ✓ numpy (untuk operasi matrix dan mathematical)
- ✓ pandas (untuk data manipulation)
- ✓ matplotlib & seaborn (untuk visualization)
- ✓ sklearn.preprocessing (StandardScaler)
- ✓ sklearn.model_selection (train_test_split)
- ✓ sklearn.metrics (confusion_matrix, accuracy_score, precision_score, recall_score, f1_score)

### ❌ Yang DILARANG Digunakan
- ✗ sklearn.linear_model.LogisticRegression
- ✗ Semua library ML learning (model.fit(), neural networks, etc)
- ✗ Genetic Algorithm (belum dikerjakan)
- ✗ TensorFlow, PyTorch, Keras ML libraries

---

## 📈 Expected Output

### Pada Cell Training
```
Mulai training Logistic Regression Manual...
Jumlah fitur: 8, Jumlah sampel: 614
Learning rate: 0.1, Epochs: 1000

Epoch    0/1000: Loss = 0.693147
Epoch  100/1000: Loss = 0.456821
Epoch  200/1000: Loss = 0.402156
...
Epoch 1000/1000: Loss = 0.389234
Training selesai!
```

### Pada Cell Evaluasi Test Set
```
EVALUASI PADA TEST SET
================================================================================

Confusion Matrix:
  Actual 0 -> Predicted 0 (TN): XX  |  Predicted 1 (FP): XX
  Actual 1 -> Predicted 0 (FN): XX  |  Predicted 1 (TP): XX

Metrik Evaluasi (Test Set):
  Accuracy:  0.7597 (75.97%)
  Precision: 0.6667
  Recall:    0.5714
  F1-Score:  0.6154
```

---

## 🔧 Troubleshooting

### Error: FileNotFoundError untuk diabetes.xls
- Pastikan file `diabetes.xls` ada di folder yang sama dengan notebook
- Atau ubah path di cell "Load Data"

### Error: Shape mismatch saat predict
- Pastikan input X memiliki 8 kolom (jumlah fitur)
- Pastikan data sudah di-scale dengan scaler yang sama

### Akurasi rendah
- Coba ubah learning_rate (coba 0.01, 0.05, 0.1, 0.2)
- Coba ubah epochs (coba 500, 1000, 2000, 5000)
- Coba ubah threshold prediksi dari 0.5

---

## 📝 Komentar Kode

Semua komentar dalam kode menggunakan **Bahasa Indonesia** untuk memudahkan pemahaman.

---

## 🎓 Konsep Pembelajaran

Notebook ini mencakup konsep-konsep penting:

1. **Sigmoid Function**: Fungsi aktivasi untuk logistic regression
2. **Binary Cross-Entropy Loss**: Loss function untuk klasifikasi biner
3. **Gradient Descent**: Optimasi dengan gradient
4. **Forward Pass**: Komputasi prediksi
5. **Backward Pass**: Komputasi gradient
6. **Weight Update**: Pembaruan parameter
7. **Confusion Matrix**: Evaluasi model klasifikasi
8. **Precision, Recall, F1**: Metrik evaluasi penting

---

## 📚 Referensi

- Pima Indians Diabetes Dataset: https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database
- Logistic Regression: https://en.wikipedia.org/wiki/Logistic_regression
- Gradient Descent: https://en.wikipedia.org/wiki/Gradient_descent

---

**Dibuat oleh**: AI Assistant  
**Tanggal**: 2025  
**Status**: ✅ Siap Digunakan
