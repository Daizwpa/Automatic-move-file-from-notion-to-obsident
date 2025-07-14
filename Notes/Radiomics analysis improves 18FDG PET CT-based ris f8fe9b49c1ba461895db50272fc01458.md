# Radiomics analysis improves 18FDG PET/CT-based risk stratification of cytologically indeterminate thyroid nodules

Author: Luca Giovanella
Score: ⭐️⭐️⭐️⭐️⭐️
DataSet: Private
Date published: 01/09/2022
Key word: Indeterminate, Quantitative, Radiomics, Standardised uptake value, Thyroid carcinoma, Thyroid cytology, [18F]FDG-PET/CT, thyroid nodule
Status: Not started
Task: Nuclear medicine, Tumour Malignancy Diagnosis, classification indetermined Bethesda cancer
Data type : PET metrics, Radiomics features, [18F]FDG-PET/CT
Journal Name: Endocrine springer
Type of paper: AI-Experiment, Experimental article

Objective:

- To evaluate whether quantitative ­[18F]FDG-PET/CT assessment, including radiomic analysis of ­[18F]FDG-positive thyroid nodules, **improved the preoperative differentiation of indeterminate thyroid nodules of non-Hürthle cell and Hürthle cell cytology.**
- 

Task:

- Collect 78 patient, 18FDG PET/CT and thyroid stimulating hormone.
- preform volumetric segmentation of each thyroid lesion.
- extract  4 PET metrics and 107 Radiomics features were extracted.
- calculate the correlation between 4 PET metrics and 107 Radiomic features and removed 65 radiomics features due to strong relation with SUVmax and Metabolic tumor volume MTV.
- Create logistic regression model using (PET metrics, 42 radiomics features and thyroid stimulating hormone) and calculate Radiomics score using linear combination ( **superposition** ).
- Compare the performance of radiomics score and cytology class (Bethesda 2 or 3) alone and together in predicting undetermined thyroid nodules cytology.

Result:

- Two RFs (shape_Sphericity and glcm_Autocorrelation) differentiated malignant from benign lesions.
- A predictive model integrating Radiomics score and cytology classes effectively stratiﬁed the risk of malignancy.
- The prevalence of thyroid cancer increased from 5 to 37% and 79% in accordance with the number (score 0, 1 or 2, respectively) of positive biomarkers.