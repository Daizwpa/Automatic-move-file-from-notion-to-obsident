# Deep learning in cancer diagnosis, prognosis and treatment selection

Date published: 08/05/2021
Status: Done
Type: Journal
Type of paper: review paper

https://doi.org/10.1186/s13073-021-00968-x

Abstract:

The increasing adoption of deep learning across healthcare domains together with the availability of highly characterised cancer datasets has accelerated research into the utility of deep learning in the analysis of the complex biology of cancer.

# The objective:

In this review, we provide an overview of emerging deep learning techniques and how they are being applied to oncology. We focus on the deep learning applications for **omics data types**, including **genomic**, **methylation** and **transcriptomic** data, as well as **histopathology-based genomic** inference, and provide perspectives on how the different data types can be integrated to develop decision support tools. We provide specific examples of how deep learning may be applied in cancer diagnosis, prognosis and treatment management. We also assess the current limitations and challenges for the application of deep learning in precision oncology, including the lack of phenotypically rich data and the need for more explainable deep learning models

# The conclusion:

**it is anticipated that artificial intelligence and DL will be used in the development, validation and implementation of decision support tools to facilitate precision oncology.**

**In this review, we showcased a number of promising applications of DL in various areas of oncology, including digital histopathology, molecular subtyping, cancer diagnosis,
prognostication, histological inference of genomic characteristics,  tumour  microenvironment  and  emerging frontiers such as spatial transcriptomics and pharmacogenomics**

**the future of applied DL in oncology will likely focus on integration of medical images and omics data using multimodal learning that can identify biologically meaningful biomarkers.**

**Important prerequisites of widespread adoption of DL in clinical setting are phenotypically rich data for training models and clinical validation of the biological relevance of DL generated insights**

**We expect as new technologies such as single-cell sequencing, spatial transcriptomics and multiplexed imaging become more accessible, more efforts will be dedicated to improving both the quantity and quality of labelling/annotation of medical data.**

## **Background:**

**Cancer care is undergoing a shift towards precision healthcare enabled by the increasing availability and integration of multiple data types including genomic, transcriptomic and histopathologic data (Fig)**

![Untitled](Deep%20learning%20in%20cancer%20diagnosis,%20prognosis%20and%20t%20366459b2d2a7448e9b4b52c4c847e24b/Untitled.png)

The use and interpretation of diverse and high-dimensionality data types for translational research or clinical tasks re-quire significant time and expertise.

Moreover, the integration of multiple data types is more resource-intensive than the interpretation of individual data types and needs modelling algorithms that can learn from tremendous numbers of intricate features.

The use of ML algorithms to automate these tasks and aid cancer detection(identifying the presence of cancer) and diagnosis (characterising the cancer) has become increasingly prevalent.

In this review, we describe the latest applications of deep learning in **cancer diagnosis, prognosis and treatment selection.** We focus on DL applications for **omics and histopathological data,** as well as the integration of multiple data types. We provide a brief introduction to emerging DL methods relevant to applications covered in this review. Next, we discuss specific applications of DL in oncology, **including cancer origin detection**, **molecular subtypes identification**, **prognosis and survivability prediction**, **histological inference of genomic traits**, **tumour microenvironment profiling and future applications in spatial transcriptomics**, **metagenomics and pharmacogenomics**. We conclude with an examination of current challenges and potential strategies that would enable DL to be routinely applied in clinical settings

## **Emerging deep learning methods:**

### Fundamental neural network methods:

Multi layer perceptron (MLP), recurrent neural network (RNN) and convolutional neural network (CNN) are the most fundamental and are frequently used as building blocks for more advanced techniques.

MLPs are the simplest type of neural networks, where neurons are organised in consecutive layers so that signals travel through the network in one direction (from input to output) [1]. Although MLPs can perform well for generic predictions, they are also prone to overfitting [6]

RNNs process an input sequence one element at a time, while maintaining history of all past elements in hidden “state vector(s)”. Output predictions are made at every element using information from the current element and also previous elements [1,7]. RNNs are typically used for analysing sequential data such as text, speech or DNA sequences.

