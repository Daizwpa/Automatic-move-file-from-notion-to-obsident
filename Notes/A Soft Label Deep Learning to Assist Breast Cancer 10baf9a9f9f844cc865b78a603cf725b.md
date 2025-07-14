# A Soft Label Deep Learning to Assist Breast Cancer Target Therapy and Thyroid Cancer Diagnosis

Author:  Ching-Wei Wang 
Score: ⭐️⭐️⭐️⭐️⭐️
DataSet: FISH breast dataset, DISH breast dataset 2, DISH breast dataset 1, private
Date published: 28/10/2022
Key word: HER2 overexpression, Thyroid cancer, brightfield dual in situ hybridization, fluorescence in situ hybridization, metastatic breast cancer, soft label deep learning, thin prep, ﬁne needle aspiration
Method: proposed new loss function 
Status: In progress
Task: Segmentation, soft label
Type: Journal
Data type : Papanicolaou-stained Whole slide image (WSI), ampliﬁcation in ﬂuorescence in situ hybridization image, dual in situ hybridization image, imagery data
Journal Name: MDPI Cancers
Explainability : No
Features selection : No
Muti-central Data: False
Output : soft labelled image
Transfer learning: No
Type of paper: Experimental article
list of features: No
Data Region : Taiwan
Mentioned: Not yet
Multimodal: No

# Objective:

- In this study, we present an automatic soft label deep learning framework to select patients for human epidermal factor receptor 2 target therapy and papillary thyroid carcinoma diagnosis.
- This approach will assist in breast cancer target therapy and thyroid cancer diagnosis with rapid examination and decrease human judgment mistakes.
- In this study, we present a soft label fully convolutional network (SL-FCN) to assist in breast cancer target therapy and thyroid cancer diagnosis, using four datasets.

# Problem statement:

- According to the World Health Organization Report 2022, cancer is the most common
cause of death contributing to nearly one out of six deaths worldwide. Early cancer diagnosis and
prognosis have become essential in reducing the mortality rate. On the other hand, cancer detection is a challenging task in cancer pathology. Trained pathologists can detect cancer, but their decisions are subjective to high intra- and inter-observer variability, which can lead to poor patient care owing to false-positive and false-negative results.
- Human epidermal growth factor receptor 2 gene ampliﬁcation (HER2; ERBB2) test is well established to determine whether a breast cancer patient is eligible for anti-HER2 target therapy [14,15].
- When breast cancer treated with **anti-HER2 target therapies**, such as trastuzumab, pertuzumab, and tyrosine kinase inhibitor lapatinib and neratinib, they have been shown to signiﬁcantly improve survival, but without appropriate anti-HER2 therapy, HER2-ampliﬁed tumors are associated with poor prognosis [16–22].
- Although immunohistochemistry (IHC) is a good screening method for negative (0+ or 1+) and strong positive (3+) results, any patient with IHC equivocal positive result (2+) should be conﬁrmed by ﬂuorescence in situ hybridization (FISH) analysis for anti-HER2 target therapies [23].
- Dual in situ hybridization (DISH) can be used for signal visualization and the beneﬁt of simultaneous morphologic correlation using light microscopy, and there is no need for specialized ﬂuorescence equipment [24,25]. FISH and DISH both use dual probes to highlight the HER2 gene and the chromosome 17 centromere (CEN17) in different colors.
- The main distinction between positive and negative ampliﬁcation status is based on the HER2/CEN17 ratio and the average HER2 copy number per nucleus in at least 20 nuclei.
- The American Society of Clinical Oncology (ASCO)/College of American Pathologists (CAP) initially issued a detailed guideline for clinical testing and interpretation of HER2 results in 2007, which were ﬁrst revised in 2013 and updated in 2018.
- Based on the 2018 ASCO–CAP guidelines, the result is classiﬁed into ﬁve categories by FISH;
    - group 1: When the HER2/CEN17 ratio is ≥2.0, and the average HER2 gene copy number ≥ 4 is reported as positive;
    - group 2: When the HER2/CEN17 ratio is ≥2.0, and HER2 gene copy number < 4 is reported as negative, unless concurrent IHC 3+
    - group 3 : When HER2/CEN17 ratio is <2.0, and HER2 gene copy number ≥ 6 is
    reported as negative, unless concurrent IHC 2+ or 3+;
    - group 4 : When HER2/CEN17 ratio is <2.0, and HER2 gene copy number ≥ 4 and <6 is reported as negative, unless concur-rent IHC 3+;
    - group 5 : When HER2/CEN17 ratio is <2.0, and HER2 gene copy number < 4 is reported as negative [24,26]
