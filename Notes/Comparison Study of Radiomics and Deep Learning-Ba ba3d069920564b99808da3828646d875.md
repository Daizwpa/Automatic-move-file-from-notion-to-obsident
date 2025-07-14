# Comparison Study of Radiomics and Deep Learning-Based Methods for Thyroid Nodules Classification Using Ultrasound Images

Author: Yongfeng wang
Score: ⭐️⭐️⭐️
DataSet: Private 
Date published: 12/03/2020
Key word: Convolutional neural network (CNN), Radiomics, Thyroid cancer, Ultrasound images, nodule classification, thyroid nodule
Method: CNN (VGG16) + Transform learning;  
Status: Done
Task: Comparison study, Tumour Malignancy Diagnosis, reduce subjectivity
Type: Journal
AUC on test: 0.7127
Accuracy on test: 0.7469
Sensitivity on test: 0.631
Specificity on test: 0.802
Data type : Radiomics features, imagery data, ultrasound image
Optimization : No
Explainability : No
Features selection : mutual information
Muti-central Data: False
Number Of Patient: 1040
Output : Binary
Transfer learning: VGG16
Type of paper: Experimental article

Objective:

- **Compare the performance of radiomics and deep learning based methods for the classiﬁcation of thyroid nodules from ultrasound images.**
- 

Problematic:

- Ultrasonography has been recommended by the American Thyroid Association (ATA) [4] and is a preferred [5] method for early detection and diagnosis of thyroid nodules due to its economy, effectivity and no radiation. However, the resemblance of the manifested pattern which exists in ultrasound images of both benign and malignant thyroid nodules may cause difﬁculties for radiologists in the process of interpreting objective and effective method that can reduce the misdiagnosis rate is becoming more and more critical in the matter of analysis and estimation of ultrasound images for thyroid nodules.

Task:

- Collect data:
- Build Radiomic based model:
    - SVM.
- Build Deep learning based model:
    - VGG16.
- Evaluation:

Results:

- The classiﬁcation of ultrasound images with thyroid nodules by using deep learning could be a better strategy to assess the thyroid nodules,
- The classiﬁcation accuracy, sensitivity, and speciﬁcity of applying radiomics based method are 66.81%, 51.19% and 75.77%, respectively, while these evaluation indexes for the deep learning based method trained to the testing samples are 74.69%, 63.10% and 80.20%, respectively.
- 

![Untitled](Comparison%20Study%20of%20Radiomics%20and%20Deep%20Learning-Ba%20ba3d069920564b99808da3828646d875/Untitled.png)

Conclusion:

- The comparison results show that the deep learning based model outperformed radiomics based method.
- 

Quote:

- Thyroid nodules can be roughly divided into benign and malignant, and about 10% of patients who present thyroid nodules were diagnosed as malignant [3].