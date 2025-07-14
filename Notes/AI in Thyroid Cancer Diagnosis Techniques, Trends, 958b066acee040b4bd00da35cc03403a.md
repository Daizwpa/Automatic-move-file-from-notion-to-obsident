# AI in Thyroid Cancer Diagnosis: Techniques, Trends, and Future Directions

Author: https://sciprofiles.com/profile/author/aFFzOUJmcGcyTmdPeTJTQWQvbDRkclhHT1VLZ2RuTHE3WnRFaU9kUk9CWT0=?utm_source=mdpi.com&utm_medium=website&utm_campaign=avatar_name
Score: ⭐️⭐️⭐️⭐️
Date published: 17/10/2023
Key word: Convolutional neural network (CNN), Deep Learning, Machine Learning, thyroid cancer segmentation, thyroid carcinoma detection
Method: thyroid cancer review
Status: Done
Task: AI application in thyroid, Cancer review, thyroid review
Type: Journal
Type of paper: review paper

Task:

- They delved into techniques such as:
    
     deep learning,
    
     artiﬁcial neural networks,
    
     Traditional classiﬁcation,
    
     probabilistic models (PMs) under supervised learning,
    
     unsupervised learning (USL),
    
     bagging algorithms,
    
     and potent boosting algorithms.
    
- Talk about dataset:
    - vital features.
    - elucidating feature selection.
    - extraction techniques critical

**Introduction:**

1.1 background:

Trust (problem) plays a pivotal role in determining user acceptance (AI).

This condition (cancer case)can be categorized into four primary subtypes: papillary carcinoma (PTC) [11], follicular thyroid carcinoma (FTC) [12], anaplastic thyroid carcinoma (ATC) [13], and medullary thyroid carcinoma (MTC) [14].

 **Inﬂuential factors such as** high radiation exposure, Hashimoto’s thyroiditis, psychological and genetic predispositions, and advancements in detection technology can contribute to the onset of these cancer types. **These conditions might subsequently lead to** chronic health issues, including diabetes, irregular heart rhythms, and blood pressure ﬂuctuations [15–17]. 

**Although the quantity of cancer cells is a signiﬁcant indicator for assessing both** invasiveness and poor prognosis in thyroid carcinoma, obtaining results is often time-consuming due to the requirement to observe cell appearance. 

Therefore, **the detection and quantiﬁcation of cell nuclei are considered alternative biomarkers for assessing cancer cell proliferation.**

Endocrinologists frequently conduct US scans in the 7–15 MHz range to identify thyroid cancer and evaluate its anatomical characteristics.

The American College of Radiology has formulated a Thyroid Imaging, Reporting, and Data System (TI-RADS) that classifies thyroid nodules into six categories based on attributes such as **composition**, **echogenicity**, **shape**, **size**, **margins**, and **echogenic foci**

Several open-source applications are available for assessing these thyroid cancer features [21,22]. However, the identification and differentiation of nodules continue to present a challenge, largely reliant on radiologists’ personal experience and cognitive abilities. This is due to the subjective nature of human eye-based image recognition, the poor quality of captured images, and the similarities among US images of benign thyroid nodules, malignant thyroid nodules, and lymph nodes.

Moreover, ultrasonography imaging is often a time-intensive and stressful procedure, which can result in inaccurate diagnoses. **Misclassiﬁcations among normal, benign, malignant, and indeterminate cases are typical [23–28].**

A ﬁne-needle aspiration biopsy (FNAB) is **typically conducted for a more precise diagnosis.** However, FNAB can be an uncomfortable experience for patients, and a specialist’s lack of knowledge can potentially convert benign nodules into malignant ones, not to mention the additional ﬁnancial burden [29,30]

**Machine learning (ML) and deep learning (DL) have surfaced as potential solutions for automating the classiﬁcation of thyroid nodules in applications such as US, ﬁne-needle aspiration (FNA), and thyroid surgery [44,45]**

1.2 Our Contribution:

2) Overview of Existing Frameworks:

Objective of AI-Based Analysis (O):

