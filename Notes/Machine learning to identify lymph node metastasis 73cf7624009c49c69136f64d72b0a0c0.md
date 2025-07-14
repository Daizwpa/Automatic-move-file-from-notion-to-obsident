# Machine learning to identify lymph node metastasis from thyroid cancer in patients undergoing contrast-enhanced CT studies

Author: T. Masuda
Score: ⭐️⭐️⭐️⭐️⭐️
DataSet: Private
Date published: 21/03/2021
Key word: Lymph node metastasis from thyroid cancer, Machine Learning, Texture analysis, computed tomography
Method: SVM + Features Extraction using 3D Slicer (radiomics)
Pre-processing: Not Mention 
Status: Done
Task: Cervical Lymph Node Metastasis, Early identiﬁcation Lymph Node Metastasis, Metastasis Diagnosis
Type: Journal
AUC on test: 0.86
Data type : CT, Clinical data, Contrast-enhanced CT
Journal Name: Radiography Elsevier indexed in PubMed
Limitation : One single central data, Explainability problem,  
Muti-central Data: False
Number Of nodules: 772
Number Of Patient: 117
Output : Binary
Type of paper: Experimental article

Objective:

The purpose of this study was to compare the identiﬁcation of lymph node metastasis from thyroid cancer on contrast-enhanced CT images with the aid of machine learning combined with texture analysis, with the ﬁndings yielded by morphological methods such as the major axis, the minor axis, the volume and sphericity.

- We hypothesised that for the detection of cervical lymph node metastasis from thyroid cancer, the diagnostic performance of machine learning with texture analysis is superior to the morphological assessment of lymph node morphology.
- Compare morphological method Verses machine learning (SVM) with texture analysis .

Problematic:

the early identiﬁcation of lymph node metastasis.

Task:

- Collect data 117 contrast-enhanced  CT image, that contains 772 lymph nodes (84 metastasis lymph node, 688 benign lymph node).
- Extract 96 texture features from contrast-enhanced CT image using 3D Slice Software.
- normalisation features.
- The ﬁrst 78 patients with 469 lymph nodes (63 metastatic, 406 benign lymph nodes) were the training dataset for model development; the 39 subsequent patients with 303 lymph nodes (21 metastatic, 282 benign lymph nodes) were the testing dataset.
- Train SVM using 96 texture features.
- trained univariate logistic regression classiﬁers using 4 morphological features
- compare logistic regression with SVM.
- use the Welch t-test to compare the 4 morphological and the 96 texture features of metastatic and benign lymph nodes.
- The area under the curve (AUC) of receiver operating characteristic (ROC) analysis obtained by univariate logistic regression analysis and the SVM classiﬁers were calculated for both datasets.

Conclusion:

- Our ﬁndings suggest that in patients with thyroid cancer and suspected lymph node metastasis who undergo contrast-enhanced CT studies, **machine learning using texture analysis is high diagnostic value for the identiﬁcation of metastatic lymph nodes.**
- 

Quote:

The image texture is determined on digital images by a set of mathematically calculated metrics and the addition of machine learning has been reported to be of high diagnostic value for the identiﬁcation of malignant tumors.10,11

the early identiﬁcation of lymph node metastasis is important for selecting effective treatments.

Contrast-enhanced computed tomography (CT) studies are widely used for the evaluation of neck and lung metastasis.

Nodal measurements of the major axis, minor axis, volume, and sphericity 4e8 are useful for differentiating between benign and metastatic cervical lymph nodes. However, the diagnosis of lymph node metastasis on contrast-enhanced CT scans tends to be difﬁcult.9

In young people, lymph node metastasis from thyroid cancer, especially cervical lymph node metastasis, has a signiﬁcant impact on the life prognosis.3