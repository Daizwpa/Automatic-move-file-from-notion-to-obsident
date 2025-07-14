# Machine Learning Algorithms for the Prediction of Central Lymph Node Metastasis in Patients With Papillary Thyroid Cancer

Author: Yijun Wu
Score: ⭐️⭐️⭐️
DataSet: Private
Date published: 21/10/2020
Key word: Central lymph node metastasis(CLNM), Machine Learning, cross-validation, feature selection, papillary thyroid cancer
Method: Machine learning models, Decision curve analysis, multivariate and univariate analysis, ROC analysis
Pre-processing: z-score normalization, normalization
Status: Done
Task: Cervical Lymph Node Metastasis, Metastasis Diagnosis, Prophylactic dissection
Type: Journal
AUC on test: 0.731
Sensitivity on test: 63.6
Specificity on test: 71.7
Data type : Clinical data, sonographic features
Journal Name: ORIGINAL RESEARCH article indexed in frontiers in Endocrinology
Limitation : this is a retrospective study in which data bias might be unavoidable, more than 50% of the tumors included were microcarcinomas (≤ 1 cm). Actually, many other centers do not biopsy or operate on thyroid nodules less than 1 cm, which limited the reproducibility of this study.
Muti-central Data: False
Number Of Patient: 1103
Output : Benign or malignant
Type of paper: Experimental article

Objective:

- this study aims to construct multiple ML-based models **for the preoperative prediction of CLNM** and **identify risk factors associated with CLNM in patients with PTC.**

Problematic:

- Central lymph node metastasis (CLNM) occurs frequently in patients with papillary thyroid cancer (PTC), but performing **prophylactic central lymph node dissection** is still controversial. There are no reliable models for predicting CLNM.
- central compartment of lymph nodes seems to be the ﬁrst station of nodal metastasis among thyroid cancer (11). The current approaches to evaluating lymph status before operation mainly included ultrasonography (US) and invasive ﬁne needle aspiration (FNA), though with limited sensitivity (12,
13). **There is still lack of more accurate method for identifying the risk of cervical lymph node metastasis.**

Task:

- Enrol 1103 PTC patient, 612 has Central lymph node metastasis while the remine others is negative case, which accounts for 491. The data includes 20 features.
- univariate and multivariate analysis to build model.
- Build six  (random forest classiﬁer (RFC), artiﬁcial neural network (ANN), decision tree (DT), gradient boosting decision tree (GBDT), extreme gradient boosting (XGBoost) and adaptive
boosting (AdaBoost) ) model and train them based 20 features.
- Apply decision curve analysis to select best model. The selected models are (DCA, GBDT, RFC and ANN).
- apply features selection for the selected models by using (classiﬁer-speciﬁc importance and  AUCs of different numbers of variables were also calculated to ﬁnd the optimal dimension of each model)
- Apply 5-fold cross validation.

data content:

- tumor size, tumor location, hypoechogenicity, multiple nodules, bilateral nodules,
microcalciﬁcation, irregular shape, unclear margin and capsular invasion.
- triiodothyronine (T3), tetraiodothyronine (T4), free T3 (FT3), free T4 (FT4), thyroid stimulating hormone (TSH), thyroid peroxidase antibody (TPO-Ab) and thyroglobulin antibody (TG-Ab).
- 

Results:

- **GBDT was identiﬁed as the best predictive model in this study because of its best performance in both ROC curve (Figure 1) and decision curve (Figure 2). The AUCs of GBDT reached the highest when 7 variables were introduced (Figure 4). These 7 variables were as follows: age, suspected LNs, tumor size, microcalciﬁcation, irregular shape, TPO-Ab and TSH.**
    
    
    ![Untitled](Machine%20Learning%20Algorithms%20for%20the%20Prediction%20of%20%205bc1b96c8c7e494cbad0728ec7c1f565/Untitled.png)
    

Output Decision curve for prediction.

![Untitled](Machine%20Learning%20Algorithms%20for%20the%20Prediction%20of%20%205bc1b96c8c7e494cbad0728ec7c1f565/Untitled%201.png)

Conclusion:

- ML algorithms can be useful for the prediction of lymph node metastasis in PTC.
- Based on multivariate analysis and feature selection, **younger age, male sex, low serum TPO-Ab and US features such as suspected LNs, microcalciﬁcations and tumor size > 1.1 cm were important risk factors for CLNM.**
- All the 6 models is  signiﬁcantly better than Ultrasound  (AUC=0.623, SD=0.017, P<0.05).
- 

Quote:

- The central compartment is regarded as the ﬁrst metastatic station, whose metastatic incidence could reach up to 90% (7).
- Previous studies have shown that CLNM was signiﬁcantly associated with local recurrence and survival (8, 30, 31)
- prophylactic central lymph node dissection (CLND) procedure would be irrelevant for patients without nodal metastasis and even cause a higher. Thus far, whether to perform CLND for PTC patients without preoperative and intraoperative suspected lymph node metastasis remains controversial.