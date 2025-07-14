# DMs-MAFM+EfficientNet: a hybrid model for predicting dysthyroid optic neuropathy

Author: Cong Wu (master student)
Score: ⭐️⭐️⭐️
DataSet: Private CT data set.
Date published: 21/09/2022
Key word: Convolutional neural network (CNN), Deep Learning, Dysthyroid optic neuropathy, Medical imaging prediction, Thyroid-associated ophthalmopathy
Method: DMs-MAFM+EfficientNet
Pre-processing: crop and augmentation
Status: Done
Task: Thyroid diseases classification
Type: Journal
Data type : CT, imagery data
Journal Name: https://link.springer.com/journal/11517
Explainability : No
Features selection : No
Muti-central Data: False
Number Of Patient: 178
Output : dysthyroid optic neuropathy binary
Type of paper: Experimental article

Thyroid-associated ophthalmopathy (TAO) is a very common autoimmune orbital disease. Approximately 4%–8% of TAO patients will deteriorate and develop the most severe dysthyroid optic neuropathy (DON).

Task:

collecting data, data pre-processing, augmentation.

Propose a hybrid deep learning model to identify dysthyroid optic neuropathy (DON) — to Classify into (DON, TAO or Normal), using eyes CT image.

Compare some version of this hybrid deep learning and other architectures.

Method:

The proposed hybrid model consists of three main models (DMs-MAFM and EfficientNet B0). The DMs-MAFA involves of a multiscale feature fusion module, multiscale channel attention aggregation module and spatial attention modules that are fused. The output of EfficientNet B0 is connected to t-Distributed stochastic neighbour embedding which is a nonlinear dimensional-reduction machine learning algorithm.

Results:

The model got Accuracy= 0.96, Sensitivity= (0.94, 0.95, 1.00), Specificity= (0.99, 0.97, 0.97), F1=(0.96, 0.95, 0.97) on the test dataset.

Objective:

This study proposes a hybrid deep learning model to accurately identify suspected DON patients using computed tomography (CT).

how did they do it:

Data processing and augmentation:

They collect CT dataset from 178 hospital  including 42 DON patients, 49 TAO patients without DON, and 87 healthy. and then they had applied pre-processing which involved those steps (segmenting the image into parts, cropping image into 224*224*3). After that the data augmentation have been applied that includes ( applied CLAHE, applied linear interpolation, applied rotation and mixing processed data with the original unprocessed data).

Methodology:

They proposed hybrid model that concatenated two module: 

![Untitled](DMs-MAFM+EfficientNet%20a%20hybrid%20model%20for%20predictin%20dfcaa3036b794506bee33316236d1f2e/Untitled.png)

the followings are:

![Untitled](DMs-MAFM+EfficientNet%20a%20hybrid%20model%20for%20predictin%20dfcaa3036b794506bee33316236d1f2e/Untitled%201.png)

![Untitled](DMs-MAFM+EfficientNet%20a%20hybrid%20model%20for%20predictin%20dfcaa3036b794506bee33316236d1f2e/Untitled%202.png)

![Untitled](DMs-MAFM+EfficientNet%20a%20hybrid%20model%20for%20predictin%20dfcaa3036b794506bee33316236d1f2e/Untitled%203.png)

![Untitled](DMs-MAFM+EfficientNet%20a%20hybrid%20model%20for%20predictin%20dfcaa3036b794506bee33316236d1f2e/Untitled%204.png)