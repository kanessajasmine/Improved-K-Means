# Improved K-Means Clustering
Improved K-Means is a modified clustering algorithm that enhances centroid initialization and distance calculation using feature weighting based on the coefficient of variation (CV).

## ✨ Features
* Weighted Euclidean Distance (based on feature importance)
* Improved centroid initialization (density-based approach)
* Handles empty clusters
* Flexible for any dataset (not limited to specific cases)

## 📦 Installation
### From GitHub
```bash
pip install git+https://github.com/username/improved-kmeans.git
```

### Local Installation
```bash
pip install -e .
```

## 🚀 Usage
```python
from improved_kmeans import improved_kmeans

labels, centroids, weights = improved_kmeans(X, n_clusters=3)
```

## 📊 Parameters
* `X` : array-like (n_samples, n_features)
* `n_clusters` : number of clusters
* `max_iter` : maximum iterations (default=100)
* `tol` : convergence tolerance (default=1e-4)
* `verbose` : print debug info

## 📤 Returns
* `labels` : cluster assignments
* `centroids` : final cluster centers
* `weights` : feature weights

## 🧠 Method Overview
1. Compute feature weights using coefficient of variation (CV)
2. Calculate weighted Euclidean distance
3. Select initial centroids based on density (nearest neighbors)
4. Perform iterative clustering (similar to K-Means)
5. Update centroids until convergence

## 📁 Project Structure
```
improved-kmeans/
│
├── improved_kmeans/
│   ├── __init__.py
│   └── core.py
│
├── setup.py
└── README.md
```

## 🎓 Use Case
This implementation is used in a research project:
"CLUSTER ANALYSIS OF DEVELOPMENT STATUS DISTRICTS/CITIES IN JAVA–BALI USING VARIATIONAL AUTOENCODER AND IMPROVED K-MEANS CLUSTERING"

## 👩‍💻 Author
Kanessa Jasmine

## 🇮🇩 Deskripsi (Bahasa Indonesia)
Improved K-Means merupakan pengembangan dari algoritma K-Means yang meningkatkan proses inisialisasi centroid dan perhitungan jarak dengan mempertimbangkan bobot setiap fitur menggunakan koefisien variasi (Coefficient of Variation / CV).

## ✨ Fitur Utama
* Menggunakan **Weighted Euclidean Distance** berbasis bobot fitur
* Inisialisasi centroid yang lebih optimal (berbasis kepadatan data)
* Mampu menangani **empty cluster**
* Dapat digunakan untuk berbagai jenis dataset (bersifat umum)

## 📦 Instalasi
### Melalui GitHub
```bash
pip install git+https://github.com/username/improved-kmeans.git
```

### Instalasi Lokal
```bash
pip install -e .
```

## 🚀 Cara Penggunaan
```python
from improved_kmeans import improved_kmeans

labels, centroids, weights = improved_kmeans(X, n_clusters=3)
```

## 📊 Parameter
* `X` : data input (n_samples, n_features)
* `n_clusters` : jumlah cluster
* `max_iter` : jumlah iterasi maksimum (default=100)
* `tol` : batas konvergensi (default=1e-4)
* `verbose` : menampilkan proses (opsional)

## 📤 Output
* `labels` : hasil label cluster
* `centroids` : pusat cluster akhir
* `weights` : bobot tiap fitur

## 🧠 Tahapan Metode
1. Menghitung bobot fitur menggunakan koefisien variasi (CV)
2. Menghitung jarak menggunakan Weighted Euclidean Distance
3. Menentukan centroid awal berdasarkan kepadatan (nearest neighbors)
4. Melakukan proses clustering seperti K-Means
5. Memperbarui centroid hingga konvergen

## 📁 Struktur Proyek
```
improved-kmeans/
│
├── improved_kmeans/
│   ├── __init__.py
│   └── core.py
│
├── setup.py
└── README.md
```

## 🎓 Kegunaan
Implementasi ini digunakan dalam penelitian:
“ANALISIS KLASTER STATUS PEMBANGUNAN KABUPATEN/KOTA DI JAWA – BALI MENGGUNAKAN VARIATIONAL AUTOENCODER DAN IMPROVED K-MEANS CLUSTERING”

## 👩‍💻 Penulis
Kanessa Jasmine
