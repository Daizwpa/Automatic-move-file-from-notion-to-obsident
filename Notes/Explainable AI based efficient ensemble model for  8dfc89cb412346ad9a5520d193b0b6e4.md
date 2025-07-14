# Explainable AI based efficient ensemble model for breast cancer classification using optical coherence tomography

Author: Babita Dhiman, Sangeeta Kamboj, Vishal Srivastava 

Score: ⭐️⭐️⭐️⭐️
DataSet: Private
Date published: 07/02/2024
Key word: Breast cancer, Ensemble methods, Machine Learning, Optical Coherence Tomography, Optimization, SHAP values, TOPSIS
Method: Ensemble classifier + TOPSIS + CS Algorithm 
Status: Done
Task: Breast cancer diagnosis, Explainability and interpretability
Type: Journal
Data type : Radiomics features, optical coherence tomography
Journal Name: Biomedical Signal  Processing and control  Elsevier indexed in science direct
Type of paper: Experimental article

Objective:

- Enhance the detection  of breast cancer to increase survival rate.
- Early detection for breast cancer.
- to enhance the interpretability of ML models for breast cancer classification using OCT images.
- The primary goal of this research is to prioritize and rank a group of base classifiers based on several evaluation criteria (*using TOPSIS*).

Problematic:

- Breast cancer is a significant global health concern, accounting for 12.9 % of deaths in 2020 [1]. Early-stage cancer patients had a much greater survival rate and a significantly lower risk of dying from their malignancy [2]. Various imaging methods, such as X-ray, Mammography, MRI, Ultrasound, and Photoacoustic Imaging have been used for breast cancer screening and diagnosis [3–6]. **However, they have limitations, such as reduced sensitivity, false-positive rates, and limited availability for surgical therapy.**
- Despite its advantages, OCT generates a large number of images, leading to time-consuming manual examination and high inter-observer variability. To address this, researchers are exploring intelligent classifier models to automate breast cancer classification using OCT images.
- The variability in individual classifier performance across datasets drives researchers towards constructing effective classifier ensembles using Multi-Criteria Decision Making (MCDM) approaches. By employing ensembles and MCDM, **researchers seek to overcome the challenges of individual classifiers and enhance the accuracy and reliability of breast cancer detection, paving the way for more advanced and efficient healthcare services.**
- The limited adoption of ML algorithms with strong predictive capabilities can be attributed to their **lack of transparency**. Just like the importance of clear and transparent labeling on food products aids in comprehension and acceptance, the significance of interpretability cannot be overstated.

Contribution:

- Firstly, the research proposes a multi-stage ensemble classifier based on TOPSIS and Crow Search-based weighted voting. TOPSIS is utilized to rank and select base classifiers for the ensemble, considering various performance metrics. The CS algorithm optimizes the weights of these classifiers to achieve an optimal combination within the ensemble. This ensemble model aims to improve classification performance, addressing the challenge of selecting and weighing classifiers effectively.
- Secondly, the paper explores the use of SHAP values which offers insights into feature importance and the impact of each feature on the final output.

Task:

- Collect 48 patients aged between 35 and 60 years. each patient has 200 images.
- **67 Extract features from images and apply feature selection through SHAP values.**
- Trained various classifier (Ridge Classifier, Ada Boost Classifier, Random Forest Classifier, K-Neighbors Classifier, Decision Tree Classifier, SVM-Liner Kernel, Gradient Boosting Classifier, Quad. Dis. Analysis, Linear Dis. Analysis, Logistic Regression,  Extra Trees Classifier, N**aïve** Bayes)
- **Select the most robust performance classifier using TOPSIS. The selected classifier are (Random Forest classifier, Gradient Boosting Classifier, Extra Trees Classifier, K-Neighbors classifier).**
- Optimize the weights of the base classifier selected with the help of TOPSIS, Crow Search Algorithm used.
- build ensemble classifier.
- Compare The proposed ensemble model’s performance is compared to two traditional ensemble models, namely majority voting (MV) and weighted voting (WV), as well as a soft computing model called particle swarm optimization-weighted voting (PSO-WV) and genetic algorithm optimization-weighted voting (GAO-WV).
- 
- test it

Result:

- The results obtained confirms that the best-performing model varies depending on the evaluation criteria, empha­sizing the need for considering multiple criteria for a reliable assessment.
- To construct an optimal model that excels in multiple criteria, utilizing an ensemble model is a viable approach.
- Enhancing the per­formance of ensemble learners requires each learner to produce an
ample number of diverse predictions, ensuring uniqueness among the generated models.
- For breast cancer classification, the proposed ensemble model sur­ passes all independent models.
- these findings show that the ensemble model-based training approach can successfully be used for breast cancer classifiers.

![Untitled](Explainable%20AI%20based%20efficient%20ensemble%20model%20for%20%208dfc89cb412346ad9a5520d193b0b6e4/Untitled.png)

![Untitled](Explainable%20AI%20based%20efficient%20ensemble%20model%20for%20%208dfc89cb412346ad9a5520d193b0b6e4/Untitled%201.png)

Conclusion:

- The combination of explainable AI and OCT in developing an ensemble model for breast cancer classifica­tion holds great promise in providing efficient, reliable, and interpret­ able diagnostic tools for the early and precise detection of breast cancer.
- 

Quote:

- Optical coherence tomography (OCT) emerges as a promising alternative. It is a non-invasive, real-time, three-dimensional imaging technology with a resolution comparable to histopathology.
- OCT can detect malignant regions within breast tissue and differentiate between healthy and cancerous tissue, including microcalcifications, invasive ductal carcinoma (IDC), and ductal carcinoma in situ (DCIS) [7,8].
- Having high transparency in the model streamlines the quality assurance process at each stage of the pipeline. Researchers with a deep understanding of the model can identify and rectify significant errors that may occur during input or execution stages, making it a valuable approach for assessing and confirming the model’s performance.
- Radiomics is a medical technique that employs data-characterization algorithms to extract numerous quantifiable properties from medical images [23]. Unlike subjective ’semantic’ traits identified by expert radiologists, radiomic elements are objective and can reveal tumor
patterns and properties imperceptible to the human eye. Utilizing ML radiomic features show great potential as a diagnostic tool for tumor classification, offering accurate categorization and reducing false positives.
- Texture analysis is widely utilized in radiomics for medical images, offering various quantitative techniques such as energy, entropy, and correlation. These textural characteristics provide
valuable information about the region of interest, including spatial color or intensity organization within the image.
- radiomics analysis is crucial in distinguishing important features such as tumor concentration, coarseness, and calcification dis­tribution [25].
- TOPSIS is a decision-making method **that prioritizes choices closest to the positive ideal solution** and **farthest from the negative ideal solu­tion** [27].
- The Crow Search Algorithm is  meta-heuristic algorithm inspired by crow’s intelligent behaviour in protecting their food sources and detecting locations where other crows hide.
- **The dataset consisting of mixed responses were put in a different folder and were used only for the testing. SHAP values are calculated after training and testing our models to interpret the results of our classification module. Fig. 4 shows the SHAP values for each feature. The SHAP values help us to understand how each pixel contributes to the prediction. The plot’s y-axis represents the feature, and the x-axis rep­resents the Shapley value. Features are ordered by importance, and color indicates the value of the feature from low to high.**

Tools:

-