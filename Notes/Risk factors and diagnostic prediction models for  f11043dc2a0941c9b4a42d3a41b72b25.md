# Risk factors and diagnostic prediction models for papillary thyroid carcinoma

Author: Xiaowen Zhang
Score: ⭐️⭐️⭐️⭐️
DataSet: private data set includes 2090
Date published: 05/09/2022
Key word: Back propagation neural network, Bethesda category, Diagnostic prediction, Logistic regression analysis, papillary thyroid carcinoma
Method: Compare performance of multi-variate logistic regression and BPNN
Status: Done
Task: Prediction of malignancy, Tumour Malignancy Diagnosis
Type: Journal
AUC on test: 0.948
Sensitivity on test: 0.931
Specificity on test: 0.883
Data type : Bethesda data, Clinical data, Demographic data, Radiomics features, TIRADS
Journal Name: Frontiers in Endocrinology indexed in Scopus
Optimization : No
Explainability : No
Features selection : Univariate logistic regression analyses
Limitation : retrospective, 
Muti-central Data: False
Number Of Patient: 2090
Output : Binary (benign or PTC)
Transfer learning: No
Type of paper: Experimental article
list of features: Bethesda Classification, Family history, HDL-C (mmol/L), Kwak TIRADS, Radiation exposure history, TPOAb (IU/mL), TSH (mIU/L), Tg (ng/mL), TgAb (IU/mL), age, maximum diameter of thyroid nodules

Objective:

- This study incorporated **demographic**, **serological**, **ultrasound**, and **biopsy** data and aimed **to compare a new diagnostic prediction model based on Back Propagation Neural Network (BPNN) with multivariate logistic regression model**, to guide the decision of surgery.
- Prediction model to predict thyroid cancer malignancy.

Problematic:

- Pre operative diagnosis of potentially TC malignant tumors.
- Most guidelines recommend ultrasound as the ﬁrst diagnostic approach for TNs. Thyroid Imaging Reporting and Data Systems (TI-RADS) are widely used to guide clinical practice. Recommendations for diagnostic ﬁne-needle aspiration biopsy (FNAB) of TNs are based on sonographic features combined with nodule sizes. Following biopsy, the Bethesda System for Reporting Thyroid Cytopathology is used worldwide to classify FNAB cytology ﬁndings and determine whether surgery is needed. However, there are limitations with the categorical Bethesda system. Bethesda III and IV cytology diagnoses, known as indeterminate, comprise approximately 30% of FNAB results (7); and management of this group of patients varies widely from clinical observation, ultrasound follow up, repeat FNAB, molecular test to thyroid surgery.
Overdiagnosis and surgery of thyroid cancer are common in clinical practice. Therefore, developing a systematic method to differentiate patients with papillary thyroid carcinomas (PTC) from benign nodules is important to guide surgery decision.

Task:

- build dataset includes 2090 patients ( 571 begin, 1519 malignant), and incorporating serological , demographic, sonograph, biopsy columns.
- Split dataset to 70% and 30%.
- Apply univariate analysis, e.g. t-test, Chi-squared test for features selection.
- Build Multi-variate logistic regression model and train it using features selected by univariate analysis with a backward stepwise selection mode.
- Build Back Propagation Neural Network and train it based on selected features.
- Measuring performance with ROC, sensitivity, speciﬁcity, negative predictive value, positive prediction value.
- 

Result:

- Multivariate logistic regression analysis indicated that Bethesda category (OR=1.90, P<0.001), TIRADS (OR=2.55, P<0.001), age (OR=0.97, P=0.002), nodule size (OR=0.53, P<0.001), and serum levels of Tg (OR=0.994, P=0.004) and HDL-C (OR=0.23, P=0.001) were statistically signiﬁcant independent differentiators for patients with PTC and benign nodules.
- Both BPNN and regression models showed good accuracy in differentiating PTC from benign nodules (area under the curve [AUC], 0.948 and 0.924, respectively). Notably, the BPNN model
showed a higher speciﬁcity (88.3% vs. 73.9%) and negative predictive value (83.7% vs. 45.8%) than the regression model, while the sensitivity (93.1% vs. 93.9%) was similar between two models.
    - 

Model input :

- Ten indicators, including age, family history of thyroid tumor, history of radiation exposure, nodule size, Bethesda category, TIRADS, serum levels of TSH, TPOAb, Tg, and HDL-C, were selected as the input variables in the BPNN model, i.e.

Conclusion:

- Bethesda category, TIRADS, nodule size, and serum levels of HDL-C were most signiﬁcant differentiators for patients with PTC and those with benign nodules.
- Based on demographic, serological, ultrasound, and biopsy data, both BPNN and multivariate logistic regression model showed excellent performance in differentiating patients with PTC from those with benign nodules, but the BPNN model provided more speciﬁc prediction for PTC than conventional regression analysis, and thus might help guide the decision of surgery. Future studies are needed to validate our ﬁndings.
- **Results from multivariate logistic regression analysis indicated that Bethesda category and TIRADS were positively associated with PTC**, which were in agreement with previous literature, **whereas age, nodule size, and serum levels of Tg and HDL-C were negatively associated with PTC.**

Limitation:

- All patients included in our study were all age 18 years or older since the proportion of patients under the age of18 years, who underwent thyroid surgery in our hospital, were small (most might have received therapy in children’s hospital). **Excluding adolescent patients could also prevent the analysis from confounding due to the heterogeneity between adults and adolescents; however, whether our conclusions could be generalized to other age groups needs further investigation.**
- 

Quote:

- More accurate preoperative diagnosis of malignancy has become an overriding concern.
- Thyroid cancer has also be come the fastest-growing cancer among women at the beginning of this century in China (4).
- most of TC are benign, adds to the burden of health system (6).
- Most guidelines recommend ultrasound as the ﬁrst diagnostic approach for TNs. Thyroid Imaging Reporting and Data Systems (TI-RADS) are widely used to guide clinical practice.
- Recommendations for diagnostic ﬁne-needle aspiration biopsy (FNAB) of TNs are based on sonographic features combined with nodule sizes. Following biopsy, the Bethesda System for Reporting Thyroid Cytopathology is used worldwide to classify FNAB cytology ﬁndings and determine whether surgery is needed. However, there are limitations with the categorical Bethesda system.
- Bethesda III and IV cytology diagnoses, known as indeterminate, comprise approximately 30% of FNAB results (7); and management of this group of patients varies widely from clinical observation, ultrasound follow up, repeat FNAB, molecular test to thyroid surgery.
- Overdiagnosis and surgery of thyroid cancer are common in clinical practice.
- A retrospective, multicohort study from China analyzed over 300,000 ultrasound images from patients with thyroid cancer and negative controls, and found that these AI-guided models showed similar sensitivity and improved speciﬁcity in identifying thyroid cancer compared with skilled radiologists.
- the risk stratiﬁcation assessment of TNs by using single features, is not an easy task.
- Machine learning based on sonographic or pathological images is still under-development and far from mature.
- With the dramatic development of molecular diagnostic technologies in recent years, researchers have discovered BRAF, RAS, and telomerase reverse transcriptase (TERT) promoter mutations, RET/PTC rearrangement, and other genetic mutations to be associated with thyroid cancers (27, 28).
- With the advance of TNs screening technology and increased detection demand, we can anticipate a dramatic increase of thyroid nodules (32).
- Very recently, two studies from South Korea conﬁrmed that a low level of HDL-C was associated with a higher risk of thyroid cancer,

![Untitled](Risk%20factors%20and%20diagnostic%20prediction%20models%20for%20%20f11043dc2a0941c9b4a42d3a41b72b25/Untitled.png)