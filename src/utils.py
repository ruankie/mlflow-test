import os
import wget

def download_data(url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"):
    """Download Iris data and save in data/ folder
    """
    if not os.path.isfile('../data/iris.csv'):
        wget.download(url=url, out='../data/iris.csv')