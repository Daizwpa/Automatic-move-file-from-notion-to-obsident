# Ultrasound-Based Radiomic Nomogram for Predicting Lateral Cervical Lymph Node Metastasis in Papillary Thyroid Carcinoma.

Author: Yuyang Tong
Score: ⭐️⭐️⭐️⭐️
DataSet: Private
Date published: 12/12/2021
Key word: Lymph node metastasis, Nomogram, Radiomics, Ultrasound, papillary thyroid carcinome
Method: Radiomics + monogram  + features selection (Genetic algorithm, Mrmr ,LASSO)
Pre-processing: Not mention
Status: Done
Task: Cervical Lymph Node Metastasis, Lateral Lymph Node Metastasis, Metastasis Diagnosis
Type: Journal
AUC on test: 93
Accuracy on test: 0.914
Sensitivity on test: 80.6
Specificity on test: 94.5
Data type : CT, Clinical data, Radiomics features, ultrasound image
Journal Name: Original Investigation academic radiology indexed in PubMed
Limitation : single-central data
Muti-central Data: False
Number Of nodules: 868
Number Of Patient: 868
Output : Binary 
Type of paper: Experimental article

Objective:

- The aim of this study was to develop an ultrasound (US)-based radiomic nomogram to preoperatively predict the lateral LNM in PTC patients.
- 

this study aimed to develop and validate a US-based radiomic nomogram that combines radiomic signature with clinical risk factors for the individualized preoperative prediction of lateral LNM in patients with PTC to facilitate designing an optimal treatment strategy.

Problematic 

- lateral neck dissection is an extensive and more invasive procedure, and may increase the risk of severe nerve injury and hypoparathyroidism (10).
- accurate preoperative identiﬁcation of lateral cervical LNM is important for decision-making and clinical management of patients with PTC.

Task

- 868 patient enrolled in this study(800 healthy, 68 sick)  divide them (600 for training and 286 for test).
- 5-year-experience radiologist make report of diagnosis of patient with CT image. the same thing with US.
- Tumor Segmentation by 2 US physicians with more than 10 years of
experience.
- Features extraction using script MATLAB , which was written by our group was used to extract US radiomic features (MAT-LAB R2015b; Mathworks).
- Perform interclass correlation coefﬁcient (ICC) to check the reproducibility of the feature extraction, segmented by two 2 us physicians.
- Features selection :
    - a two-sided Wisconsin rank-sum test was used to select features related to lateral CLN status.
    - Genetic algorithm combined with minimum-redundancy-maximum-relevance was applied to remove the redundant features.
    - a sparse representation classiﬁcation was used to sequence the top 50 features according to their importance.
    - LASSO logistic regression method was applied to select the most useful predictive lateral CLN status-related features from the training cohort.
- Student’s t test(continuous variables)or x2 test (categorical variables) were used to identify the clinical factors associated with lateral LNM.
- build nomogram using multivariate logistic analysis.

  

Result

- The radiomic nomogram demonstrated favorable discrimination in both the training and the validation cohorts, outperforming the radiomic signature and the radiologists’ subjective prediction of cervical LNM.
- 

Their Nomogram:

![Untitled](Ultrasound-Based%20Radiomic%20Nomogram%20for%20Predicting%20%20cda1a3dc94e940e597aa1af01c485309/Untitled.png)

Quote:

- **Cervical lymph nodes (CLNs) can be divided into two compartments, central (level VI) and lateral compartment (level IIV).**
- The incidence of central LNM in PTC patients has been reported as high as 30% -- 80% (6), and up to 40% PTC cases are involved with lateral cervical LNM (7).
- Considering the indolent clinical course of PTC, **ipsilateral lobectomy** is recommended for small unifocal tumor without extrathyroid extension or LNM (8).
- Ultrasound (US) is the ﬁrst-line noninvasive imaging modality for preoperative assessment of CLNs status, with a reported high speciﬁcity (80.5%	97.4%), but relatively low sensitivity (36.7%	61.0%) (11). Contrast-enhanced computed tomography (CT) has similar sensitivity and speciﬁcity compared to the US (12).
- In addition, ﬁne-needle aspiration (FNA) is an alternative way to conﬁrm LNM; however,
FNA is an invasive procedure with a risk of bleeding and infection (13).
- Features in this system can be divided into 10 categories: demographic information, tumor
size, orientation, position, shape, margin, boundary, echo pattern, posterior acoustic pattern, and calciﬁcation.
- One of the main goals for preoperative imaging in patients with PTC is to identify the presence of cervical LNM. US examination is the most widely used imaging modality for PTC staging. **Unfortunately, the detection rate of the CLN metastasis is not desirable. In our data, 86 tumors had lateral LNM; however, only 70.9% (61/88) of them were correctly reported as positive by the US. In addition, 10.8% of patients were misclassiﬁed according to the sonographic appearance of the lymph nodes, which was consistent with the previous study (20).**
-