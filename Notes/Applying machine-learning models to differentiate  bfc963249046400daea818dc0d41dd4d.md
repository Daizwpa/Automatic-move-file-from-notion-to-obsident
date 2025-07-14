# Applying machine-learning models to differentiate benign and malignant thyroid nodules classified as C-TIRADS 4 based on 2D-ultrasound combined with five contrast-enhanced ultrasound key frames

Author: Jia-hui Chen
Score: ⭐️⭐️⭐️⭐️⭐️
DataSet: Private
Date published: 03/04/2024
Key word: Machine Learning, Ultrasound, contrast-enhanced ultrasound, key frames, radiologists, radiomics features, thyroid nodule
Method: SVM, DT, RF*, GBoostDT, XGBoost
Status: Done
Task: Tumour Malignancy Diagnosis, radiomics
Type: Journal
AUC on test: 0.94
Accuracy on test: 0.9
Sensitivity on test: 0.82
Specificity on test: 0.93
Data type : Radiomics features, ultrasound image
Journal Name: Frontiers in Endocrinology
Optimization : No
Explainability : No
Features selection : No, features importance based on Decision tree
Muti-central Data: False
Number Of nodules: 313
Number Of Patient: 300
Output : Binary (malignant or benign)
Transfer learning: No
Type of paper: Experimental article

Chen j et al. Compared six different machine learning models  (SVM, LR,DT, RF, GBoostDT and XGBoost) to differentiated malignant nodules that has been classified as 4 category in scoring system of China version C-Tirades. 

Objective:

- To apply machine learning to extract radiomics features from thyroid two-dimensional ultrasound (2D-US) combined with contrast-enhanced ultrasound (CEUS) images to classify and predict benign and malignant thyroid nodules, classiﬁed according to the Chinese version of the thyroid imaging reporting and data system (C-TIRADS) as category 4.

Problem statement:

- Thyroid nodules are a common clinical condition. In recent decades, the use of high-resolution ultrasound has rapidly increased worldwide (1, 2). The detection rate of thyroid nodules can reach 67%; however, only 5–15% of them are malignant (3, 4). In clinical practice, many patients suffer some complications after surgical thyroidectomy (5, 6). Moreover, the status quo of overdiagnosis and overtreatment has added unnecessary burdens to patients. In 2020, Chinese experts developed the Chinese version of the thyroid imaging reporting and data system (C-TIRADS) to evaluate the characteristics of thyroid nodules, providing a more practical and concise tool for daily clinical practice (7). **Most nodules classiﬁed as C-TIRADS 3 or 5 can be quickly distinguished accurately using two-dimensional ultrasound (2D-US) alone; however, there is a wide range of malignancy rates among thyroid nodules classiﬁed as C-TIRADS 4 (2–90%).** Moreover, some hypoechoic Hashimoto nodules with blurred margins can be classiﬁed as C-TIRADS 4 (8). and mummiﬁed nodules with internal necrotic components may also exhibit marked hypoechogenicity (9). Distinguishing these from malignant nodules poses challenges, leading to the low speciﬁcity of 2D-US and warranting ﬁne needle aspiration (FNA), an invasive procedure (2). Thus, there is a need to explore new methods for a more precise diagnosis of thyroid nodules which are classiﬁed as C-TIRADS 4.

Task:

- Collect 313 pathologically diagnosed thyroid nodules (2013 malignant, 110 benign), two 2D-US and five contrast-enhanced ultrasound key frames.
- Labeling the region of interest on 7 images, using LabelMe software.
- Extract radiomics from 7 images of each nodules, using Darwin Research Platform.
- Randomly split data into training and test sets in 9:1 ratio.
- Built six classifiers, SVM, DT, RF, Gradient boosting decision tree and  extreme gradient boosting.
- Evaluate the performance models.
- Compare the performance of model with two radiologists, one is junior and other is senior.

Results:

- The AUC of the diagnosis of US, CEUS and US combined CEUS by junior radiologist and senior radiologist were 0.755, 0.750, 0.784, 0.800, 0.873, 0.890, respectively.
- The RF classiﬁer performed better than the other ﬁve, with an AUC of 1 for the training cohort and 0.94 (95% conﬁdence interval 0.88–1) for the test cohort. The sensitivity, speciﬁcity, accuracy, PPV, NPV, and F1-score of the RF model in the test cohort were 0.82, 0.93, 0.90, 0.85, 0.92, and 0.84, respectively.

Conclusion:

- Our model, based on 2D-US and CEUS key frames radiomics
features, had good diagnostic efﬁcacy for thyroid nodules, which are classiﬁed as C-TIRADS 4. It shows promising potential in assisting less experienced
junior radiologists.