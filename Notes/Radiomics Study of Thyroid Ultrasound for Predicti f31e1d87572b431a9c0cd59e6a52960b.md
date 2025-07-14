# Radiomics Study of Thyroid Ultrasound for Predicting BRAF Mutation in Papillary Thyroid Carcinoma: Preliminary Results

Author: M.-r. Kwon
Score: ⭐️⭐️
DataSet: Private
Date published: 01/04/2020
Method: Radiomic and compare 3 different model LR, SVM and RF
Status: Done
Task: Genetic Diagnosis, Predicting BRFV600E Mutation
Type: Journal
AUC on test: 0.651
Accuracy on test: 64.3
Sensitivity on test: 66.8
Specificity on test: 61.8
Data type : Radiomics features, ultrasound image
Journal Name: ORIGINAL RESEARCH HEAD & NECK
Optimization : No
Explainability : No
Features selection : MRMR
Muti-central Data: False
Number Of nodules: 96
Output : Binary (BARFV600E-positive or BARFV600E-Negative)
Transfer learning: No
Type of paper: Experimental article
Mentioned: In Review
Tool used: MRIcron software for segmentation, Py-Radiomics for radiomics extraction

Objective:

the purpose of this study was to evaluate whether radiomics study of gray-scale US could predict the presence or absence of BRAF mutation in PTC.

Problematic:

According to 2015 American Thyroid Association guidelines, active surveillance of PTC has emerged as a safe alternative to surgical intervention in low-risk patient with PTCs.10 **In this
era, preoperative knowledge of the BRAF mutation status can be one of preoperative modulators for planning an appropriate treatment strategy, such as the determination of an early surgical intervention.**

Task:

- Collected 96 thyroid nodules that include 48 nodules precent BRAF mutation and  48 nodules absent BRAF mutation.
- Extracted a total of 86 radiomics features derived from histogram parameters, gray-level cooccurrence matrix, intensity size zone matrix, and shape features. using Py-Radiomics.
- Split the dataset to80% training set  (n = 77) and 20% test set (n =18).
- Two method of Feature selection were performed using minimum redundancy maximum relevance (mRMR) and Pearson correlation–based feature selection from the training set.
- Build 3 different classiﬁer models, including logistic regression, support vector machine, and random forest.
- Training model using 5fold cross-validation.
- Compare the performance using accuracy, sensitivity, speciﬁcity, positive predictive value, negative predictive value, and area under the receiver operating characteristic curve.

The result:

- The radiomics approach demonstrated that all classiﬁcation models showed moderate performance for predicting the presence of BRAF mutation in papillary thyroid cancers with an area under the curve value of 0.651, accuracy of 64.3%, sensitivity of 66.8%, and speciﬁcity of 61.8%, on average, for the 3 models.
- accuracy, 58.6% (range, 56.16%–60.42%); sensitivity, 63.9% (range, 60.44%–66.89%); and specificity, 53.8% (range, 52.22%–56.67%)

Conclusion:

- **Radiomics study using thyroid sonography is limited in predicting the BRAF mutation status of papillary thyroid carcinoma.** Further studies will be needed to validate our results using various diagnostic methods.

Quote:

- The B-Raf proto-onco-gene, serine/threonine kinase (BRAF)mutation plays a central role  in the pathogenesis of PTC, promoting carcinogenesis through the action of the mitogen-activated protein kinase pathway.3,4
- **The frequency of the BRAF mutation in PTC has been reported to range from 29% to 83% and is known to be the most common genetic alteration in PTC.5,6**
- Many studies have reported that the BRAF mutation is associated with poor clinicopathologic outcomes, such as a high incidence of advanced clinical stage, extrathyroidal extension, and increased recurrence.6-9
- **These results suggest that preoperative knowledge of the BRAF mutation status can be helpful in categorizing patients as high risk and planning an appropriate treatment strategy.**
- **To our knowledge, there have been no published studies aimed at identifying the presence of BRAF mutation using radiomics features of US.**
    
    
    Several studies have investigated whether gray-scale ultrasound (US) findings could predict the presence of the BRAF mutation in PTC and have reported controversial results.
    
    5 Previous studies have reported that histograms and texture analyses of US are useful for differentiating benign and malignant thyroid nodules.16-21
    
    US is the most widely used standard imaging tool in thyroid pathology and is very helpful in dis- criminating between malignant and benign thyroid nodules.
    
    Radiomics is usually performed using tomographic images, including CT, MR imaging, or PET images because these modalities can acquire 3D volume data and data acquisition can be
    standardized by setting scan parameters of the machines so that they are identical.
    
    US has several limitations in quantitative analysis in contrast to tomographic images: Only 2D data can be acquired through this technique along with lack of representative features due to a **limited amount of image data, operator dependency, and dependency on US machines.** 30
    

To our knowledge, there have been no published studies aimed at identifying the presence of BRAF mutation using radiomics features of US.

Tools:

MRIcron software for segmentation.

Py-Radiomics (https://[www.radiomics.io/pyradiomics.html](http://www.radiomics.io/pyradiomics.html)) to extract features.