# Diagnostic Value of Machine Learning-Based Quantitative Texture Analysis in Differentiating Benign and Malignant Thyroid Nodules

Author: Bulent Colakoglu
Score: ⭐️⭐️⭐️⭐️⭐️
DataSet: Private
Date published: 31/10/2019
Method: RF
Status: In progress
Task: Tumour Malignancy Diagnosis, noninvasive method, reduce subjectivity
Type: Journal
Data type : imagery data
Journal Name: Journal of oncology Wiley online library
Optimization : No
Explainability : No
Limitation : retrospective
Muti-central Data: False
Number Of nodules: 235
Number Of Patient: 102
Output : Binary
Transfer learning: No
Type of paper: AI-Experiment, Experimental article
list of features: GlcmZ3AngScMom, GrlmHMGLevNonUni, GrlmHRLNonUni, GrlmNRLNonUni, GrlmZRLNonUni, HistPerc 99, HogO8b2

Objective:

- The aim of this study is to evaluate the diagnostic value of machine learning- (ML-) based quantitative texture analysis in the diﬀerentiation of benign and malignant thyroid nodules.
- 

Problematic:

- The nodules that are strongly suspected to be malignant as appraised by US are further evaluated by ﬁne-needle aspiration biopsy (FNAB) or tissue biopsies; hence, a noninvasive method with an ability to diﬀerentiate malignant and benign nodules is desirable [8, 9].
- Sonographic features such as irregular margin, solid composition, hypoechogenicity, elongated
shape, and microcalciﬁcations indicate malignancy [8, 9]. However, these features are somewhat qualitative, and the experience of a radiologist has a substantial inﬂuence on diagnostic accuracy [10–15].  Over the years, various reporting systems have been introduced to reduce inconsistencies among radiologists and promote communication between clinicians and radiologists. However, these reporting systems still rely on a radiologist’s subjective interpretations. Moreover, some radiologists are reluctant to use these reporting systems owing to their complexity [8–10].

Results:

Conclusion:

- Quantitative textural analysis of thyroid nodules using ML classiﬁcation can accurately discriminate benign and malignant thyroid nodules. Our ﬁndings should be validated by
multicenter prospective studies using completely independent external data.
- 

Task:

- Collect data:
    - Collect
- Texture Feature Extraction:
    - QMaZda texture analysis software was used for quantitative texture feature extraction [29]
    - segment the ROI by radiologist.
    - extract 306 features includes:
        - ﬁrst-order histograms (13),
        - gradient-map-based features (5),
        - gray-level co-occurrence matrix (GLCM) features (176),
        - gray-level run-length matrix (GRLM) features(28),
        - autoregressive model features (5),
        - Haar wavelets (12), Gabor transform features (24),
        - histogram of oriented gradients (HOG; 8),
        - local binary patterns (LBP; 35) .
- Features selection:
    - use Environment for Knowledge Analysis (WEKA) toolkit version 3.8.2 to features selection[31].
    - They applied feature selection after cross validation; hence, relevant features were selected using only the training partitions of the dataset to avoid the “double-dipping” phenomenon, which occurs when the whole dataset is used for the selection and might lead to biased or over-optimistic results [32, 33].
- Dimension reduction:
- **A total of seven texture features were selected for the ﬁnal model: one histogram (HistPerc 99), one HOG (HogO8b2), four GRLM (GrlmHRLNonUni, rlmHMGLevNonUni, GrlmNRLNonUni, and GrlmZRLNo-nUni), and one GLCM (GlcmZ3AngScMom).**
- Build RF.
- Evaluate the model by fold cross validation.

Quote:

- Thyroid nodules are common, with a prevalence of up to 67% in the adult population [1, 2]. Approximately 5%–15% of these nodules are malignant, and the diﬀerentiation of malignant and benign nodules is mandatory for forming individual management strategies [3–7].
- Sonographic features such as irregular margin, solid composition, hypoechogenicity, elongated shape, and microcalciﬁcations indicate malignancy [8, 9].  However, these features are somewhat qualitative, and the experience of a radiologist has a substantial inﬂuence on diagnostic accuracy [10–15].
- 
- Radiomics is deﬁned as the machine learning- (ML-) or deep learning-based mining of quantitative texture features extracted from conventional imaging modalities. The aim is to improve the precision and diagnostic accuracy of imaging methods, mostly in the ﬁeld of cancer research [16, 17].

![Untitled](Diagnostic%20Value%20of%20Machine%20Learning-Based%20Quantit%20b3918317c1fc4e1b8ffb935925cf3026/Untitled.png)