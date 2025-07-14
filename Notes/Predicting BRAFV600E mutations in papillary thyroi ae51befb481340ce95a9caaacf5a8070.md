# Predicting BRAFV600E mutations in papillary thyroid carcinoma using six machine learning algorithms based on ultrasound elastography

Author: Enock Adjei Agyekum
Score: ⭐️⭐️⭐️⭐️
DataSet: Private
Date published: 03/08/2024
Method: Radiomic Compare SVM, KNN, LR, NB …
Status: Done
Task: Genetic Diagnosis, Predicting BRFV600E Mutation
Type: Journal
Data type : Elastography ultrasound, ultrasound image
Journal Name: Scientific reports nature
Explainability : No
Features selection : Pearson’s Correlation Coefficient, Recursive Feature Elimination
Muti-central Data: False
Number Of Patient: 138
Output : Binary (with BRAFV600E or without BRAFV600E)
Transfer learning: No
Type of paper: Experimental article
Mentioned: In Review
Multimodal: No
Tool used:  ITK-SNAP; PyRadiomics

## Objective:

- this study seeks to create and validate six distinct machine learning algorithms to predict ­BRAFV6OOE mutation in PTC patients prior to surgery

## Problematic:

- It is interesting to note that the presence of the ­BRAFV600E mutation has become a more reliable molecular marker for PTC ­recurrence3. Therefore, finding ­BRAFV600E mutations in thyroid tumors has implications for prognosis and serves as a marker for tumor recurrence. The
BR ­AFV600E mutation is also strongly linked to the existence of extrathyroidal extension (ETE) and cervical lymph node metastasis (CLNM) in PTC patients, suggesting an ­invasion4,5.
- identifying tumors using FNA biopsy samples from type 4a nodules is difficult because
tumor cells vary in quantity, quality, and ­purity 8. A sensitive and precise ­BRAFV600E mutation detection method will thus aid in the early detection of ­PTC9. Because ­BRAFV600E gene mutations produce 99.8% of malignant nodules, it is a significant tumor marker for PTC.
- 

## Task:

- collected elastography image data from 138 PTC patients (n = 75 have mutation, 63  do not have  mutation).
- stratified sample technique splitting dataset  into  training (70%) and validation (30%) .
- extract 479 radiomic features from US, using PyRadiomics.
- Pearson’s Correlation Coefficient (PCC) and Recursive Feature Elimination (RFE) with stratified tenfold cross-validation were used to select 27 relevant features.
- recursive feature elimination (RFE) for feature selection was applied to the whole dataset using the Scikit-learn python ­module 24 to choose representative features for the training cohort.
- build six machine learning algorithms including support vector machine with the linear kernel
(SVM_L), support vector machine with radial basis function kernel (SVM_RBF), logistic regression (LR), Naïve Bayes (NB), K-nearest neighbors (KNN), and linear discriminant analysis (LDA).
- Compare the performance the six model to predict the possibility of ­BRAFV600E, with accuracy, AUC, sensitivity, specificity, PPV, NPV, decision curve analysis (DCA), and calibration curves of the machine learning algorithms.
- 

## Result:

- AUCs for NB, KNN, LDA, LR, SVM_L, and SVM_RBF were 0.80 (95% confidence interval [CI]: 0.65–0.91), 0.87 (95% CI 0.73–0.95), 0.91(95% CI 0.79–0.98), 0.92 (95% CI 0.80–0.98), 0.93 (95% CI 0.80–0.98), and 0.98 (95% CI 0.88–1.00), respectively
- Among the six machine learning algorithms, the support vector machine with radial basis function (SVM_RBF) achieved the best ACC (0.93), AUC (0.98), SEN (0.95), SPEC (0.90), PPV (0.91), and NPV (0.95).
- Machine learning algorithms based on US elastography radiomic features are capable of predicting the likelihood of ­BRAFV600E in PTC patients, which can assist physicians in identifying the risk of ­BRAFV600E in PTC patients.
- There was a significant difference in echogenicity, vertical and horizontal diameter ratios, and elasticity between PTC patients with ­BRAFV600E and PTC patients without ­BRAFV600E.

## Conclusion:

- Finally, our study found that machine learning-based US elastography radiomic models performed well in predicting the potential of ­BRAFV600E in PTC patients, which can assist physicians in identifying the risk of B ­RAFV600E in PTC patients.

## Quote:

- The most common BRAF mutation is thymine (T) to adenine (A) missense mutation in nucleotide 1796 (T1796A, V600E)
- The ­BRAFV600E gene encodes a protein-dependent kinase (PDK), which is a key component of the mitogen-activated protein kinase pathway and essential for controlling cell proliferation, differentiation, and death.
- The ­BRAFV600E mutation causes PDK to be activated improperly and continuously, resulting in abnormal proliferation and differentiation in PTC.
- The ­BRAFV600E mutation is a significant contributor to the papillary thyroid carcinoma (PTC) phenotype, which aids in the diagnosis and differential diagnoses of PTC before ­surgery1,2.
- Ultrasound-guided FNA cytological examination of thyroid nodules can diagnose PTC before surgery, but 15% to 30% of the cytological results belong to the Bethesda system definition with uncertain detection results (including Bethesda Type III: atypical lesions or follicular lesions of unknown significance (AUS/FLUS), Type IV: follicular tumors suspected follicular tumors, and Type V: suspected malignant tumors (SUSP)).
- "TBSRTC Classification Malignant Risk and Management Recommendation" **recommends FNA cytology combined with ­BRAFV600E mutation detection, but are all invasive.**
- More importantly, According to earlier research, ­BRAFV600E mutation in thyroid tumors is thought to be a sign of severe illness and PTC-related ­mortality3.
- It is interesting to note that the presence of the ­BRAFV600E mutation has become a more reliable molecular marker for PTC ­recurrence3.
- finding ­BRAFV600E mutations in thyroid tumors has implications for prognosis and serves as a marker for tumor recurrence.
- The BR ­AFV600E mutation is also strongly linked to the existence of extrathyroidal extension (ETE) and cervical lymph node metastasis (CLNM) in PTC patients, suggesting an ­invasion4,5.
- Xing et al.7 revealed a close link between ­BRAFV600E mutation and ETE, CLNM, and advanced illness stages in a large comprehensive international multicenter investigation.
- A sensitive and precise ­BRAFV600E mutation detection method will thus aid in the early detection of ­PTC9. Because ­BRAFV600E gene mutations produce 99.8% of malignant nodules, it is a significant tumor marker for PTC.
- The main imaging method for evaluating thyroid nodules is ultrasound (US)10. Grayscale US has recently been found to be able to predict the mutation of ­BRAFV600E in PTC. However, the findings are still up for ­debate11,12, which may be related to the drawbacks of the conventional US image, such as its dependence on the radiologist’s experience and interobserver ­variation13.
- Recently, there has been a lot of interest in the medical area in the use of radiomics in conjunction with machine learning, which is an important subset of AI and plays a tremendous supporting role in increasing diagnostic and prognostic ­accuracy22,23.
- The BRAF V600E mutation has become a distinctive and important molecular marker in the management of PTC due to its substantial relationship with aggressive clinical pathological outcome, serious molecular derangements, and selection of treatment methods in PTC.
- **The higher AUCs and ACCs in the current study could be attributed to the US elastography radiomic features used, which provided more information than the grayscale US.**

Selected features:

![Untitled](Predicting%20BRAFV600E%20mutations%20in%20papillary%20thyroi%20ae51befb481340ce95a9caaacf5a8070/Untitled.png)