# An Artificial Intelligence Model Based on ACR TI-RADS Characteristics for US Diagnosis of Thyroid Nodules

Author: Yufan Chen, BS
Link: https://github.com/CuberMessenger/MultiTask-US-AI-Model
DataSet: private
Date published: 22/03/2022
Method: InceptionResNetV2
Status: Done
Task: Cancer review
Type: Journal
Data type : imagery data, ultrasound image
Journal Name: Radiology  indexed in PubMed
Type of paper: Experimental article

Objective:

- **To develop an artificial intelligence model based on American College of Radiology Thyroid Imaging Reporting and Data
System characteristics for diagnosing thyroid nodules**
- **identifying nodule characteristics (hereafter, MTI-RADS) and to compare the performance of MTI-RADS , radiologists, and a model trained on benign and malignant status based on surgical histopathologic analysis (hereafter, MDiag).**

Problematic:

- US-based diagnosis of thyroid nodules is subjective and influenced by radiologists’ experience levels.
- Radiologists widely use TI-RADS to evaluate thyroid nodules in clinical practice. However, the diagnostic accuracy of TI-RADS depends on the radiologist’s experience level, leading to inconsistent diagnoses between readers, especially among inexperienced radiologists (7–9). Hoang et al (10) showed that there is low interobserver agreement among radiologists’ interpretations.

Task:

- 
- 1588 surgically proven nodules from 636 consecutive patients (mean age, 49 years 6 14 [SD]; 485 women) were included, the data set retrieved from two hospital.
- Cropping ROI.
- The histograms of the input were equalized, and a multiscale convolution kernel was added to the models. Random horizontal flip, random shift along two axis directions (5%), and random scaling (95%–105%) were applied for data augmentation.
- MTIRADS and MDiag composed of InceptionResNetV2 and a fully connected classifier.
- MTIRADS  trained on US images of 1345 nodules for multi output.
- MDiag  trained only on benign and malignant status.
- the fivefold cross-validation was used for the training set to build five models for tow models.
- Compare the performance the two model with radiologists with different experience levels.
- compare deep learning with important US characteristics with deep learning without US characteristics and with junior radiologists (11–13).

Result:

- MTI-RADS AUC 0.91 and sensitivity 83. (55of 66 nodules)
- MTI-RADS no significantly different from those of experienced radiologists (0.93 [P = .45] and 92% [61 of
66 nodules; P = .07]). junior radiologists (0.78 [P , .001] and 70% [46 of 66 nodules; P =.04])
- The specificity of MTI-RADS (87% [154 of 177 nodules]) was higher than that of both experienced and junior radiologists (80% [141 of 177 nodules; P = .02] and 75% [133 of 177 nodules; P = .001], respectively).
- The AUC of MTI-RADS was higher than that of MDiag (0.91 vs 0.84, respectively; P = .001)

Conclusion:

- The area under the receiver operating characteristic curve (AUC) of an artificial intelligence model based on the American College of Radiology Thyroid Imaging Reporting and Data System (TI-RADS) was higher than that of a model trained on benign and malignant status based on surgical histopathologic analysis. The AUC and sensitivity of the model based on TI-RADS exceeded those of junior radiologists; the specificity of the model was higher than that of both experienced and junior radiologists.

Model:

 MTIRADS:

- MTI-RADS was composed of a convolutional neural network based on InceptionResNetV2 and a fully connected classifier (14).
- 

MDiag:

Quote:

- thyroid nodules are exceedingly common in clinical practice and are detected in up to 65% of the general population with US; approximately 10% of all thyroid nodules are malignant (1)
- The high rate of nodule detection may result in overdiagnosis and overtreatment (2).
- To improve the diagnostic accuracy of US, the American College of Radiology published the Thyroid Imaging Reporting and Data System (TI-RADS) in 2017 (3)
- It has been demonstrated that TI-RADS can improve the performance of thyroid nodule stratification and that use of this system leads to a lower rate of unnecessary biopsy than other guidelines (4,5), such as the American Thyroid Association guideline (6).
-