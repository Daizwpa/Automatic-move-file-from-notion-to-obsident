# AI-Based multimodal Multi-tasks analysis reveals tumor molecular heterogeneity, predicts preoperative lymph node metastasis and prognosis in papillary thyroid carcinoma: A retrospective study

Author: Yu, Yunfang
Score: ⭐️⭐️⭐️⭐️⭐️
DataSet: Two dataset private and public 
Date published: 11/07/2024
Key word: Cervical lymph node metastases, Disease-free survival, Molecular heterogeneity, Multi-model analysis, papillary thyroid carcinome
Method: Pre-trained ResNet50 backbone and self-attention
Status: Done
Task: Genetic Diagnosis, Metastasis Diagnosis, Survive rate
Type: Journal
Data type : Clinical data, Histologic Images, molecular data
Journal Name: International Journal of Surgery Publish Ahead of Print
Explainability : GradCAM algorithm
Features selection : No
Muti-central Data: True
Number Of Patient: 1011
Output : predict LNM and disease-free survival (DFS).
Transfer learning: Yes
Type of paper: Experimental article
Mentioned: Not yet
Multimodal: Yes

Objective:

- to **predict LNM** and **disease-free survival (DFS).**

Task:

- Use tow dataset one private, other public, in total of 1011
    - 256 patients from cohort 1 (private).
    - 275 patients from cohort 2 (private).
    - 499 patients from TCGA (public).
- 
- They utilized the GradCAM algorithm to generate heatmaps from pathology-based deep learning models, which visually highlighted high-risk tumor areas in PTC patients

Results:

- BRAF mutations were significantly associated with LNM and impacted **disease-free survival** .
- The model achieve AUC of  0.86, 0.84 and 0.83 in training, validation and cohort 2, respectively.
- Disease-free survival AUC:
    - High-risk patients in the training cohort had significantly lower DFS rates (P < 0.001). Model AUCs were 0.91 at 1 year, 0.93 at 3 years, and 0.87 at 5 years.
    - In the validation cohort, high-risk patients also had lower DFS (P < 0.001); the AUCs were 0.89, 0.87, and 0.80 at 1, 3, and 5 years.

Quotes:

- Molecular heterogeneity, driven by genetic alterations and tumour microenvironment components, contributes to the complexity of PTC.
- The presence or absence of PTC LNM substantially influences the choice of surgical procedures and treatment plans[3].
-