CNNs are designed to draw spatial relationships from image data. CNNs traverse an image and apply small feature-filter matrices, i.e. convolution filters, to extract granular features [1]. .Features extracted by the last con-volution layer are then used for making predictions. CNNs have also been adapted for analysis of non-image data, e.g. genomic data represented in a vector, matrix or tensor format [8]

A review by Dias and Torkamani [7] described in detail how MLPs, RNNs and CNNs operate on biomedical and genomics data.

 Moreover, the use of MLPs, RNNs and CNNs to assist clinicians and researchers has been proposed across multiple oncology areas, including radiotherapy [9], digital histopathology[10, 11] and clinical and genomic diagnostics [7]. 

While routine clinical use is still limited, some of the models have already been FDA-approved and adopted into a clinical setting, for example CNNs for the prediction of malignancy in pulmonary nodules detected by CT [12],and prostate and breast cancer diagnosis prediction using digital histopathology [13, 14].

### Advanced neural-network methods:

**GCNNs are specifically designed to analyse graph data, e.g. using prior biological knowledge
of an interconnected network of proteins with nodes representing proteins and pairwise connections representing protein–protein interactions (PPI) [15], using resources such as the STRING PPI database [16].**

**This enables GCNNs to incorporate known biological associations between genetic features and perceive their cooperative patterns, which have been shown to be useful in cancer diagnostics [17].**

**Semantic segmentation is an important CNN-based visual learning method specifically for image data (Fig.2b). The purpose of semantic segmentation is to produce a class label for every single pixel in an image and cluster parts of an image together into each class, where the class represents an object or component of the image. Semantic segmentation models are generally supervised, i.e. they are given class labels for each pixel and are trained to detect the major ‘semantics’ for each class.**

**To enhance the predictive power of DL models, different data types (modalities) can be combined using multimodal learning (Fig.2c). In clinical oncology, data modalities can include image, numeric and descriptive data.**

**The two most important requirements for a multimodal network are the ability to create representations that contain dense meaningful features of the original input, and a mathematical method to combine representations from all modalities**

**There are several methods capable of performing the representative learning task, e.g. CNNs, RNNs, deep belief networks and autoencoders (AE) [21]; score-level fusion [22]; or multimodal data fusion [23].**

**The multimodal learning applications discussed in this review are based on AE models. In simplistic terms, AE architecture comprises of an encoder and a decoder working in tandem.** **The encoder is responsible for creating a representation vector of lower dimension than the input, while the decoder is responsible for reconstructing the original input using this low dimensional vector [24]. This forces the encoder to ‘learn’ to encapsulate meaningful features from the input and has been shown to have good generalisability [24].
Moreover, it provides DL models the unique ability to readily integrate different data modalities, e.g. medical images, genomic data and clinical information, into a single ‘ end-to end optimised’ model [8].**

**A major challenge with implementing DL into clinical practice is the ‘black box’ nature of the models [25].
High-stake medical decisions, such as diagnosis, prognosis and treatment selection, require trustworthy and explainable decision processes.**

**Most DL models have limited interpretability**

**Another challenge in applying DL in oncology is the requirement  for  large  amounts  of  robust,  well-phenotyped training data to achieve good model generalisability**

**Pre-training on abundant datasets from other domains may help overcome the challenges
of limited data (a process known as transfer learning). The pre-trained neural network would then be reconfigured and trained again on data from the domain of interest. This approach usually results in a considerable reduction  in  computational  and time  resources for
models training, and a significant increase in predictive performance, compared to training on small domain specific datasets[39].**

### **Deep learning in oncology:**

**However, even with the emerging DL approaches, human intervention remains essential in oncology. Therefore, the goal of DL is not to outperform or replace humans, but to provide decision support tools that assist cancer researchers to study the disease and health professionals in the clinical management of people with cancer [79].**

### Deep learning for microscopy-based assessment of cancer:

**Cancers are traditionally diagnosed by histopathology or cytopathology to confirm the presence of tumour cells within a patient sample, assess markers relevant to cancer and to characterise features such as tumour type, stage and grade.**

**A histology image viewed at high magnification (typically 20x or 40x) can reveal millions of subtle cellular features, and deep CNN models are exceptionally good at extracting features from high-resolution image data [ 82].**

