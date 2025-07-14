# Thyroid Disease Prediction Using Selective Features and Machine Learning Techniques

Author: Rajasekhar Chaganti
Score: ⭐️⭐️⭐️
DataSet: UCI: Thyroid Disease
Date published: 13/08/2022
Key word: Machine Learning, bidirectional feature elimination, forward feature selection, thyroid prediction
Method: RF
Status: Done
Task: Thyroid diseases classification
Type: Journal
Data type : Clinical data, Demographic data, blood test data
Number Of Patient: 9172
Output : multi-class
Type of paper: Experimental article

# The Objective:

The study presents a thyroid disease prediction approach which utilizes random forest-based features to obtain high accuracy. The approach can obtain a 0.99 accuracy to predict ten thyroid diseases.

# The conclusion:

Results indicate that extra tree classiﬁer-based selected features tend to provide the highest accuracy of 0.99 when used with the RF model.

Other feature techniques yield poor results due to feature reduction, which degrades the performance of both the deep learning and machine learning models, especially linear models. The lower computational complexity of the machine learning models like RF makes them good candidates for thyroid disease prediction.

Similarly, 10-fold cross-validation results corroborate these ﬁndings.

Performance comparison with state-of-the-art approaches indicates the superior performance of the proposed approach.

We see the feature reduction and 5-class classiﬁcation problem as the limitation of the study
and intend to increase the number of classes in our future work.

## *The Technique used:*

 *Wrapper method (forward feature selection, backward feature elimination, bi-directional elimination, and machine learning feature selection), Machine Learning Feature Selection.*

# The introduction:

# The Literature Review:

## Thyroid Cancer Detection:

The study [6] leveraged the least absolute shrinkage and selection operator (LASSO) and LR model to select the malignant thyroid nodule-associated ultrasonic characteristics. Then, RF is applied along with a scoring system to classify the malignant thyroid nodules. The logistic lasso regression (LLR) with RF obtained the best performance with 82% accuracy.

Another study [7] performed machine learning-based prediction of the BRAF mutation presence in the conﬁrmed cancer thyroid nodules. The authors selected 96 thyroid nodule ultrasonic images for this study. 86 radiomic features were extracted from the images, and three models, LR, SVM, and RF were applied to predict the presence of the BRAF mutation. The classiﬁcation accuracy is reported as 64.3% for all three models.

Idarraga et al. [8] performed machine learning-based thyroid nodule malignancy prediction using the ultrasonic and ﬁne-needle aspiration (FNA) feature to avoid false-negative diagnosis in the early stages of thyroid cancer. The RF technique performed better than other techniques like decision tree (DT) and gradient descent (GD). All the above-mentioned works’ performance is not optimal to predict the thyroid cancer diagnosis and still has room for performance improvement.

## Thyroid Disease Prediction:

Garcia et al. [9] predicted the high probable molecules initiating the thyroid hormone homeostasis using machine learning algorithms RF, LR, GBM, SVM, and deep neural networks (DNN). The early prediction of the molecules is helpful for further testing in the ﬁrst stages of thyroid disease. The molecular events were obtained from ToxCast datasets for running the experiments. The article reported that Thyroid Peroxidase (TPO) and Thyroid Hormone receptor (TR) achieved the best predictive performance with an F1 score of 0.83 and 0.81, respectively.

The authors in [10] utilized the image processing techniques and feature selection methods to pick the important features from the dataset and achieve the best performance for thyroid disease prediction.

Razia et al. [11] **compared the performance of various machine learning algorithms to classify Thyroid disease into normal, Hypothyroidism, or hyperthyroidism categories**. The authors obtained the datasets from the University of California Irvine (UCI) machine learning library. The dataset contains **7200 samples**, and each sample has **21 attributes**. The authors reported that DT outperformed the SVM, NB, and multilinear regression (MLR) with 99.23%. However, multi-classiﬁcation is limited to three categories, and limited information is provided on data pre-processing to assess the applicability of the results for real-time datasets.

A multi-kernel SVM is proposed in the paper [12] to classify  thyroid diseases. The authors mentioned that the multi-kernel SVM achieved 97.49% performance accuracy on UCI thyroid datasets. The improved gray wolf optimization performs the feature selection and enhances the performance.

A study [13] performed multiclass hypothyroidism using selective features and ma- chine learning algorithms. Hypothyroidism is classiﬁed into four categories. The results show that RF performed well with 99.81% accuracy compared to the SVM, KNN, and DT algorithms. However, the authors did not mention the performance of their proposed methodology for thyroid disease classiﬁcation. 

