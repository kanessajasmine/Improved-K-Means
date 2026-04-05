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
This implementation is developed as part of a research project on clustering regional development status in Indonesia using Variational Autoencoder and Improved K-Means.
This implementation is adapted from the Improved K-Means method proposed in [1].

## 📚 References
[1] X. Wang and L. Wang, "Research on Intrusion Detection Based on Feature Extraction of Autoencoder and the Improved K-means Algorithm," 2017 10th International Symposium on Computational Intelligence and Design (ISCID), 2017, pp. 352–356, doi: 10.1109/ISCID.2017.170.

## 🇮🇩 Deskripsi (Bahasa Indonesia)
Improved K-Means merupakan pengembangan dari algoritma K-Means yang meningkatkan proses inisialisasi centroid dan perhitungan jarak dengan mempertimbangkan bobot setiap fitur menggunakan koefisien variasi (Coefficient of Variation / CV).

## 🎓 Kegunaan
Implementasi ini digunakan dalam penelitian:
“ANALISIS KLASTER STATUS PEMBANGUNAN KABUPATEN/KOTA DI JAWA – BALI MENGGUNAKAN VARIATIONAL AUTOENCODER DAN IMPROVED K-MEANS CLUSTERING”


## 👩‍💻 Penulis
Kanessa Jasmine
