# Human understandable thyroid ultrasound imaging AI report system — A bridge between AI and clinicians

Author: Siqiong Yao
Score: ⭐️⭐️⭐️⭐️
Link: https://github.com/Snowinbio/TiNet-iScience2023
DataSet: Private 
Date published: 21/04/2023
Method: foreground optimization segmentation network + Resnet18
Status: In progress
Task: Risk stratiﬁcation based on AI, TI-rads, Tumour Malignancy Diagnosis
Type: Journal
Data type : imagery data, ultrasound image
Journal Name: CellPress indexed in (ScienceDirect and PubMed)
Type of paper: Experimental article

Objective:

- the aim of this study is to design, develop, and validate an AI report system for ultrasonographical thyroid cancer diagnosis that, in addition to malignancy prediction, provides human understandable features that AI used to derive its diagnosis.
- to develop and validate a human understandable AI report system.

Problematic:

- Artiﬁcial intelligence (AI) enables accurate diagnosis of thyroid cancer; however, **the lack of explanation limits its application.**

Task:

- we collected 10,021 ultrasound images from 8,079 patients across four independent institutions
- build  model named “TiNet” can extract thyroid nodule features such as texture, margin, echogenicity, shape, and location using a deep learning method.
- 

Results:

- it offers excellent prediction performance (AUC 0.88).
- TiNet demonstrated signiﬁcantly higher performance (AUC 0.88) compared with TIRADS (0.80) in the external test set (p < 0.001, by De-Long’s test; Figure 4).
- Particularly, the speciﬁcity of TIRADS was relatively low. Furthermore, we have conﬁrmed the contribution of ﬁve features to the prediction were the textured feature (65.23%), edge margin feature (12.29%), echogenicity feature (8.43%), shape feature (7.67%), and growth position information (6.38%). Figure 5 presented the performance of the thyroid and nodule segmentation modules.

Model:

- TiNet was designed with ﬁve channels to extract features for texture, margin, echogenicity, shape, and location of thyroid nodules and nodule segmentation was a prerequisite for analysis.
- To address this, we employed a foreground optimization segmentation network which took the feature pyramid network (FPN)26 as the backbone to enhance the contextual relevance of the foreground by calculating the global similarity matrix.
- In texture and margin channels, we used Resnet-1827 as the framework for feature extraction. Echogenicity and shape channels were calculated based on echo difference and aspect ratio respectively.
- In the location channel, we segmented the thyroid using the U-Net28 and creatively used a differential homeomorphism-based registration29 method to perform homogeneous positioning of nodules in ultrasound images of various patients, and then we designed a deep graph convolutional neural network (DGCNN)30,31 to location information of nodules for thyroid cancer prediction.
- 

Limitation:

- this work was retrospective and the data collection was limited.
- the data that we collected were mainly single papillary thyroid nodules.
- TiNet only extracted ﬁve features related to clinical diagnosis of thyroid cancer. We have reason to believe that more valuable information about thyroid cancer prediction can be tried to ﬁnd based on the architecture-design of TiNet.

Conclusion:

- TiNet can serve as a bridge between AI-based diagnosis and clinicians, enhancing human–AI cooperative medical decision-making.

Why clinicians interest with Explainable AI:

- First, clinicians are interested in understanding how AI achieves its higher diagnostic accuracy compared to human experts. A speciﬁc question is whether AI models ﬁnd some novel features unrecognized by human experts before, or does AI only optimize known features with more precise digitization (e.g., converting categorical features into numerical features).12,13
- Second, in real-world healthcare settings, clinicians must combine AI predictions with their own ultrasound ﬁndings and other types of clinical information of patients to achieve medical-related decision-making. However, this task would be difﬁcult to perform without interpreting AI results, especially when AI predictions contradict clinicians’ own assessment.14
- Third, current AI models are mostly trained and validated in cleaned and selective data. Hence, unexpected errors likely occur in complicated real-world healthcare settings.15,16 For example, if a clinician mistakenly inputs an X-ray image into an ultrasound AI model, the AI will still output a prediction anyway. Without a human understandable interpretation of AI, clinicians would ﬁnd it difﬁcult to be aware of the occurrence of such error, which could potentially harm the patients.17

Quote:

- Ultrasonography is currently the most commonly used method for detecting thyroid cancer, and with improvements in resolution, detection rates of thyroid cancer keep increasing.1
- According to previous studies, artiﬁcial intelligence (AI) on ultrasound images using deep learning models could achieve higher diagnostic performance for thyroid cancer than human experts.2–8
- However, AI models have been extensively criticized for their black-box nature; that is, they can provide a prediction, but fail to interpret themselves as a human understandable reasoning process.9–11.
-