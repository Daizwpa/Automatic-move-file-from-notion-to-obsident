# A generic deep learning framework to classify thyroid and breast lesions in ultrasound images

Author: Yi-Cheng Zhu
Score: ⭐️⭐️⭐️⭐️⭐️
DataSet: Private
Date published: 12/11/2020
Key word: Breast cancer, Cancer recognition, Deep convolutional neural network, Thyroid cancer, Ultrasonography
Status: Done
Task: Tumour Malignancy Diagnosis
Data type : imagery data, ultrasound image
Optimization : No
Features selection : No
Number Of Patient: 1611
Output : Binary (Malignant or Benign)
Transfer learning: VGG19
Type of paper: Experimental article

Objective:

- propose a generic DCNN architecture with transfer learning and the same architectural parameter settings to train models for thyroid and breast cancers (TNet and BNet) respectively, and test the viability of such a generic approach with ultrasound images collected from clinical practices.

Problematic:

- The diagnosis depends on the experience and cognitive capabilities of individual radiologists (subjectivity)
- Limitation of conventional machine learning (radiomics) such as “ The performance of these models influence by image modalities, image qualities, similarity in morphology of lesions, type of cancers.
- 

Task:

- Collection ultrasound for both breast  and thyroid in total 1611.
- Evaluate the ultrasound image using Ti-rads and Bi-rads.
- Pre-processing:
    - Cropping: manual.
    - Data augmentation:
        - Geometric methods: rotation and mirroring.
        - Singular value decomposition method.
- Building CNN models: VGG19 pre-trained in ImageNet.

Results:

- Test results show that both TNet and BNet built on the same DCNN architecture have achieved good classification results (86.5% average accuracy for TNet and 89% for BNet).
- **Furthermore, we used TNet to classify breast lesions and the model achieves sensitivity of 86.6% and specificity of 87.1%, indicating its capability in learning features commonly shared by thyroid and breast lesions.**
- The area under curve (AUC) for thyroid nodule classification is 0.861 (95% CI: 0.792–0.929) for the TNet model and 0.757–0.854 (95% CI: 0.658–0.934) for the three radiologists.
- The AUC for breast cancer classification is 0.875 (95% CI: 0.804–0.947) for the TNet model and 0.698–0.777 (95% CI: 0.593–0.872) for the radiologists

Conclusion:

- In conclusion, the CNN-based models (TNet, BNet and even TBNet) have shown good performance in classifying both thyroid and breast cancers.
- 

Quotes:

- Previous evi­dences suggest that the chance of having breast and thyroid cancers in the same female patients is greater than that of the general population [13,14]. A possible association between breast and thyroid cancer has also been demonstrated, including shared hormonal risk factors and genetic susceptibility [15]. **Furthermore, thyroid and breast cancers do share common image characteristics under high frequency ultrasound scans such as malignant lesions with a taller-than-wide shape ratio, hypo-echogenicity, and ill-defined margins [16,17].**
- Compared with MRI and CT, US is a universally used imaging modality that is non-invasive, non-radiative, and of lower cost. The accuracy of US-based diagnoses of thyroid or breast cancers, however, largely depends on the experience and cognitive capabilities of individual radiologists [2].
- Due to such challenges, many studies have reported the usefulness of computer-aid diagnosis (CAD) systems [3]. Exploiting machine learning and com­puter vision techniques, a CAD system attempts to extract morphological and texture features from ultrasound images and train effective models based on the extracted features to classify the status of malignancy for
the thyroid and breast lesions.
- 

The key contributions of this paper include: 

- a generic CNN-based modelling framework suited for both thyroid and breast lesion classification based on a modified version of an known architecture [18],
- a novel singular value decomposition (SVD) technique for data augmen­tation to enlarge the training set and generalize the trained models
- trained CNN models on thyroid or breast images captured from US machines of different makes that can learn common features of both types of lesions, and
- an evaluation showing that the trained TNet and BNet perform well and that the TNet model either matches or even outperforms experienced radiologists in classifying both breast and thyroid lesions.
-