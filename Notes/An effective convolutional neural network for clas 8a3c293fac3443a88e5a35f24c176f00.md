# An effective convolutional neural network for classification of benign and malignant breast and thyroid tumors from ultrasound images

Author: Ronghui Tian
Score: ⭐️⭐️⭐️⭐️⭐️
Link: No code
DataSet: private dataset
Date published: 17/05/2023
Key word: Breast cancer, Convolutional neural network (CNN), Thyroid cancer, Transfer learning (TF), classification
Method: CNN model
Status: Done
Task: Tumour Malignancy Diagnosis
Type: Journal
Data type : ultrasound image
Journal Name: Physical and Engineering Sciences in Medicine springer index in PubMed
Explainability : gradient‐weighted class‐activation
Muti-central Data: False
Transfer learning: Yes
Type of paper: Experimental article

# Objective:

develop an effective convolutional neural network (E-CNN) for the classification of benign and malignant breast and thyroid tumors from ultrasound images.

## Problematic:

- **The high similarity affects the sensitivity and specificity of the diagnosis.** In terms of treatment, benign tumors are generally easy to treat with good results, while malignant tumors have complex treatment measures
with unsatisfactory effects. If benign tumors are misdiagnosed as malignant tumors, it will lead to transitional treatment and increase the burden on patients. On the contrary, **malignant tumors are misdiagnosed as benign, which will delay treatment and aggravate the patient's condition**. Therefore, it is of great significance to distinguish between benign and malignant tumors in clinical diagnosis and treatment.

Motivation:

- That is, breast cancer and thyroid cancer are mutually primary tumors and second primary tumors. Ultrasonographic evidence shows that the breast and thyroid tumors from ultrasound images have similar features: hypo-echoic mass, irregular margins, greater-than-1 aspect ratio, internal microcalcifications, and abundant blood flow. Therefore, we are inspired to develop an effective convolutional neural network (E-CNN) for the classification of benign and malignant breast and thyroid tumors in ultrasound images, aiming to assist radiologists in their diagnosis.

## Task:

- Collected 1052 ultrasound image of breast tumors using tow different ultrasound machines (dataset A), and 8245 ultrasound image of thyroid tumours from 76 thyroid cases using one ultrasound machine  (dataset B).
- Crop ROI, augment, normalizing.
- cropping algorithm to adaptively augment dataset
- Build model CNN
- customized the Balance Category Proportion Loss (BCPL) function. to deal with Imbalanced dataset
- Cross validation.
    - transferred the breast model to classify typical tumor images of 76 patients.

## Result:

- the proposed E-CNN was applied to classify and evaluate 9297 mixed images (breast and thyroid images). The mean classification accuracy was 0.875, and the mean area under the curve (AUC) was 0.955.
- The finetuning model achieved a mean classification accuracy of 0.945, and a mean AUC of 0.958. Meanwhile, the transfer thyroid model realized a mean classification accuracy of 0.932, and a mean AUC of 0.959, on 1052 breast tumor images
- The tenfold validation results were averaged to illustrate the classification performance of the E-CNN.

## Conclusion:

- The experimental results demonstrate the ability of the E-CNN to learn the features and classify breast and thyroid tumors.
- The experimental results demonstrate the ability of the E-CNN to learn the features and classify breast and thyroid tumors. Besides, it is promising to classify benign and malignant tumors from ultrasound images with the transfer model under the same modality.

## Limitation:

## Quote:

- thyroid cancer exhibits a rapid upward trend in China in recent years [3]. It is widely believed that thyroid cancer is related to high iodine or iodine-deficient diet, radiation exposure, increased estrogen secretion, genetic factors, as well as benign thyroid diseases like nodular goiter, hyperthyroidism, thyroid adenoma, and especially chronic lymphocytic thyroiditis.
- Studies have shown that early screening and diagnosis are effective ways to improve the survival rate of breast and thyroid cancer patients [4–6].
- If benign tumors are misdiagnosed as malignant tumors, it will lead to transitional treatment and increase the burden on patients. On the contrary, malignant tumors are misdiagnosed as benign, which will delay treatment and aggravate the patient's condition.
- The data pre-processing enhances the representation of the
image and improves the generalization ability of the CNN.
- medical images are usually noisy, which affects the performance of segmentation and classification tasks. Although there are several denoising methods [31],
- LeNet-5 is the first ever CNN to be applied in the visual field [32].
- 

# The Done work:

*• They proposed new CNN architecture (ECNN) and train two model using two different ultrasound data sets (breast, thyroid). After that they transformed the two models to others type of cancer. They implemented pre-processing , augmentation, data balance, cross-validation and new loss function they name it “Balance Category Proportion Loss (BCPL)” inspired from Cross entropy.*

They performed tenfold cross-validation on breast and thyroid data.

The proposed E-CNN was applied to classify and evaluate 9297 mixed images (breast and thyroid images).

They transferred the breast model to classify typical tumor images of 76 patients

![Untitled](An%20effective%20convolutional%20neural%20network%20for%20clas%208a3c293fac3443a88e5a35f24c176f00/Untitled.png)

Model

 - multi-scale model.

- ECNN model consists of 23 convolutions and two full-connected layers,
- All three layers of stacked convolution use 3 × 3 kernels.
- A rectified linear unit (ReLU) follows each convolutional layer to eliminate vanishing gradients
- ECNN model consists of  base conv, five module and two full connected layers
- the modules generally has tow type:
    - 1- the convolutional kernel and pooling window are both of size 3 × 3, and the step size is still 2 × 2. The two branches output a different number of feature maps, which are of the same size. The feature maps are fused as the input to the next module.
    - 2- The second module inspired by Res2Net, has the ability to express multi-scale high- dimensional features in a more refined manner.
    the Res2Net module divides the feature maps into 4
    groups, denoted by ­Xi, where i ∈ {1, 2, 3, 4}. Each group has
    3 × 3 convolutional layers, and the output is denoted by Mi ()