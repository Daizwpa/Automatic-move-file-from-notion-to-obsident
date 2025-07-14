# Towards Trust of Explainable AI in Thyroid Nodule Diagnosis

Author: Truong Thanh Hung Nguyen,
Link: https://github.com/hungntt/xai_thyroid/tree/master
DataSet: thyroid ultrasound dataset (I think it’s private)
Date published: 08/03/2023
Key word:  Object detection, Explainable artiﬁcial intelligence, Medical imaging, thyroid nodule
Status: In progress
Task: Explainability and interpretability
Type: Journal
Type of paper: Experimental article

# The objective:

we apply state-of-the-art **eXplainable artiﬁcial intelligence (XAI)** **methods** to explain the prediction of the black-box AI models in the thyroid nodule diagnosis application. 

# What’s done:

**We propose new statistic-based XAI methods, namely Kernel Density Estimation and Density map, to explain the case of no nodule detected.**

this paper, our main contributions are:

**We applied several XAI methods**, namely LIME [22], RISE [18], Grad-CAM[25], Grad-CAM++ [4], Ada-SISE [28], LRP [3], and D-RISE [19] to explain the two-stage model’s classiﬁcation and localization of nodules.

**We proposed two statistic-based XAI methods**, namely Kernel Density Estimation (KDE) and Density map (DM), to monitor the two-stage model’s localization process from the ﬁrst stage to the second stage and further explain the case of no nodule detected, especially false negative case.

**We evaluated XAI methods’ performance and suitability for the speciﬁc nodule detection cases with qualitative and quantitative results and a surveyed XAI’s trust to end-users.**

# **Conclusion:**

Our implemented and proposed XAI methods can cover all prediction cases with high consistency with the object detector and doctors’ knowledge.

according to our evaluations and surveys, we recommend end-users use Grad-CAM++ as the default method since it requires a very short  time to explain plausibly per case. At the same time, D-RISE is  suitable when we require explicitly separate explanations for each nodule due to its faithfulness but high computational time. In future works,

# Introduction:

A medical diagnosis system **must be accurate, transparent, and explainable** to gain end-users’ trust.

Considering the explainability capability, simple AI methods such as linear regression and decision trees are self-explanatory.

**Still, these methods lack the complexity required for tasks such as classifying two and three-dimensional medical images.**

Given the increasing ubiquity of advanced techniques such as deep neural networks (DNNs), a new challenge for medical AI is its so-called black-box nature, with decisions that seem opaque and inscrutable, even for experts to understand [8]

**it poses a challenge for applying DNNs to high-stakes problems such as medical imaging until we can develop methods that allow radiologists to develop understanding and appropriate trust**.

# Related Works:

## Backpropagation-based methods:

Backpropagation-based methods calculate the gradients of the model’s output to the input features or hidden neurons.

Hence, they utilize the backward pass of information ﬂow to understand neuronal inﬂuence and relevance of input towards the output.

The ﬁrst gradients explanation technique proposed in [26] computes
how much a change in each input dimension changes the predictions in a small neighbourhood around the input. 

Some preceding backpropagation-based equations
take relative importance given to gradient value during backpropagation to generate **saliency maps** [33, 27]. While **LRP** [3] modiﬁes backpropagation rules to measure the relevance or irrelevance of the input features to the models’ prediction.

## CAM-based methods:

Based on the CAM-method [34], an extensive research eﬀort on CAM-based methods has been put to blend high-level features extracted by CNNs into a unique explanation map.

**Grad-CAM [25]** and **Grad-CAM++ [4]** are two improvements over CAM that utilize backpropagation to provide a better visual explanation for classiﬁers.

## Perturbation-based methods:

Perturbation-based methods are a class of techniques for explaining the decision-making process of DNNs by modifying the model’s input and observing the output’s changes.

LIME [22] explains the prediction by learning an interpretable model
that approximates the model locally around a data point using occlusions of super- pixels.

RISE [18] proposed a method for producing saliency maps using random perturbation techniques without having to analyse the model’s complex structure.

D-RISE [19] extended RISE to produce saliency maps for object detectors.

SISE [23] improved upon RISE’s ﬁdelity and plausibility using attribution-based input sampling techniques.

Still, it has high computational costs when there are many activation
maps with positive slopes that are ineﬃcient in the prediction process. 

Ada-SISE [28] was developed to solve this problem by removing unnecessary objects, which saves computational time and provides a better reasonable explanation.

## Statistic-based methods:

Kernel Density Estimation (KDE) is a non-parametric mathematical method for estimating the probability density function of a continuous variable [29, 32] which is one of the most common methods for estimating density level, set estimation, clustering, or unsupervised learning [17]. Recently, KDE has been made explainable
with LRP for outlier and inlier detection in unsupervised learning models without the ground-truth labels [15]. Density map is commonly used in crowd counting literature, which is usually for estimating the distribution of objects, namely people in the scene [13]. However, the idea of counting the model’s detected boxes to
estimate the distribution of predicted boxes as an explanation has not been applied in previous works.

## XAI in the medical diagnosis system:

Several XAI applications for diﬀerent cancer diagnoses are proposed to answer the black-box AIs. In recent years, there have been 37 publications on how XAI is applied in skin cancer detection [10]. More than half of the articles applied current XAI methods to their model, nearly 40% tried to solve speciﬁc problems such as bias detection and the eﬀect of XAI on man-machine interactions, and the remaining 10% oﬀered novel XAI methods or enhanced existing techniques.

Recently, during the outbreak of COVID-19, LIME is also applied to explain the model’s interpretability for screening patients with COVID-19 symptoms [2]. In the same context as our study, AIBx [30] employed the image similarity model and physicians to create an
XAI model, increasing physicians’ conﬁdence in the predictions during the thyroid cancer diagnosis process.

However, the application of a wide-ranged number of XAI methods to nodule detection on thyroid ultrasound datasets has not been discovered yet. Urgently, very little is known about the inﬂuence of XAI on the predictive performance, conﬁdence, and model trust of doctors and radiologists in an artiﬁcial setting, and nothing is known about its eﬀects in a clinical setting.

# Methodology:

## Object Detector and XAI categorization:

### Analysis of images with nodule

![Untitled](Towards%20Trust%20of%20Explainable%20AI%20in%20Thyroid%20Nodule%20%20ab920bd85e864fa888ef0558a897dbc5/Untitled.png)

*They use fast R-CNN[21] and retinaNet[14] architecture to detect thyroid in ultrasound image.*

The model detection process comprises two stages:

- the Region Proposal Network generates object proposals from input images.
- a bounding box is predicted for each object proposal, with a probability of whether the box contains a thyroid nodule.
- In the second stage, the Region-of-Interest pooling layer implements bounding box regression and bounding box classiﬁer.

We categorize XAI methods in terms of their applicability to three main blocks of an
object detector (as shown in Fig. 2):

Region Proposal Generation (**Which proposals are generated by the model during the model’s ﬁrst stage?**): Kernel Density Estimation (KDE), Density map (DM).

Classiﬁcation (**Which features of an image make the model classify an image containing a nodule(s) at the model’s second stage?**): LRP, Grad-CAM, Grad-CAM++, LIME, RISE, Ada-SISE, D-RISE.

Localization (**Which features of an image does the model consider to detect a speciﬁc box containing a nodule at the model’s second stage?**): D-RISE.

### Local Interpretable Model-agnostic Explanation (LIME):

- *randomly sample data around the neighbourhood of the input instance for which produced prediction.*
- *The generated data are used to train a local model.*
- *the local model's predication generates an explanation by weighting each sample according to the instance.*
- *then LIME uses LASSO as a feature selection technique to choose the most important segments that contribute the most to the prediction for the explanation.*

### Random Input Sampling for Explanation (RISE):

## Notes

- 

## Key takeaways

- 

## Quotes

> 
> 

## Summary

-