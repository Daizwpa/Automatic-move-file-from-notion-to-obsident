# Deep learning-based artificial intelligence model to assist thyroid nodule diagnosis and management: a multicentre diagnostic study

Author: Sui Peng
Score: ⭐️⭐️⭐️⭐️⭐️
DataSet: Private 
Date published: 01/04/2021
Method: Deep learning
Status: Done
Task: Integration strategy AI, Tumour Malignancy Diagnosis
Type: Journal
Data type : imagery data, ultrasound image
Journal Name: The LANCET Digital health journal EL-SEVIER indexed PubMed
Explainability : class activation maps
Muti-central Data: True
Type of paper: Experimental article

Objective:

- developed a deep-learning AI model (ThyNet) to differentiate between malignant
tumours and benign thyroid nodules and aimed to investigate how ThyNet could help radiologists improve diagnostic performance and avoid unnecessary fine needle aspiration.
- investigated whether radiologists could improve their diagnostic performance with the assistance of the ThyNet model when reading ultrasound images and videos and explored the potential of the ThyNet-assisted strategy to help radiologists avoid unnecessary fine needle aspirations.

Problematic:

- Strategies for **integrating artificial intelligence (AI) into thyroid nodule management** require additional development and testing.
- Reduce the number of unnecessary FNA Biopsy.

Task:

- Collect 18049 image from 8339 patient in two different hospitals.
- Collect test set 4305 image from 2775 patient in seven different hospitals and dived it to three dataset (A, B and C).
    - 2185 images of 1424 patients with thyroid nodules enrolled from four independent hospitals (test set A) were used to test ThyNet against diagnosis made by radiologists.
    - 1754 images of 1048 patients with thyroid nodules enrolled from two hospitals (test set B) were used to test the ThyNet-aided diagnostic process.
    - 366 images of 303 patients with thyroid nodules enrolled from three hospitals (test set C) were used to test ThyNet in a real-world clinical setting.
- resized to 256 × 256 pixels before being cropped to 224 × 224 pixels. Standard image pre-processing (clipping, flipping, and rotating) for deep learning to generate a larger, more
complicated and diverse dataset to improve accuracy and generalisability
- Build ThyNet
- Heatmaps were generated by the GRAD-CAM methods.
- ThyNet was tested in three stages (figure 1).
    - the diagnostic performance of ThyNet was compared with 2 radiologist ( six junior, six senior)  (with test set A);
    - improvement in the diagnostic performance of radiologists when assisted by
    ThyNet was evaluated (with test set B);
    - the application of ThyNet in actual clinical practice was investigated (with test set C).

Model:

- it is a combined architecture of three networks: ResNet, ResNeXt, and DenseNet
- learning settings:
    - Stochastic gradient descent
    - cross-entropy loss were used for network weight tuning and algorithm optimisation.
    - The initial learning rate was 0·01, which decreased by one-tenth every 100 epochs;
    the final learning rate was 0·0001.
    - To prevent overfitting, batch normalisation was used and the weight decay rate
    was set to 0·0005.
    - We used a batch size of 128 images and a Rectified Linear Unit activation function.

Result:

- The area under the receiver operating characteristic curve (AUROC) for accurate diagnosis of ThyNet (0·922 [95% CI 0·910–0·934]) was significantly higher than that of the radiologists (0·839 [0·834–0·844]; p<0·0001).
- In the simulated scenario, the number of fine needle aspirations decreased from 61·9% to 35·2% using the ThyNet-assisted strategy, while missed malignancy decreased from 18·9% to 17·0%.
- ThyNet-assisted strategy improved the pooled AUROC of the radiologists from 0·837 (0·832–0·842) when diagnosing without ThyNet to 0·875 (0·871–0·880; p<0·0001) with ThyNet for
- reviewing images, and from 0·862 (0·851–0·872) to 0·873 (0·863–0·883; p<0·0001) in the clinical test, which used images and videos

Conclusion:

- The ThyNet-assisted strategy can significantly improve the diagnostic performance of radiologists and help reduce unnecessary fine needle aspirations for thyroid nodules.
- The classifications made by the ThyNet system could be used to reduce the workload involved in the decision- making process of fine needle aspiration, while preserving the standard of care.
- fine needle aspirations could have been avoided with the assistance of ThyNet due to the high probability of being malignant.
- The ThyNet-assisted strategy not only improved the diagnostic accuracy of radiologists when
reviewing images only but also when reviewing images and videos in a clinical setting.
- Of note, the combination of the ACR TI-RADS classification with AI assistance improved the negative predictive value and positive predictive value, which has the potential to reduce the number of unnecessary fine needle aspirations.
- 

Quote:

- Thyroid nodules are found in up to 68% of asymp­tomatic adults in the general population.1 Approximately 7–15% of thyroid nodules are thyroid cancer, which is the most rapidly increasing malignancy in all populations.
- The large number of thyroid nodules, with only a fraction being cancerous, calls for a reliable method to accurately differentiate malignant from benign nodules.
- Routine decision making for patients with thyroid nodules depends on ultrasound or invasive fine needle aspiration.2 However, the assessment of ultrasound features is time consuming, subjective, and often dependent on a radiologist’s experience and the available ultrasound devices.3
- Ultrasound conclu­sions are often inconsistent and even with fine needle aspira­tions
15–30% of the samples still yield indeterminate cytological findings.4
- The absence of multicentre training cohorts and a small number of ultrasound devices in previous studies restricted their generalisability in clinical practice.
- In our preliminary study, a machine learning system showed a better predictive value for
malignant thyroid nodules compared with humans using American College of Rheumatology (ACR) Thyroid Imaging Reporting and Data System (TI-RADS).7
- The introduction of deep learning in thyroid imaging has also achieved a better diagnostic performance than experienced radiologists.12,13
- The noise information (e.g., paramaters of the ultrasound device),