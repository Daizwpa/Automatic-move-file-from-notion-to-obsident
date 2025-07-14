# AI-BRAFV600E: A deep convolutional neural network for BRAFV600E mutation status prediction of thyroid nodules using ultrasound images

Author: Chuang Xi
Score: ⭐️⭐️⭐️⭐️⭐️
Link: https://github.com/zhaVzha/DCNN-Thyriod-BRAF
DataSet: private ultrasound dataset
Date published: 05/04/2023
Key word: BRAFV600E mutation, Deep Learning, Thyroid cancer, Ultrasound, thyroid nodule
Method: DCNN + Heatmaps
Pre-processing: median filter, contrast-limited adaptive histogram equalization, Normalization, rectangular segmentation, resizing to 224*224, Augmentation : rotation (within 10◦);  flipping; and random. cropping.
Status: Done
Task: Genetic Diagnosis, Predicting BRFV600E Mutation
Type: Journal
Data type : ultrasound image
Journal Name: Wiley Online Library open access View
Optimization : No
Explainability : gradient‐weighted class‐activation
Features selection : No
Limitation : Retrospective study;  
Muti-central Data: True
Number Of Patient: 528
Output : Binary ( mutated or wild)
Transfer learning: They trained their model first on ImageNet
Type of paper: Experimental article
list of features: No
Mentioned: In Review
Multimodal: No
Tool used: ITK-SNAP software for segmenting the ROI

# Objective:

This study aimed to develop a deep convolutional neural network (DCNN) model based on ultrasound images to predict the BRAFV600E mutation status of thyroid nodules.

 develop a DCNN model based on ultrasound images that could be used to  conveniently and non-invasively predict the BRAFV600E mutation status of thyroid nodules.

## Problematic:

the detection of this mutation requires specimens obtained through invasive modalities, such as
fine-needle aspiration (FNA) and surgery. Therefore, it is necessary to develop a non-invasive method for the prediction of the BRAFV600E mutation status of thyroid nodules.

  

# Task:

- Collect ultrasound image from center 1 (979 images, 528 patients)
- In the test stage, we collected 531 images for independent test sets from 282 patients at four hospitals.
- a total of 528 patients from center 1 were included in the primary set (BRAFV600E-mutant type: 447 images, 239 patients; BRAFV600E-wild type: 532 images, 289 patients).
- apply median filtering on the images to  to balance the variety of images and used contrast limited adaptive histogram equalization16 to ensure the same range of grayscale values of all images
- Experienced radiologist using ITK-SNAP software segmented the ROI.
- we applied data augmentation for each image through rotation (within 10◦), flipping, and random cropping.
- build DCNN model.
- fivefold cross-validation to train the model using the primary set (80% images for training and 20% images for validation).
- areas under the receiver operating characteristic curve (AUC), accuracy, sensitivity, and specificity in four independent test sets from center 1 to center 4 (531 images, 282 patients)
- use heatmap for visualizing the most prediction reign.

Model:

# What did they do (Method):

 They trained and validated the DCNN model based on the primary set from center 1 (979 images, 528 patients). The DCNN network consists of Conv block, Down-sample block, Gaussian error linear unit, Global Average Polling, and Full Connected. The predictive performance of this model was evaluated by using areas under the receiver operating characteristic curve (AUC), accuracy, sensitivity, and specificity in four independent test sets from center 1 to center 4 (531 images, 282 patients). Heatmaps were used to visualize the most predictive regions of each image. Specimens obtained through fine-needle aspiration or surgery were used to detect the BRAFV600E mutation.

How did they do it:

They build the model using Pytorch 1.8.1. and train it first on Image-net dataset and then they retrain it on  their dataset of thyroid ultrasound. they used Adam as optimizer with batch size 32 and learning rate 0.0001. they reduced  the learning rate plateau.

# Result:

- The DCNN model achieved encouraging predictive performance by fivefold cross-validation (AUC 0.95) in the primary set.
- The deep learning score revealed significant differences between BRAFV600E-mutant and BRAFV600E-wild-type groups (all test sets p < .001).
- The heatmaps visualized the most predictive region located inside or alongside the thyroid nodules.
- in the independent internal test set (AUC0.93) and three independent external test sets (AUC 0.84–0.88).

## Conclusion:

A DCNN model with encouraging predictive performance was developed based on ultrasound images to predict the BRAFV600E mutation status of thyroid nodules.

## Quote:

- The initiation and progression of thyroid cancer involve multiple genetic alterations that have diagnostic effects and can guide treatment.2
- The BRAFV600E mutation is representative of these genetic alterations and promotes carcinogenesis and pathogenesis of thyroid cancer by activating the mitogen-activated protein kinase pathway.3
- the detection of BRAFV600E mutation has been widely used as a valuable diagnostic method for the discrimination of benign and malignant thyroid nodules.4
- Except for its diagnostic efficacy, BRAFV600E mutation also represents a poor prognosis with an increased risk of mortality and a decreased ability of radioiodine uptake.5
- Therefore, the detection ofBRAFV600E mutation could certainly help physicians select appropriate treatment and follow-up strategies for patients with thyroid nodules or thyroid cancer.
- Some studies have reported that **the BRAFV600E mutation is frequently associated with malignant ultrasound features, including hypoechogenicity, microcalcifications, irregular margins, a taller-than-wide shape, and extrathyroidal invasion.**6 Therefore, it seems reasonable to predict BRAFV600E mutation by analyzing features of ultrasound images.
- Radiomics has shown promising results in the non-invasive assessment of genetic alterations in a variety of malignancies.8
- **the ultrasound has some intrinsic limitations, such as performer dependency of image interpretation and various diagnostic  accuracies among different radiologists,7 which bring
difficulties to the prediction of BRAFV600E mutation by ultrasound features.**