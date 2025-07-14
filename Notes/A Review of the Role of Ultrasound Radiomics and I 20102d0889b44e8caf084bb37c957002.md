# A Review of the Role of Ultrasound Radiomics and Its Application and Limitations in the Investigation of Thyroid Disease

Author: Wen-Wu Lu
Score: ⭐️⭐️⭐️⭐️⭐️
Date published: 19/10/2022
Key word: Artificial intelligence (AI), Doppler, Ultrasonography, thyroid nodule
Status: In progress
Task: radiomics review
Type: Journal
Journal Name: Medical science Monitor journal indexed in PubMed
Type of paper: tool review

Objective:

- In this article, we first describe the workflow of ultrasound radiomics, followed by an overview of the application of ultrasound radiomics to the thyroid.

Conclusion:

- In conclusion, ultrasound radiomics, as a technique for extracting image data, plays an important role in the evaluation of medical images of related diseases. However, there are some
deficiencies, and more efforts are needed to standardize the discipline of ultrasound radiomics and to apply ultrasound radiomics to clinical work.
- Ultrasound radiomics has yielded many achievements in the screening, diagnosis, and evaluation of thyroid tumors and can be used as an evaluation tool for clinicians to assess the pathophysiological status of various aspects of the thyroid.
- ACR TI-ARDS is one of the most popular models, in which 5 risk factors related to malignant thyroid nodules can be distinguished by radiologists with human vision, which plays a significant role in clinical application. However, ultrasound radiomics often considers other meaningful risk factors based on ACR TI-RADS and has improves TI-RADS. At present, radiomics no longer only pays attention to the image features of patients, but also considers other clinical factors so that the diagnosis and treatment of patients are more individualized and comprehensive, and it is used to solve clinical problems [55].

Radiomics Limitation:

- most studies have insufficient sample sizes. Adequate sample size is key to building an excellent radiomics model. If the sample size is too small, the image features extracted may not be representative and not convincing enough. It is often manifested as overfitting or overly good results on the model.
- most ultrasound imaging groups are influenced by clinician experience. For example, the data acquisition and target segmentation processes in the workflow are uncontrollable, and these 2 steps are the biggest challenges concerning reproducibility in radiomics research. The case data collected in most current radiomics studies are not derived from public databases, and research results are usually not transferable to applications. Therefore, most studies advocate using multi-center data to develop radiomics models, which can enhance the persuasiveness of the
study and the generalizability of the model [56]
- In addition, manual segmentation methods are still essential segmentation methods. This creates unavoidable errors and subjectivity. Last but not least, most ultrasound radiomics-based thyroid studies have used retrospectively collected data [23,24,36-38,43,45].
- 

Quote:

- Ultrasonography is the most common, beneficial, safe, and cost- effective method of thyroid imaging [1]. Ultrasound screening methods play an important role in the management of thyroid nodules [2].
- Radiomics is a new field of medical image research that further expands the quantitative analysis of medical images [6]
- The ultrasound radiomics is based on ultrasound images to delineate the region of interest (ROI), and then extract features to quantify the disease information contained in the image, which helps to analyze the correlation between the image and the clinical pathology of the disease.
- it can be used to diagnose benign and malignant thyroid nodules, predict lymph node status in thyroid cancer, analyze molecular biological characteristics, and predict the survival of thyroid cancer patients.
- doctors are affected by experience when observing ultrasound imaging to diagnose thyroid nodules, and experienced doctors have higher diagnostic accuracy than younger doctors [3].
- Ultrasound imaging is a type of medical imaging that contain features of a large amount of information. In early studies, the medical image characteristics of the thyroid were analyzed to observe the abnormal areas in the organization [4,5].
- Radiomics is a new field of medical image research that further expands the quantitative analysis of medical images [6].
- Unlike physicians who use machines to visually observe lesions, radiomics acquires various information in images that are difficult to quantify clinical outcomes through visual observation [7].
- Radiomics is a powerful tool in the field of oncology and has high utility for individualized patient care [9]
- Ultrasound radiomics uses image segmentation to obtain ROIs to extract
features. The ROI is not necessarily a thyroid nodule or tumor, but can also be surrounding normal tissue. Imaging information in the ROI is used to develop diagnostic, predictive, or prognostic models.
- Currently, **the application of ultrasound thyroid imaging mainly includes** **diagnosis of benign and malignant thyroid nodules**, **prediction of thyroid cancer aggressiveness to the tissue**, **analysis of tumor phenotype or the presence of genetic mutations**, and **prognostic analysis of thyroid cancer** patients (Table 1).
- Ultrasound radiomics is a branch of radiomics, which extracts and analyzes quantitative imaging
features from ultrasound images, and **can obtain features such as tumor shape, texture, and wavelet, providing clinicians with valuable diagnostic, prognostic, or predictive information [11].**
- The ultrasound radiomics workflow is summarized as extracting information from ultrasound images, transforming them into feature data, and analyzing them.
- Radiomics was initially defined as the extraction of high-throughput features from medical images. These features are usually associated with the patient’s disease state, which is
difficult for physicians to express in words, but can be converted into corresponding data information and become image features that can be quantitatively described. Most of the currently used features are obtained from segmented ROIs, which are mainly composed of voxel intensities, including morpho- logical, first-, second-, and higher-order features [25].
- The characteristic of many tumors is often determined by biopsy, but some tumors are heterogeneous, and biopsy samples are not representative of the entire lesion. Ultrasound radiomics, which analyzes the overall image of the lesion, can visualize tumor heterogeneity and can serve as an intermediate step between imaging and biosy [16].

Radiomics workflow:

1. Data collection:
2. ROI segmentation:
3. Features extraction:
4. Features selection:
5. Modeling:
    - Building a model is the ultimate goal of many radiomics projects, often with finalized features, including supervised learning, unsupervised learning, and semi-supervised learning.
    - The most commonly used supervised learning models in ultrasound radiomics are built through logistic regression models [23,24], and other learning models such as support vector machines (SVM) and random forests [38].
    -