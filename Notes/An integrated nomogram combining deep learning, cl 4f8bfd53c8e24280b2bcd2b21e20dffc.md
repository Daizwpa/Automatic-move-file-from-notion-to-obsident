# An integrated nomogram combining deep learning, clinical characteristics and ultrasound features for predicting central lymph node metastasis in papillary thyroid cancer: A multicenter study

Author: Luchen Chang
Link: http://thyai.zzinf.com/
DataSet: private
Date published: 21/02/2023
Key word: Central lymph node metastasis(CLNM), Deep Learning, Monogram, Ultrasound, papillary thyroid carcinoma
Method: Mask R-CNN for segmentation ,SE-ResNeXt-50 for classification 
Status: In progress
Task: Cervical Lymph Node Metastasis, Metastasis Diagnosis
Type: Journal
AUC on test: 0.829
Sensitivity on test: 0.759
Specificity on test: 0.768
Data type : Clinical data, sonographic features, ultrasound image
Journal Name: frontiers in endocrinology 
Muti-central Data: True
Number Of Patient: 3359
Output : Binary 
Type of paper: Experimental article
list of features: microcalcification, tumour position

Objective:

The present study aimed to develop and validate an effective preoperative nomogram combining deep learning, clinical characteristics and ultrasound features for predicting CLNM.

The purpose of the present study was to (1) evaluate the value of this system to predict CLNM and to (2) combine it with additional clinical and ultrasound characteristics to establish a more robust and generalizable model for the prediction of CLNM in PTC patients.

Task:

- collect data from two center. the first center dataset accounting for  3359 PTC, and divided to  70% training and 30% validation sets, 2114 and 906, respectively. the second center dataset include 339, considered to use for testing. (clinical data, sonographic data, raw ultrasound image).
- Used the Mask R-CNN framework as a computer vision framework for nodules segmentation.
- used SE-ResNeXt-50 as the classiﬁcation model (30). output [benign nodules (BN), malignant nodules without cervical lymph node metastasis (MN-LN(-)), and malignant nodules with cervical lymph node metastasis (MN-LN(+))].
- established logistic regression model based on the relationships among cervical lymph node status, sex, age and model prediction results.
- used data in the training cohort to construct the nomogram, which included the  AI-predicted value, clinical characteristics and ultrasound features.

- used mirrored, rotated, folded and normalized data augmentation during the training process and applied random dropout to prevent the model from overﬁtting.
- 

Construct an integrated nomogram combining deep learning, clinical characteristics and ultrasound features using multivariable logistic regression to predict CLNM in PTC patients.

Result:

Multivariate analysis indicated that the AI model-predicted value, multiple, position, microcalciﬁcation, abutment/perimeter ratio and US- reported LN status were independent risk factors predicting CLNM.

The area under the curve (AUC) for the nomogram to predict CLNM was 0.812 (95% CI, 0.794-0.830) in the training cohort, 0.809 (95% CI, 0.780-0.837) in the internal validation cohort and 0.829(95%CI, 0.785-0.872) in the external validation cohort.

Problematic:

A key and controversial problem in thyroid cancer management is if **prophylactic central lymph node dissection (CLND) is necessary.** CLND is recommended for patients who are suspected of CLNM in preoperative assessment. Some researchers demonstrated that prophylactic CNLD can more accurately stage tumors and reduce recurrence rates in patients with intermediate and high-risk thyroid cancer, while others argue that patients may gain no beneﬁt or some temporary morbidity (such as hypocalcemia and spinal accessory nerve dysfunction), and endoscopic lymphadenopathy (9, 10). Therefore, most studies do not recommend the routine use of prophylactic CLND in PTC (11, 12).

Quote:

The options for surgeon operation or follow-up depend on the state of CLNM while accurate
prediction is a challenge for radiologists.

Central lymph node metastasis (CLNM) is a predictor of poor prognosis for papillary thyroid carcinoma (PTC) patients

However, PTC easily metastasizes to cervical lymph nodes, and the prevalence of central lymph node metastasis (CLNM) can reach as high as 40% to 60% (5, 6)

PTC is usually an indolent cancer, and the 10- year survival rate of PTC can reach 93% if standardized treatment is accepted (4).

**CLNM status is an important risk factor for high recurrence rates and low patient survival (7, 8).**

A key and controversial problem in thyroid cancer management is if prophylactic central lymph node dissection (CLND) is necessary. CLND is recommended for patients who are suspected of CLNM in preoperative assessment.

Some researchers demonstrated that prophylactic CNLD can more accurately stage tumors and reduce recurrence rates in patients with intermediate and high-risk thyroid cancer, while others argue that patients may gain no beneﬁt or some temporary morbidity (such as hypocalcemia and spinal accessory nerve dysfunction), and endoscopic lymphadenopathy (9, 10). Therefore, most studies do not recommend the routine use of prophylactic CLND in PTC (11, 12).

According to the American Thyroid Association guidelines, preoperative neck ultrasound (US) is recommended to evaluate cervical lymph nodes, but the diagnosis rate is not accurate; although it has high diagnostic value for accessing lateral lymph node metastasis(LLNM), it has relatively low sensitivity in the diagnosis of CLNM (13–15).Thus, an effective and non-invasive way to predict CLNM before surgery is urgently needed to provide optimal surgical treatments.

**The nomogram showed that the AI model-predicted value was the largest contributor to the scores followed by US-reported CLN status**

Several studies have investigated deep learning to diagnose thyroid malignancy and have achieved better performance than human readers (22–25).