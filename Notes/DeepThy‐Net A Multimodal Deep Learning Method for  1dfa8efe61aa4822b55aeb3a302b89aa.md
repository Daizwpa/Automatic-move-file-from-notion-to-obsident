# DeepThy‐Net: A Multimodal Deep Learning Method for Predicting Cervical Lymph Node Metastasis in Papillary Thyroid Cancer

Author: Jincao Yao
Score: ⭐️⭐️⭐️⭐️⭐️
DataSet: Private
Date published: 10/08/2022
Key word: Deep Learning, Medical imaging, Ultrasound imaging, computational methods, lymph-node metastasis, papillary thyroid cancer
Method: Multimodal deep learning CNN
Pre-processing: crop tumour area (224*224), scaling and brightening by 0.9-1.1 times, horizontal or vertical reversals, -10 to +10 random rotations
Status: Done
Task: Cervical Lymph Node Metastasis, Metastasis Diagnosis
Type: Journal
AUC on test: 0.874
Sensitivity on test: 82
Specificity on test: 85
Data type : Clinical data, imagery data, ultrasound image
Journal Name: Advanced Intelligent systems indexed Willy online library
Muti-central Data: True
Number Of Patient: 6032
Output : trinary (Central-only, Central and lateral, Non-metastasis)
Type of paper: Experimental article

Objective:

- **prediction of different patterns of cervical lymph node metastasis (CLNM) in PTC.**
- 

Problematic:

- Timely and accurate detection of the CLNM in PTC during the active surveillance process and application of effective treatment modalities are crucial for effective PTC management.

Task:

- Collect 23617 US images from 6,032 patient  with clinical profile of patient. The data collect from 3 different  medical centre.
    
    ![Untitled](DeepThy%E2%80%90Net%20A%20Multimodal%20Deep%20Learning%20Method%20for%20%201dfa8efe61aa4822b55aeb3a302b89aa/Untitled.png)
    

- They Applied on image the following pre-processing technique ( crop tumour area (224*224), scaling and brightening by 0.9-1.1 times, horizontal or vertical reversals, -10 to +10 random rotations)
- They build model known as DeepThy-Net. which is Deep CNN model to extract features map. After extracting features map they concatenated with clinical data given from doctors and pass them to full connected layer. The final out put is either (Central-only metastasis, Central and lateral metastasis, non- metastasis).
- In this study, we improved the basic CSAC, and built four
enhanced cross-layer sparse atrous convolution (E-CSAC)
- Visualize the extract features map.
- Compare the model  performance with other models, also with and without clinical features data.

 

Result:

- the model is tested in two independent test sets, and the experimental results show that the area under curve (AUC) is between 0.870 and 0.905, indicating clinical applicability.

Quote:

- Papillary thyroid cancer (PTC) accounts for more than 80% of thyroid cancers, and ultrasound (US) imaging is the preferred method for the diagnosis of PTC.
- Thyroid cancer is a common disease with an incidence rate of 6.6%, and its incidence is threefold higher among women compared with men.[1,2]
- Papillary thyroid cancer (PTC) accounts for more than 80% of all thyroid cancers, and some of them develop cervical lymph node metastases (CLNM).[3–6]
- Although ultrasound (US) imaging is the preferred method for the diagnosis of PTC,[7–9]
- However, given the varying operating skills and experience of radiologists, the incidences of misdiagnoses and missed diagnoses are still high, especially in the early stages of metastasis.[12–15]
- Although many studies have shown that the features of PTC lesion in US images were highly correlated with CLNM, there is still no accurate or efficient method that can predict the risk of different CLNM patterns prior to operation.[16–19]
- exploring a noninvasive assessment method for different CLNM patterns is of great value for the treatment and disease management of PTC.
- To address this problem, earlier studies attempted to use clinical factor-based statistical methods to predict the risk of different CLNM in PTC.[20–24].
- Generally, these traditional methods mainly relied on clinical experience or risk factors, and the prediction accuracy was not high.
- With the development of medical image processing and feature extraction technology, many studies have begun to use machine learning(ML) models and high-throughput radiomic features (HTRF)of the tumor US images to obtain better results.[23,24]

The model architecture.

![Untitled](DeepThy%E2%80%90Net%20A%20Multimodal%20Deep%20Learning%20Method%20for%20%201dfa8efe61aa4822b55aeb3a302b89aa/Untitled%201.png)