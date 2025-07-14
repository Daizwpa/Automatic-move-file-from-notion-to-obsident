# Deep Learning Fast Screening Approach on Cytological Whole Slides For Thyroid Cancer diagnosis

Author: Yi-Jia Lin
Score: ⭐️⭐️⭐️⭐️
DataSet: private
Date published: 02/08/2021
Key word: Deep Learning, ThinPreq, Thyroid Cancer Diagnosis, Thyroid Fine needle aspiration, Whole slide image, cytology
Method: collected data, pre-process, adapted VGG16, compare the performance  with U-net and SegNet (statistical analysis and run time analysis).
Status: Done
Task: Tumour Detection
Type: Journal
Data type : cytology images
Type of paper: Experimental article

Note:

Thyroid ﬁne needle aspiration **(FNA) is an important, safe tool for diagnosing PTC with an accuracy of approximately 94%, and a high degree of sensitivity, speciﬁcity [4,5].**

**The wide use of thyroid FNA has greatly** **reduced the unnecessary thyroid surgical intervention** and **thus increased the percent of malignant nodules among all nodules surgically removed.**

Traditionally a time-consuming cytologic analysis is performed by an experienced pathologist who manually examines the glass slides under a light microscope.

The most common stain for cytological preparations is the Papanicolaou stain

Artiﬁcial intelligence-related applications are also facing challenges, including regulatory roadblocks, **quality of data**, **interpretability**, **algorithm validation**, **reimbursement**, and **clinical adoption** [36].

Objective:

**This study presents a fast, fully automatic and efficient deep learning framework for fast screening of cytological slides for thyroid cancer diagnosis**. We confirmed the robustness and effectiveness of the proposed method based on evaluation results from two different types of slides: thyroid fine needle aspiration smears and ThinPrep slides.

The Problematic:

In clinical practice, visual inspection of cytopathological slides is an essential initial method used by the pathologist to diagnose PTC. Manual visual assessment of the whole slide images is difficult, time consuming, and subjective, with a high inter-observer variability, which can sometimes lead to suboptimal patient management due to false-positive and false-negative.

The results:

the results show that the proposed method achieves an accuracy of 99%, precision of 85%, recall of 94% and F1-score of 87% in segmentation of PTC in FNA slides and an accuracy of 99%, precision of 97%, recall of 98%, F1-score of 98%, and Jaccard-Index of 96% in TP slides

Method:

![Untitled](Deep%20Learning%20Fast%20Screening%20Approach%20on%20Cytologic%2045bedce2ee1a48068595398c675bc33e/Untitled.png)

Pre-process:

WSI is formatted into hierarchical data structure.

Processed by fast background ﬁltering.

Model:

The proposed deep learning network consists of a padding layer, six convolutional layers, ﬁve max-pooling layers, two dropout layers, one deconvolutional
layer, and a cropping layer.

Evaluation metrics:

accuracy, precision, recall, F1-score, and Jaccard-Index.

Run time analysis:

the proposed method takes 0.4 minute to process a WSI using four GeForce GTX 1080 Ti GPUs and 1.7 minute using a single GeForce GTX 1080 Ti GPU, whereas the U-Net model takes 13.2 minutes and the SegNet model takes 15.4 minutes.

The limitation of the study:

Cytopathologists have to face quantitatively **insufﬁcient specimens** for a deﬁnitive diagnosis.

 They used the majority of data in testing 78% and they only use 21% for training!!!

![Untitled](Deep%20Learning%20Fast%20Screening%20Approach%20on%20Cytologic%2045bedce2ee1a48068595398c675bc33e/Untitled%201.png)