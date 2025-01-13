# Acoustic Anomaly Detection for Predictive Maintenance in Hydroelectric Powerplants.

## Introduction

This repository focuses on acoustic anomaly detection using predictive models to detect faults or irregularities in hydroelectric machinery. The primary goal is to leverage sound data for monitoring and maintenance, ensuring efficient and timely detection of potential issues.

This project implements various machine learning techniques, including AutoEncoders, Local Outlier Factor (LOF), Isolation Forest (IF), and PCA, to detect anomalies in hydroelectric powerplant machinery based on sound recordings.

**Video Introduction**: https://youtu.be/CkA2gpYUkdY

## Table of Contents
- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Models](#models)
- [Notebooks](#notebooks)

---

## Project Overview

- **Key Features:**
  - Preprocessing of raw sound data into Mel-spectrograms.
  - Implementation of AutoEncoders for unsupervised anomaly detection.
  - Application of classical machine learning methods like LOF, Isolation Forest, and PCA.
  - Comparison between models for anomaly detection effectiveness.

- **Applications:**
  - Predictive maintenance of hydroelectric powerplants.
  - Acoustic monitoring for fault detection in real-world and synthetic datasets.

---

## Repository Structure

```
├── Data/
│   ├── mel/           # Preprocessed Mel-spectrogram data
│   ├── raw/           # Raw sound recordings
│       └── Copy the files of the data folder here...
├── Models/AutoEncoder/
│   ├── AE_Real.pth        # Pre-trained model on real data
│   ├── AE_Synthetic.pth   # Pre-trained model on synthetic data
│   ├── AE_WM.pth          # Pre-trained model on washing machine data
├── Notebooks/
│   ├── AutoEncoder/       # AutoEncoder training and evaluation notebooks
│       ├── AutoEncoder_Real.ipynb
│       ├── AutoEncoder_Synthetic.ipynb
│       ├── AutoEncoder_WashingMachine.ipynb
│   ├── LOF, IF, PCA/     # LOF, IF, PCA anomaly detection notebooks
│       ├── LOF_IF_PCA_Real.ipynb
│       ├── LOF_IF_PCA_Synthetic.ipynb
│       ├── LOF_IF_PCA_WashingMachine.ipynb
│   ├── Data Analysis/     # LOF, IF, PCA anomaly detection notebooks
│       ├── LOF_IF_PCA_Real.ipynb
├── Recording/
│   └── record.py          # Script for recording sound data
├── README.md
```
---

## Installation

To run the project, ensure you have the following dependencies installed:
- Python 3.8 or later
- Required libraries:
- numpy
- pandas
- matplotlib
- librosa
- torch
- scikit-learn
- jupyterlab

---

## Usage

1. **Prepare the Dataset**  
   - Place raw sound data in the `Data/raw/` directory.  
   - Use `record.py` in the `Recording/` folder to record custom sound data.

2. **Preprocess Data**  
   - Convert raw sound recordings into Mel-spectrograms and store them in the `Data/mel/` directory.

3. **Train Models**  
   - Use the notebooks in `Notebooks/AutoEncoder/` to train AutoEncoders on specific datasets.  
   - Use the notebooks in `Notebooks/LOF, IF, PCA/` to apply LOF, IF, and PCA to the datasets.

4. **Evaluate Models**  
   - Compare the performance of AutoEncoders and classical ML models using test metrics like precision, recall, F1-score, and AUC.

5. **Visualization**  
   - Generate spectrogram visualizations for detected anomalies.  
   - Visualize the confusion matrices and ROC curves for model performance evaluation.

---

## Models

### AutoEncoders
- **AE_Real.pth**: Pre-trained model for real-world hydroelectric data.  
- **AE_Synthetic.pth**: Pre-trained model for synthetic datasets.  
- **AE_WM.pth**: Pre-trained model for washing machine anomaly detection.

### Classical ML Models
- **LOF (Local Outlier Factor)**  
- **Isolation Forest (IF)**  
- **PCA (Principal Component Analysis)**

---

## Notebooks

### AutoEncoder Notebooks
1. **AutoEncoder_Real.ipynb**  
   - Train and evaluate an AutoEncoder on real-world data.  
2. **AutoEncoder_Synthetic.ipynb**  
   - Train and evaluate an AutoEncoder on synthetic data.  
3. **AutoEncoder_WashingMachine.ipynb**  
   - Train and evaluate an AutoEncoder on washing machine sound data.

### LOF, IF, PCA Notebooks
1. **LOF_IF_PCA_Real.ipynb**  
   - Apply LOF, IF, and PCA on real-world data.  
2. **LOF_IF_PCA_Synthetic.ipynb**  
   - Apply LOF, IF, and PCA on synthetic data.  
3. **LOF_IF_PCA_WashingMachine.ipynb**  
   - Apply LOF, IF, and PCA on washing machine data.

### Data Analysis Notebook
1. **Data Analysis.ipynb**  
   - VIsual Analysis of Datasets. 

---
