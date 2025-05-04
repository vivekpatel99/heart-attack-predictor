import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.metrics import confusion_matrix

from src.constants import README_ASSETS


def plot_roc_curve(y: np.ndarray, y_hat: np.ndarray) -> None:
    fpr, tpr, _ = metrics.roc_curve(y, y_hat)
    fig, ax = plt.subplots(figsize=(8, 6))  # You can adjust figsize if needed
    ax.plot(fpr, tpr, label="ROC curve (area = %0.2f)" % metrics.auc(fpr, tpr))
    ax.plot([0, 1], [0, 1], "k--")  # Plot the diagonal line
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.set_title("ROC Curve for Heart Attack Prediction")
    ax.legend(loc="lower right")
    plt.tight_layout()  # Adjust layout
    plt.savefig(f"{README_ASSETS}/roc_curve.png")  # Save the plot to a file
    plt.close(fig)  # Close the figure


def plot_confusion_matrix(y: np.ndarray, y_hat_best_model: np.ndarray) -> None:
    cm = confusion_matrix(y, y_hat_best_model)
    # Create a ConfusionMatrixDisplay object
    cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Heart Attack", "No Heart Attack"])
    # Plot the confusion matrix
    # Create a figure with a specific size
    fig, ax = plt.subplots(figsize=(8, 6))  # Adjust (width, height) as needed
    # Plot the confusion matrix
    cm_display.plot()
    cm_display.plot(ax=ax)
    plt.tight_layout()  # Adjust layout to prevent labels cutting off
    # Save the plot as an image file
    plt.savefig(f"{README_ASSETS}/confusion_matrix.png")
    plt.close(fig)
