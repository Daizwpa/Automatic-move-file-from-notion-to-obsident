# Deep learning-based multifeature integration robustly predicts central lymph node metastasis in papillary thyroid cancer

Author: Zhongzhi Wang
Score: ⭐️⭐️⭐️⭐️⭐️
DataSet: Private
Date published: 08/02/2023
Key word: BRAFV600E mutation, Central lymph node metastasis(CLNM), Convolutional neural network (CNN), papillary thyroid carcinome
Method: Nomogram and 1DCNN
Status: Done
Task: Cervical Lymph Node Metastasis, Metastasis Diagnosis
Type: Journal
AUC on test: 0.78
Sensitivity on test: 0.62
Specificity on test: 0.82
Data type : Clinical data, Clinicopathological data, Genetic mutations
Journal Name: BMC Cancer
Optimization : No
Muti-central Data: False
Number Of Patient: 488
Output : Binary
Transfer learning: No
Type of paper: Experimental article
list of features: BRAFV600E, age, aspect ratio, capsular invasion, combined benign thyroid disease, maximum diameter of thyroid nodules, microcalcification, nodule boundary, number of lesions, sex, tumour position

Objective:

**Established prediction models based on genetic mutations and clinicopathological factors that can be used to evaluate CLNM of PTC with hight sensitivity and specificity**, thus achieving the ideal combination of molecular and traditional diagnostic methods for clinical application.

Task:

- Collect data and filter data with the help of experts.
- Construct a nomogram model and validate using the Hosmer–Lemeshow test.
- Build a 1D-CNN model to predict lymph node metastasis using 11 clinicopathological features (binary classification).
- Analyse the performance of model.

Method:

They collected clinicopathological data and analysed the correlation between CLNM and clinicopathological features. and constructed a nomogram prediction model based on the analysis's result using statistically significant indicators from the binary logistic regression analysis and a 1D-CNN model that consists of a 12-layer, which includes one input layer, six 1D convolutional layers, one flattening layer, two dropout layers and two fully connected layers.

**Conclusions The deep learning-based multifeature integration prediction model provides a reference for the clinical diagnosis and treatment of PTC.**

What did they do:

they included 488 patients diagnosed with PTC by ultrasound-guided fine-needle aspiration biopsy, collected clinicopathological data, analysed the correlation between CLNM and clinicopathological features using univariate analysis and binary logistic regression, and constructed a nomogram prediction model and D1-CNN prediction model of CLNM. they validated the model using a set contains subclinical metastasis and clinical metastasis.

features used:

- 

11 clinicopathological features (sex, age,
combined benign thyroid disease, maximum diameter
of thyroid nodules, nodule location, aspect ratio, micro-
calcification, nodule boundary, capsular invasion, BRAF
V600E gene mutation and number of lesions) were incor-
porated in the construction of a one-dimensional con-
volutional neural network (1D-CNN) model, which was
based on the PyTorch framework and realized by Python
programming [25]. We constructed a 12-layer 1D-CNN,
as shown in Supplementary Fig. 1, which includes one
input layer, six 1D convolutional layers, one flattening
layer, two dropout layers and two fully connected layers.

Quote :

Few highly accurate tests can diagnose central lymph node metastasis (CLNM) of papillary thyroid cancer (PTC).

Cervical lymph node metastasis in PTC is closely related to the local recurrence of tumors, disease-free survival (DFS), and overall survival (OS). 

The mode and scope of surgery are determined by the presence of lymph node metastasis and the site of metastasis.

Central lymph node metastasis (CLNM) is the primary cervical lymph node metastasis site in PTC [3–5].

Preoperative ultrasound has high diagnostic value in detecting lateral neck lymph node metastasis (LLNM) but is less sensitive in diagnosing CLNM [6, 7]

The accuracy of intraoperative palpation for CLNM by surgeons is usually less than 30% [8].

PTC is usually characterized by chromosomal rearrangements of RET or point mutations in the RAS or BRAF proto-oncogene, and mutations in the BRAF, RAS, or RET genes are found in nearly 70% of PTC cases [19, 29].

Of these, BRAF mutations are seen in 60%-70% of PTCs, making them the most common mutations in PTC [30, 31].

our study showed that the BRAF V600E gene mutation (OR = 6.410, P < 0.001) was an independent risk factor for CLNM, suggesting that it may serve as an important reference in predicting lymph node metastasis.

In further analyses, in addition to the BRAF V600E mutation, we also found that age, maximum diameter of thyroid nodules, and capsular invasion were also independent risk factors for CLNM.