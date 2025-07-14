# Prediction of lung metastases in thyroid cancer using machine learning based on <scp>SEER</scp> database

Author: Wenfei Liu
Score: ⭐️⭐️⭐️⭐️⭐️
DataSet: SEER
Date published: 12/06/2022
Key word: Machine Learning, Thyroid cancer, lung metastasis, partial dependency plot, prediction
Method: RF
Pre-processing: oversampling, one hot encoding (for categorical features)
Status: Done
Task: Distant Metastasis, Lung Metastasis, Metastasis Diagnosis
Type: Journal
AUC on test: 0.99
Accuracy on test: 0.99
Sensitivity on test: 0.88
Data type : Demographic data, clinico-pathological data
Journal Name: Cancer medicine Willy indexed in PubMed
Optimization : No
Limitation : the algorithm model is skewed because important medical information about molecular diagnosis, such as the BRAF gene mutation in TC patients, is not available., Third, although the accuracy of the models was over 90%, prospective research is required to further verify the practice of the model
Muti-central Data: True
Number Of Patient: 9950
Output : binary
Transfer learning: No
Type of paper: Experimental article
list of features: N stage, T stage, age, diagnosis date, gender, grade, histological type, laterality, race

Objective:

- This study aimed to develop a machine learning algorithm model to predict lung metastasis of thyroid cancer for providing relative information in clinical decision-­making.
- In the present study, our aim was to develop six machine learning algorithm models for predicting LM based on the SEER database and to compare the assessment indicators of models to select the optimal machine learning model for **analyzing the correlation between LM and clinicopathological characteristics in patients with TC.**

Problematic:

- **Computerized tomography (CT) scans accurately detect lung metastasis (LM)
in TC.4 However, it is well known that CT scans are ineffective in filtering out TC patients with a high risk of LM**. **Thus, the development of a clinical algorithm model for the prediction of LM in TC is beneficial in making medical decisions for diagnosis and treatment in advance to greatly improve patient prognosis**

Task:

- Use SEER and clinicopathological data from 2010 to 2015.
- divided the data set into No Lung Metastasis and Lung Metastasis and apply Person’s chi-square  to study the difference between the two group (NLM and LM).
- Apply univariate analysis to logistic regression to identify features closely related to Lung Metastasis.
- They applied SMOTE for test set and under-sampling for dataset.
- split the data set into 80% for training and 20% test.
- Developed six machine learning SVM, LR, XGBoost, DT, RF, KNN.
- Perform Five-Fold cross validation.
- Compare performance: accuracy, precision, recall, F1-score, AUR curve.
- apply **Partial Dependence Plots (agnostic method) to interpret ml model.**
- 

result:

- Evaluation indicators of the best model-­RF were as following: accuracy (0.99), recall rate (0.88), precision (0.61), F1-­score (0.72), AUC value (0.99), and the Brier score (0.016).
- Multivariate logistic regression showed that age, T stage, N stage, and histological type were independent factors in TC with LM.
- The machine learning model trained with the data processed by the over-­sampling method was better than that with the data processed by under-­sampling method.
- **We believe that the most likely explanation is that lateral lymph node metastasis should be helpful for the migration of tumor cells to distant organs through lymphatic vessels.**
- Multivariate logistic regression showed that age, T stage, N stage, and histological type were independent factors in TC with LM.

Conclusion:

- Univariate logistic analysis showed that age, sex, grade, T stage, N stage, and histological type were significant with LM as illustrated in Table 4.
- Multivariate logistic regression showed that all these variables, except sex, were independently related with LM (Table 5).
- The optimal predictive model shows that from 20 to 40 years of age, the risk of LMs decreases with increasing age. However, from the age of 60 years, the risk of LMs increases with age.
- The risk of LM increases gradually with an increase in the degree of  T staging, N staging, and grade.
- Patients with PTC had the lowest risk of LM, those with FTC and ATC had nearly the same risk of LM, and those with ATC had the greatest risk of LM.
- **RF learning model performed better and can be applied to forecast
lung metastasis of thyroid cancer.**

Quote:

Lung metastasis (LM) is one of the most frequent distant metastases of thyroid cancer (TC).

Thyroid cancer (TC) is one of the most prevalent malignant tumors of the endocrine system, accounting for approximately 1%–­3% of all new malignant tumors worldwide.

TC usually encompasses four histological types: papillary thyroid carcinoma (PTC), follicular thyroid carcinoma (FTC), medullary thyroid carcinoma (MTC), and anaplastic thyroid cancer (ATC).4

**Therefore, TC generally exhibits an extensive range of clinical behavior, from indolent carcinomas with high survival rates to extremely aggressive malignancies, such as ATC, with
high mortality rates. Hence, the prognosis of patients with TC also exhibits significant variability.5,6**

Generally, tumor metastasis greatly worsens the patient's prognosis and may even be the major factor contributing to the death of the patient.

For differentiated TC, the most prevalent site of distant metastasis was the lung, which accounted for 85.6% of all distant metastases.4,7,8

Computerized tomography (CT) scans accurately detect lung metastasis (LM) in TC.4 However, it is well known that CT scans are ineffective in filtering out TC patients with a high risk of LM.

Thus, the development of a clinical algorithm model for the prediction of LM in TC is beneficial in making medical decisions for diagnosis and treatment in advance to greatly improve patient prognosis. Over the years, advances in clinical models have reached a mature stage. There are perfect clinical models with high accuracy to predict the performance of malignant tumors, including nomograms forecasting survival in patients with ATC, radiomics nomogram for preoperative prediction of lymph node metastasis in colorectal cancer, and an individualized nomogram to identify occult peritoneal metastasis in patients with advanced gastric cancer.9–­11

ML are being utilized to address increasingly complex problems with astonishing success, particularly extensively applied in the medicine.13 Several studies have investigated the medical applications of machine learning, including medical image recognition, treatment support, and biomedical research.14–­16

ML are being utilized to address increasingly complex problems with astonishing success, particularly extensively applied in the medicine.13 Several studies have
investigated the medical applications of machine learning, including medical image recognition, treatment support, and biomedical research.14–­16

The surveillance, epidemiology, and end results (SEER) program is a database produced by the National Cancer Institute that provides data on cancer-­related incidence, stage, treatment, and patient survival rates. The database contains information from 18 population-­based tumor
registries, having one nonrandom sample of 28% of the USA population, and records nearly 100% of the cancer cases in each registry.17

Partial dependency plots (PDPs) were created to illustrate the overall distribution of the target variable by the feature variables and the effect of the feature variables on the response of the target variable.26,27

The machine learning model trained with the data processed by the over-­sampling method was better than that with the data processed by under-­sampling method.

For differentiated TC, the most prevalent site of distant metastasis was the lung, which accounted for 85.6% of all distant metastases.4,7,8

![Untitled](Prediction%20of%20lung%20metastases%20in%20thyroid%20cancer%20us%20bc6a76e561e441e2a4c6d76afab78e39/Untitled.png)

- Ming Hao et al. also highlighted that the SOMTE algorithm can be broadly applied to solve an unbalanced classification problem in categorizing unbalanced PubChem Bio Assay data, which is consistent with our findings.29

list features:

TNM stage, grade, race, laterality, survival