# Thyroid Region Prior Guided Attention for Ultrasound Segmentation of Thyroid Nodules

Author: Haifan Gong 
Score: ⭐️⭐️⭐️⭐️
Link:  https://github.com/haifangong/TRFE-Net-for-thyroid-nodule-segmentation
DataSet: TN3K; private TG3K; DDTI
Date published: 01/03/2023
Key word: Attention modeling, Benchmark, Ultrasound images, segmentation, thyroid nodule
Status: Not started
Task: Segmentation
Type: Journal
Data type : ultrasound image
Journal Name: Computers in Biology and Medicine
Type of paper: Experimental article

Objective:

<aside>
💡

Problem:

- the existed models usually do not explicitly constrain the thyroid nodules to be located in the thyroid gland area, which leads to the algorithms generating incorrect location of thyroid nodules outside the thyroid gland region.
- Another issue is that the current publicly available benchmark Pedraza et al. (2015) for thyroid nodules segmentation is limited and monolithic. The developed algorithms are usually based on ultrasonic data from a single center (i.e., the imaging captured from single equipment with fixed setting), which deviates from the realistic application scenario. Therefore, there is a need to construct a data set that contains ultrasound thyroid imaging from different devices of different settings.
</aside>

<aside>
➡️

Task:

1. Collect dataset from different instruments, including  GE Logiq E9, ARIETTA 850, and RESONA 70B.
2. Select samples based on the following criteria:
    - At least one thyroid nodule is in the image;
    - The image doesn’t contain the blood signal;
    - Only one representative image (i.e., the nodule closer to the center) is retained among the images from the same perspective or the same area of a patient.
    
    after selecting the samples with the above criteria, we obtain 3,493 images from 2,421 patients.
    
3. pre-process these images by ensuring that each image is converted to gray-scale and the non-ultrasound image area is cropped.
4. 
</aside>

<aside>
💡

Role of automatic segmentation:

- The automatic segmentation of thyroid nodules is a fundamental component for developing an intelligent diagnosis system and is also valuable for ultrasound guided thyroid puncture biopsy or resection of nodules Chen et al. (2020).
</aside>

The characteristic dataset of :