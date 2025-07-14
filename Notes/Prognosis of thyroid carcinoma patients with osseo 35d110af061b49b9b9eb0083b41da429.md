# Prognosis of thyroid carcinoma patients with osseous metastases: an SEER-based study with machine learning

Author: Wanying Shi
Score: ⭐️⭐️⭐️
DataSet: SEER dataset from 2010 to 2016, of 579 patients 
Date published: 03/03/2023
Key word: Machine Learning, Osseous metastases, Radioactive iodine, Random forest, Surveillance, Survival, Thyroid carcinoma
Status: Done
Task: Distant Metastasis, Prognostic, Survive rate
Type: Journal
Type of paper: Experimental article

Objective:  

Ascertain (find out) the risk factors for survival.

Develop an effective model to predict the 3-year, 5-year overall survival (OS) and cancer-specific survival (CSS) for thyroid cancer patients with OM.

Note:

Osseous metastasis (OM) is the second most common site of thyroid cancer distant metastasis and presents a poor prognosis. 

Accurate prognostic estimation for OM has clinical significance.

Problematic:

- Utilizing historical clinical datasets to guide future treatment choices is beneficial for patients and physicians.

Task:

- 

Method:

Methods We retrieved the information of patients with OMs between 2010 and 2016 from the Surveillance, Epidemiology, and End Result Program. The Chi-square test, and univariate and multivariate Cox regression analyses were performed. Four machine learning (ML) algorithms, which were most commonly used in this field, were applied.

Results:

- Advanced age, tumor size ≥ 40 mm, combined with other distant metastasis were associated with worse OS in DTC OMs patients. Radioactive iodine (RAI) significantly improved CSS in both males and females.
- Patients with ≥ 55 years old (HR 1.934, 95% CI 1.137–3.292, p = 0.015), size ≥ 40 mm (vs < 10 mm: HR 3.893, 95% CI 1.401–10.813, p = 0.009), with other distant metastases (liver or lung) were significantly related with worse OS.
- Patient performed total thyroidectomy (vs no surgery performed HR 0.458, 95% CI 0.282–0.742, p = 0.002), RAI (EBRT vs RAI: HR 4.469, 95% CI 2.871–6.957, p < 0.001, No radiotherapy vs RAI: HR 4.666, 95% CI 2.969–7.332, p < 0.001) showed improved OS.
- Our study had the largest cohorts, which indicated that age ≥ 55, tumor size > 40 mm, and combined with distant metastasis (liver, lung, brain) decreased OS.
- For a worse CSS, DTC patients would have an age of ≥ 55, with combined liver or lung metastasis.
- total thyroidectomy and RAI can improve OS and CSS.

Task:

- Collect data from SEER.
- Chi-square test.
- univariate and multivariate Cox regression analyses.
- implement four machine learning ( LR, SVM, XGBoost, RF).

Model Establishment:

model objective:

 model to predict the 3-year, 5-year overall survival (OS) and cancer-specific survival (CSS) for thyroid cancer patients with OM.

Dataset: SEER database.

pre-processing: 

Implement Rose package to balance data.

Divide data randomly into train and test sets in a ratio of 7:3.

Build four model (LR, SVM, XGBoost, RF) with default parameter.

Test:

AUROC, accuracy score, recall rate, and specificity.

The RF get the hight result.

![Untitled](Prognosis%20of%20thyroid%20carcinoma%20patients%20with%20osseo%2035d110af061b49b9b9eb0083b41da429/Untitled.png)

![Untitled](Prognosis%20of%20thyroid%20carcinoma%20patients%20with%20osseo%2035d110af061b49b9b9eb0083b41da429/Untitled%201.png)