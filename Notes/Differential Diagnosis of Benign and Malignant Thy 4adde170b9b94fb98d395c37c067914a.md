# Differential Diagnosis of Benign and Malignant Thyroid Nodules Using Deep Learning Radiomics of Thyroid Ultrasound Images

Author: Hui Zhoua
Score: ⭐️⭐️⭐️
DataSet: private dataset
Date published: 05/04/2020
Key word: Deep Learning, Diagnose, thyroid nodule, thyroid ultrasound, ultrasound radiomics
Method: CNN + Transform learning
Pre-processing: Augmentation
Status: Done
Task: Tumour Malignancy Diagnosis, reduce subjectivity
Type: Journal
AUC on test: 0.97
Sensitivity on test: 0.895
Specificity on test: 0.841
Data type : imagery data
Journal Name: European Journal of Radiology  indexed in PubMed
Optimization : No
Explainability : class activation maps
Features selection : No
Muti-central Data: True
Number Of nodules: 1750
Number Of Patient: 1734
Output : Binary (Benign or malignant) and Heatmap for ROI in  image 
Transfer learning: Yes
Type of paper: Experimental article

Objective:

- investigating whether a Radiomics approach can make better use of thyroid ultrasound images and achieve more accurate diagnosis of differentiating malignant from benign thyroid nodules.
- We aimed to propose a highly automatic and objective model named deep learning Radiomics of thyroid (DLRT) for the differential diagnosis of benign and malignant thyroid nodules from ultrasound (US) images

Problematic:

- The sensitivity and specificity of using US for thyroid cancer diagnosis varied from 27% to 63% and 78.0% to 96.6% in various studies [1, 8, 12]. This is likely due to interobserver variability in assigning sonographic features to nodules and that US is highly operator dependent. Different examiners, different US instruments, and different definitions of US features will eventually affect the diagnostic accuracy. As a result, **US remains highly subjective and depends on clinical experience.**
- 

Task:

- collect US images and fine-needle aspiration biopsies from 1734 patient with 1750 thyroid nodules.
- Apply augmentation strategy  through number of random transformation.
- Made model called Deep Learning Radiomics of Thyroid (DLRT)  was used for the differential diagnosis of benign and malignant thyroid nodules. binary classification. the model is CNN based transfer learning (transformed model was from  previous studies without any modification).
- adapt Class Activation Map to generate heat map.
- test the performance with an external validation cohort
- Compare the performance of model with two radiologist (senior, junior) as well as two deep learning model ( basic CNN, TL model)
- Comparison between different ultrasound instruments

Result:

- the model records 0.96 , 0.95, 0.97 AUC in the training, internal and external cohorts, respectively.
- **No significant difference was found when applying DLRT on thyroid US images acquired from different US instruments.**
- Both human observers provided lower sensitivity and specificity than all three Radiomics models
- DLRT was a highly automatic end-to-end approach. It only required one mouse click on the nodule center as the manual trigger.

Conclusion:

- DLRT shows the best overall performance comparing with other deep learning models and human observers. It holds great promise for improving the differential diagnosis of benign and malignant thyroid nodules.
- Our work demonstrated several advantages over other studies attempted to differentiate malignant and benign nodules using computer-aided analysis on thyroid US images [9, 18, 21].

Limitation:

- **Statistical comparisons of AUC, sensitivity, and specificity also confirmed that no significant difference (all P > 0.05) was found, if DLRT was applied to US images acquired by different scanners**

Quote:

- **With the continuous improvement of ultrasonic instruments, the application of high-frequency ultrasound (US) to small organs has become an important part of the non-invasive ultrasound diagnosis, particularly in the field of thyroid imaging.**
- **Currently, US is the first clinical choice of thyroid nodules screening, because of its high sensitivity, non-radioactivity, easy-to-operate, and rapid diagnostic work-up.**

- US features can be utilized to differentiate malignancies from benign thyroid nodules. **For example, a cystic or spongiform appearance usually suggest a benign nodule only needed a long-term follow-up**, **whereas the solid composition, hypoechogenicity, infiltrative or irregular margins, and micro-calcifications are generally considered to be risk factors of malignancy [7, 8]** which may need further treatment, such as resection. Some studies demonstrated that a combination of US features provided certain diagnostic accuracy [9]. However, many other studies indicated a considerable overlap of US features appearing in both benign and malignant nodules [10, 11]
- Among the large number of detected nodules, most of them are benign, clinically insignificant, and safely managed by the surveillance program. However, approximately 10% of patients presenting thyroid nodules are at risk of malignancy [3],
- Fine-needle aspiration (FNA) biopsy has gained worldwide acceptance as the golden standard for the definitive diagnosis of benign and malignant thyroid nodules [1, 5].
- **American Thyroid Association (ATA) 2015 guidelines emphasize the significance of ultrasonography in detecting thyroid nodules [1],**  2012 European Society of Oncology (ESMO) thyroid cancer guidelines as the first-line diagnostic method.
- Thyroid nodules are defined as discrete lesions within the thyroid gland, radiologically distinct from surrounding thyroid parenchyma [1]. They are becoming increasingly common in clinical practice, **being detected in up to 65% of the general population [2]**. **Among the large number of detected nodules, most of them are benign**, clinically insignificant, and safely managed by the surveillance program. However, approximately 10% of patients presenting thyroid nodules are at risk of malignancy [3], and the incidence of thyroid cancer has continuously increased worldwide [4].

Method:
model name: DLRT, deep learning Radiomics of thyroid

![Untitled](Differential%20Diagnosis%20of%20Benign%20and%20Malignant%20Thy%204adde170b9b94fb98d395c37c067914a/Untitled.png)