O1. Classiﬁcation: Thyroid carcinoma classiﬁcation refers to the categorization of thyroid
cancers based on their histopathological features, clinical behaviour, and prognosis

**Advances in AI and machine learning are helping to** automate and improve the accuracy of thyroid carcinoma classiﬁcation, with many models trained to classify tumors based on medical images or genetic data

O2. Segmentation: The segmentation of thyroid carcinoma refers to the process of **identifying and delineating the region of an image** that corresponds to a thyroid tumor

O3. Prediction: The prediction of thyroid carcinoma involves the use of various diagnostic tools, tests, and techniques—often employing machine learning models—**to anticipate the probability of a patient developing thyroid cancer.**

Pre-processing:

**Dimensionality reduction (DR)** is a technique used in the ﬁeld of ML, particularly
in the pre-processing and feature engineering phases, that transforms data from a high-
dimensional space into a lower-dimensional space.

Principal component analysis (PCA) is a multivariate statistical pre-processing method
that transforms variables into a reduced set of uncorrelated variables

Supervised learning:

SL is a method of machine learning where an algorithm is trained **to classify or predict the condition based on labeled data**, which, in this case, are medical data related to thyroid cancer.

The performance of these methods heavily relies on the quality and quantity of the available data. T

Traditional Classiﬁcation (TCL):

The choice of the right algorithm depends on several factors ( e.g. the particulars of the problem, the number of variables, most suitable model for the task, other pertinent factors) 

Unsupervised learning:

In AI and computer science, USL involves analyzing data without pre-existing labels
or annotations.

USL lacks this labeling, making it difficult to assess the accuracy of the results.

Clustering:

The purpose of this method is to segment a set of thyroid cancer data into various
homogeneous groups that possess similar characteristics, making it easier to classify the un-labeled datasets into benign and malignant.

Clustering can also help identify cancer without precise deﬁnitions [92].

C1. K-means (KM):

The K-means (KM) method is a technique for data partitioning and a combinatorial optimization challenge. It is commonly utilized in USL, in which observations are separated into K groups.

C2. Entropy-based  (EB): In 

2.5. Deep learning (DL):

DL is a subset of ML and AI that is based on ANNs with representation learning. ANNs are deﬁned as a class of information processing systems comprised of interconnected nonlinear elements known as neurons.

**In thyroid cancer, DL has been deployed to perform different tasks, including:**

Image classiﬁcation

Pathological analysis

Genomic data analysis

Radiomics

Predictive analysis

Extreme Learning Machine (ELM)

Multilayer Perceptron (MLP)

Radial Basis Function (RBF)

Denoising Autoencoder (DAE)

Convolutional Neural Network (CNN)

Recurrent Neural Network (RNN)

Restricted Boltzmann Machine (RBM)

Generative Adversarial Network (GAN)

Probabilistic Models (PM)

2.6. Ensemble Methods (EMs)

2.6.1. Bagging (B)

B1. Bootstrap aggregation (BA):

B2. Feature bagging (FB):

2.6.2. Boosting (O)

O1. AdaBoost

O2. Gradient tree boosting (XGBoost):

3.Thyroid Cancer datasets:

In this section, we present an overview of the most signiﬁcant thyroid databases

ThyroidOmics:

The dataset consists of the results of the discovery stage of the genome wide association analysis (GWAS) meta-analysis for thyrotropin (TSH), free thyroxine (FT4), increased TSH (hypothyroidism), and decreased TSH (hyperthyroidism) as reported in [179,180].

Thyroid Disease Data Set (TDDS):

The three deﬁned classes in this dataset include normal (not hypothyroid), hyperfunctioning,
and subnormal functioning [181].

KEEL Thyroid Dataset:

TNM8 Dataset:

Gene Expression Omnibus (GEO):

Surveillance, Epidemiology, and End Results (SEER):

Digital Database Thyroid Image (DDTI):

Cancer Genome Atlas (TCGA):

National Cancer Data Repository (NCDR):

Prostate, Lung, Colorectal, and Ovarian (PLCO) dataset

Feature:

This primarily involves identifying a subset of relevant features that positively impact the classiﬁcation accuracy and eliminating irrelevant variables.

Feature Selection Methods (FS):

FS1. Information gain (IG):

Information gain (IG) is a straightforward method for classifying thyroid cancer features. This method evaluates the likelihood of having cancer by comparing the entropy before and after the examination.

IG is utilized as a feature selection technique to eliminate redundant and irrelevant symptoms in datasets related to diabetes, breast cancer, and heart disease.

FS2. Correlation-based feature selection (CFS):

CFS is a technique frequently used for evaluating the correlation between different cancer features.

FS3. Relief (R):

The relief algorithm, commonly known as RA, is an effective method used
in selecting important features by assessing their differentiation quality by assigning scores. This technique calculates the weight of various features based on the correlation between cancer attributes.

FS4. Consistency-based subset evaluation (CSE):

4.2. Feature Extraction Methods (FE):

FE1. Principal components analysis (PCA):

FE2. Texture description:

FE3. Active contour (AC):

FE4. Local binary patterns (LBP):

FE5. Gray-level co-occurrence matrix (GLCM):

FE6. Independent component analysis (ICA):

Limitations and Open Challenges:

Insufﬁcient clean data and accuracy:

Thyroid gland imaging: 

DL models’ hyperparameters:

Computation cost and storage space:

Imbalanced dataset:

Sparse labels:

The volume of data:

Error susceptibility:

Data form:

Unexplainable AI:

Lack of cancer detection platform:

The digitization and loss data:

Contrast:

6. Example of Thyroid Cancer Detection Using AI:

*here they just implemented Neural network on UCI dataset for classify thyroid disorder. for more information please go down to paper.*

7 Critical Analysis And Discussion:

Limitations and open challenges:

Insufﬁcient clean data and accuracy:

Thyroid gland imaging:

DL models’ hyperparameters:

Computation cost and storage space:

Imbalanced dataset:

The distribution of cancer elements within categories related to thyroid tissue cells is often uneven.

This unbalanced distribution of features in cancer cell detection datasets often results in the suboptimal performance of AI algorithms used for the detection [270].

Sparse labels: 

The volume of data: 

researchers are facing challenges in suggesting algorithms that can effectively handle a limited number of samples, noisy samples, unannotated samples, sparse samples, incomplete samples, and high-dimensional samples. This requires AI algorithms that are highly efﬁcient and capable of processing vast quantities of data exchanged between healthcare providers and patients or among specialist physicians [271].

Error susceptibility:

Despite AI being self-sufficient, it is still susceptible to errors.

Data Form:

With the growing demand for various medical imaging technologies that result in vast
quantities of data needed for AI algorithms, coordinating and organizing this information has become a daunting task. This can largely be attributed to the absence of proper labeling, annotation, or segmentation of the data, making it difﬁcult to manage effectively [273].

Unexplainable AI:

Lack of cancer detection platform:

The digitization and loss data:

the risk of signiﬁcant information loss during the quantiﬁcation and inaccuracies that may arise from data compression utilized in autoencoder algorithms.

Contrast:

The absence of sufﬁcient contrast in the tissues neighboring the TG complicates the process of accurately analyzing and diagnosing thyroid cancer.

8. Future Research Directions:

This section highlights promising research trends that will have a major effect on enhancing thyroid cancer detection in the future.

8.1. Explainable Artiﬁcial Intelligence (XAI):

8.2. Edge, Fog, and Cloud Computing for Implementation:

8.3. Reinforcement Learning (RL):

8.4. Transfer Learning (TL):

8.5. Panoptic Segmentation (PS):

8.6. Internet of Medical Imaging Things (IoMIT):

8.7. Three-Dimensional Thyroid Cancer Detection (3D-TCD):

8.8. AI in Thyroid Surgery (AI-TS):

8.9. Wavelet-Based AI:

8.10. Learning with Reduced Data:

8.11. Recommender Systems (RSs):

8.12. Federated Learning (FL):

8.13. Generative Chatbots:

9. Conclusions: