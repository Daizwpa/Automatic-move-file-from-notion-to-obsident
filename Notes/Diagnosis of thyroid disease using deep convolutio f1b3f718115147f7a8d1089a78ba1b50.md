# Diagnosis of thyroid disease using deep convolutional neural network models applied to thyroid scintigraphy images: a multicenter study

Author: Huayi Zhao
Score: ⭐️⭐️⭐️⭐️⭐️
DataSet: Private
Date published: 11/08/2023
Key word: Deep convolutional neural network, artiﬁcial intelligence, nuclear medicine physicians, thyroid diseases, thyroid scintigraphy
Method: AlexNet, ShufﬂeNetV2, MobileNetV3, ResNet-34*
Status: Done
Task: Nuclear medicine
Type: Journal
Data type : 99mTc-pertechnetate thyroid scintigraphy, imagery data
Journal Name: Frontiers in Endocrinology
Explainability : Class-specific attentional
Muti-central Data: True
Number Of Patient: 3194
Output : Graves’ disease, subacute thyroiditis, thyroid tumors, and normal
Transfer learning: AlexNet, MobileNetV3, ResNet-34, ShufﬂeNetV2
Type of paper: Experimental article

Objective:

- to improve the diagnostic performance of nuclear medicine physicians using a deep convolutional neural network (DCNN) model.

Problem statement:

- the interpretation of thyroid scintigraphy ﬁndings relies heavily on the expertise of nuclear medicine physicians. The ﬁnal diagnosis results are easily limited by physicians’ experience
and subjective factors, which can lead to misdiagnosis or affect the accuracy rate. Therefore, the use of deep learning technology to assist clinicians in the high-precision diagnosis of thyroid diseases is of great clinical signiﬁcance.

Task:

- Collecting multi-center dataset, 3194 SPECT thyroid images were collected for model training (n=2067), internal validation (n=514) and external validation (n=613). acquired by using Millennium VG scanner, a Symbia T6 SPECT/CT, and a Symbia Intevo Bold scanner.
- Build four pre-trained classifier AlexNet, ShufﬂeNetV2, MobileNetV3 and ResNet-34 to classify thyroid disease. They trained using Cross-Entropy with Adam optimizer (attenuation weight of 1e-4 ).  The initial learning rate was set to 2.5 × 10 −5 and was gradually updated using the stochastic gradient descent algorithm.
- Apply 5-fold cross-validation on the model with the highest accuracy.
- Compare the performance of the model with two nuclear medicine physicians junior 2 year experience and senior with 5 year experience.
- Visualizing heatmap attention using Class-specific attentional.

Results:

- The improved ResNet- 34 model performed best, with an accuracy of 0.944.
- In Internal validation set, the ResNet-34 model showed higher accuracy (p < 0.001) when compared to that of the senior nuclear medicine physician, with an improvement of nearly 10%.
- Our model achieved an overall accuracy of 0.931 for   higher accuracy than that of the senior physician (0.931 vs. 0.868, p < 0.001).

Conclusion:

- The DCNN-based model performed well in terms of diagnosing thyroid scintillation images.
- The DCNN model showed higher sensitivity and greater speciﬁcity in identifying Graves’ disease, subacute thyroiditis, and thyroid tumors compared to those of nuclear medicine physicians, illustrating the feasibility of deep learning models to improve the diagnostic efﬁciency for assisting clinicians.

Quotes:

- Many studies have demonstrated that thyroid scintigraphy is an effective method for
differentiating Graves’ disease, thyroiditis, and thyroid tumors (7, 8).
-