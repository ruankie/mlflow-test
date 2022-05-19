# Description
Testing MLFlow experiment tracking on simple data science project inside a containerised dev environment.

# How to use
### Open containerised dev environment
1. Clone this repo
1. Open in VS Code (make sure you have the `Remote-Containers` extension installed)
1. Use the `Remote - Containers` extension in VS Code and run the `Open Folder in Container...` command to start developing inside the container

### Run tracked experiments
1. Run `notebooks/ml-iris-data-exploration.ipynb` to download and explore the data.
1. Run `notebooks/ml-iris-modelling.ipynb` to experiment with different models and track their parameters and metrics

# References
* [Original analysis by Jane from Kaggle](https://www.kaggle.com/code/jchen2186/machine-learning-with-iris-dataset/notebook)
* [MLflow tutorial](https://www.mlflow.org/docs/latest/tutorials-and-examples/tutorial.html)