# Computer Vision Fundamentals in Python

This repository contains Python code for exploring foundational concepts in computer vision. The goal of this project is to build a deep understanding of low-level image processing techniques by implementing operations from scratch and experimenting with different filters, noise effects, and image transformations. 

The project focuses on:
- Basic image manipulation and preprocessing
- Noise addition and filtering
- Edge detection and convolution filtering
- Experimentation with different parameter values to observe visual effects

This repository will continue to grow as more tasks are added.

## Repository Structure

Each file in this repository corresponds to a different aspect of image processing, with a primary focus on understanding the basics through custom implementations and parameter experimentation. The notebooks are designed to be educational, providing explanations of each step to aid learning.

- **ImageManipulationPIL.py**: Basic image handling with the Python Imaging Library (PIL).
  - **Features**: Open, display, and manipulate images; convert to grayscale; resize; rotate; and apply transformations to pixel values.

- **ImageProcessingClassificationwithKNN.ipynb**: Image segmentation and binarization.
  - **Features**: Segment parts of an image, binarize it by setting pixel intensity thresholds, and observe the effects of binary thresholds (0 or 255) on the image’s visibility.

- **CVFiltersAndCustomConvolution.ipynb**: Convolution and edge detection filters.
  - **Features**: Implement custom convolution filters, such as emboss and Prewitt filters, and explore the effects on images.
  - **Note**: Contains functions for both custom convolution and OpenCV's built-in `filter2D` for comparison.

- **NoiseAndFiltering.ipynb**: Noise addition and filtering.
  - **Features**: Apply Gaussian and impulse noise to images, then attempt to reduce noise using various filters (median, Gaussian, Laplacian).
  - **Goal**: Understand the behavior of different filters in noise reduction and observe how each filter affects image quality.

## Requirements

This project requires the following Python libraries:
- `opencv-python`: For image processing operations.
- `numpy`: For matrix manipulation and filter creation.
- `matplotlib`: For displaying images.
- `scikit-learn`: For machine learning tasks, such as dataset handling and data splitting.

You can install these dependencies using:
```bash
pip install opencv-python numpy matplotlib scikit-learn
