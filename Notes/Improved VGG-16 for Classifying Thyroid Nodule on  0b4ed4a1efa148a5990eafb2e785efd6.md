# Improved VGG-16 for Classifying Thyroid Nodule on Thyroid Ultrasound Images

Author: Thia Anissa
Score: ⭐️⭐️⭐️⭐️
DataSet: Private
Date published: 11/04/2023
Key word: Deep Learning, characteristic, classification, composition, thyroid nodule
Method: VGG16 
Status: Done
Task: Tumour characteristic
Type: Conference
Data type : ultrasound image
Type of paper: Experimental article

# The Objective:

This study developed a method to help experts define the composition characteristics. *for thyroid nodules.* 

# Done work:

The experts have already cropped the dataset and then moved to pre-process using an adaptive median filter.

 Subsequently, the data were classified with the improved VGG16 into four categories those are cystic, solid, complex, and spongiform.

# The conclusion:

The proposed method comprises pre-processing and classification by improved VGG-16. Using 50 ultrasonography images collected from the Radiology Unit of Sardjito General Hospital, the data were classified into four categories according to their nodule composition: spongiform, cystic, and solid. Compared to other architectures, this study achieved higher values with an accuracy of 99.65%, sensitivity of 99.03%, specificity of 99.89%, PPV of 99.59%, NPV of 99.90%, and F1-score of 0.993.

# The Introduction:

Thyroid nodules can be observed using ultrasound, MRI, and CT scans. However,
ultrasound is considered the best detection tool due to the lack of radiation emitted.

On the other hand, ultrasound has the disadvantage of being operator-dependent. In practice, acquiring a medical image is highly dependent on the work of doctors. It can lead to subjective diagnostic results based on experience, and diagnosis results may differ between doctors [4].

According to the American College of Radiology (ACR) proposed a Thyroid Imaging Report and Data System (TI-RADS), the level of malignancy of thyroid cancer is assessed from five components [5], [6]. The final diagnosis of thyroid nodule malignancy requires an evaluation of each component’s characteristics [7]. The experts should examine these components because malignancy cannot be determined
solely by one component. **The component characteristics that become a reference for thyroid nodule malignancy are composition, echogenicity, shape, margins, and echogenic foci [5].**

# The methodology:

The thyroid ultrasound images used in this study were collected from the Radiology Unit of Sardjito General Hospital.

![Untitled](Improved%20VGG-16%20for%20Classifying%20Thyroid%20Nodule%20on%20%200b4ed4a1efa148a5990eafb2e785efd6/Untitled.png)

The proposed method comprises several steps. Those are pre-processing, augmentation, and classification.

![Untitled](Improved%20VGG-16%20for%20Classifying%20Thyroid%20Nodule%20on%20%200b4ed4a1efa148a5990eafb2e785efd6/Untitled%201.png)

RoI:  Each image was cropped by experts and became the region of interest (RoI).

# The Pre-processing:

The adaptive median filter is used to enhance the image and remove noise in the image [12].

This filter performs filtering on a 3x3 window and iterates up to a 7-by-7 size.

# The Augmentation:

To perform the augmentation, this study used traditional augmentation, which is horizontal flip, vertical flip, and rotation in various angels. The rotation for each flip process is added 0.1° - 0.2°.

# The classification:

![Untitled](Improved%20VGG-16%20for%20Classifying%20Thyroid%20Nodule%20on%20%200b4ed4a1efa148a5990eafb2e785efd6/Untitled%202.png)

The measurement components used consist of accuracy, sensitivity (true positive rate), specificity, positive predicted value, negative predictive value, false positive rate, and F score. The measurement components are obtained from the value index as follows:

![Untitled](Improved%20VGG-16%20for%20Classifying%20Thyroid%20Nodule%20on%20%200b4ed4a1efa148a5990eafb2e785efd6/Untitled%203.png)

As far as our dataset is concerned, the imbalance issue always exists. Since the evaluation of the performance of this model is not enough, we added AUC as an evaluation matrix. Multiple categories are evaluated using the micro-average
AUC [25]. For the macro-average AUC calculation, each category is treated as two categories for calculating the FPR and TPR, and the average is calculated regardless of the imbalance between categories. The experiments perform separate calculations for the micro-average AUC and macro-average AUC.

# The Results and Analysis: