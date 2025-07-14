# Early diagnosis of thyroid cancer diseases using computational intelligence techniques: A case study of a Saudi Arabian dataset

Author: Sunday O
Score: ⭐️⭐️
Link: No code
DataSet: Private
Date published: 09/02/2021
Key word: Artificial neural network, Decision trees, Diagnose, Ensemble methods, Machine Learning, Naïve bayesian, Random forest, Support vector machine, Thyroid cancer disease
Method: SVM, ANN, RF*, NB
Status: Done
Task: Tumour Malignancy Diagnosis
Type: Journal
Accuracy on test: 0.9
Data type : Clinical data, blood test data
Type of paper: Experimental article
list of features: Alanine transaminase, Alkaline phosphatase levelAlkaline phosphatase level, Hematocrit, Hemoglobin, Mean corpuscular hemoglobin, Mean corpuscular hemoglobin concentration, Mean corpuscular volume, Mean platelet volume, Platelet count, Red blood cell count, Red blood cell distribution width, White blood cells, age, gender
Data Region : Saudi Arabia

Objective:

- In this paper, we introduce our work developing machine learning-based tools that can serve as early warning systems by detecting TC at very early stages (pre-symptomatic stage).

Task:

- This section discusses the machine learning algorithms used in this work, such as Support Vector Machines (SVM), Artificial Neural Network (ANN), Random Forest (RF), and Naïve Bayes (NB).

- the missing values were handled by replacing them with the mean value of each
feature.

- Feature selection was implemented using the correlation coef­ficient to rank the features.

- evaluate the accuracy, using the 10-fold cross-validation and direct partition ratio evaluation methods with defined equations.
- In addition, confusion matrices were created by using the optimal parameters of the SVM, ANN, RF, and NB. Then, the ratio was compared between the false positives (FP), false negatives (FN), true positives (TP), and true negatives (TN) by finding the F-measure, which is an efficient approach to identifying an optimal technique.

- The grid search systematic approach was used to find the optimal parameters of each technique. The potential values for certain param­eters were entered into the grid search, which can then generate the best potential performance to enhance accuracy. It must be noted that 10-fold cross-validation was used for the optimization strategy.

Results:

- The highest accuracy rate obtained was 90.91% with the RF technique, while SVM, ANN, and NB achieved 84.09%, 88.64%, and 81.82% accuracy, respectively.
- 

Conclusion:

- The highest accuracy rate obtained was 90.91% with the RF technique, while SVM, ANN, and NB achieved 84.09%, 88.64%, and 81.82% accuracy, respectively. These levels were obtained by using only seven features out of an available 15.

Quotes:

- In recent times, researchers have noticed that chronic diseases have become more common. In the Kingdom of Saudi Arabia, the number of patients with thyroid cancer (TC) has become a concern, necessitating a proactive system that can help cut down the incidence of this disease.
- Thyroid cancer (TC), characterized by endocrine malig­nancy, has one of the fastest growing rates of occurrence.

<aside>
📌

- Some of the most common indicators  of TC in a patient history are:
    - high doses of radiation,
    - a family history of TC,
    - and age older than 40 years.
    
    However, there is an equal possibility of TC developing according
    
</aside>

- TC is characterized by abnormal growth in cells that lead to tumor development, and these cells do not die as normal cells do. While the thyroid tumor grows, it causes clear symptoms, such as hoarseness, difficulty in swallowing, swelling in the neck, and pain in the neck re­gion [4].