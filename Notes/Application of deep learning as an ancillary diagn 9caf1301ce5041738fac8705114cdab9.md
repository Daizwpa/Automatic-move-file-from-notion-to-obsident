# Application of deep learning as an ancillary diagnostic tool for thyroid FNA cytology

Author: Mitsuyoshi Hirokawa MD
Score: ⭐️⭐️⭐️⭐️
Link: https://github.com/huggingface/pytorch-image-models
DataSet: private pathology image
Date published: 16/12/2023
Key word: Artificial intelligence (AI), Deep Learning, computer‐assisted diagnosis, cytology, thyroid gland
Method: Transform learning 
Status: Done
Task: Tumour Malignancy Diagnosis
Type: Journal
Data type : Histologic Images, cytology images
Optimization : No
Explainability : gradient‐weighted class‐activation
Features selection : No
Muti-central Data: False
Number Of nodules: 393
Number Of Patient: 393
Output : 9 classes
Transfer learning: EfficientNetV2-L
Type of paper: Experimental article

Objective:

The objective of this study was to demonstrate the accuracy of AI‐based image analysis for
thyroid fine‐needle aspiration cytology (FNAC) and to propose its application in clinical practice.

Task:

- They collected 9782 images from 393 thyroid nodules. the collected images have 15 patches of 256*256 with and without carcinoma. so the number of instance is 148,395. for more information look at table 1. (73,257 positive and 75,138 negative images)
- They pre-trained EfficientNetV2-L model on ImageNet dataset and then used to classification tumours (PTC, FA, FTC, oxyphilic cell–type follicular tumor, PDTC, ATC, MTC, and thyroid lymphoma) as positive and benign tumours as negative. using  AdamW (lr = 1e‐4, weight decay = 5e‐5) with the cosine scheduler (minutes_lr = 1e‐5)
- they applied data augmentation (a horizontal flip, vertical flip, and CutMix (α = 1; p = .5)).
- the cross‐entropy error was used as the loss function.
- generalized mean pooling was used immediately before the fully connected layer
- Although label smoothing and focal loss were used, the results were not refined.
- split the dataset to 80% for training and 20% for testing( patch images from the same nodule were not traversed in the data for training, validation, or testing)
- Preform 5-fold cross validation.

Quote:

- The diagnostic accuracy of thyroid fine‐needle aspiration cytology (FNAC) has improved because of the development and widespread use of ancillary techniques, such as rapid on‐site evaluation, liquid‐based cytology (LBC), biochemical measurement of the needle washout fluid, immunocytochemistry, and flow cytometry.1–4 In addition, molecular testing using aspirated materials has been incorporated as an option into the clinical management of nodules that are diagnosed as follicular neoplasm (FN) or atypia of undetermined significance (AUS).5

Results:

- 

Conclusion:

-