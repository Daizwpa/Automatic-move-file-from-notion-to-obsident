# Ultrasound-based radiomics XGBoost model to assess the risk of central cervical lymph node metastasis in patients with papillary thyroid carcinoma: Individual application of SHAP

Author: Yan Shi
Score: ⭐️⭐️⭐️⭐️⭐️
DataSet: private dataset includes 587 PTC.
Date published: 26/08/2022
Key word: Lymph node metastasis, Machine Learning, Radiomics, Ultrasound, papillary thyroid carcinoma
Method: XGBoost + SHAP + Boruta + MRMR + LASSO + PCA
Status: In progress
Task: Cervical Lymph Node Metastasis, Metastasis Diagnosis
Type: Journal
AUC on test: 90.8
Data type : Clinical data, Radiomics features
Explainability : SHAP
Features selection : Boruta, LASSO, MRMR
Number Of nodules: 153
Number Of Patient: 587
Output : binary
Type of paper: Experimental article
list of features: age, calciﬁcation, capsular invasion, diameter, radiomics score

Objective:

- A radiomics-based explainable eXtreme Gradient Boosting (XGBoost) model was developed **to predict central cervical lymph node metastasis (CCLNM) in patients with papillary thyroid carcinoma (PTC), including positive and negative effects.**
    
    

The problematic:

- Previous studies were primarily based on radiomics features, and logistic regression analysis was used to construct a nomogram for clinical prediction. The logistic model has good interpretability, and its model coefﬁcient represents the importance of features to the prediction results. However, **some variables with a causal relationship with the output variables may not be statistically signiﬁcant (11). If variables are excluded only from statistical assumptions, available information will be reduced and features of improving prediction ability may be missed.**
- Several *(machine learning)* classiﬁcation algorithms were used to compare diagnostic performance, such as eXtreme Gradient Boosting (XGBoost), deep learning, and transfer learning (6, 13, 14). However, **these algorithms all have the “epistemic opacity” problem.**
    
    

metrics:

- The balanced accuracy (BA), F-score, Matthew’s correlation coefﬁcient (MCC), precision, recall, and area under the receiver operating characteristic (ROC) curve (AUC) were applied to assess the XGBoost mode

SHAP:

- SHAP provides a powerful method to measure the importance of features (23, 24) and is introduced to solve the inexplicability bug of machine-learning models.
- 
- 
- The SHAP value corresponds to the measure of additive feature attributions.

Task:

- Collect ultrasound image from 587 PTC.
- Divide the cohort by 8:2 ratio ( training, test) set.
- Extract radiomics features (Shape, first-order, texture, wavelet, square root, logarithm, gradient, square, exponential) from ultrasound image of the primary PTC lesion using Pyradiomics software. 939 features were extracted from the original ultrasound images
- A minimum-redundancy maximum relevance (mRMR) was used to remove redundant features. The mRMR algorithm was used to select the 100 most critical features.
- The least absolute shrinkage and selection operator (LASSO) logistic regression method using 10-fold cross-validation was applied to select the most useful predictive CCLNM status-related features from the training cohort.  11 potential features were chosen among 100 elements in the training cohort with nonzero coefﬁcients in the 10-fold cross-validation LASSO logistic regression model.
- mRMR and LASSO logistic regression **were to build radiomics scores,**  11 features were used to calculate the radiomics score.
- Five key features were selected by the Boruta algorithm: capsular invasion, radiomics score, diameter, age, and calciﬁcation.

- Clinical features, ultrasound features, and radiomics score were screened out by the Boruta algorithm, and the XGBoost model was constructed from these characteristics.

- apply (SMOTE), an oversampling method that randomly generates new instances of minority classes to balance the number of categories (22), during the training process.
- Performance comparison with traditional machine learning models.
- The consistency of PTC ultrasonic image features was evaluated by two radiologists using Kappa.
- Interclass correlation coefﬁcient  was used to assess the interobserver agreement of the feature extraction
- 
- SHapley Additive exPlanations (SHAP) was used for individualized and visualized interpretation.
- 

Result:

- The area under the curve was 91.53% and 90.88% in the training and test cohorts, respectively for XGBoost.
    
    The XGBoost model outperformed the radiologist, increasing the AUC by 44%.
    

dataset:

- The 469 patients in the training cohort, 121 had CCLNM and 348 did not have CCLNM.
    
    the 118 patients in the test cohort, 32 patients had CCLNM.
    

Quote:

- Central cervical lymph node metastasis (CCLNM) is a critical factor affecting prognosis and recurrence in papillary thyroid carcinoma (PTC) patients (1). Therefore, preoperative prediction of CCLNM in an accurate and non-invasive manner is important
- Ultrasound is the preferred method for evaluating PTC according to American Thyroid Association (ATA) guidelines (2).
- **ultrasound shows limitations** for assessing central cervical lymph nodes because of the interference from gas in the esophagus and trachea.
- **Ultrasound only detects 20-31% of CCLNM preoperatively and only alters the surgical procedure of 20% of patients (3).**
- Radiomics mine quantitative image features from medical imaging in a high-throughput manner to improve predictive, diagnostic, and prognostic accuracy (4).

- Ultrasound-based radiomics can assess lymph node metastasis in PTC patients to some extent (9, 10)
- Machine learning is widely used in the medical ﬁeld and has a high predictive accuracy (12). However, this model is a complex nonlinear relationship and the limitation of its application in clinical practice is caused by the inexplicability of the model.
- Imbalanced data problems signiﬁcantly degrade the classiﬁcation performance in machine learning (21).
- A Boruta algorithm incorporating the **independent ultrasound variables**, **clinical factors**, and **radiomics score** selected the ﬁnal predictors for CCLNM.