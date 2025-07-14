# PTC-MAS: A Deep Learning-Based Preoperative Automatic Assessment of Lymph Node Metastasis in Primary Thyroid Cancer

Author: Ruqian Fu
Score: ⭐️⭐️⭐️⭐️⭐️
DataSet: private
Date published: 12/05/2023
Key word: Deep Learning, Lymph node metastasis, Thyroid cancer, Transfer learning (TF), Ultrasonography, cancer diagnosis
Method: Yolos for detection tumour + ensemble learning ( DenseNet, ResNet, and GoogLeNet) for classification 
Pre-processing: imageJ for pre-processing, https://github.com/labelmeai/labelme , mosaic, , horizontal ﬂipping, random scaling, 
Status: Done
Task: Cervical Lymph Node Metastasis, Metastasis Diagnosis, preoperative assessment
Type: Journal
AUC on test: 0.858
Accuracy on test: 0.838
Sensitivity on test: 0.735
Specificity on test: 0.907
Data type : B-mode Ultrasound image, imagery data, ultrasound image
Journal Name: Diagnostics MDPI
Optimization : Genetic
Explainability : class activation maps
Limitation : retrospective, single-center
Muti-central Data: False
Number Of nodules: 2431
Output : Binary
Transfer learning: DenseNet, GoogleLeNet, ResNet
Type of paper: Experimental article

Objective:

- developing the Primary Thyroid Cancer Lymph Node Metastasis Assessment System (PTC-MAS)

Problematic:

- To differentiate between benign and malignant lymph nodes, grey-scale ultrasound is typically used to evaluate size, shape, margins, hilum, and nodal echogenicity, whereas color Doppler ultrasound examines vascular location and impedance values [7]. However, assessing cervical lymph nodes by grey-scale and color Doppler ultrasound using AJCC lymphatic subdivisions is a subjective and labor-intensive procedure that often results in low sensitivity (25–60%) [8–10]. This, in turn, increases the risk of prophylactic lymph node dissection in low-risk thyroid cancer patients without LNM, which can lead to complications such as hypoparathyroidism and laryngeal nerve dysfunction [9]. Therefore, preoperative assessment of cervical lymph nodes is essential in patients with thyroid cancer [11,12], as ultrasound examination can be challenging, even for experienced radiologists, due to interference from gas in the trachea and esophagus, as well as the varying degrees of expertise among radiologists [6].

Task:

- collect tow dataset A (2431) and B (1002). A used to develop yolo for thyroid nodule recognition system. B used to develop metastasis assessment system. B is subset of A.
- pre processing
    - noise removal using Labelme by radiologist .
    - annotate anchore box using labelme by radiologist.
    - augmentation  mosaic , horizontal, flipping, random scaling,
- build yolos  v5 and enhance hyperparameters of yolos using genetic algorithm.
- extracted image from yolos used as input for subsequent model for classification
- use three method to crop the image
- build ensemble learning (DenseNet, ResNet, and GoogLeNet) and used soft voting

Results:

Model:

- The system has two parts: YOLO Thyroid Nodule Recognition System (YOLOS) for obtaining regions
of interest (ROIs) of nodules, and LMM assessment system for building the LNM assessment system
using transfer learning and majority voting with extracted ROIs as input.

![Untitled](PTC-MAS%20A%20Deep%20Learning-Based%20Preoperative%20Automat%20b058ca56dd2b417189088abf5754f689/Untitled.png)

Conclusion:

Limitation:

This study has several limitations that should be acknowledged. Firstly, it is a retrospective and single-center study, which may introduce data bias. To enhance the generalizability of our ﬁndings, future prospective multicenter studies should be conducted. These studies can involve dynamic imaging and a more extensive range of thyroid cancer types to provide a more comprehensive evaluation of our system’s performance. Secondly, the ultrasound images used in this study were static, and features from multiple cross-sections were not considered. Future studies can incorporate dynamic imaging and analyze features from multiple planes to improve the accuracy of our model. Thirdly, the majority of thyroid cancers included in this study were papillary carcinomas, and there were fewer images of other pathological types of thyroid cancers. A larger sample size with a more diverse range of thyroid cancer types would provide a more comprehensive evaluation of our model’s performance. Fourthly, it is important to note that our system assesses LNM in primary thyroid cancer but does not provide information regarding benign or malignant nodes and cannot localize corresponding lymph nodes.

Quote:

- ultrasound is the imaging modality of choice for the evaluation of cervical lymph node metastasis (LNM), enabling identiﬁcation and characterization of abnormal central and lateral cervical lymph nodes, thereby facilitating surgical management [3,4].
- LNM risk, which includes the risk of recurrence, distant metastases, and diseasespeciﬁc mortality, is a critical factor to consider in the management of thyroid cancer [13–15].
- Traditional statistical analysis has been used in several studies [16–20] to evaluate LNM risk based on factors such as tumor size, patient age, extrathyroidal invasion, vascular invasion, microcalciﬁcation, and concomitant Hashimoto’s disease. Of these, tumor size
has been identiﬁed as an independent risk factor for LNM.
- Furthermore, radiomics requires radiologists to manually extract multiple features after selecting regions of interest (ROIs), which can be a labor-intensive and biased process [27–29].