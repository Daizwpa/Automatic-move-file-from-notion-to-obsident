# Weakly supervised learning on unannotated H&amp;E‐stained slides predicts <scp> <i>BRAF</i> </scp> mutation in thyroid cancer with high accuracy

Author: Deepak Anand
Score: ⭐️⭐️⭐️⭐️
DataSet: ISBI 2017 Thyroid Tissue Microarray (TH-TMA17) dataset for training, TCGA-THCA for testing ; not available any more.
Date published: 04/08/2021
Key word: BRAF V600E, Deep Learning, H&E, Thyroid cancer, computational pathology, weakly supervised learning
Method: TF (VGG16) +Attention NN
Pre-processing: Downscale image to 5x magnification,  Augment each spot to 50 using random rotation , 
Status: In progress
Task: Genetic Diagnosis, Predicting BRFV600E Mutation
Type: Journal
Data type : H&E stained digital pathology images, Histologic Images, hematoxylin and eosin stained slides
Journal Name: The Journal of Pathology, pathological society, indexed in PubMed
Type of paper: Experimental article
Mentioned: Not yet

## Objective:

- We used a weakly supervised learning technique to train a DNN to predict BRAFV600E mutational status, determined using DNA testing, in H&E stained images of thyroid cancer tissue without regional annotations.
- 

<aside>
❓

Why Weakly supervised learning:

- The core problem with strongly supervised learning is that merely annotating the tumor regions in H&E gives each patch a definitive label, in spite of the presence of regions that are irrelevant or ambiguous to the mutational status due to spatial heterogeneity that is hard for humans to delineate [15,16].
</aside>

## Problematic:

- Apart from these technical and scientific limitations, the cost and accessibility of both DNA sequencing and BRAF IHC panels are major concerns in low-income countries [19].

- expert knowledge is reliable for annotating regions informative of malignancy and other known histological patterns (strong supervision), it is unreliable for identifying regions informative of mutational status. This poses a serious impediment to obtaining higher prognostic accuracy and discovering new knowledge of pathobiology.
- recent studies have expressed concern over the discordance of immunohistochemistry (IHC) assays with the gold standard DNA tests for BRAF mutation detection, due to the dependence of the former on tissue staining protocols [14–16]. Intratumor heterogeneity for BRAF mutation could mean that even DNA testing, which is based on a bulk sample of the tumor, could miss a mutated region.

## Task:

- build three model that work together to detect BRAF region, the  first model is detection model for detecting tumour region, the second one is subtyping model that classify tumor to PTC or FTC, the thread one is prediction model that predict the tumour has BRAF mutation.
- Training the two first model (detection, subtyping) using two strategy traditional strong supervised, and weakly supervised. however the thread model (prediction) trained only with weakly supervised.
- Train DNN using weakly supervised learning technique also called attention-based multiple instance learning (A-MIL) to detect BRAF mutation state.
- trained on a single-institutional ISBI 2017 Thyroid Tissue Microarray (TH-TMA17) dataset
- weakly supervised learning known as attention-based multiple instance learning (A-MIL) to train a DNN to predict BRAF mutation status,
- Develop visualization technique based on WSL  to highlight regions that are important.
- testing the accuracy of predicting the BRAF status, an external validation cohort was taken from whole slide images from The Cancer Genome Atlas Thyroid Cancer dataset (TCGA-THCA)
- To save computational requirements, the images were downscaled to 5x magnification, which reduced the size of the TMA spot images in TH-TMA17 from approximately 10000x10000 pixels to 2500x2500 pixels.
- Each spot image was augmented 50 times using random rotations and mirror flips during training and testing to show different variations of the same disease condition to the DNN.
- color normalized using the stain color basis extracted
- These three DNNs were trained separately on 74 randomly sampled patients each from the TH-TMA17 cohort and were tested on 11 held-out patients (6 mutated, 5 wildtype; supplementary material, Table S1)

## Result:

- the trained model gave an AUC = 0.98 (95% CI: 0.97-1.00), which is much higher than the previously reported results for detecting any mutation using H&E by DNNs trained using strong supervision.
- These results highlight the potential of weakly supervised learning for training DNN models for problems where the informative visual patterns and their locations are not known a priori.
- we show that WSL methods are even more appropriate for detecting mutations in H&E images to counter our inability to annotate their locations precisely and accurately by hand.

Conclusion:

- This approach could also identify highly informative areas regarding BRAF mutation within each image. We found that these areas were enriched with histomorphological features previously associated with BRAF mutation by pathologists as well as more likely to be positive for this mutation by IHC.
- Our work also confirms the utility of transferred learning from large labeled image datasets,
- we were able to identify BRAF mutation with extremely high accuracy on an independent dataset
- These and similar algorithms can be potentially incorporated into clinical workflows especially in areas with limited resources for molecular testing and little or no access to expert pathologists
- We also developed a new visualization technique to map the spatial foci that indicate mutational positivity or negativity within the same images, which has the potential to further our biological understanding of the mutation phenotype.

## Quote:

- 80% of thyroid cancers are classified as papillary and are treated differently than the follicular subtype, and a follicular variant of the papillary subtype is a frequent cause of misclassification [3,4].
- 50% of papillary tumors, compared to only 10% of the follicular ones, have the BRAF V600E mutation which is associated with worse clinical features and outcomes [5,6].
- Targeted therapies for BRAF-positive TCa have shown promising initial results and are already the standard of care for BRAF-mutated colon, skin, and non-small cell lung cancers [7–13].
- Intratumor heterogeneity for BRAF mutation could mean that even DNA testing, which is based on a bulk sample of the tumor, could miss a mutated region.
- The core problem with strongly supervised learning is that merely annotating the tumor regions in H&E gives each patch a definitive label, in spite of the presence of regions that are irrelevant or ambiguous to the mutational status due to spatial heterogeneity that is hard for humans to delineate [15,16].
- weakly supervised learning (WSL), which has shown to be useful for training DNNs to detect tumors and their histological variants while reducing the annotation burden [31–35].
- antibodies are available for detecting only the commonest mutation, i.e. V600E, whereas as many as 30 different low-prevalence mutations have been identified in the BRAF gene across all tumor sites
- The attention mechanism used in our work helped the DNN suppress the negative effects of uninformative regions on classification accuracy even though the training cohort was smaller and sourced from fewer hospitals compared to the testing cohort.
- The significance of our findings is that WSL offers a way to train classifiers to recognize pathological conditions when:
    - (a) tissue regions with discriminative visual patterns cannot be identified and annotated before training, and
    - (b) the datasets are small in size. Compared to our work, the notable previous studies for detecting mutations using H&E whole slide image used strong supervision and larger multi-institutional training cohorts [22,26–30].
- We also show that this approach tends to generalize well to independent cohorts and helps discover informative regions.

## Method:

train multiple DNN for three tasks on H&E stained digital pathology images of thyroid tissue:

1- to detect tumor versus healthy regions.

2-  to classify tumors into papillary versus follicular carcinomas.

3-  to identify BRAF mutation in tumor regions.

![Screenshot 2023-11-13 164434.png](Weakly%20supervised%20learning%20on%20unannotated%20H&E%E2%80%90stai%206728a8d13e7e49898d9f6604afc852d2/Screenshot_2023-11-13_164434.png)

![Untitled](Weakly%20supervised%20learning%20on%20unannotated%20H&E%E2%80%90stai%206728a8d13e7e49898d9f6604afc852d2/Untitled.png)