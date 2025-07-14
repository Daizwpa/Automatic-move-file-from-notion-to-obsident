# Machine learning-based prediction model for distant metastasis of breast cancer

Author: Hao Duan 
Score: ⭐️⭐️⭐️⭐️
Link: https://github.com/dw666666/Prediction-model-of-distant-metastasis-of-breast-cancer
DataSet: GSE9893 dataset we can get it from repository of github
Date published: 01/01/2024
Key word: Biomarkers, Breast cancer distant metastasis, Predictive model, Weighted correlation network analysis, machine learning algorithms
Method: machine learning
Status: Done
Task: Distant Metastasis, Recurrence prediction
Type: Journal
AUC on test: 0.913
Accuracy on test: 0.936
Data type : DNA, next-generation transcriptome sequencing
Journal Name: Computers in Biology and Medicine
Optimization : No
Explainability : No
Features selection : LASSO, difference anal­ysis, weighted gene co-expression network analysis
Output : probability
Transfer learning: No
Type of paper: Experimental article

Objective:

- Breast cancer is the most prevalent malignancy in women. Advanced breast cancer can develop
distant metastases, posing a severe threat to the life of patients. Because the clinical warning signs of distant metastasis are manifested in the late stage of the disease, there is a need for better methods of predicting metastasis.

Problematic:

Task:

- we obtained the differentially expressed genes of breast cancer distant metastasis by performing differential analysis on the selected dataset.
- we obtained the significant module gene set by performing WGCNA on the selected dataset.
- the differential genes and significant module genes were intersected to obtain the breast cancer distant metastasis target genes
- the breast cancer distant metastasis target genes were analyzed by PPI, GO and KEGG, etc.
- LASSO regression analysis of breast cancer distant metastasis target genes to obtain distant metastasis of breast cancer biomarkers
- correlation, expression characteristics and regulatory mechanism analysis of distant metastasis of breast cancer biomarkers.
- extraction of expression data of distant metastasis of breast cancer biomarkers.
- multiple breast cancer distant metastasis prediction models are constructed using expression data of breast cancer distant metastasis biomarkers based on logistic regression models, random forest models and other models.
- the best performing breast cancer distant metastasis prediction model was selected based on the evaluation index.

Method:

![Untitled](Machine%20learning-based%20prediction%20model%20for%20distan%2063ef28432b564dab855d1cf675b6fda6/Untitled.png)

Results:

- Validation showed that our 21-gene pre­dictive model for distant metastasis performed well and was able to predict the presence of distant breast cancer metastasis in breast cancer sufferers with excellent precision and effectiveness.

Conclusion:

- In summary, we identified 21 biomarkers of distant metastases in
breast cancer.
- 

Quote:

- In advanced stages of breast cancer, distant metastasis of cancer cells can occur [2,3], leading to multiorgan lesions and threatening the lives of sufferers with breast cancer.
- In addition to the level of medical care and treatment options, the
timing of treatment for breast cancer with distant metastases is also an
important factor affecting its treatment outcome.
- **At present, the diagnosis of distant metastases in sufferers with breast cancer is still mostly based on the observation of clinical symptoms in the corresponding organs caused by metastases and the presence of imaging changes in certain areas.**
- However, the above diagnostic methods cannot detect distant metastasis of breast cancer at an early stage and cannot provide better treatment timing and more treatment time for sufferers with deteriorating breast cancer.
-