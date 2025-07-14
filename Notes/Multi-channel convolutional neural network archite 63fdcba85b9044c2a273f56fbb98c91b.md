# Multi-channel convolutional neural network architectures for thyroid cancer detection

Author: Xinyu Zhang
Score: ⭐️⭐️⭐️⭐️
Link: https://github.com/Amyyy-z/Multi-channel-DCNN
DataSet: the Digital Database Thyroid Image (DDTI), and private data
Date published: 21/01/2022
Method: Proposed Xception + Multi-channel CNN
Status: Done
Task: Tumour Malignancy Diagnosis
Type: Journal
Type of paper: Experimental article

# What’s done?

The present study adopts Xception neural network as the base structure and designs a practical framework, which comprises three adaptable multi-channel architectures that were positively evaluated using real-world data sets

# The objective:

This research study proposes a framework with adaptive multi-channel architecture that incorporates Xception structure. Regarding highlighting the use of different medical image modalities, a comparison between ultrasound images and CT scans was presented in this paper. The framework allows clinicians to choose the most suitable architecture for thyroid cancer detection, ignoring the input data set characteristics, selecting the output choices, and making it applicable to both balanced and imbalanced data sets.

# Related Work:

Thyroid disease includes functional (i.e., hypothyroidism, hyperthyroidism, and thyroiditis) and neoplastic (i.e., goiter, adenoma, and four types of malignant thyroid nodules. These four malignant types of nodules are formed as four kinds of thyroid cancer: papillary carcinoma, follicular carcinoma, anaplastic carcinoma, and medullary carcinoma [8].

## 1) Machine learning techniques for thyroid disease detection:

With the help of machine learning techniques, thyroid disorder can be efficiently detected [26–38].

Compare to diagnosing thyroid disorder, detecting thyroid cancer is another intense area for scholars to excavate. Classifying thyroid nodules into benign and malignant is a demanding research direction due to increased thyroid cancer instances. Many researchers have adopted machine learning techniques to extract various features from ultrasound images for thyroid cancer detection.

The most commonly seen features used for classifying thyroid nodules through ultrasound images are nodule size, echogenicity, microcalcifications, margin, shape, contour, and vascularity [39].

## 2) Deep learning techniques for thyroid disease detection:

Artificial neural networks (ANN) and CNN are the two most commonly used and outstanding deep learning models for classifying thyroid nodules. Previous studies indicated that ANNs were accurate for distinguishing thyroid nodules between “benign” and “malignant” and have obtained accuracy rates around 82% [48, 49].

## 3) Multi-channel CNN for CAD design:

multi-channel CNN architectures were built and evaluated for sentiment analysis [60], high dynamic range imaging [61], or sentence relation classification [62], all showing ascendant performance.

the goal of increasing medical image classification performance in mind, researchers incorporate multi-channel designs in the medical field.

[63] designed a novel neural network called “LVSNet” for liver vessel segmentation. Within the designed network, they have introduced a multi-scale feature fusion block that evenly divides the features into 4 filter groups; those filter groups are then connected in hierarchical residual learning; in this way, the number of scales in one block can be enhanced.

[64] proposed a “Progressive Atrous Spatial Pyramid Pooling” (PASPP) block for chest CT image  segmentation to detect coronavirus disease 2019 (COVID-19) through adopting different dilation rated convolutions to perceive features with various scales.

[65] adopted magnetic resonance image (MRI) with multi-channel CNN to identify infants who have the risk of autism disease and obtained an accuracy of0.724. Several other research studies accentuated that multi-channel CNN architectures demonstrate enhanced diagnostic performance for particular disease [66–68]

multi-channel CNN architecture designs are distinct depending on the tasks, and researchers tend to ignore the fairly strong association between filter size and CNN performance. Therefore, this research study proposes a multichannel CNN architecture that renovates filter size selection while taking advantage of CT characteristics to drive a diagnosis of thyroid cancer.

## Overall research gaps:

most models take time to classify nodules one by one, which is time-consuming and inefficient. Besides, thyroidectomy is expected for removing all malignant thyroid nodules rather than thyroid glands solely. Hence, classifying each nodule via ultrasounds is time-consuming, and locating malignant nodules during surgeries is impracticable, not to mention the sensitiveness of ultrasound images to speckle noises.

Therefore, the implementation of binary classification tasks using ultrasound images is still challenging for clinical adoptions. Compared to ultrasound images, CT is an efficient tool for detecting abnormal thyroid glands with higher diagnostic accuracy rates [23], and it is always required before surgeries. Nevertheless, studies adopting CT for thyroid cancer detection are still far lacking.

conventional CNN architectures might be outdated as they require more computational resources for generating deeper models in image classification tasks [69]; thus, Xception is currently the right choice due to its enhanced performance with efficiency [24].

# Methodology

This section presents and explains the proposed “multi-channel Xception-based thyroid can-
cer detection” (MXTCD) framework.

### The MXTCD framework

The MXTCD framework was designed and consisted of two main steps:

. Initially, Step 1i:

 indicates that we input medical images into the Xception model for         pre-training purposes using binary classification tasks. This paper incorporates real-world CT scans and ultrasound images to present precise knowledge to the readers regarding the impact of medical image type selections on the detection results. Due to the different input features, we have trained and also fine-tuned the model separately for different data sets. In order to have a comprehensive comparison among all the selected models, the models were then evaluated based on their accuracy rates, f1 score, precision, recall, negative predictive value (npv), and running time.

Step 2: 

applies the Xception-based multi-channel architectures for binary and multi-class classification tasks depending on the clinicians’ needs. Three optional architectures are proposed for selections: the single input dual-channel (SIDC), the double inputs dual channel (DIDC), and the four-channel architectures. Researchers can obtain the enhanced accuracy rates for the specific input data set characteristics regarding thyroid cancer detection through those architectures.

![Untitled](Multi-channel%20convolutional%20neural%20network%20archite%2063fdcba85b9044c2a273f56fbb98c91b/Untitled.png)

### Xception:

Xception, known as “Extreme Inception”, was inspired by Inception models and was firstly introduced by [24].

Xception model maps cross-channel correlations from the input image and addresses spatial correlations of each output channel separately. Therefore, we intend to adopt the Xception model in this work to identify abnormal thyroid nodules from medical images since the model emphasizes spatial correlations of the inputted medical images to better locate and classify the lesion.

In the medical field, clinicians need to deal with a vast amount of complex medical images, making Xception the most appropriate choice since it can provide enhanced diagnostic accuracy and efficiency compared to traditional clinical diagnosis and conventional CNN models [24]. Our ablation evaluations also supported this statement. Therefore, this study selects Xception as the base structure for implementing the multi-channel architectures.

### Multi-channel CNN model:

In this section, the three optional multi-channel architectures were explained based on their
design and implementation.

### Single input dual-channel CNN model:

![Untitled](Multi-channel%20convolutional%20neural%20network%20archite%2063fdcba85b9044c2a273f56fbb98c91b/Untitled%201.png)

Medical images are in different formats and qualities, and sometimes researchers rely on a single type of medical image for making decisions through CAD techniques. In order to obtain a promising diagnostic result for this situation, the SIDC model is designed and presented in Fig 3.

The main advantage of applying the dual channel architecture is:  With the SIDC architecture, enlarged receptive fields can lead to more valuable information be obtained from the original input image; thus, increased classification accuracy rates can be achieved.

By looping through dual-channel architecture, different filter sizes can automatically learn different features from the input images. Specifically, smaller filter sizes will learn detailed textures such as edges, while larger filter sizes will learn more abstract features.

### Double inputs dual-channel CNN model:

![Untitled](Multi-channel%20convolutional%20neural%20network%20archite%2063fdcba85b9044c2a273f56fbb98c91b/Untitled%202.png)

expects to design a patient-specific malignant thyroid.

Evidently, the SIDC model cannot achieve the goal since it focuses on cancerous lesion detection rather than diagnosing individual patient’s thyroid status.

Noteworthy, the DIDC architecture is made for CT scans solely at the current stage. The reason is that CT scans provide a comprehensive view of the thyroid gland, while ultrasound images focus on specific nodules.

the proposed DIDC model has advantages in:

It is designed as patient-specific to detect malignant thyroid nodules for individual patients.

It offers the status of both sides of thyroid glands to the doctors and patients.

The architecture outputs the overall status of the gland, making diagnostic and treatment decisions more efficiently.

CT scans provide a whole sight of thyroid glands, including the left and right lobes, while ultrasound images primarily include one or more nodules in each image at a time …. Not all patients undergo one type of, thyroid disease at a time;

Personalized precision medicine is demanding in the medical domain as no two patients have 100% identical physical conditions or symptoms [76]; thus, feature maps generated from an individual patient or even individual lobes are distinguished from each other.

Under this situation, segmenting whole thyroid CT glands into the left and right sides is necessary to make the labeling process much more accurate and efficient. As ultrasonography does not have this characteristic, this architecture was not implemented with ultrasound images.

Additionally, the left and right input images must be applied in two separate streams so the model can evaluate both sides simultaneously. Both left and right input CT scans must be extracted from one patient. Furthermore, the scale of both input data sets (i.e., the number of both input image sets) must be equal. Similarly, these requirements also apply to our four- channel architecture.

### Four-channel CNN model:

![Untitled](Multi-channel%20convolutional%20neural%20network%20archite%2063fdcba85b9044c2a273f56fbb98c91b/Untitled%203.png)

the four-channel model has several advantages:

It persists the increased accuracy rates obtained by the SIDC model since two different filter sizes were utilized.

It is also designed as patient-specific obtained from the DIDC model.

It enhances the original diagnostic accuracy, at the same time, helps doctors identify each patient’s thyroid status, and helps with decision-making more accurately and effectively.

The four-channel architecture in Fig 5 also only applies to CT scans.

## Data sets acquisition:

![Untitled](Multi-channel%20convolutional%20neural%20network%20archite%2063fdcba85b9044c2a273f56fbb98c91b/Untitled%204.png)