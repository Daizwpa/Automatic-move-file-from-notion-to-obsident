# Comparison of six machine learning methods for differentiating benign and malignant thyroid nodules using ultrasonographic characteristics

Author: Jianguang Liang
DataSet: Private
Date published: 12/10/2023
Key word: GlmNet, KNN, Logistic regression analysis, Machine Learning, Paired t-test, Random forest, Support vector machine, linear discriminant, thyroid nodule
Method: SVM, LDA, RF, *LG, KNN
Status: In progress
Task: Tumour Malignancy Diagnosis
AUC on test: 0.9284
Accuracy on test: 0.8648
Sensitivity on test: 0.8333
Specificity on test: 0.8889
Data type : Clinical data, sonographic features
Number Of Patient: 525
Type of paper: AI-Experiment, Experimental article
list of features: gender, margin
Data Region : China

Objective:

- Comparison SVM, LDA, RF, LG, KNN in terms of accuracy, sensitivity…

Tasks:

- Collect total of 525 patients with thyroid nodules (malignant 228, benign 297).
- Construct six machine learning SVM, LDA, RF, LG, GlmNet, K-NN. using 13 sonographic features.
- Apply 10-fold cross validation

Results:

- The logistic regression algorithm had better diagnostic performance than the other ML algorithms.
- The accuracy, sensitivity, specificity, NPV, PPV, and AUC obtained by running logistic regression were 86.48%, 83.33%, 88.89%, 87.42%, 85.20%, and 92.84%, respectively.