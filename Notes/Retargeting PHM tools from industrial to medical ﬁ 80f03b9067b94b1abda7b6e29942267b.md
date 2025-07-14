# Retargeting PHM tools: from industrial to medical ﬁeld

Author: Abir Belaala
DataSet: Cleveland Heart Disease Dataset
Date published: 17/09/2020
Status: Done
Task: Heart Diseases
Type: Conference
Journal Name: EUROPEAN CONFERENCE OF THE PROGNOSTICS AND HEALTH MANAGEMENT SOCIETY 2020
Type of paper: AI-Experiment, Experimental article

Keywords: None

# The objective:

The aim of this paper is to apply an adaptation of a PHM model from fault diagnosis of aircraft engine to diagnosis human heart disease.

# The conclusion:

This work could be considered as a ﬁrst step to reduce the gap between industry and medical ﬁelds, by exchanging the applied techniques, and by  showing that models applied for machine’s health diagnosis could be applicable for human’s health diagnosis.

The obtained results allow us to think about generalized PHM model using domain adaptation and transfer learning to solve other challenging applications

# Introduction:

This statistics shows the need of having computer aided diagnosis (CAD) system that is able to provide a preliminary assessment of a patient based on simple accessible medical tests.

In order to develop a CAD for heart disease, a new scheme is proposed based on PHM adaptation using UCI heart disease dataset (Cleveland Heart Disease Dataset, 1990). The proposed scheme consists of: (a) the pre-processing step to improve data quality (missing data imputation and scaling dataset), (b) the feature selection step to improve classiﬁcation performance (based on embedded method), (c) the diagnosis phase to identify the absence or the presence of heart disease (using Improved Dragging Regularized ELM (ID-RLM)). The performance of our proposed scheme is compared with previous work.

# 2. ENGINEERING PHM VS MEDICAL PHM

This success of PHM in industry motivates us to think about the implementation of this process in the medical ﬁeld. In the last decades, computer-aided diagnosis and computer-aided prognostics in medical domain have been active areas in computer science ﬁeld. However, the accuracy and reliability are still lacking. 

The main duties of PHM expertise are **to identify incipient system fault or component;** to implement failure diagnostics and prognostics, and health management (Atamuradov et al., 2017).

We may infer that an adaptation of PHM can be applied in the medical ﬁled with two key points being taken into account:

- Working on human body is more complicated, any mistake leads to critical consequences.
- The data generation and sharing in medical ﬁled still hard to achieve, and the privacy of patients should be taking in consideration.

# 3. ADAPTED PHM TOOL

Figure 1 shows the general schematic diagram of our proposed tool adapted from (Zhao et al., 2017) to diagnose heart disease. The details of each processing stage are described in the subsequent sections.

![Untitled](Retargeting%20PHM%20tools%20from%20industrial%20to%20medical%20%EF%AC%81%2080f03b9067b94b1abda7b6e29942267b/Untitled.png)

## 3.1. Data description

The Cleveland dataset (Cleveland Heart Disease Dataset, 1990)

*You can download from here: [https://archive.ics.uci.edu/dataset/45/heart+disease](https://archive.ics.uci.edu/dataset/45/heart+disease)*

## 3.2. Data pre-processing:

### 3.2.1. Missing data:

In this paper, we are going to apply the KNN techniques.

### 3.2.2. Scaling data:

data columns are re-scaled to a range of [0 − 1].

### 3.2.3. Feature selection:

Feature selection process is very signiﬁcant to ﬁnd most relevant attributes to the classiﬁcation and then to the diagnosis.

Feature selection has many advantages:

- To make the model simpler to interpret.
- To decrease the variance of the model, and therefore over-ﬁtting.
- To decrease the computational time and cost.
- to increase the performance of the model.

In the literature, there are three main types of feature selection techniques:

- ﬁlter.
- wrapper.
- embedded methods

In this paper we will choose the third one, which combine the advantages of ﬁlter and wrapper methods as implemented by algorithms that have their own built-in feature selection methods. Random Forests (RF) are often used as embedded feature selection.

![Untitled](Retargeting%20PHM%20tools%20from%20industrial%20to%20medical%20%EF%AC%81%2080f03b9067b94b1abda7b6e29942267b/Untitled%201.png)

![Untitled](Retargeting%20PHM%20tools%20from%20industrial%20to%20medical%20%EF%AC%81%2080f03b9067b94b1abda7b6e29942267b/Untitled%202.png)

## 3.3. Diagnosis:

Extreme learning machine (ELM) is proposed and implemented by (Liang, Huang, Saratchandran, & Sundararajan, 2006) as a single hidden layer feedforward network. 

The reason behind this success is the efﬁciency and the effectiveness of the model based on two main advantages:

- ELM generates randomly hidden layer biases and input weights. Unlike the traditional neural network, ELM determines the output weights without tuning by iterations as error back-propagation.
- ELM searches to minimize both training errors and the norm of output weights, based on Bartlett’s theory which beneﬁts the generalization on the unseen data.

Despite the evidence of the drawback of ELM, it has a weak point presented in the generation of extra hidden nodes to reach the same generalization performance as the traditional neural networks.

A large size network leads to more computational time in the testing phase, which is not suitable for testing time view.

We here apply the improved version (ID-RELM) for diagnosis, which abandons the reference
points and can improve the classiﬁcation performance by retargeting the ELM label vector.

## 3.4. Performance Metrics:

The used model is evaluated using the below metrics:

![Untitled](Retargeting%20PHM%20tools%20from%20industrial%20to%20medical%20%EF%AC%81%2080f03b9067b94b1abda7b6e29942267b/Untitled%203.png)

![Untitled](Retargeting%20PHM%20tools%20from%20industrial%20to%20medical%20%EF%AC%81%2080f03b9067b94b1abda7b6e29942267b/Untitled%204.png)

# 4. EXPERIMENTATION

By combining RF features selection with ID-RELM, the highest classiﬁcation performances are achieved as we can remark in Table 3 (the accuracy increases to 0.94 and AUC is 0.94).

We now come to compare the obtained diagnosis results from the adapted PHM tool using ID-RELM & RF to several methods that were recently proposed to contribute in developing
the decision support system for heart disease diagnosis (see Table 4).

![Untitled](Retargeting%20PHM%20tools%20from%20industrial%20to%20medical%20%EF%AC%81%2080f03b9067b94b1abda7b6e29942267b/Untitled%205.png)