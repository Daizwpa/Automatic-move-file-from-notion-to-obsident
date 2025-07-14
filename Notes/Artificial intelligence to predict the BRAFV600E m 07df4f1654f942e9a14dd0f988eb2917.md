# Artificial intelligence to predict the BRAFV600E mutation in patients with thyroid cancer

Author: Jiyoung Yoon
Score: ⭐️⭐️⭐️
DataSet: private
Date published: 25/11/2020
Method: logistic model
Status: Done
Task: Genetic Diagnosis, Predicting BRFV600E Mutation
Type: Journal
AUC on test: 0.706
Data type : Clinical data, imagery data, ultrasound image
Journal Name: Plos one indexed in PUBmed
Optimization : No
Explainability : No
Features selection : No
Muti-central Data: False
Number Of nodules: 469
Number Of Patient: 469
Output : Binary (BRAFV600E+ or BRAFV600E)
Transfer learning: No
Type of paper: Experimental article
list of features: ACR TIRADS, CNN score, age, sex, size
Mentioned: Not yet
Multimodal: Yes
Tool used: The produced pyrogram was analyzed with the PyroMark Q24 software (Qiagen) to distinguish mutant versus wild-type alleles by relative peak height.

Objective:

*To investigate the capability of CNN on US to predict BRAFV600e mutation.* 

Task:

- Collect 469 of thyroid cancer in 469 patient. 380 (81%) positive, 89 (19%) negative.
- Ultrasound examination: calculate ACR Ti-rads by radiologist 19 years of experience.
- use CNN model to provide risk malignancy for ultrasound image from pervious work .
- Conduct Univariate and multi-variate logistic regression analyses to identify independent predictive factors for BRAFV600e.
- use clinical data  and the probability from CNN model to build logistic regression to predict BRAFv600E mutation.

Method:

probability of BRAFV600E mutation = Logistic_Regression(Age, ACR-tirads, sex, size, CNN value[0, 1])

result:

- On multivariate analysis, older age (OR = 1.025, p = 0.018), smaller size (OR = 0.963, p = 0.006), and higher CAD value (OR = 1.016, p = 0.004) were significantly associated with the BRAFV600E mutation.
- The CAD value yielded an AUC of 0.646 (95% CI: 0.576, 0.716) for predicting the BRAFV600E mutation.
- the multivariable model yielded an AUC of **0.706** (95% CI: 0.576, 0.716)
- In this study we showed that a WSL approach could accurately predict BRAF V600E mutation status in independent samples based on their H&E images alone.
- The multivariable model showed significantly better performance than the CAD value alone (p = 0.004).

Conclusion

- The multivariable model showed significantly better performance than CAD value alone (P=0.04).
- Deep learning-based CAD for thyroid US can help us predict the BRAFV600E mutation in thyroid cancer. More multi-center studies with more cases are needed to further validate our study results.
- Several previous studies have tried to identify US features that can predict BRAF status [9,
16, 17]. A recent review article concluded that US features of PTCs correlate with their particular molecular mutations, and BRAFV600E mutation is known to be associated with suspicious US findings, such as hypoechogenicity, non-parallel orientation, taller-than-wide shape, spiculated/microlobulated margins, and the presence of microcalcifications [25]
- The CAD value, which was calculated from a program that we developed using deep CNN, was associated with the BRAFV600E mutation in multivariable analysis. Our findings with the AUCs of the ROC curve indicate that the CAD value can help predict the BRAFV600E mutation in thyroid cancer.
- the multivariable model which was composed with patient age, tumor size, and the CAD value showed significantly increased predictability.

Note:

- The BRAFV600E mutation is the most commonly detected oncogene in thyroid cancer and is
highly specific for papillary thyroid cancer (PTC) [1, 2].
- The mutation (BRAFV600E) has been **used in diagnostic** methods adjunctive to fine needle aspiration (FNA) for thyroid nodules, **especially those with indeterminate cytology results** [1–5].
- **BRAFV600E mutation is a known predictor of aggressive PTCs** as it has been associated with higher cancer stage and a higher rate of extrathyroidal extension and lymph node metastases [6–8].
- Considering that ultrasonography (US) features have also been associated with the BRAFV600E mutation [3–5, 9]. we can assume that the **mutation test is a cost-effective tool for thyroid nodules with suspicious US features**. However, US itself is inherently limited by its subjectivity, leading to the low reproducibility of its results [10, 11]
- Several previous studies have focused on US features to predict BRAF status, and these
studies have found that US characteristics associated with malignancy (marked hypoechogenicity, taller-than-wide shape, etc.) are also associated with BRAF positivity [9, 16, 17].
- However, interpretation of US image is operator-dependent and inter-observer variability is moderate to substantial [10, 11, 26].
- A recent study evaluated the value of US-based radiomics for predicting BRAFV600E mutation in pathologically proven PTCs, but radiomics features extracted from US had limited value [29].
- The Korean population is known for its high mutation prevalence and 81% of the PTCs in our study showed the BRAFV600E mutation [38]