**Automating cancer grading with histology-based deep CNNs has proven successful, with studies showing that performance of deep CNNs can be comparable with pathologists in grading prostate [40–42], breast [43], colon cancer [44] and lymphoma [45].**

**Explain-ability methods can enable and improve histology-based classification models
by allowing pathologists to validate DL-generated predictions.**

**Hägele et al. applied the Layer-wise Relevance Propagation (LRP) [29] method on DL models classifying healthy versus cancerous tissues using whole-slide images of lung cancer [46]. The LRP algorithm assigned a relevance score for each pixel, and pixel-wise relevance scores were aggregated into cell-level scores and compared against pathologists ’annotations. These scores were then used to evaluate DL model performance and identify how multiple data biases affected the performance at cellular levels [ 46], these insights allow clinician and software developers to gain insights into DL models during development and deployment phases.**

**In addition to classification and explain-ability, semantic segmentation approaches can also be applied on histopathology images to localise specific regions One notable approach to perform semantic segmentation is to use generative adversarial networks (GANs) [47].**

**Using this approach, Poojitha and Lal Sharma trained a CNN-based generator to segment cancer tissue to ‘help’ a CNN-based classifier predict prostate cancer grading [47]. The GAN-annotated tissue maps helped the CNN classifier achieve comparable accuracy to the grading
produced  by  anatomical  pathologists,  indicating  DL models can detect relevant cell regions in pathology images for decision making.**

### Molecular subtyping of cancer:

**Transcriptomic profiling can be used to assign cancers into clinically meaningful molecular subtypes that have diagnostic, prognostic or treatment selection relevance.**

**DL methods have the potential to be highly generalisable in profiling cancer molecular subtypes due to their ability to train on a large number of features that are generated by transcriptomic profiling. Furthermore, due to their flexibility, DL methods can incorporate prior biological knowledge to achieve improved performance.**

**Rhee et al. trained a hybrid GCNN model on expression profiles of a cancer hallmark gene set, connected in a graph using the STRING PPI network [16] to predict breast cancer molecular subtypes, PAM50 [18]. This approach outperformed other ML methods in subtype classification. Furthermore, the granular features extracted by the GCNN model naturally clustered tumours into PAM50 subtypes without relying on a classification model demonstrating that the method successfully learned the latent properties in the gene expression profiles [18].**

**The use of multimodal learning to integrate transcriptomic with other omics data may enable enhanced subtype predictions.**

**As multi-omics analysis  becomes  increasingly  popular,  multimodal learning methods are expected to become more prevalent in cancer diagnostics.**

**Digital histopathology images are an integral part of the oncology workflow [11] and can be an alternative to transcriptomic-based methods for molecular subtyping. CNN models have been applied on haematoxylin and eosin (H&E) sections to predict molecular subtypes of
lung [49], colorectal [50], breast [51, 52] and bladder cancer [53], with greater accuracy when compared to traditional ML methods.**

### Diagnosing cancers of unknown primary:

**Determining the primary cancer site can be important during the diagnostic process, as it can be a significant indicator of how the cancer will behave clinically, and the treatment strategies are sometimes decided by the tumour origin [96, 97]. However, 3–5% of cancer cases are metastatic cancers of unknown origin, termed cancers of unknown primary (CUPs) [98, 99]. Genomic,
methylation and transcriptomic profiles of metastatic tumours have unique patterns that can reveal their tissues of origin [100–102].**

### Cancer prognosis and survival:

Prognosis prediction is an essential part of clinical oncology, as the expected disease path and likelihood of survival can inform treatment decisions [111].

DL applied to genomic, transcriptomic and other data types has the potential to predict prognosis and patient survival [59–62, 112].

The most common survival prediction method is the Cox proportional hazard regression
model (Cox-PH) [113–115  ], which is a multivariate linear regression model finding correlations between survival  time  and  predictor  variables.

### Precision oncology

### The tumour microenvironment

### **The new frontiers**

## **Challenges and limitations: the road to clinical
implementation:**

**Data variability**

**Paucity of public phenotypically characterised datasets**

**AI explainability and uncertainty**