# Classifying driver mutations of papillary thyroid carcinoma on whole slide image: an automated workflow applying deep convolutional neural network

Author: Peiling Tsou
Score: ⭐️⭐️⭐️⭐️⭐️
DataSet: Public 
Date published: 06/11/2024
Key word: Convolutional neural network (CNN), Deep Learning, digital pathology, driver mutations, papillary thyroid carcinome, whole slide images
Method: Extract tile form WSI and pass it through Google’s Inception v3 model
Status: Done
Task: Genetic Diagnosis, Mutation Classification
Type: Journal
AUC on test: 0.865
Accuracy on test: 84.2
Data type : H&E stained digital pathology images, imagery data
Journal Name: https://www.frontiersin.org/journals/endocrinology
Optimization : No
Features selection : No
Muti-central Data: False
Number Of nodules: 500
Output :  Binary classification. BRAFV600E, RAS mutations 
Type of paper: Experimental article
list of features: No
Mentioned: In Review
Tool used: HistoQC for to identify tissue regions on the WSI; HistomicsTK; Tensorﬂow

Objective:

- we aimed to develop an automated image pre-processing workﬂow that uses WSI inputs to categorize PTCs based on driver mutations.
- 

Problematic:

- Papillary thyroid carcinoma (PTC), which accounts for nearly 80% of all thyroid cancers, is a
mitogen-activated protein kinase (MAPK) -driven malignancy characterized by two mutually exclusive driver mutations: BRAFV600E and mutated RAS, each triggering different downstream signaling events (2). The BRAFV600E mutation is present in almost half of all PTC cases. RAS point mutations, affecting speciﬁc loci (codons 12, 13, and 61) in the N-RAS, H-RAS, or K-RAS genes, occur in 10% to 15% of PTC patients (3). Notably, the BRAFV600E mutation not only correlates with increased tumor aggressiveness (4) but also hampers the tumour’s ability to uptake radioactive iodine (RAI) (5), resulting in unfavourable prognoses (6, 7). Tumors with the BRAFV600E mutation do not respond to the ERK-mediated negative feedback on RAF, causing elevated MAPK signaling (8). Conversely, tumors driven by RAS activate RAF dimers that are sensitive to ERK (extracellular signal-regulated kinases) negative feedback, which in turn decreases MAPK signaling. These differences in signaling mechanisms lead to signiﬁcant phenotypic divergence, which could be crucial for therapeutic or prognostic strategies.
- Current mutation detection techniques, such as immunohistochemistry, real-time polymerase chain reaction (PCR) and automated platforms all require a substantial amount of tumor tissue for analysis (16).

Task:

- Grab the dataset at Histopathology slides from The Cancer Genome Atlas repository.
- Used HistoQC to identify tissue regions on the WSI and mask out low-quality regions such as blood, bubbles, blurred regions, or pen marks.
- Color normalization was applied to the tissue region on the whole slide.
- We iterated over the WSI for candidate 512x512 pixel patches at 20X magniﬁcation
- **Implemented a nuclear segmentation** python package HistomicsTK (28) to characterize cellular nuclei and calculate the numbers, staining density, and dimension ratios of nuclei in the patch.
- Augmentation By applying vertical and horizontal ﬂips, along with 90-degree rotations, we generated 8 possible variations for each patch, from which two were randomly selected for the training data.
- used modified version of inception v3 architecture.
- Train with Adam optimizer (learning rate of 0.001) and ﬁnal SoftMax activation layer implemented.

Results:

- The newly developed pipeline performed equally well as the expert-curated image classiﬁer.
- The best model achieved Area Under the Curve (AUC) values of 0.86 (ranging from 0.847 to 0.872) for validation and 0.865 (ranging from 0.854 to 0.876) for the ﬁnal testing subsets.
- Notably, it accurately predicted 90% of tumors in the validation set and 84.2% in the ﬁnal testing set.
- the performance of our new classiﬁer showed a strong correlation with the expert-curated classiﬁer (Spearman rho = 0.726, p = 5.28 e-08), and correlated with the molecular expression-based classiﬁer, BRS (BRAF-RAS scores) (Spearman rho = 0.418, p = 1.92e-13).

Quotes:

- Papillary thyroid carcinoma (PTC), which accounts for nearly 80% of all thyroid cancers, **is a
mitogen-activated protein kinase (MAPK) -driven** malignancy characterized by two mutually exclusive driver mutations: BRAFV600E and mutated RAS, each triggering different downstream signaling events (2).
- The BRAFV600E mutation is present in almost half of all PTC cases.
- RAS point mutations, affecting speciﬁc loci (codons 12, 13, and 61) in the N-RAS, H-RAS, or K-RAS genes, occur in 10% to 15% of PTC patients (3).
- Notably, the BRAFV600E mutation not only correlates with increased tumor aggressiveness (4) but also hampers the tumour’s ability to uptake radioactive iodine (RAI) (5), resulting in unfavourable prognoses (6, 7).

- ***Food and Drug Administration (FDA)*** approval of the ﬁrst WSI system for primary diagnosis in pathology (24, 25)
-