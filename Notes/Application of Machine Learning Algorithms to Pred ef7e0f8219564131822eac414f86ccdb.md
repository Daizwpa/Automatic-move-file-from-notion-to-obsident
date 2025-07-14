# Application of Machine Learning Algorithms to Predict Central Lymph Node Metastasis in T1-T2, Non-invasive, and Clinically Node Negative Papillary Thyroid Carcinoma

Author: Jiang Zhu
Score: ⭐️⭐️
Link: https://jin63.shinyapps.io/ML_CLNM/
DataSet: Private
Date published: 01/03/2021
Key word: Central lymph node metastasis(CLNM), lymph node dissections, machine learning algorithms, papillary thyroid carcinoma, prediction model
Method: Compare six model (Logistic regression, Gradient boosting machine, Extreme gradient boosting, Random forest, Decision tree, and Neural network)
Pre-processing: Not mention
Status: Done
Task: Cervical Lymph Node Metastasis, Metastasis Diagnosis, Prophylactic dissection
Type: Journal
AUC on test: 0.75
Accuracy on test: 0.67
Sensitivity on test: 0.667
Specificity on test: 0.674
Data type : Clinical data, intraoperative data
Journal Name: Frontiers in medicine indexed in PubMed
Limitation : retrospective study, one single institution data, model does not get high performance 
Muti-central Data: False
Number Of Patient: 1271
Output : Binary 
Type of paper: Experimental article

Objective:

- This study seeks to develop and validate models for predicting the risk of central lymph node metastasis (CLNM) in these patients based on machine learning algorithms.
- The purpose of this study is to develop ML-based models **using preoperative and intraoperative clinicopathological characteristics** to predict the likelihood of CLNM for individualized treatment and to obtain the best ML algorithms for online CLNM prediction in PTC.

Problematic:

Task:

- Collect 1,271 patients with following characteristics ( T1-T2 stage, non-invasive, and clinically node negative (cN0) PTC).
- perform statistical analysis. ( t-test, X test).
- train 6 model.
- Extract features important for each model.

Features:

- gender, age, tumor size, tumor location, chronic lymphocytic thyroiditis (CLT), multifocality, bilaterality, and the presence of LNM.

Result:

Conclusion:

- In multivariate logistic regression analyses, gender, tumor size and location, multifocality, age, and Delphian lymph node status were all independent predictors of CLNM.
- With the incorporation of preoperative and intraoperative risk factors, ML algorithms can achieve acceptable prediction of CLNM with XGboost model performing the best.

Quote:

- Prophylactic central lymph node dissection  is not recommended for a subset of patients with small (T1 or T2), non-invasive, clinically node-negative (cN0) PTC according to the 2015 American Thyroid Association (ATA) guidelines (9),