# incorporation of a machine learning pathological diagnosis algorithm into the thyroid ultrasound imaging data improves the diagnosis risk of malignant thyroid nodules

Author: Wanying Li
Score: ⭐️
Link: https://github.com/liuwencai6/thyroid_final/tree/main
DataSet: Private 
Date published: 08/12/2022
Key word: Machine Learning, malignant, prediction model, thyroid nodule, web calculator
Method: DT, XGBoost, Gradient Boosting machine, Naïve Bayes classifier, RF, LR
Status: Done
Task: Tumour Malignancy Diagnosis, reduce Biopsy, reduce subjectivity
Type: Journal
Explainability : SHAP
Features selection : LASSO, logistic analysis
Number Of Patient: 9999
Output : Binary
Transfer learning: No
Type of paper: Experimental article
list of features: age, echogenic foci, echogenicity, margin, metastasis lymph node, shape

Objective:

- Establishing a machine learning model based on ultrasound features and clinical features to predict malignant thyroid nodules

Problematic:

- 

Task:

- Collect patient 9999 and extract information.
- Apply lasso for features selection lasso and then logistic regression.
- Build sex models DT, XGBoost, Gradient Boosting machine, Naïve Bayes classifier, RF, LR.
- preform 10 fold Cross-validation
- Evaluate the model using the following metrices: AUC, accuracy, precision, recall,  F1 score.
- Assess the influence of variables on prediction results using SHAP, Heat map of the correlation.
- Select the best cutoff.
- embedded the best model (XGBoost) into web risk calculator

Results:

- XGBoost recorded the best results.
- Our ﬁndings indicated that the proposed model could detect malignant thyroid nodules accurately and reduce unnecessary biopsies by estimating risk stratiﬁcation.
- Previous ﬁndings unveiled that the abnormal cervical lymph nodes may indicate malignant nodule metastasis (28), which is consistent with our study.

Conclusion:

- Combining clinical characteristics and features of ultrasound images, ML algorithms can achieve reliable prediction of malignant thyroid nodules.

Quotes:

- The incidence of sonographically detected thyroid nodules is increasing in individuals; approximately 50% to 68% can be detected in healthy individuals. Most of these nodules are benign and asymptomatic (1–3), and only about 8% to 16% are malignant nodules (4–6).
- The complexity and diversity of thyroid nodules, it is challenging for doctors to distinguish
which nodules harbour clinically relevant malignancies (7).
- For more than 30 years, ultrasound and ﬁne-needle aspiration (FNA) cytology were the traditional diagnostic methods as the cornerstones in the clinical management of patients with thyroid nodules (8).
- FNA provides the most effective and practical diagnostic information for evaluating whether a nodule is malignant to reach a deﬁnitive diagnosis, which has traditionally been used to meet this purpose (9, 10). However, approximately 50% of all biopsied nodules proved to be benign and grew indolent with non-aggressive behavior (6, 11, 12). Moreover, biopsies in one out of seven thyroid nodules may not yield ﬁnal cytological results and usually require repeated biopsies or additional evaluation (13). Obviously, it is not cost-effective to submit all these lesions to FNA.
- It is reported that 30%–80% of patients with thyroid cancer have cervical lymph node
metastasis (29).