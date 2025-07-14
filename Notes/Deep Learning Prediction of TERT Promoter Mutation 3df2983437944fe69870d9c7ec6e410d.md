# Deep Learning Prediction of TERT Promoter Mutation Status in Thyroid Cancer Using Histologic Images

Author: Jinhee Kim
Score: ⭐️⭐️⭐️⭐️
DataSet: Whole slide image Private dataset
Date published: 09/03/2023
Key word: CRNN, Color transformation, Convolutional neural network (CNN), Deep Learning, TERT, Thyroid cancer
Method: pretrained CNN (for detection) + pretrained RCNN ( for prediction)
Status: Done
Task: Genetic Diagnosis, Predicting TERT Promoter Mutation
Type: Journal
Data type : Histologic Images, imagery data
Journal Name: MDPI medicina
Number Of Patient: 25
Type of paper: Experimental article
Mentioned: In Review

The model  DenseNET161 + CRNN with HSV-strong color transform got highest result  99.9% sensitivity and 60% speciﬁcity.

Objective:

To evaluate the mutation status of the TERT promoter in thyroid cancer using our deep learning model.

Problematic:

Real-time PCR testing [34] and next-generation sequencing [35] are currently being used to conﬁrm TERT promoter mutation status. However, testing all thyroid cancers for the TERT promoter mutation might not be cost effective considering the low incidence of TERT promoter mutations in thyroid cancer [7]. Therefore, predicting TERT promoter mutations via histologic images using a deep learning approach can be a useful screening tool.

Task:

- Collect 80 case of TC . 13 (16.3%) of all case has TERT promote mutation. confirmed using (Real-time PCR test), containing two type of TERT (C228T and C250T).
- select The 13 Real-time PCR confirmed TERT mutation positive and 12 TERT mutation negative. The total dataset is **25**.
- pre-processing image: (Annotation of Tumor and TERT Positives, Down-sampling Ratio,
- Using the hue–saturation–value (HSV)-strong color transformation scheme.
- To address the problem of unbalanced class in dataset. they applied weighted-cross-entropy.
- CNN model for detection areas in histologic image. They applied weighted-cross-entropy.
- Recurrent-CNN (CRNN) for predicting TERT promoter mutations within tumor areas.
- precision, recall, f1 score, accuracy, and area under the curve (AUC) score were utilized to evaluate tumor classiﬁcation performance.
- 

Result:

- the overall experiment results show 99.9% sensitivity and 60% speciﬁcity (improvements of approximately 25% and 37%, respectively, compared to image normalization as a baseline model) in predicting TERT mutations.
- Most bar plots show that the performance scores of the CNN architecture using the
color transformation methods were better than those using image normalization, resulting
in an improvement of approximately >6% (±2%) in terms of both accuracy and AUC score.
- The ﬁgures show that DenseNet161, VGG16, and EfﬁcientNet_b4 had the best performance
results with HSV-strong, HED-strong, and HSV-light transformation methods, respectively.

- The model DenseNET161 + CRNN with HSV-strong color transform got highest result 99.9% sensitivity and 60% speciﬁcity.

Conclusion:

Highly sensitive screening for TERT promoter mutations is possible using histologic image analysis based on deep learning.

Model:

CNN:

![Untitled](Deep%20Learning%20Prediction%20of%20TERT%20Promoter%20Mutation%203df2983437944fe69870d9c7ec6e410d/Untitled.png)

RCNN:

To extract the features of each patch, we applied ResNet152 as a CNN module and added Long Short-Term Memory (LSTM) (which has three RNN layers) to integrate the features and establish a Two-layer MPL module to make final prediction.

![Untitled](Deep%20Learning%20Prediction%20of%20TERT%20Promoter%20Mutation%203df2983437944fe69870d9c7ec6e410d/Untitled%201.png)

Quote

- TERT promoter mutations have been repeatedly found in human cancer, particularly with high frequency in human melanoma and thyroid cancer [5,6].
- Notably, TERT promoter mutations in thyroid cancer have been associated with aggressive clinical behavior [9–11].
- the detection of TERT promoter mutations is important for prognostic stratiﬁcation and patient management.
- Pathogenic mutations in the TP53, BRAF, RAS, and other genes can also promote histologic changes associated with thyroid cancer [39,40]
- TERT promoter mutations occur infrequently in thyroid cancer.
- Notably, TERT promoter mutations in thyroid cancer have been associated with aggressive clinical behavior [9–11]. Thus, the detection of TERT promoter mutations is important for prognostic stratiﬁcation and patient management
- Evidence has shown that digital pathology with artiﬁcial intelligence (AI) can have a wide range of applications [12]. In fact, the use of digital pathologic images can improve  quantitative analysis of certain histologic features, such as tumor-inﬁltrating lymphocytes [13].
- Furthermore, current studies have been actively investigating methods for predicting the mutation status of genes with diagnostic and therapeutic implications using digital pathologic images [14–17].
- Conventionally, a two-step approach is used for predicting genetic alternations in various cancer types [14,15,18]. First, typical tumor areas are distinguished using tissue slides, and subsequently, another deep neural network is applied to classify mutations at the tile level within tumor areas. Recent advances include attention-based multiple-instance learning performed by aggregating tile features with weight-scoring values learned by a neural network for slide-level prediction [19–21].
- It is important to consider the color diversity of histopathological images when training AI for better tumor classiﬁcation. Recent studies have introduced deep neural networks along with color normalization or transformation methods [22,23] as an image pre-processing step that reduces the generalization error.
- Aberrant functionality of the TERT gene can be acquired through other mechanisms, including **TERT mRNA overexpression** and **aberrant promoter methylation patterns** [36–38].

Limitation:

- lack of data.
- The data noise, the WSI might have other type of mutation like BRAF, RAS, TP53.
- We did not perform a subgroup analysis of thyroid cancer because of the limited
number of cases