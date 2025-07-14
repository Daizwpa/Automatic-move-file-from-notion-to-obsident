# A machine learning-based approach to predicting the malignant and metastasis of thyroid cancer

Author: Jianhua Gu
Link: http://www. cancer-thyroid.com/
DataSet: Private 
Key word: Machine Learning, Risk prediction, Thyroid cancer, metastasis, thyroid nodule
Method: features selection lassoCV
Status: In progress
Task: Metastasis Diagnosis, Tumour Malignancy Diagnosis
Type: Journal
Data type : Tabular  data
Number Of Patient: 1735
Type of paper: AI-Experiment, Experimental article

Objective:

Also, in many countries, including China, Clinical follow-up observation is often used for thyroid nodules with TI-RADS 3, and surgery is often used for TI-RADS 5 and above. The choice of treatment for TI-RADS 4 (especially TI-RADS 4a) is controversial. Therefore, we focused on the prediction of thyroid nodules with TI-RADS 4. Timely and effective evaluation of preoperative risk factors allows accurate differentiation of benign and malignant thyroid nodules and screening of patients most likely to metastasize.

The ﬁrst aim is the construction of a classiﬁcation model for TC based on risk factors.

 The second aim is the construction of a prediction model for metastasis based on risk factors.

Task:

- Retrospectively collect approximately 70 preoperative demographic and laboratory test indices from 1735 TC patients.
- make pipeline machine learning :(linear regression model ridge,  Logistic Regression (LR), eXtreme Gradient Boosting (XGBoost))
- comprehensive comparative analysis with the prediction model using only thyroid imaging reporting and data system (TI-RADS).

Result:

The XGBoost model achieved the best performance in the ﬁnal thyroid nodule diagnosis (AUC: 0.84) and metastasis (AUC: 0.72-0.77) predictions.

Based on multivariate analysis and feature selection, age, obesity, prothrombin time, ﬁbrinogen, and HBeAb were common signiﬁcant risk factors for tumor progression and metastasis. Monocyte, D-dimer, T3, FT3, and albumin were common protective factors. 

Tumor size (11.14 ± 7.14 mm) is the most important indicator of metastasis formation. 

In addition, GGT, glucose, platelet volume distribution width, and neutrophil percentage also contributed to the development of metastases.

Quote:

Thyroid Cancer (TC) is one of the most common malignant tumors of the endocrine system, with the ninth highest incidence worldwide, and three times the incidence in women than in men
(1, 2).

Surgical resection is the primary treatment, and the extent of thyroidectomy depends on the pathologic type of TC and metastasis of lymph nodes (4).

Although the majority of patients TC have a good prognosis, a subset of patients develops lymph node metastasis, whose ﬁve-year survival rate is substantially reduced.

Regional lymph node metastasis in patients with differentiated thyroid cancer,
especially of a papillary type, has been frequent.

Obesity, smoking, and hormones are all possible causes of TC, and environmental factors, especially ionizing radiation, are currently considered to be recognized risk factors for TC (8).

Early diagnosis, management of malignant nodules and scientiﬁc treatment are crucial for TC prognosis.