# Real-Time-Animal-Species-Detection

The aim of this project is to develop an efficient computer vision model capable of real-time wildlife detection.

<!-- <p align="center">
  <img src="./demo/demo.gif" alt="Demo GIF">
</p> -->

## Table of Contents

- [Datasets](#datasets)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Evaluation](#evaluation)
- [Web App](#web-app)
- [Contirbuting](#contributing)
- [Author](#author)

## Datasets

The dataset used in this project consists of labeled images of 10 different animal classes: Buffalo, Cheetahs, Deer, Elephant, Fox, Jaguars, Lion, Panda, Tiger, Zebra. You can find the datasets:

- [Dataset 1](https://www.kaggle.com/datasets/biancaferreira/african-wildlife)
- [Dataset 2](https://www.kaggle.com/datasets/brsdincer/danger-of-extinction-animal-image-set)
- [Dataset 3](https://www.kaggle.com/datasets/antoreepjana/animals-detection-images-dataset)

## Project Structure

    ├── config
    │   └── custom.yaml
    ├── data
    │   ├── images
    │   └── labels
    ├── logs
    │   └── log.log
    ├── notebooks
    │   └── yolov8.ipynb
    ├── runs
    │   └── detect
    │       ├── train
    │       └── val
    ├── scripts
    │   ├── app.py
    │   ├── convert_format.py
    │   └── train_test_split.py
    ├── README.md
    └── requirements.txt

## Getting Started

Follow theses steps to set up the environment and run the application.

1. Create a python virtual environment.

   ```bash
   python3 -m venv venv
   ```

2. Activate the virtual environment.

   venv\Scripts\activate

   ```

   ```

3. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application.
   ```python
   streamlit run './scripts/app.py'
   ```

## Evaluation

The performance of the model is evaluated by metrics such as Precision, Recal, and Mean Average Precision (mAP).

| Model  | Precision | Recall | F1-score | mAP@0.5 | mAP@0.5:0.95 |
| ------ | --------- | ------ | -------- | ------- | ------------ |
| YOLOv8 | 0.944     | 0.915  | 0.93     | 0.95    | 0.804        |
