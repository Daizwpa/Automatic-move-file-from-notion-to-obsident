# Direct Prediction of BRAFV600E Mutation from Histopathological Images in Papillary Thyroid Carcinoma with a Deep Learning Workflow

Author: Zihan Wu
Score: ⭐️⭐️⭐️⭐️⭐️
DataSet: Private dataset 
Date published: 17/03/2020
Key word: BRAFV600E mutation, Deep Learning, Histopathological image classification, Whole slide image, papillary thyroid carcinome
Method: CNN (for scoring tumor) + CNN (for predicting m mutation)
Status: Done
Task: Genetic Diagnosis, Predicting BRFV600E Mutation
Type: Conference
Data type : Histologic Images
Journal Name: CSAI 2024
Type of paper: Experimental article
Mentioned: In Review

## Objective:

- Propose a workflow **to predict BRAFV600E mutation status in papillary thyroid cancer directly from histopathological image.**
- Build a PTC dataset, including 6,541,586 patches of 512×512 pixels from 439 H&E stained Whole slide Image (WSIs) of 436 different PTC cases provided.

## Problematic:

- **the mainstream methods for BRAFV600E mutation detection are not entirely satisfying**. Formalin-Fixed Paraffin-Embedded (FFPE) tissue specimens and tissues derived by Fine-Needle Aspiration Biopsy (FNAB) are mainly used for the detection through the Real-time Quantitative PCR Detecting System [9, 10]. Both two approaches request an additional molecular pathological test, while the latter one can even be quite inaccurate due to the insufficiency
and unreliability of tissue samples and the unskilful handling of operators.

## Task:

- Build a PTC dataset of 6541586 patches  of 512×512 pixel from 439 H&E stained Whole Slide Images (WSIs) to perform our experiments.
- Build two model tumour classification and mutation classification using CNN architecture.
- Train **model using three different data set (PTC theirs, PCam, PAIP)**
- 

## Result:

- The model got AUC 0.884,  0.884, 0.860 in PTC, PCam, PAIP dataset respectively.
- The model get best outcome in all three dataset.
- The experiment demonstrates the availability and feasibility of our work and its potential in further research and applications.

## Conclusion:

## Quote:

- **BRAFV600E is a prominent oncogenic mutation** and has been found to have strong associations with the mortality and recurrence of PTC.
- Papillary Thyroid Carcinoma (PTC) is the most common type of thyroid malignancy, accounting for over 80% of all thyroid cancers [1, 2].
- Among all thyroid cancers, Xing et al. [5] found that BRAFV600E mutations only occurred in PTC and PTC-derived anaplastic cancers.
- BRAFV600E mutations were found to be strongly associated with the metastasis, mortality and recurrence of PTC [6–8].
- histopathological images are used to distinguish subtypes and variants in thyroid cancers [11]
- We believe that if mutations can be directly predicted from histopathological images, the costs and reliability can be improved a lot.
- histopathology is a clinical gold-standard and ubiquitously available through the whole cancer diagnosis and treatment process.
- BRAFV600E happens in more than half PTC cases [17].
- RAS mutations only found in 10-15% of PTC patients [16].

![Untitled](Direct%20Prediction%20of%20BRAFV600E%20Mutation%20from%20Histo%205f0757cac7934b08bf5bf9e5f7dea6cc/Untitled.png)

Method:

build two models one for detection tumour and other for binary classification the tumour either has brafv600e mutation or not.