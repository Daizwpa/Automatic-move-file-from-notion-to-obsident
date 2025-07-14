# Risk stratification of papillary thyroid cancers using multidimensional machine learning

Author: Yuanhui Li, PhD
DataSet: Private 
Date published: 01/11/2023
Key word: Machine Learning, papillary thyroid cancer, proteomics, risk stratiﬁcation
Status: In progress
Task: Risk stratiﬁcation based on AI, Tumour Malignancy Diagnosis, preoperative assessment
Data type : Clinical data, Genetic mutations, immunological data, proteomic data
Journal Name: International Journal of surgery 
Optimization : No
Explainability : SHAP
Number Of Patient: 558
Output : Binary ( high-risk PTC or low-risk PTC)
Transfer learning: No
Type of paper: Experimental article
list of features: BRAFV600E, Extrathyroid extension, PDZ and LIM domain, age, capsular invasion, cathepsin L, collagen alpha-1[XII] chain, dipeptidyl peptidase 2, integrin subunit beta-5, lymphocytes, monocytes, multi-focality, neutrophils, platelets, tubulin beta-2A, tumour diameter

Objective:

- To differentiate low-risk PTC from intermediate-/high-risk PTC for constructing a Preoperative Risk Assessment Classiﬁer for PTC (PRAC-PTC).
- At present, we focus on the biological behaviour of malignant tumours and intend to distinguish low-risk and intermediate-/high-risk PTC before surgery to provide guidance for precision treatment.

Problem statement:

- Papillary thyroid cancer (PTC) is one of the most common endocrine malignancies[1,2]. Although the prognosis of PTC is favourable, it tends to have a hight rate of recurrence (10-35%), which may lead to treatment failure and death[3]. PTCs can be divided into different risk levels. In recent years, it has been believed that some relatively inert PTCs can be managed with active surveillance without immediate surgery. However, 15–30% of invasive PTCs have a poor prognosis and require active surgical treatment[1,4]. At present, achieving an accurate preoperative risk assessment of PTC to avoid excessive or insufﬁcient treatment remains challenging.
- 

Task:

- Collect three dataset,  discovery set [274 patients, 274 formalin-ﬁxed parafﬁn-embedded (FFPE)], s the retrospective test set (166 patients, 166 FFPE), and the prospective test set (118 patients, 118 ﬁne-needle aspiration).
- Proteomic proﬁling was conducted by FFPE and ﬁne-needle aspiration tissues from the patients.
- Preoperative clinical information and blood immunological indices were collected.
- The BRAFV600E mutation were detected by the ampliﬁcation refractory mutation system.

Conclusion:

- This study demonstrated that the PRAC-PTC that integrating clinical data, gene mutation information, immune indices, high-throughput proteomics and machine learning technology in multicentre retrospective and prospective clinical cohorts can effectively stratify the preoperative risk of PTC and may decrease unnecessary surgery or overtreatment.
- 

Quotes:

The modiﬁed 2015 American Thyroid Association (ATA) management guidelines proposed a three-tiered clinicopathologic risk stratiﬁcation system that classiﬁed PTC patients as either low, intermediate, or high-risk based on structural recurrence[5].

- Low-risk PTC patients show no evidence of extrathyroidal extension or small-volume metastases.
- Intermediate-risk PTC patients have microscopic extrathyroidal extension, clinical N1
disease or cervical lymph node metastases ( >5 metastatic lymph nodes or maximum diameter of metastatic focus ≥0.2 cm and <3 cm).
- High-risk PTC patients are characterised by gross extrathyroidal extension, metastatic lymph nodes greater than or equal to 3 cm, incomplete tumour resection, and distant metastases[5].