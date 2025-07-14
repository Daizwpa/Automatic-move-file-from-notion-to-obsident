# The ultrasound-based radiomics-clinical machine learning model to predict papillary thyroid microcarcinoma in TI-RADS 3 nodules

Author: Zhang Chen
Score: TBD
DataSet: private
Date published: 12/01/2024
Key word: Conventional ultrasound, Machine Learning, Nomogram, Radiomics, papillary thyroid microcarcinoma
Method: radiomic  based on LightGBM
Pre-processing: Lasso
Status: In progress
Task: Tumour Malignancy Diagnosis
Type: Journal
Data type : Radiomics features, ultrasound image
Journal Name: Original Article Translational cancer research 
Optimization : No
Features selection : LASSO
Number Of Patient: 221
Output : Binary (malignant or benign)
Transfer learning: No
Type of paper: Experimental article

Objective:

- The main objective of this study was to investigate the efficacy of a machine learning model that utilizes ultrasound-based radiomics features and clinical information in accurately predicting the presence of PTMC in TI-RADS 3 nodules.

Problematic:

- Conventional ultrasound (CUS) technology has proven to be successful in the identification
of thyroid nodules. Moreover, the American College of Radiology Thyroid Imaging Reporting and Data System (ACR TI-RADS) was developed for the purpose of evaluating the risk of thyroid nodules based on ultrasound imaging. Nevertheless, identifying papillary thyroid microcarcinoma (PTMC) from TI-RADS 3 nodules using this system can be difficult due to overlapping morphological features.

Task:

- A total of 221 patients with TI-RADS 3 nodules were included, consisting of 91 cases of PTMC and 130 benign thyroid nodules.
- extract radiomics 1477 features from ultrasound using Pyradiomics.
- fifteen select features Lasso
- Light Gradient Boosting Machine (LightGBM) was employed to build both radiomics , clinical models and a radiomics-clinical model, which fused radiomics features with clinical information

Result:

- The combined “radiomics-clinical” model demonstrated superior diagnostic accuracy
compared to the clinical model for distinguishing PTMC in both the training dataset [area under receiver operating curve (AUC): 0.975 vs. 0.845] and the validation dataset (AUC: 0.898 vs. 0.811).

Conclusion:

- Utilizing an ultrasound-based radiomics approach has proven to be effective in predicting
PTMC in patients with TI-RADS 3 nodules.

Quote:

- **The small size of the cancer, its subtle onset, slow advancement, lack of apparent clinical symptoms, and frequent co-occurrence with other thyroid disorders pose difficulties in making an accurate preoperative diagnosis, resulting in a certain degree of both underdiagnosis and misdiagnosis.**
- ultrasound’s ability to differentiate between benign and malignant thyroid nodules, it remains the preferred imaging technique for evaluating the morphological features of thyroid nodules. This is due to its numerous advantages, including high resolution, lack of ionizing radiation, portability.
- the rate of metastasis of PTMC to the cervical lymph nodes has been reported to be high (16-18).
-