Another study [14] tested three feature selection methods along with SVM, DT, RF, LR, and Naive Bayes (NB) to make early pre-dictions for hypothyroidism. Three feature selection methods, recursive feature selection (RFE), univariate feature selection (UFS), and principal component analysis (PCA), are tested in combination with ML algorithms. The RFE combination with ML algorithms performed better than other feature selection methods. All the ﬁve ML algorithms obtained 99.35% accuracy when combined with RFE feature selection. However, the data sample
size is very small, with only 519 records. A large-scale dataset is needed to evaluate the effectiveness of their method.

The authors [15] evaluated the performance of the thyroid disease classiﬁcation using various machine learning algorithms. SVM, RF, DT, NB, LR, K nearest neighbor (KNN), and MLP are used for disease prediction. A dataset sample of 1250 is taken from hospitals and laboratories in Iraq. The MLP predicted the thyroid classiﬁcation with 96.4% accuracy. However, there is still room for performance improvement.

 Hosseinzadeh et al. [16] proposed a multiple multi-layer perception (MMLP) technique to classify thyroid diseases. When the MMLP is applied along with a set of six networks, the accuracy is improved by 0.7% compared to a single MLP. Although MMLP obtained 99% classiﬁcation accuracy on large dataset samples, training deep learning techniques like MMLP is costly and needs high computational resources to train faster. 

The KNN with various distance functions is implemented to test the thyroid disease detection in [17]. The chi-square and L1-based featured selection methods were used to select the optimal features before applying the KNN with Euclidean and Cosine distances. The authors reported that KNN obtained promising results. However, the tested sample size is very small, with 590 samples in total.

Mishra et al. [18] applied the ML techniques sequential minimal optimization (SMO), DT, RF, and K-star classiﬁer to predict hypothyroid disease. A sample size of unique 3772 records is considered for this study. The authors reported that RF and DT performed better than the other two techniques, with accuracy scores of 99.44% and 98.97%. However, the authors did not consider hyperthyroid predication.

Alyas et al. [19] performed a comparative analysis of the machine learning techniques DT, RF, KNN, and artiﬁcial neural network (ANN) to detect thyroid disease. The tests were conducted on the largest dataset and considered both sampled and unsampled data for thyroid disease prediction. RF
obtained the best prediction with 94.8% accuracy. However, the authors did not perform the thyroid disease type prediction tests.

Researchers also applied deep learning models to predict thyroid disease classiﬁcation. For instance, the authors [20] used a deep neural network (DNN) to predict the thyroid disease classiﬁcation. The performance evaluation is done on the UCI dataset of 3152 unique samples. The authors reported 99.95% accuracy when using DNN to classify thyroid disease. However, a large dataset is required to train the model for performance evaluation properly. Additionally, more computing resources are needed to train the deep learning models.

![Untitled](Thyroid%20Disease%20Prediction%20Using%20Selective%20Feature%205bcb8b8ee1144428984b77dfa977d83a/Untitled.png)

## Proposed Methodology:

![Untitled](Thyroid%20Disease%20Prediction%20Using%20Selective%20Feature%205bcb8b8ee1144428984b77dfa977d83a/Untitled%201.png)

### Dataset Acquisition:

**The datasets created for our study are obtained from the UCI thyroid disease datasets**.
The UCI machine learning repository maintains a variety of thyroid disease datasets [22].
The dataset contains 9172 sample observations and each sample is represented by 31 features.

After selecting the target classes for experiments, we performed the data balancing. Normal class samples were 6771 in total, which is more compared to other target class samples, so we randomly selected only 400 samples for the normal class to make dataset balance. It is followed by the feature selection process, where many feature selection techniques are applied. Experiments are performed with an 80–20 train–test split using several machine learning and deep learning models.

![Untitled](Thyroid%20Disease%20Prediction%20Using%20Selective%20Feature%205bcb8b8ee1144428984b77dfa977d83a/Untitled%202.png)

The class counts clearly show that the dataset is highly imbalanced. For instance, most of the samples in the dataset do not belong to any particular class. Therefore, the data preprocessing is performed to obtain the standard dataset for our performance evaluation

we performed the dataset balancing by randomly selecting 400 samples for the normal class while other classes with at least 200 samples are selected.

