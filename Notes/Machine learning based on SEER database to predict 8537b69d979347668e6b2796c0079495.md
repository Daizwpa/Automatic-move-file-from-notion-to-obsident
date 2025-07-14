# Machine learning based on SEER database to predict distant metastasis of thyroid cancer

Author: Qiau L
Score: ⭐️⭐️⭐️⭐️
DataSet: SEER
Date published: 23/08/2023
Key word: Machine Learning, SEER database, Thyroid cancer, distant metastasis
Method: DT, ElasticNet, LR, XGBoost, RF, MLP, Radial basis function support vector machine
Pre-processing: under-sampling 
Status: Done
Task: Distant Metastasis, Metastasis Diagnosis
Type: Journal
AUC on test: 0.96
Accuracy on test: 0.906
Sensitivity on test: 0.929
Specificity on test: 0.884
Data type : Clinicopathological data, Demographic data
Journal Name: Research Square
Optimization : No
Limitation : retrospective study, 
Muti-central Data: True
Number Of Patient: 25729
Output : Binary (distant metastasis or no distant metastasis)
Type of paper: Experimental article
list of features: age, capsular invasion, gender, histological type, martial status, number of lymph nodes metastasis, race

Objective:

This paper aims to predict distant metastasis of thyroid cancer through the construction of machine learning models to provide a reference for clinical diagnosis and treatment.

Problematic:

- Patients with thyroid cancer with distant metastases may present with clinical symptoms at the appropriate site[23]. However, some patients who present with distant metastases at the first visit may have no clinical symptoms or may even have insidious distant metastases[24]. Conventional examinations (e.g. ultrasound or additional neck CT) [8] may not be able to accurately diagnose the clinical stage of these patients, and surgical treatment of the primary site alone may not achieve the desired treatment outcome. Due to the small number of cases
with distant metastases, there are fewer relevant studies both at home and abroad[7, 25]. There is still a lack of a more ideal model to predict distant metastasis.

Task:

- fetch seer data from 2010 to 2015
- SEER-stat software (National Cancer Institute SEER-stat Software Surveillance Research Program, www.SEER .concar.gov/seerstat, version 8.4.1) was used to generate case lists. Thyroid cancer (ICD-O-3 Hist/behave, malignant) codes included: 8260,8340,8342,8343,8344,8350,8050,8330,8331,8332,8335,8337,8510,8020,8021,8022.
- Inclusion criteria were as follows: thyroid gland resection with thyroidectomy with regional lymph node dissection in the neck; diagnosis confirmed by histopathology; thyroid cancer as the only primary malignancy; no previous history of malignancy. Cases with incomplete information were removed.
- uses the under sampling technique to balance the data for optimizing the model.
- employee univariate and multivariate logistic to screen independent risk factors.
- build sex model (DT, ElasticNet, LR, XGBoost, RF, MLP, Radial basis function support vector machine) and train them on fetched seer data.
- five-fold cross-validation
- the DeLong test is a nonparametric statistical test used to compare the differences in AUC of two classifiers (or two models)
- we plotted a calibration curve to evaluate the calibration of the prediction model (Fig. 3a).
- We further performed a decision curve analysis (DCA). net benefit (NB) is the percentage of net positives in the total sample.
- Mean Decrease Accuracy and Mean Decrease Gini are two important indicators of the importance of the variables in this model for the model

Results:

- Through univariate analysis, we found that age, gender, race, marital status,
tumor size, histological type, capsular invasion, multifocality, number of lymph nodes dissected and number of lymph nodes metastases were statistically significant (P<0.05),
- This research found that race and marital status were independent risk factors for distant metastasis, which may be related to individual mental status, lifestyle habits or hormone levels.
- 

Conclusion:

- The machine learning model constructed in this study helps in the early diagnosis of distant thyroid metastases and helps physicians to make better decisions and medical interventions.

Method:

Data on demographic and clinicopathological characteristics of thyroid cancer patients between 2010 and 2015 were extracted from the National Institutes of Health (NIH) Surveillance, Epidemiology, and End Results (SEER) database. 

Our research used univariate and multivariate logistic models to screen independent risk factors, respectively. 

Decision Trees (DT), ElasticNet (ENET), Logistic Regression (LR), Extreme Gradient Boosting (XGBoost), Random Forest (RF), Multilayer Perceptron (MLP), Radial Basis Function Support Vector Machine (RBFSVM) and other seven machine learning models were compared and evaluated by the following metrics: The area under receiver operating characteristic curve (AUC), calibration curve, decision curve analysis (DCA), sensitivity(also called recall), specificity, precision, accuracy, F1 score. 

Interpretable machine learning was used to identify possible correlation between variables and distant metastasis.

Quote:

- Most clinical studies related to thyroid cancer have built predictive models based on the presence or absence of lymph node metastasis[8, 9]. Predictive models related to distant thyroid metastases are fewer and are limited to specific pathological types or specific metastatic sites[10, 11]. The reasons for this are often based on the small number of clinical cases related to distant metastasis in the study center, the large bias and the low level of evidence.
- The Surveillance, Epidemiology and End Results (SEER) database is a publicly available and nationally representative cancer reporting system in the United States[14]. It is uniquely suited for epidemiologic studies of incidence, prevalence, and treatment patterns quantified by geographic and demographic factors, as well as for longitudinal studies of specific disease subgroups and rare or inert cancer types, e.g., distant metastases of thyroid cancer.
- The prognosis for poorly differentiated or undifferentiated thyroid cancer tends to be poor, with an incidence of 2% to 15% of all thyroid cancers and a five-year disease-specific survival rate of 66% for patients[17, 18].
- Overall, the presence of distant metastases is an important factor suggesting poor disease prognosis in a small percentage of patients (approximately 3-15%)[19-22].
- Extrathyroid extension or capsular invasion has been shown to be associated with lymph node metastasis in numerous studies[9, 31-33].
-