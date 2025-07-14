# Diagnosis of cervical lymph node metastasis with thyroid carcinoma by deep learning application to CT images

Author: Tiantian Wang
Score: ⭐️⭐️⭐️⭐️⭐️
DataSet: Private
Date published: 26/06/2023 12:00 AM (GMT+1)
Key word: Artificial neural network, Deep Learning, Lymph node metastasis, computed tomography, computer-aided diagnosis
Method: fast R-CNN (ResNet50+FPN+ROI Align+Anchor Design) (detection) + Residual network with attention module A-ResNet50-W (classification)
Status: In progress
Task: Cervical Lymph Node Metastasis, Metastasis Diagnosis
Type: Journal
AUC on test: 0.894
Accuracy on test: 0.96
Sensitivity on test: 0.988
Specificity on test: 80
Data type : Axial CT images, CT
Journal Name: Frontiers in Oncology
Limitation : small dataset, single central dataset,
Muti-central Data: False
Number Of nodules: 676
Number Of Patient: 574
Output : Binary
Transfer learning: A-ResNet50-W, ResNet50+FPN
Type of paper: Experimental article

Objective:

This study attempts **to make the CAD process more consistent with radiologists’ diagnostic considerations by introducing a novel deep learning framework guided by the analysis of CT data for automated detection and classiﬁcation of LNs in CT images.**

Problematic:

**The diagnostic accuracies using CT depends on the level of radiologists**, **which puts less experienced radiologists at a greater risk of misdiagnosis** or missed diagnosis. Especially for **determining the surgical extent with cervical LNs on CT,** **undertreatment of metastatic neck nodes during primary surgery due to underdiagnosis will cause local recurrence, overtreatment with prophylactic lateral compartment dissection will increase surgical morbidity (10, 11).**

The Task:

- propose an improved region-based detection network  to learn pyramidal features for detecting small nodes at different feature scales.
- propose a residual network with an attention module  to perform the classiﬁcation of LNs.
- Compared the model with existent model and other version of it and radiologist

Method:

Result:

The classiﬁcation method showed superior performance over other state-of-the-art methods with an accuracy of 96%, true positive and negative rates of 98.8 and 80%, respectively. It outperformed radiologists with an area under the curve of 0.894.

Quote:

The proposed CAD method implementation can mitigate several clinical problems.

Firstly, the CAD method can reduce the radiologist’s workload by reducing the inherent dependence of the diagnostic process on radiologists.

Thirdly, the CAD method has good diagnostic performance and can be used as an auxiliary tool to help radiologists make clinical diagnosis for LNM.

Finally, the CAD method may potentially reduce the frequency of unnecessary FNAs for benign LNs. In the future, we are also going to use the breast cancer dataset for testing our proposed network. The experimental results would help us to improve the detection and classiﬁcation networks we proposed.

Although ultrasonography is considered the ﬁrst choice for evaluating cervical LNM in thyroid cancer patients (9–12), it has not shown sufﬁcient accuracy in the diagnosis of LNM in previous studies (13–15). Ultrasonography can only detect 20-31% of patients with central cervical LNM, whereas the detection rate for lateral cervical LNM is 70-93.8% (14, 15). Computed tomography (CT) is recommended for preoperative examinations of cervical LNM as an adjunct to ultrasonography in recent research and treatment guidelines (16–19).

However, CT scans’ spatial resolution and contrast resolution are not high enough for cervical lymph nodes (LNs) to be accurately detected, as these LNs are not obvious and cannot be easily distinguished from accompanying blood vessels.