# The progress of radiomics in thyroid nodules

Author: XiaoFan Gao
Score: ⭐️⭐️⭐️
Date published: 07/03/2023
Key word: Artificial intelligence (AI), Machine Learning, PTC, Radiomics, thyroid nodule
Status: Done
Type: Journal
Type of paper: tool review

Objective:

So in this article, we explain the development, deﬁnition, and workﬂow of radiomics. And then, we summarize the applications of various imaging techniques in identifying benign and malignant thyroid nodules, predicting invasiveness and metastasis of thyroid lymph nodes, forecasting the prognosis of thyroid malignancies, and some new advances in molecular level and deep learning. The shortcomings of this technique are also summarized, and future development prospects are provided.

The introduction:

The benign thyroid nodules without surgical indications generally do not require special treatment.

malignant thyroid nodules should be elective surgical treatment once diagnosed, and neck dissection should be performed if lymph node metastases are present.

Some patients need to be treated with Iodine-131 nuclide after the operation (7) and predict the prognosis.

Papillary thyroid carcinoma (PTC) is the most common pathological type of thyroid cancer. It usually has a good prognosis, but relapse patients have a poor prognosis.

The challenge for clinicians is to balance treatment approaches so that patients with low-risk or benign thyroid nodules are not over-treated, while patients with high-risk or malignant thyroid nodules need  more aggressive therapies. Therefore, the differential diagnosis of thyroid nodules and the risk stratiﬁcation are essential and helpful for the subsequent individualized treatment.

Currently, ultrasound(US), computed tomography (CT), magnetic resonance imaging(MRI), and nuclear medicine imaging, such as positron emission tomography/computed tomography (PET/
CT), are commonly used in the clinic to evaluate thyroid nodules (9). They are mainly used to assess the benignity and malignancy of nodules, the degree of invasion by adjacent tissues, and lymph node metastasis (10).

Medical imaging has become routine clinical practice to provide information about the characteristics of human tissues in a non-invasive and repeatable manner (11). However, current risk stratiﬁcation for diagnostic imaging of thyroid nodules is subjective. It relies heavily on the clinician’s empirical judgment, and there is a large amount of untapped digital information in various images. Many researchers have attempted to develop non-subjective methods, including artiﬁcial intelligence models, to mine previously unused data in pictures to help solve this problem.

Radiomics:

The development of radiomics:

The technology of radiomics based on machine learning is getting more and more attention in clinics. Since the birth of artiﬁcial intelligence, humans have tried to apply it to medicine (13). Some early applications, such as Computer Aided Detection (CADe) and Computer Aided Diagnosis System (CADx), were developed to detect and diagnose abnormal areas in human tissues by analysing image features (14).

The deﬁnition of radiomics:

The term “radiomics” was ﬁrst proposed by Dutch scholar Philippe Lambin et al. in 2012 (15).

It is deﬁned as extracting high- throughput features from medical images, using automatic or semi-automatic analysis methods to conduct deeper data mining of image information, and associating it with other clinical data for evidence- based clinical diagnosis and treatment decision support.

Image segmentation:

There are three methods of image segmentation: manual segmentation, semi-automatic segmentation, and automatic segmentation.

Application of radiomics in the diagnosis and treatment of thyroid nodules:

Differentiate benign and malignant thyroid nodules:

Ultrasound for differentiating benign and malignant thyroid nodules:

With the continuous improvement of ultrasound instruments, the application of high-frequency **ultrasound to small organs has become an essential part of non-invasive ultrasound diagnosis (23).**

**The 2015 guidelines of the American Thyroid Association (ATA) emphasize the signiﬁcance of ultrasound in detecting thyroid nodules (24).**

Most studies have focused on developing a radiomics score for predicting thyroid malignancy using ultrasound images and investigating it as a complementary tool to improve the performance of risk stratiﬁcation systems.

MRI for differentiating benign and malignant thyroid nodules:

MRI has a high contrast resolution, can provide excellent soft tissue contrast, and can be all-round, multi-angle, and multi-plane to discriminate evaluation of nodules for benign and malignant differentiation (29), while no radiation damage compared with CT.

*MRI has a lot of using propose, but*  due to its long operation time, motion
artifacts and other problems are **rarely used to diagnose thyroid nodules.**

CT for identiﬁcation of benign and malignant thyroid nodules:

Thyroid imaging studies are mostly based on ultrasound, with fewer studies on CT and MRI.

Enhanced CT scans can show the characteristic enhancement of the thyroid, nodules, and surrounding tissues, which is of great signiﬁcance for the qualitative diagnosis of thyroid nodules.

CT images can avoid the bias of ultrasonic images due to subjective operation, the image standardization is higher, and the trained model has a stronger generalization ability.

Prediction of invasion and thyroid lymph node metastasis:

Although PTC is considered an indolent tumor, some cancer cells will metastasize to lymph nodes around the thyroid gland (39, 40), mainly including central lymph node metastasis and lateral neck lymph node metastasis.

**Therefore, the preoperative judgment of LNM metastasis is an important indicator for the prognosis, surgical scope, and surgical method of thyroid cancer. Accurate preoperative diagnosis of thyroid lymph node metastases is crucial to determining staging and individualized treatment plans (42, 43).**

They talk about radiomics  ( definition, tools, method), and application of radiomics in diagnosis and treatment of thyroid nodules e.g. ( **diagnosis and treatment of thyroid nodules and predication of invasive thyroid node lymph node metastasis**) using different type of image (Ultrasound, MRI, CT). and finally they mention common problem of radiomics.

Note from article:

predicate of invasive thyroid lymph node  **is an important indicator for prognosis** **the prognosis, surgical scope, and surgical method of thyroid cancer and crucial to determining staging and individualized treatment plans.**