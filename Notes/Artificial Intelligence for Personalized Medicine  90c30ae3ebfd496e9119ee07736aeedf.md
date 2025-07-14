# Artificial Intelligence for Personalized Medicine in Thyroid Cancer: Current Status and Future Perspectives

Author: Ling-Rui Li
Score: ⭐️⭐️⭐️⭐️⭐️
Date published: 09/02/2021
Key word: Thyroid cancer, Ultrasound, artiﬁcial intelligence, biomarker, histopathology, personalized medicine, ﬁne-needle aspiration biopsy
Status: Done
Task: Cancer review, Histopathology Review, Review
Journal Name: Frontiers in Oncology  
Type of paper: review paper

Objective:

- we started with several challenges regarding personalized care in TC
    - inconsistent rating ability of ultrasound physicians,
    - uncertainty in cytopathological diagnosis,
    - difﬁculty in discriminating follicular neoplasms, and inaccurate prognostication.
- We then analyzed and summarized the advances of AI to extract and analyze morphological, textural, and molecular features to reveal the ground truth of TC
- In this review, we aimed to summarize the use of AI for extracting and analyzing morphological, textural, and molecular features to reveal detailed information and personalize therapies for TC patients.

Quotes:

- There are abundant anatomical structures (texture, internal architecture, and spatial distribution) and molecular components (gene variation, protein expression, etc.) within TC.
- TN with several typical ultrasound features implies an increased risk of malignancy, such as solid composition, hypoechogenicity, irregular margin, microcalciﬁcation, and taller-than-wide shape.
However, these properties can neither conﬁrm nor exclude the diagnosis of TC (19).
- The observer’s agreement among multiple centers is poorly satisfactory in assessing these features (7).
- Thyroid Imaging Reporting and Data Systems (TI-RADS) are enormously valuable to PTC as risk stratiﬁcation systems, while relatively less to FTC, MTC, and other malignancies (20). Interestingly, the AI model appears to be a promising tool to facilitate a better knowledge of TN via quantitative analysis of typical US features and introduction of texture features.

- Given patients and their disease features, primary human cell cultures both from surgical biopsies and from ﬁne-needle aspiration (FNA) samples foster the targeted therapies (6).
- A meta-analysis suggested that a taller-than-wide shape displays TN’s variation in space and orientation growth, and it is deﬁned as the most suggestive feature for malignancy(42)
- Texture features refer to the characterization of spatial distribution and surface orientation with numerical features (43). Thus, texture analysis as a powerful alternative will make it possible for radiologists to comprehend the TN in depth and gain a correct diagnosis.
- The major difference between follicular carcinoma and follicular adenoma is the occurrence of capsular or vascular invasion (67). Preoperative examinations of both US and FNA have difﬁculty in making a reliable diagnosis. A highly vascularized tumor protrusion on the US strongly indicates FC, which is rather rare yet (68).

<aside>
🔥 Molecular:

- molecular tests provide a noninvasive and accurate option to reduce clinical and healthy uncertainty (8, 67).
- Each genome contains as much information as 100,000 photographs (74). Next-generation sequencing (NGS) can perform high-speed analysis of multiple genes parallelly in a single operation, producing billions of molecular fragments (74, 75)
- Some molecular alterations such as BRAF mutations (81) are diagnostic of cancer, but most of the other alterations (82, 83) show overlap in both benign and malignant lesions
</aside>

<aside>
🔥 Information about personalized medicine:

- In the era of personalized medicine, precise and efﬁcient risk stratiﬁcation is important before, during, and after treatment, to choose and adjust its type and intensity.
- 
</aside>

<aside>
🔥 Despite the mounting advantages of the AI model in optimizing and even creating workﬂows, many remarkable factors hold its ultimate practice back in the real world. The three main factors are:

- poor availability of large-high-quality datasets to guarantee great robustness
- lack of explainability for conclusions from a black-box algorithm to solidify the trust between physicians and patients (47, 48);
- ﬁnancial burden from speciﬁc equipment and research costs (48).
</aside>

Upon reliable evidence obtained by the US and FNA examination, tumor information from the resected specimens is signiﬁcant for pathologists to diagnosis TC such as tumor size, pathologic types, and degree of malignancy.

Objective:

- In this review, we aimed to summarize the use of AI for extracting and analyzing morphological, textural, and molecular features to reveal detailed information and personalize therapies for TC patients.

Task:

- The review exhibits several challenges regarding personalized care in TC, including:
    - inconsistent rating ability of ultrasound physicians.
    - uncertainty in cytopathological diagnosis.
    - difﬁculty in discriminating follicular neoplasms.
    - inaccurate prognostication.
    
    Also, they analyzed and summarized the advances of AI to extract and analyze morphological, textural, and molecular features to reveal the ground truth of TC.
    

Question:

outlines:

- Introduction.
- Application of AI in the US diagnosis of thyroid nodules.
    - Performance of typical US features.
    - Performance of Texture features.
- Application of AI in Cytopathological evaluation from FNA.
    - Performance of Morphological features.
    - Performance of Biomolecular.
- Application of AI in Histopathological analysis.
    - Performance of Morphological Features.
    - Performance of Genetic Parameters.
- Conclusion

Conclusion:

- their combination with
AI technology will make individual medical strategies possible.
- The most used  ultrasound features in diagnosing thyroid are  shape, margin, echogenicity, calciﬁcation, composition, and size.

Quote:

- Risk stratiﬁcation guided by reﬁned information becomes a crucial step toward the goal of personalized medicine.
- The diagnosis of TC mainly relies on imaging analysis, but visual examination may not reveal much information and not enable comprehensive analysis.
- Artiﬁcial intelligence (AI) is a technology used to extract and quantify key image information by simulating complex human functions. This latent, precise information contributes to stratify TC on the distinct risk and drives tailored management to transit from the surface (population-based) to a point (individual-based).
- In the era of personalized medicine, precise and efﬁcient risk stratiﬁcation is important before, during, and after treatment, to choose and adjust its type and intensity.
- So far, TC’s diagnosis mainly relies on image analysis (e.g., ultrasound images, cell smears, and tissue sections), but information obtained only by our naked eyes hardly enables a comprehensive analysis of the tumors (5).
- G**iven patients and their disease features, primary human cell cultures both from surgical biopsies and from ﬁne-needle aspiration (FNA) samples foster the targeted therapies (6)** However, many tough challenges still hinder a clear break of personalized treatment such as inconsistent rating ability of ultrasound (US) physicians (7), uncertainty in cytopathological diagnosis (8), difﬁculty in discriminating follicular neoplasms (9, 10), and inaccurate prognostication.
- TN with several typical ultrasound features implies an increased risk of malignancy, such as solid composition, hypoechogenicity, irregular margin, microcalciﬁcation, and taller-than-wide shape
- Thyroid Imaging Reporting and Data Systems (TI-RADS) are enormously valuable to PTC as risk stratiﬁcation systems, while relatively less to FTC, MTC, and other malignancies (20).
- A meta-analysis suggested that a taller-than-wide shape displays TN’s variation in space and orientation growth, and it is deﬁned as the most suggestive feature for malignancy(42).
- Texture features refer to the characterization of spatial distribution and surface orientation with numerical features (43). Thus, texture analysis as a powerful alternative will make it possible for radiologists to comprehend the TN in depth and gain a correct diagnosis.
- FNA is a primary preoperative examination to evaluate TN. Its report system, the Bethesda System for Reporting Thyroid Cytopathology (TBSRTC),
- PTC, the most common TC (>80%), arises from abnormal growth of thyroid epithelial cells (28, 38).
- FNA is a primary preoperative examination to evaluate TN. Its report system, the Bethesda System for Reporting Thyroid Cytopathology (TBSRTC), is a state-of-the-art and category-based method for clinicians’ decision-making. While TBSRTC includes six diagnostic categories on the estimated risk of malignancy (ROM) (Table 2), 15%–30% of TN continues to be classiﬁed as indeterminate TN (ITN), most frequently TBSRTC categories III, IV, and V (8).