- Accurate assessment of HER2 status is an essential step to identify the subset of breast cancer patients who may beneﬁt from the anti-HER2 targeted therapy [17,26–28]. Manual assessment of the HER2 ampliﬁcation status is very time-consuming, laborious, and error-prone.
- However, analysis of HER2 expression is challenging due to unclear
and blurry cell boundaries with large variations on cell shapes and signals as illustrated in
Figure 1.

# Tasks:

- The pathologists produced a reference standard by manually annotating the HER2, ERBB2, and CEN17 signals in the FISH and DISH images.
- Developed soft label fully convolutional network (SL-FCN).
- In our study, we proposed a new loss function, namely the soft weight softmax loss function, which utilizes soft labels and integrates the concept of a label smoothing method [45,54] into the softmax loss function (see Sections 3.2.1 and 3.2.2) to improve the image segmentation results on data with blurry or unclear cell boundaries.
- Compare the model’s  performance with thirteen deep learning approaches, including  U-Net, U-Net with InceptionV5, Ensemble of U-Net with Inception-v4, Inception-Resnet-v2 encoder, and ResNet-34 encoder, SegNet, FCN, modiﬁed FCN, YOLOv5, CPN, SOLOv2, BCNet, and DeepLabv3+ with three different backbones, including MobileNet, ResNet,
and Xception, on three clinical datasets, including two DISH datasets on two different magniﬁcation levels and a FISH dataset.
- 

# Results:

- The result:
    - on DISH breast dataset 1 shows:
        - SL-FCN: achieves high accuracy of 87.77 ± 14.97%, recall of 91.20 ± 7.72%, and F1-score of 81.67 ± 17.76%.
    - on DISH breast dataset 2 shows:
        - SL-FCN: achieves high accuracy of 94.64 ± 2.23%, recall of 83.78 ± 6.42%, and F1-score of 85.14 ± 6.61%.
    - on the FISH breast dataset show:
        - SL-FCN: achieves high accuracy of 93.54 ± 5.24%, recall of 83.52 ± 13.15%, and F1-score of 86.98 ± 9.85%.
- SL-FCN: method outperforms most of the benchmark approaches by a signiﬁcant margin (p < 0.001).
- In evaluation of segmentation of PTC on Papanicolaou-stained WSIs:
    - SL-FCN: method achieves high accuracy of 99.99 ± 0.01%, precision of 92.02 ± 16.6%, recall of 90.90 ± 14.25%, and F1-score of 89.82 ± 14.92% and signiﬁcantly outperforms the baseline methods, including U-Net and FCN (p < 0.001).

# Conclusion:

- The algorithms we developed are more objective, precise, and unbiased than the current standard manual interpretation results for anti-HER2 target therapy.
- the high degree of accuracy, precision, and recall, the results show that the proposed
method could be used in assisting breast cancer target therapy and thyroid cancer diagnosis with faster evaluation and minimizing human judgment errors.

# Quote:

- Immunohistochemistry (IHC) is **a technique that uses antibodies to detect and visualize antigens in tissue samples.**
- What is soft labelling :
    - In traditional segmentation methods, the network usually receives binary ground truth labels or hard labels (label values are 0 and 1 only), which may cause information loss, especially for the pixels at the boundary between two different types [45]. **To prevent this limitation, instead of hard labels, researchers [45–47] propose to use soft labels** (label values are continuous values between 0 and 1), which can preserve more image information throughout the training process [47]