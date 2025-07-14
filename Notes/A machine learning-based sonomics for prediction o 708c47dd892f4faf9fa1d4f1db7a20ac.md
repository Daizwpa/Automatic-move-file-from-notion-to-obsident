# A machine learning-based sonomics for prediction of thyroid nodule malignancies

Author: Mohsen arabi
DataSet: Private
Date published: 09/06/2023
Key word: Machine Learning, Radiomics, Ultrasound imaging, thyroid nodules
Status: Done
Task: Tumour Malignancy Diagnosis
Type: Journal
Data type : Radiomics features, ultrasound image
Journal Name: International Journal of Basic and Clinical Endocrinology endocrine springer indexed in PubMed
Type of paper: AI-Experiment, Experimental article

Objective:

- This study aims to use ultrasound derived features as biomarkers to assess the malignancy of thyroid nodules in patients who were candidates for FNA according to the ACR TI-RADS guidelines.
- 

Problematic:

- the visual interpretation of ultrasound images is the essential primary assessment in patients with thyroid nodules, this method suffers from limitations, such as dependence on the radiologist’s experience and loss of sufﬁcient quantitative measurements. Comparing before and after applying ACR TI-RADS, using TI-RADS can improve the accuracy of thyroid nodules management and reduce the biopsy recommendation for thyroid nodules analysis. But the accuracy of TI-RADS risk stratiﬁcation can be as low as 52%, which is considered low [9–11].
- 

Task:

- Collected 210 patient. 162 patients (137 benign and 25 malignant) were included as the training dataset. 48 patients (35 benign and 13 malignant) were included as the validation dataset.
- statistic significant different test between training and validation sets also between malignant and benign.
- Extracted  64 radiomics features including intensity, shape, and texture features.
- univariate analysis using t-student test.
- build two model RF and XGBoost combined with  different selection techniques LASSO and MRMR.  The models were  train by 1000 bootstrap techniques. multivariate analysis
- Evaluation of models performed using accuracy, sensitivity, speciﬁcity, and area under the receiver operating characteristic curve (AUC).
- 

Result:

- In the univariate analysis, Gray Level Run Length Matrix - Run-Length Non-Uniformity (GLRLM-RLNU) and gray-level zone length matrix - Run-Length Non-Uniformity (GLZLM-GLNU) (both with an AUC of 0.67) were top-performing for predicting nodules malignancy.
- XGBoost classiﬁer with LASSO feature selection and RF classiﬁer with MRMR feature selection
reached the highest accuracy in the training and validation datasets, respectively.
- the decision tree-based ensemble learning (RF and XGBoost) along with MRMR indicated high performance in distinguishing benign from malignant nodules.
- Consistent with prior research, in our study, machine learning-based models improved prediction performance up to an AUC of 0.99 in the training set and 0.95 in the validation set. Similarities in the results of various studies can provide evidence for the reliability and consistency of the ﬁndings.
- 

Conclusion:

- Ultrasound-extracted features can be used as non-invasive biomarkers for thyroid nodules’ malignancy prediction.
- In univariate analysis, we found no feature with high predictive power. However, models with high powers were achieved in multivariable modeling. These results reveal that there is no single measure for classifying thyroid nodules. Nevertheless, radiomics features can be considered predictive biomarkers in thyroid nodule workups.
- ultrasound images were used for radiomics analysis. No ionizing radiation exposure or
adverse biological effects are associated with ultrasound imaging, and it is an accessible and non-expensive imaging modality. To these issues, radiomics analysis of ultrasound
images could be used as the ﬁrst line for detection, diagnosis, and prognosis of thyroid nodules compared to the other modalities such as CT, MRI, and SPECT.
- 

Limitation:

- the sample size was small. Future investigations with larger numbers of patients are needed to warrant our results. Also, using balance data from benign and malignant patients and balanced TI-RADS scores can improve the results.
- the clinical data were not used for uni/multivariable modeling, which could improve the results.

Quote:

- Ultrasound imaging is a cost-effective, non-invasive, and accessible approach for differentiating and scoring benign and malignant thyroid nodules.
- the classiﬁcation system of the thyroid nodules proposed by the American College of Radiology (ACR) called TIR-ADS (Thyroid Imaging, Reporting, and Data System), visual interpretation of ultrasound images can be used for risk-stratiﬁcation of thyroid lesions and determining the probability of malignancy in thyroid nodules. Ranging from benign (TR1) to highly suspicious (TR5), the TIRADS system is based on the cumulative score of the
nodule out of ﬁve categories, including composition, echogenicity, margins, presence of echogenic foci, and shape.
- Thyroid nodules with smooth borders are most likely benign in nature. However, irregular and lobulated margins increase the risk of thyroid malignancy. Echogenic foci include bright spots in thyroid nodules as large comet-tail artifacts, macro calciﬁcations, peripheral rim calciﬁcations, and punctate echogenic foci. Finally, the shape means wider than tall or taller than wide on an axial US image in which a taller-than-wide shape is associated with a higher probability of malignancy [1–4].
- Radiomics converts medical image data into comprehensive quantitative features that enable the extraction of high-throughput data to improve treatment decision-making.
- Previous studies have reported that radiomic features extracted from medical images can be accurate, reliable, and non-invasive for cancer diagnosis, prognosis, and response prediction.
- The applicability of radiomics and ML approaches in the clinical setting is one of the most promising and challenging ﬁelds of modern diagnostic imaging and has resulted in better characterization of thyroid nodules [20].
- **In univariate analysis, only one factor or variable can be used to ﬁnd clinical and radiomic-based reliable features.**
- A multivariate analysis is a type of statistical analysis that involves the assessment of multiple variables simultaneously. In other words, it allows for examining the relationships between several variables at once.
- The Thyroid Imaging Reporting and Data System (TI-RADS) is a standardized system for classifying thyroid nodules based on their ultrasound characteristics.
- There are several versions of TI-RADS developed by different organizations, including ACR/TI-RADS, European Thyroid Imaging Reporting and Data System (EU-TIRADS), the American Thyroid Association guidelines (ATA) TI-RADS, Korean Thyroid Imaging Reporting and Data System (K-TIRADS), Chinese TIRADS (C-TIRADS) and Artiﬁcial Intelligence Thyroid Imaging Reporting and Data System (AI-TIRADS).
- Some studies suggested that ACR/TI-RADS recommendation for biopsy is fewer than the others, and the efﬁciency of KWAK-TIRADS and ATA guidelines is better than ACR/TI-RAD [25, 26]. In another study, C-TIRADS is recommended to stratify malignancy risk in thyroid nodules [27].
- The existence of multiple TIRADS systems can be attributed to each system’s distinct advantages and limitations. One notable limitation is the variability in the terminology and standards employed by different researchers when characterizing thyroid nodules using ultrasound features. While each TIRADS system serves a speciﬁc purpose, none have achieved widespread recognition and usage, and ongoing research is underway to validate them [28–35].
-