![Untitled](Thyroid%20Disease%20Prediction%20Using%20Selective%20Feature%205bcb8b8ee1144428984b77dfa977d83a/Untitled%203.png)

![Untitled](Thyroid%20Disease%20Prediction%20Using%20Selective%20Feature%205bcb8b8ee1144428984b77dfa977d83a/Untitled%204.png)

Such minor differences can lead to the wrong diagnosis even by medical experts as human error is expected. Incorrect diagnosis may lead to wrong medication and further complexities. So, an automated system can be very helpful to assist medical experts and even make automated disease predictions without any human mistakes. So, 

this study follows a machine learning approach to make automatic predictions for different
thyroid diseases.

### Feature Selection:

**We deployed several feature selection techniques such as forward feature selection,** backward feature elimination, **bi-directional elimination,** and **machine learning feature selection.** These techniques help to extract the important features from the dataset to train the machine learning models.

The redundant and undesired features may need to be removed from the original datasets to train the model faster, easily interpret the data, and avoid overﬁtting problems. 

We have considered the wrapper method for feature selection, as determining the right set of features for thyroid disease classiﬁcation is essential  The feature selection is based on the speciﬁc ML algorithm used to ﬁt the dataset in the wrapper method. A greedy selection method selects the combination of feature sets and evaluates the performance of the feature set combinations against the evaluation criteria. The evaluation criteria may include metrics such as p-value, accuracy, F1-score, etc., to assess the performance of feature set combinations. The detailed description of the selected four feature selection techniques and machine learning feature selection is as follows.

**Forward Feature Selection:**

In FFS [25], we start with a null model and then try to ﬁt the model with each feature value. The feature with a low p-value is selected for the next round. Then, we start ﬁtting the model with two feature combinations. The minimum p-value feature set in the ﬁrst round should be the one feature candidate when ﬁtting the models with two feature combinations. The low p-value of two features is considered for ﬁtting the model with three feature combinations. This process is repeated until the minimum p-value for each feature in the feature set is less than the signiﬁcance level.

**Backward Feature Elimination:**

In BFE, we start with a model with all the features. The highest p-value feature is selected to be removed from the model and then ﬁt the model. The removed feature p-value must be greater than the signiﬁcance level value. This process is repeated until all the high p-value features are eliminated from the model while ensuring that all the eliminated features p-value greater than the signiﬁcance level. By the end of this process, the ﬁnal set of the existed features are the most relevant and valuable features used for accurate detection and classiﬁcation.

**Bi-Directional Elimination:**

The BiDFE method combines the forward feature selection and backward feature elimination methods. **This method is similar to forward feature selection. But, when the new feature is selected, the backward elimination process kicks it to compare it with previously selected features**. Suppose any previously chosen features with a p-value is greater than the deﬁned signiﬁcance level ‘out’ value is eliminated. In this method, two signiﬁcance level values should be determined with ‘in’ and ‘out’ of value ranges. The feature p-value should be less than the signiﬁcance level inner value to include in the feature selection and greater than the signiﬁcance level outer value to exclude the feature from the feature list.

**Machine Learning Feature Selection:**

Machine learning-based methods, especially ensemble techniques, are used to select the essential features. We have considered the extra tree classiﬁer technique as one of the feature selection methods in this work [27,28]. The extra tree classiﬁer randomly constructs multiple decision trees using the training dataset. The splitting of the nodes in the decision tree is followed by either the Gini index or entropy criteria. The Equation (12) is used to measure the entropy. The value c indicates the unique class labels, and the pi is the fraction of the rows containing the label i in the dataset.

Entropy measures the information about the disorder of the features with the target. We have considered the entropy criteria in our feature selection process. The entropy of obtained features from each decision is determined, and the cumulative entropy values for each feature are used to ﬁnd the important features.

**Machine Learning Models:**

This study employs several machine learning models for thyroid disease detection. RF, LR, SVM, ADA, and GBM are applied to the problem at hand. These models are ﬁne-tuned to optimize their performance.

![Untitled](Thyroid%20Disease%20Prediction%20Using%20Selective%20Feature%205bcb8b8ee1144428984b77dfa977d83a/Untitled%205.png)

## Results and Discussion:

### Results Using Original Feature Set

![Untitled](Thyroid%20Disease%20Prediction%20Using%20Selective%20Feature%205bcb8b8ee1144428984b77dfa977d83a/Untitled%206.png)

### Performance of Models with FFS:

### Results Using BFE Features: