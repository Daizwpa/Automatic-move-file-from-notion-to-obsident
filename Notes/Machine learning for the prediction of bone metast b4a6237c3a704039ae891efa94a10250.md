# Machine learning for the prediction of bone metastasis in patients with newly diagnosed thyroid cancer

Author: Wen-­Cai Liu
Score: ⭐️⭐️⭐️
DataSet: SEER
Date published: 28/01/2021
Key word: Machine Learning, Random forest, SEER database, Thyroid cancer disease, bone metastasis
Method: RF, multivariate logistic regression + features selection + adjust model parameter
Pre-processing: No mention 
Status: Done
Task: Bone Metastasis, Distant Metastasis, Metastasis Diagnosis
Type: Journal
AUC on test: 0.917
Accuracy on test: 0.904
Sensitivity on test: 0.833
Specificity on test: 0.905
Data type : Clinical data, Clinicopathological data, Demographic data
Journal Name: cancer medicine indexed WILEY
Limitation : the model is based on machine learning and deep learning algorithms, so there may be some difficulties in clinical interpretation of the important features screened out by the model, this is a study based on a North American population, so there may be gaps in population applicability, so it is necessary to include a broader population in future studies, the SEER database records information at the time of initial diagnosis, which means that subsequent treatment data are missing, and we were unable to include them in the BM prediction analysis of TC patients.
Number Of nodules: 17138
Number Of Patient: 17138
Output : Prediction bone metastasis
Type of paper: Experimental article
list of features: Insurance status, Marital status, N stage, T stage, age, grade, histological type, laterality, race, sex

Objective:

- This study aimed to establish a machine learning prediction model that can be used to predict bone metastasis (BM) in patients with newly diagnosed thyroid cancer (TC).

Problematic:

- The current detection method is mainly bone scanning, however, due to the defects of high
cost, radiation damage, and low sensitivity to micro metastases focus.[10] Patients’ bone scanning are recommended only in the presence of suspicious skeletal-­related events (SRE), and it has been reported that the median time to develop SRE is 5 months after bone metastasis (BM).[6] **By then, many TC patients may miss out on the best treatment opportunities because they may have developed an advanced disease or multiple metastases.**
- The 5-­year survival rate of TC patients who develop Bone metastasis is 61%, and the 10-­year survival rate is 27%.9.

Task:

- Collect a total of 17,138 patients were included in the study, with 166 (0.97%) developed bone metastases from SEER between 2010 to 2016.
- Test all collected features with Pearson correlation.
- Randomly divided the dataset into training set and test set at 7:3.
- Use Chi-square test to analysis the difference between test set and training test.
- Train two models Random forest (FR) with n_tree of (5000) and multivariate logistic regression (LR) using all features .
- **Improve the the models using Extract features from two previse**  models and adjust the parameters of the RF model, iterated over the n_tree values from 1 to 500 to choose the best n_tree value (n_tree = 7)
- The model was 10-­folds cross-­validated in the training set (Figure 2B) and validated in the test set.
- 

Result:

- Person correlation  showed no significant correlation between them (Figure 3), indicating that the variables are independent of each other.
- multivariate LR model with enter variable selection method, seven characteristics were identified as independent risk factors, including sex (p = 0.015), age (p = 0.011), race (p < 0.001), grade (p = 0.029), histology (p = 0.043), T stage (p < 0.001), and N stage (p = 0.005) (Table 2).
- The improved random forest (RF2) model using the top seven significant features has the best
prediction performance among all machine learning models (AUC: 0.917, accuracy: 0.904, sensitivity: 0.833, specificity: 0.905, Table 3; Figure 5B)
- In this study, we found that the top seven most important features in the RF model are precisely the risk factors screened out in the LR model, including grade, T stage, histology, race, sex, age, and N stage. Although SRE has long been recognized as a sign of BM, it is not reasonable to

Conclusion:

- Grade, T stage, histology, race, sex, age, and N stage were the important prediction features of Bone metastasis.
- The RF model constructed in this study could accurately predict bone metastases in TC patients, which may provide clinicians with more personalized clinical decision-­making recommendations. Machine learning technology has the potential to improve the development of BM prediction models in TC patients.
- RF model, variable  importance was evaluated in terms of out-­of-­bag (OOB) error rate, which can reflect the contribution of each variable when categorizing BM versus no BM (Figure 4). Grade, followed by T stage and histology were the top three most important variables. Interestingly, in the RF model, the top seven most important variables are consistent with the risk factors screened by the LR model.
- **suspicious skeletal-­related events** **has long been recognized as a sign of BM, it is not reasonable to consider targeted screening for BM in TC patients only when they have symptoms of bone involvement, as this would delay their treatment. Therefore, models are necessary to predict patients with TC at high risk for bone metastases, and to provide early attention and screening.**

Quote:

- However, if a TC patient has distant metastasis (DM), the overall prognosis will deteriorate significantly.5–­7
- According to reports, approximately 4% of TC patients will develop bone metastasis.8
- The 5-­year survival rate of TC patients who develop Bone metastasis is 61%, and the 10-­year survival rate is 27%.9.
- **The majority of TC metastases are asymptomatic and are detected only during systemic  surveillance or systemic metastatic examination of malignant thyroid nodules.**
- Because of the low incidence and asymptomatic nature of BM, testing for BM is often overlooked during the initial diagnosis of a patient with TC.
- Bone metastases can cause severe spinal cord compression, pathologic fractures, bone pain, and other SREs, thus, worsening the patient's life quality.
- It has been reported that approximately 78% of patients with BM from TC developed at least one suspicious skeletal-­related events [6].
- Bone scintigraphy is usually used to identify possible bone metastases in patients newly diagnosed with TC. However, because bone scintigraphy is expensive and has radiation damage, further follow-­up examination may not be appropriate with this method.
- studies have shown that biopsy is not only difficult and painful, but also increases the risk of tumor cell proliferation, which means it may not be safe for routine diagnosis [22].