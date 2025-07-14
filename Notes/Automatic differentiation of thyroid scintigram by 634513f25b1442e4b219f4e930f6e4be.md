# Automatic differentiation of thyroid scintigram by deep convolutional neural network: a dual center study

Author: Pei Yang 
Score: ⭐️⭐️⭐️⭐️
DataSet: Private
Date published: 25/11/2021
Key word: Artificial intelligence (AI), Deep Learning, thyroid scintigraphy
Method: ResNet50, DenseNet169, InceptionV3*, and InceptionResNetV2 
Pre-processing: Convert to grayscale, augmentation (flip, rotate, mix-up), normilzation
Status: Done
Task: Classification of Scintigram, Nuclear medicine
Type: Journal
Data type : 99mTc-pertechnetate thyroid scintigraphy, imagery data
Journal Name: BMC Medical Imaging
Optimization : No
Explainability : No
Features selection : No
Muti-central Data: True
Number Of Patient: 3389
Output : Diffusely increased or Diffusely decreased or Focal increased or heterogeneous uptake
Transfer learning: Yes
Type of paper: Experimental article

Objective:

- we aimed to develop an artificial intelligence (AI) system to automatically classify the four patterns of thyroid scintigram.

Problem statement:

- 

Task:

- Collecting 3087 thyroid scintigrams from center 1 and 302 case from center 2.
- Select ResNet50, DenseNet169, InceptionV3, and Inception ResNetV2  pre-trained model to construct Classifier.
- Evaluate the performance.

Results:

- The overall accuracy of four pre-trained neural networks in classifying four common **uptake patterns of thyroid scintigrams** all exceeded 90%, and the InceptionV3 stands out from others. It reached the highest performance with an overall accuracy of 92.73% for internal validation and 87.75% for external validation, respectively.
- Accordingly, the corresponding performances also obtained an ideal result of 0.939, 1.000, 0.974, and 0.915 in external validation, respectively

Conclusion:

- Deep convolutional neural network-based AI model represented considerable performance in the classification of thyroid scintigrams, which may help physicians improve the interpretation of thyroid scintigrams more consistently and efficiently.

Quates:

- Thyroid scintigraphy with 99mTc-pertechnetate is an essential complementary exanimation for the evaluation of thyroid function as a follow-up to blood biochemical tests and thyroid ultrasonography.
- It is a valid and convenient avenue to identify the causes of thyrotoxicosis, especially for distinguishing Graves’ disease (GD) and toxic multinodular goiter (TMG) when both thyrotropin receptor antibody was negative or differentiating GD from thyroiditis [1].
- The interpretation of thyroid scintigram is always focused on the degree of radionuclide uptake, which was mostly described as diffuse or focal, homogeneous or heterogeneous, and increased or decreased [2]