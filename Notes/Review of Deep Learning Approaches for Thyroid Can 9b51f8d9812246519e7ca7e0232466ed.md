# Review of Deep Learning Approaches for Thyroid Cancer Diagnosis

Date published: 21/05/2022
Status: Done
Type: Journal
Type of paper: review paper

https://doi.org/10.1155/2022/5052435

## The o**bjective:**

In this study, we explained the objectives of dee learning in thyroid cancer imaging and **conducted a literature review on its potential, limits, and current application in this area.** We gave an overview of **recent progress in thyroid cancer diagnosis** using deep learning methods and **discussed various challenges and practical problems** that might limit the growth of deep learning and its integration into clinical workflow.

## **The Conclusion:**

The AI-based CAD systems development for processing thyroid images was very fast over the last decades.

Thyroid nodule treatment will be improved if these technologies are **thoroughly verified**.

Despite the empirical strengths and successes of previous deep learning algorithms and methods in assessment metrics are issues that need to be covered in next researches.

CNN is by far the most popular deep learning method for thyroid cancer diagnosis.

VGG16 method is the technique that has been widely used for thyroid nodule classification.

Moreover GANs, RNN, and LSTM methods have been utilized in some research.

The number of published  papers is not enough and more investigations are required.

**Pre-processing approaches for improving deep learning models performance is mandatory.**

## **Introduction:**

Thyroid cancer happens when rogue cells reproduce too rapidly for the immune system to control.

Thyroid cancer is detected using two major methods: (1) palpation of the neck during a physical examination. (2) Ultrasonography, which can detect palpable and non-palpable nodules, especially those less than 1cm in diameter.

Ultrasonography is used to identify the characteristics of thyroid nodules as the primary diagnostic tool. These identified characteristics help to classify nodules into benign or malignant type.

Implementing artificial intelligence in CAD tools makes them smarter and increases the accuracy and consistency of the ultrasonography features interpretation, Ultimately decreasing the unnecessary biopsy.

Machine learning and deep learning are the underlying techniques of AI-based CAD systems that greatly impact the medical field. These method rely on expert’s knowledge to choose the essential features from a set of predefined specified characteristics collected from the region of interest .

In thyroid ultrasound images, features such as margin, shape, echogenicity, calcification, and composition and have been used in many studies to develop CAD systems.

## Deep Learning Methods Reviews:

### **1) Convolutional Neural Networks:**

The specificity, sensitivity, and accuracy rates are used to measure the method’s functionality.

CNNs are mainly focused on identifying suspicious nodules and diagnosing diseases like cancerous cells by the classification of nodules into malignant and benign types. This characteristic led to the growth of using CNNs over last years.

Lee et al. introduced a CAD system that works based on a deep learning approach for patients with thyroid cancer. Eight different CNN models were used to compare the accuracy of methods in classifying thyroid cancer tumors. The ResNet50 had a better performance with higher accuracy, sensitivity, and specificity rate. [29]

The other method that was proved to have a good performance is VGG16. Lin et al. proposed a deep learning approach based on VGG16 and used the whole slide images (WSIs) database for this purpose. the result of the proposed approach indicated 99% accuracy and 94% sensitivity. [31]

Xception neural network also demonstrated high accuracy in diagnosing brain tumors.  Zhang et al. indicated the high accuracy of this approach by applying Xception neural network to CT images. [38]

CascadeMaskR-CNN utilized  ultrasound images of thyroid cancer to diagnose benign from malignant tumors. The experimental result indicated 94% of accuracy.[46]

### **2) Generative Adversarial Networks:**

These  models estimate the potential distribution of the given dataset and them generate new samples from the estimated distribution.

GANs generate fair data that are very close to the real data. this method is the second most used approach that has been used for thyroid nodules classification.

Zhang et al. proposed an adversarial learning-based approach for tissue recognition from medical images by synthesizing medical images. The synthetic model is based on Wasserstein, deep convolutional GANs, and boundary equilibrium GANs approaches. The researchers reported 98.83% accuracy for tissue recognition synthetic images.[52]

paper written by Yang and Qianqian, a semi-supervised  learning model proposed integrated domain knowledge in training dual path conditional GANs. Also, a semi-supervised support vector machine is suggested for classifying thyroid nodules. After putting the model to the test, they found that it successfully avoids the mixed outcomes that might arise when using a limited dataset.[53]

Zhao et al. introduced a novel thyroid cancer classification approach based on multimodal domain adaption. To deal with visual discrepancies between nodal data, the researchers create semantic consistency GANs and  used adversarial learning between dual domains, which is based on the self-attention mechanism. The rate of accuracy of this research for classifying benign and malignant modules was 94.30%.[54]

Shi et al. presented an adversarial augmentation technique that is knowledge-guided to synthesize medical images. They designed term and image encoders for extraction domain knowledge based on radiologists ideas. then, for high-quality thyroid nodule images and to constrain the the auxiliary classifier GANs, domain knowledge is used as a condition. The researchers tested the proposed model on the classification of the ultrasonography thyroid module.  The accuracy of model is reported to be 91.46%.[55]

The effectiveness of GANs for creating high-resolution pathology images was investigated by Levine et al. the researchers looked at ten different forms of cancer histologically, including five cancer types form the five primary histological subtypes of ovarian carcinoma and the caner Genome Atlas. They showed that Histotype-classified actual and synthetic images had similar accuracies.[56]

### Autoencoders (AE):

Unsupervised learning and deep architectures rely heavily on autoencoders for transfer learning and other tasks.

AE has been widely used in the medical field for tumor classifications. However this method has not applied widely for the classification of thyroid cancer.

Ferreira et al. applied six distinct AE types for thyroid nodules classification, as well as two different techniques to train the classification model. With an F1 score of 99.6.1% +-0.54, they conclude that combining a deeper classification network with the reconstruction of the input space outperformed previous studies.[57]

Ferreira et al. contributed to the literature by automatically classifying tumor samples by analysing their gene expressions. The researchers tried to develop a methodology for distinguishing five different cancer types form RNA-Sea datasets, including thyroid, skin, stomach, breast, and lung cancer. In this research, they adopted autoencoders for initializing weights on deep neural networks and compared the performance of three different autoencoders. The results indicated an average F1 score of 99.03 for the RNA-Seq data.[58]

To categorize thyroid nodules, Li et al. employed the stacked denoising sparse autoencoder, this study used immune-related genes to build a classifier with a stacked denoising sparse autoencoder using data of gene expression from thyroid nodule tissues. the experimental results on distinguishing benign and malignant thyroid nodules demonstrated an accuracy of 92.9%.[59]

### **Long Short-Term Memory:**

Chen et al. proposed a new approach that divided the report into two layers: a word vector layer and sentence presentation layer, with each layer employing the bidirectional LSTM and attention mechanism. Finally, they provided a model with good performance.[60]

Wu et al. applied ML algorithms  such as gradient boosting trees, k-nearest neighbor, decision trees,  Naive Bayes, logistic regression, random forest, and LSTM model using time-series tumor marker data on two large asymptomatic cohorts, including 163,174 records, Compared to the other ML models, the LSTM model proved the best at handling erratic data.[61]

### **Deep belief Network:**

These algorithms provide solutions for the limitations of training conventional neural networks in deep layered net-works, including getting stuck in local minima due to poor parameters, slow learning, and requiring big training datasets.

The only paper that applied the DBN method for thyroid nodule diagnosis is the research done by Pavithra and Parthiban. They presented a new pigeon inspired optimization(PIO) problem with the DBN model, named PIO-DBN, for the classification and diagnosis of thyroid disease. The PIO-DBN model reached the maximum accuracy of 98.91% and 96.28%on the two thyroid datasets used to evaluate the model.[62]

### **Recurrent Neural Network RNN:**

For thyroid cancer nodule diagnosis, Begum et al. utilized bBidirectional RNN to evaluate the risk of getting thyroid illness in patients. the result of applying the proposed approach was a 98.72% rate of accuracy.[63]

Santillan et al. studied distinguishing malignant from benign thyroid lesions by applying five neural network approaches, and the results indicated that RNN model preformed better than the rest, having an accuracy of 98%.[64]

## **Discussion:**

It is a challenging to interpret ultrasound images, and the interpretation can be altered based on radiologists prior medical knowledge and observational skills.

There is a significant need for AI-based CAD systems with better designs and practicality consistent nodule management solutions in practice.

The literature demonstrated that although CAD systems provide similar sensitivity to experienced radiologists, they still cannot reach the level of specificity and accuracy of experts. Therefor, a probable option to consider is to combine the specificity and accuracy of radiologists with the sensitivity of CAD systems and use these systems as assistants for operators with less experience at primary care centers.

Future research should scrutinize  the effectiveness of theses methods and techniques for pre-processing images is necessary as they can alter the performance of deep learning models significantly.

Other challenges that need to be addressed in future research include coping with data limitations, creating valid and public datasets, and developing standard evolution measures. 

Furthermore, all deep learning approaches, including B-mode, Doppler, contrast-enhanced ultrasound, SWE, should be used on multimodal images to get a complete picture of the lesions. 

Thyroid nodule diagnosis accuracy can be improved by registering, training and evaluation thyroid nodules multimodal images.

 Besides, the lack of standard metrics for evaluating the suggested methods performance makes it difficult to compare their outcomes.

Based on the recent publication, it can be concluded that among all deep learning techniques, CNNs have been widely applied in order to diagnose thyroid cancer. Thee results yielded high sensitivity, specificity, and accuracy. However, other deep learning methods have not been applied widely, and there are not enough papers to make the comparison between methods reasonable. The second most used deep learning method to diagnose thyroid nodules is GANs. The high rate of sensitivity, specificity, and accuracy indicates that the application of this method on multimodal images can result in finding models with a better performance. The other popular deep learning approaches like RNN, DBN, and LSTM have not been used widely, and more research should be done to find out the rate of accuracy.

