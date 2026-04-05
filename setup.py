from setuptools import setup, find_packages

setup(
    name="improved-kmeans-kanessa",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scikit-learn"
    ],
    author="Kanessa Jasmine",
    description="Improved K-Means with feature weighting (CV) and density-based initialization",
)
