import numpy as np
from sklearn.metrics import pairwise_distances

def improved_kmeans(X, n_clusters, max_iter=100, tol=1e-4, verbose=False):
    """
    Improved K-Means clustering with weighted initialization.

    Parameters:
    -----------
    X : array-like, shape (n_samples, n_features)
        Input data.
    n_clusters : int
        Number of clusters.
    max_iter : int
        Maximum iterations.
    tol : float
        Convergence tolerance.
    verbose : bool
        Print debug info.

    Returns:
    --------
    cluster_idx : ndarray
        Cluster labels.
    centroids : ndarray
        Final centroids.
    weights : ndarray
        Feature weights (CV-based).
    """

    mean = X.mean(axis=0)
    std = X.std(axis=0, ddof=1)

    mean = np.where(mean == 0, 1e-8, mean)
    cv = np.abs(std / mean)
    weights = cv / (cv.sum() + 1e-12)

    def weighted_euclidean(a, b):
        return np.sqrt(np.sum(weights * (a - b) ** 2))

    dist_matrix = pairwise_distances(X, X, metric=weighted_euclidean)
    avg_dist = dist_matrix.mean()

    neighbor_mask = dist_matrix < avg_dist
    neighbors_count = neighbor_mask.sum(axis=1) - 1
    sorted_idx = np.argsort(-neighbors_count)

    centroids_idx = []
    for idx in sorted_idx:
        if not any(neighbor_mask[idx, c] for c in centroids_idx):
            centroids_idx.append(idx)
        if len(centroids_idx) == n_clusters:
            break

    if len(centroids_idx) < n_clusters:
        remaining = [i for i in range(X.shape[0]) if i not in centroids_idx]
        centroids_idx += remaining[:(n_clusters - len(centroids_idx))]

    centroids = X[centroids_idx]

    for _ in range(max_iter):
        cluster_idx = np.array([
            np.argmin([weighted_euclidean(x, c) for c in centroids])
            for x in X
        ])

        new_centroids = []
        for k in range(n_clusters):
            members = X[cluster_idx == k]

            if len(members) > 0:
                new_centroids.append(members.mean(axis=0))
            else:
                farthest = np.argmax(pairwise_distances(X, centroids).min(axis=1))
                new_centroids.append(X[farthest])

        new_centroids = np.array(new_centroids)

        if np.all(np.abs(new_centroids - centroids) < tol):
            break

        centroids = new_centroids
    return cluster_idx, centroids, weights