## Reference:

[29]. H. Lee, E. J. Ha, and J. H. Kim, “Application of deep learningto the diagnosis of cervical lymph node metastasis fromthyroid cancer with CT,”European Radiology, vol. 29, no. 10,pp. 5452–5457, 2019.

[31] Y. J. Lin, T. K. Chao, M. A. Khalil et al., “Deep learning fastscreening approach on cytological whole slides for thyroidcancer diagnosis,”Cancers, vol. 13, no. 15, p. 3891, 2021.

[38] X. Zhang, V. C. S. Lee, J. Rong, F. Liu, and H. Kong, “Multi-channel convolutional neural network architectures for thy-roid cancer detection,”PLoS One, vol. 17, no. 1, Article IDe0262128, 2022.

[46]. Lu, Y. Yang, and W. Chen, “Application of deep learning inthe prediction of benign and malignant thyroid nodules onultrasound images,”IEEE Access, vol. 8, Article ID 221480,2020.

[52] Q. Zhang, H. Wang, H. Lu, D. Won, and S. W. Yoon, “Medicalimage synthesis with generative adversarial networks fortissue recognition,” inProceedings of the 2018 IEEE Inter-national Conference on Healthcare Informatics (ICHI),pp. 199–207, NY, USA, June 2018.

[53] W. Yang and D. Qianqian, “DScGANS: integrate domainknowledge in training dual-path semi-supervised conditionalgenerative adversarial networks and S3VM for ultrasonog-raphy thyroid nodules classification,”Lecture Notes inComputer Science, vol. 11767, pp. 558–566, 2019.

[54] J. Zhao, X. Zhou, G. Shi et al., “Semantic consistency gen-erative adversarial network for cross-modality domain ad-aptation in ultrasound thyroid nodule classification,”AppliedIntelligence, vol. 52, no. 9, Article ID 10383, 2022.

[55] G. Shi, J. Wang, Y. Qiang et al., “Knowledge-guided syntheticmedical image adversarial augmentation for ultrasonographythyroid nodule classification,”Computer Methods and Pro-grams in Biomedicine, vol. 196, Article ID 105611, 2020.

[56] . B. Levine, J. Peng, D. Farnell et al., “Synthesis of diagnosticquality cancer pathology images by generative adversarialnetworks,”:e Journal of Pathology, vol. 252, no. 2,pp. 178–188, 2020.

[57] M. F. Ferreira, R. Camacho, and L. F. Teixeira, “Autoencodersas weight initialization of deep classification networks appliedto papillary thyroid carcinoma,” inProceedings of the 2018IEEE International Conference on Bioinformatics and Bio-medicine (BIBM), pp. 629–632, CA, USA, November 2019.

[58] M. F. Ferreira, R. Camacho, and L. F. Teixeira, “Usingautoencoders as a weight initialization method on deep neuralnetworks for disease detection,”BMC Medical Informaticsand Decision Making, vol. 20, no. S5, p. 141, 2020.

[59] Z. Li, K. Yang, L. Zhang, C. Wei, P. Yang, and W. Xu,“Classification of thyroid nodules with stacked denoisingsparse autoencoder,”International Journal of Endocrinology,vol. 2020, Article ID 9015713, 8 pages, 2020.

[60] D. Chen, J. Zhang, and W. Li, “(yroid nodule classificationusing two levels attention-based Bi-directional LSTM withultrasound reports,” inProceedings of the 2018 9th Interna-tional Conference on Information Technology in Medicine andEducation (ITME), pp. 309–312, Hangzhou, China, October2018.

[61] X. Wu, H. Y. Wang, P. Shi et al., “Long short-term memorymodel – a deep learning approach for medical data with ir-regularity in cancer predication with tumor markers,”Computers in Biology and Medicine, vol. 144, Article ID105362, 2022.

[62] R. Pavithra and L. Parthiban, “Pigeon Inspired OptimizationWith Deep Belief Network For (yroid Disease DiagnosisAnd Classification,”Computer Science, Medicine, Article ID231815424, 2020.

[63] A. M. Begum, M. I. Tresa, A. Professor, and K. Ramakrishnan,“Machine learning based dysfunction thyroid cancer detection with optimal analysis,”Turkish J. Comput. Math.Educ., vol. 12, no. 7, pp. 818–823, 2021.

[64] A . Santillan, R. C. Tomas, R. Bangaoil et al., “Discriminationof malignant from benign thyroid lesions through neuralnetworks using FTIR signals obtained from tissues,”Ana-lytical and Bioanalytical Chemistry, vol. 413, no. 8,pp. 2163–2180, 2021.