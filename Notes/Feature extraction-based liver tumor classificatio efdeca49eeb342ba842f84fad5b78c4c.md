# Feature extraction-based liver tumor classification using Machine Learning and Deep Learning methods of computed tomography images

Author: Mubasher H. Malik, Hamid Ghous, Tahir Rashid, Bibi Maryum, Zhang Hao & Qasim Umer
DataSet: Private
Date published: 25/04/2024
Key word: CT images, Computer vision, Deep Learning, Machine Learning, feature extraction, liver tumor
Status: In progress
Task: Liver Diagnosis
Data type : CT, Radiomics features
Journal Name: Cogent Engineering Taylor & Francis Taylor & Francis Group
Type of paper: AI-Experiment, Experimental article
Data Region : Pakistan

Objective:

- *This article try to compare the performance of machine learning verses Deep learning in classification liver tumour using 6 already extracted features. Also they compare the performance pre-trained Deep learning model given it CT image directly.*
- The aim of this research is to proof that DL algorithms could not produce better using already extracted manual feature list while the rational of using pre-trained DL algorithms is to support the fact that using automatic feature extraction layers of pre-trained algorithms can produce better results (Figure 3).

Problematic:

Task:

- They setup two experiments:
    - First experiment: Compare the performance of ML  versus DL While the input is lit of already extracted features.
    - Second experiment: Compare the performance ML  Versus pre-trained model while ML take already extracted feature and pre-trained model take image directly.

Results:

- During experiments, it was observed that ML classifiers performed outstandingly as compare to DL classifiers using complete feature list and individual feature list as well.
- DL classifiers produced low frequency using already extracted features list with complete and individual feature list.
- ML classifier RF, Boost, SVM, and DT produced 99.6%,99.7%, 98.0%, and 96.5% accuracy respectively using a complete feature list of six features.
- On the other hand, DL classifiers, NN, LSTM, Bi-LSTM, and CNN produced 50.0%, 53.0%, 54.0%, and 54.0% accuracy, respectively, using a complete feature list of all features
- second experiment, pre-trained DL algorithms: LSTM+CNN (Naeem & Bin-Salem, 2021; Rayan et al., 2023), Resnet50, and VGG16 attained 97.0%, 78.0%, and 88.0% accuracy respectively.

Conclusion:

Quote: