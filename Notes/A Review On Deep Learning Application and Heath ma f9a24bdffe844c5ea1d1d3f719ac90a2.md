# A Review On Deep Learning Application and Heath management

Date published: 08/05/2019
Status: Done
Type: Journal
Type of paper: review paper

Digital Object Identifier 10.1109/ACCESS.2019.2950985

Received October 20, 2019, accepted October 30, 2019, date of publication November 1, 2019, date of current version November 18, 2019.

# The objective:

This paper surveys recent advancements in PHM methodologies using deep learning with the aim of identifying research gaps and suggesting further improvements.

# The done job:

# the result:

The survey validates the universal applicability of deep learning to various types of input in PHM, including vibration, imagery, time-series and structured data.

It also reveals that deep learning provides a one-ﬁts-all framework for the primary PHM subﬁelds: fault detection uses either reconstruction error or stacks a binary classiﬁer on top of the network to detect anomalies; fault diagnosis typically adds a soft-max layer to perform multi-class classiﬁcation; prognosis adds a continuous regression layer to predict remaining useful life.

The general framework suggests the possibility of transfer learning
across PHM applications.

The survey reveals some common properties and identiﬁes the research gaps in
each PHM subﬁeld.

# The conclusion:

Traditional PHM applications have a fairly high technical barrier, as they require human expertise in statistics, signal processing, domain knowledge and many other skills. The most attractive specialty of deep learning is the automation of feature learning without the need for supervision. This
greatly reduces the height of the technical barrier of PHM applications.

Deep learning provides a one-ﬁts-all framework for PHM applications: 

fault detection uses reconstruction error or stacks a binary classiﬁer on top of the learned network to detect anomalies; 

fault diagnosis typically adds a soft-max layer to perform multi-class classiﬁcation; 

prognosis adds a continuous regression layer to predict remaining useful
life.

The selection of a concrete deep learning architecture is application-dependent; it mainly depends on the type of data available. The analysis in this paper may suggest how to select an appropriate deep learning architecture for a speciﬁc application scenario.

# Introduction:

Prognostics and Health Management (PHM) has emerged as a critical approach to achieving a competitive edge in many industries because of its potential for reliability, safety and cost reduction.

PHM uses measurements, models and software to perform incipient fault detection, condition assessment and failure progression prediction [1], [2].

It provides users with the ability to perceive the health state of a part, asset, subsystem or system [3]. As shown in Fig. 1, a holistic PHM framework typically incorporates data collection, data manipulation, fault detection, fault diagnosis, prognosis and decision support in sequential order [2], [4], [5].

![Untitled](A%20Review%20On%20Deep%20Learning%20Application%20and%20Heath%20ma%20f9a24bdffe844c5ea1d1d3f719ac90a2/Untitled.png)

Advances in sensor technology and Information and Communication Technologies (ICT) have led to the creation of ‘Industrial Big Data.’’ These data tend to be multi-modal, unstructured, decentralized, heterogeneous, fast-ﬂowing and highly nonlinear [16], **posing signiﬁcant challenges to traditional data-driven methods in PHM applications.**

Traditional methods also require a large number of labelled samples for training. It is hard to meet this requirement in many real-world applications where experiments are costly or even not allowed.

Many researchers have applied deep learning technologies to PHM applications. Some focus on a subﬁeld of PHM, e.g., fault diagnosis or prognosis [23], [24];

However, **none provides a comprehensive survey of the full coverage of the PHM domain from an  application perspective.**

the major problems in the ﬁeld are: **studies to various PHM subﬁelds are somewhat independent from each other**, leading to a lack of sharing of data, models and knowledge; existing researches share many commonalities, yet scholars are still reinventing the wheels; there are no guidelines on the design or selection of a ‘‘good’’ deep learning model for different applications; a uniﬁed evaluation system to different methods is still missing.

# II. DEEP LEARNING MODELS

## A. AUTO-ENCODER AND ITS VARIANTS

An auto-encoder has a feed-forward network architecture which can learn feature representations of input data without supervision. It consists of two components, i.e., an encoder and a decoder

Variants of auto-encoders include the following:

Sparse Auto-Encoder (SAE):

Denoising Auto-Encoder (DAE):

Contractive Auto-Encoder (CAE):

*For more information look at the paper.*

## B. RESTRICTED BOLTSMANN MACHINEAND ITS VARIANTS

*For more information look at the paper.*

## C. CONVOLUTIONAL NEURAL NETWORK

*For more information look at the paper.*

## D. RECURRENTNEURAL NETWORK AND ITS VARIANTS

*For more information look at the paper.*

# III. APPLICATIONS OF DEEP LEARNING IN PHM

 In the literature, most related work studies the PHM subﬁelds individually, mainly fault detection, fault diagnosis or prognosis; very few focuses on decision making. Accordingly, we organize our review into the following three subsections and categorize existing work according to the type of data input. 

## A. FAULT DETECTION

Fault detection, also called anomaly detection, aims to detect instances which deviate so much from others that they are suspected of being generated by different mechanisms [44].

Fault detection can be simpliﬁed to a binary classiﬁcation task, i.e., to classify whether the item of interest is working well or if something has gone wrong [5].

Depending on the availability of positive (faulty) samples, fault detection applications using deep learning can be grouped into two categories: supervised and unsupervised.

### 1) SUPERVISED LEARNING:

When there are enough faulty data, may not limit to a certain faulty type, a classiﬁer can be constructed to discriminate faulty from normal states.

The classiﬁer tries to learn a function, mapping from sensor measurements to their state labels with the aim of separating the two classes.

But in most real-world scenarios, data available for training have a skewed class distribution, also known as imbalanced classes, the majority of which are negative (normal samples) and a minority positive. In such circumstances, techniques like data augmentation, oversampling or under sampling and stratiﬁed cross validation should be integrated into the learning process to improve the generalization capability [45].

Some related works:

Vibration:

In fact, this is the most researched subject in PHM.

The prevailing deep learning model for vibration data is CNN.

Janssens et al. built a classiﬁer to detect bearing faults from the vibration signal [46]. In their use of CNN, the internal representation of the vibration signal was captured by two perpendicularly mounted accelerometers. They then used random forests to classify the learned high-level features. The main point is to use CNN’s capability to exploit the spatial structure in data to capture the covariance of the frequency decomposition of the data. By doing so, the model can differentiate between complex bearing conditions by learning the patterns of changes in the joint accelerometer signal.

Abdeljaber et al. used 1DCNN to detect structural damage using vibration signals [47]. They fed raw vibration signals directly to the 1D CNN model and outputted a binary label
(damaged/undamaged), forming end-to-end learning. This method allows feature engineering and classiﬁcation to be jointly trained, leading to better accuracy.

In their study, Bach-Andersen et al. ﬁrst extracted frequency domain features from the vibration data of a wind turbine drivetrain using traditional signal analysis techniques [48]. Then they down-sampled the frequency spectrum to some predetermined dimensions and fed the spectrum data to their CNN model. Though superior accuracy was reported, the hand-crafted features may not be better than the features learned from an end-to-end architecture. Similar work appears in [49].

The use of other deep learning models includes work by Luo et al. [50]. These researchers built an architecture comprised of stacked SAE and fully-connected layers to distinguish impulse responses from non-impulse responses in the vibration data of machine tools. They pretrained their SAE layers with vibration data frames in an unsupervised fashion
and ﬁnetuned the whole network using back propagation under supervision. They compared time domain, frequency domain, time-frequency domain and SAE features. SAE features were found to be more accurate and stable than traditional signal-based features in classifying the two types of responses. The results prove the value of integrating feature learning into a deep learning model.

Although vibration data are collected in the form of time series, their sampling frequency is typically signiﬁantly higher than ordinary time-series data. The source of time-series data is not restricted to one type of sensor; multiple sensors can be fused together.

One of the earliest papers using RNN for fault detection was by Hu et al. [51]. They constructed a very simple RNN architecture to model a bi-process combining software fault detection and correction; its prediction accuracy outperformed feedforward ANN.

Zhang et al. used an LSTM network to capture long-term dependencies in time-series data to detect line trip faults in a power system [52]. Taking current, voltage and active power data as the input, they built three separate LSTMs, the outputs of which were concatenated and further fed to an SVM classiﬁer.

Obst built an RNN to learn spatial-temporal correlations between sensors in a distributed wireless sensor network [53]. The residuals between actual sensor readings and the RNN
predictions were used to detect sensor faults. It is noteworthy that anomalous patterns may exist in the covariation between multiple sensors, even though each sensor signal behaves normally. Overall, the above research shows the value of data fusion.

CNN is another architecture commonly adapted for timeseries data.

Guo et al. constructed a CNN to detect faulty feeders in zero-sequence current waveform acquired from power distribution systems [54]. Interestingly, they applied continuous wavelet transform to the raw current signal and inputted the obtained time-frequency grey scale images to the CNN. They reported that accurate and robust predictions are possible with the proposed method.

Ince et al. also dealt with current signals using CNN [55]. They inputted the raw signal to a 1D CNN and stacked it with fully connected layers, similar to the method proposed in [47]. The temporal information in time-series data can be captured by a CNN because of the sliding window mechanism in its convolutional operation, and the size of the kernel may have a great impact on the length of the learnable temporal dependencies.

Imagery:

Imagery data are attracting attention in fault detection applications. As has been repeatedly proven in the ﬁeld of computer vision, CNN can achieve state-of-the-art performance in classifying imagery data.

Gibert et al. proposed using CNN to inspect railway tracks, speciﬁcally to detect
broken or missing fasteners [56]. They trained the network for two purposes: track inspection and material identiﬁcation. The multi-task learning setting allowed the knowledge learned in one task to be transferred to another (i.e., transfer learning), forming a mutually beneﬁcial mechanism.  Similar work used CNN for railway track inspection [57], road pavement crack detection [58], and concrete crack detection [59].

Video data are a composition of images along the temporal dimension. However, if its architecture is not modiﬁed, CNN is not good at encoding temporal information. Most existing research has used CNN to learn patterns from video frames, essentially images, and then model the temporal dependencies.

Chen and Jahanshahi built a CNN to detect crack patches in video frames of metallic
surfaces in a nuclear power plant [60]. Their CNN model does not encode temporal information itself, but the output forms spatiotemporal registration tubelets which can be fed to a Naïve Bayes classiﬁer to detect crack patches.

Jha et al. combined CNN and the Gaussian process to detect instable combustion behavior from high-speed grey-scale videos of a swirl-stabilized combustor [61]. They used CNN to extract features from video frames and adopted the Gaussian process to model the dynamics in the sequential images. As reported in the paper, the model generalizes better when the Gaussian process is added.

Depending on their complexity, the imagery data may not be readily fed to a CNN, outputting the desired state label. Sometimes the object of interest needs to be located in an image before classiﬁcation can take place.

Chen et al. proposed a three-stage architecture to locate and detect defective fasteners in images of a catenary support device [62]. The ﬁrst stage used the SSD (i.e., Single-Shot multi-box Detector) framework to locate cantilever joints; the second employed the YOLO (i.e., You Only Look Once) framework to locate six different fasteners, and the third used a primitive CNN to detect missing or potentially missing fasteners.

Lei and Sui used the Faster R-CNN architecture to locate and detect broken insulators and bird nests in high voltage line images [63]. It is worth noting that they reused the
pretrained ResNet-101 network, a very deep network trained for the ImageNet competition, to initialize their detection network. This strategy allows the knowledge learned in one ﬁeld to be transferred to another (i.e., transfer learning). It shortens the time for training and reduces the number of required labelled samples. We discuss this in Section IV.

Structured data:

Last but not least, structured data constitute a major source of fault detection in industry. In contrast to the abovementioned three types of data, structured data may be multi-sourced, distributed and heterogeneous, requiring considerable effort in data fusion and preprocessing. From an algorithmic perspective, structured data have been heavily
approached using conventional machine learning techniques, such as SVM, random forest, and feedforward neural network with shallow architectures. The key is to ﬁnd good feature representations that can be discriminative in separating positive from negative samples.

To this end, Chen et al. proposed a CNN-based architecture to learn deep representation of SCADA (i.e., Supervisory Control and Data Acquisition) data to detect icing accretion faults in wind turbines [64]. Their input data included 22 measurements related to wind, energy and temperature, and the output was a high-dimensional embedded feature space that could preserve within-class and between-class information while having high discriminative capability. Mandal et al. built a DBN to detect faults in a fast breeder test reactor [65]. They fed 175 thermocouple readings into the DBN and output a binary label, indicating faulty or normal. In short, complex cross-correlations between multiple sensors can be captured using deep architecture and nonlinear transformation.

The selection of deep learning models in fault detection depends on the application domain and the type of data available, but there are some common practices across models:

in model design, the backbone architecture is typically stacked with a logistic layer as the ﬁnal layer, implying that cross-entropy loss can be used.

in the learning process, regularization techniques such as dropout and weight decay are usually adopted to prevent overﬁtting, and the amount of regularization is a hyperparameter that needs to be tuned.

**precision**, **recall**, **ROC (Receiver Operating Characteristics) curve**, **AUC (Area Under the Curve)** and **F-score** are commonly used metrics to evaluate model accuracy.

### 2) UNSUPERVISED LEARNING

In an unsupervised setting, normal operating conditions are modelled beforehand, and faults are detected as deviations from the normal behaviour in a process also known as the one-class classiﬁcation problem.

Intuitively, this problem tries to learn patterns from negative samples, speciﬁcally, to ﬁnd a low dimensional embedding that can capsulize most informative features, from which the samples can be reconstructed with minimal information loss.  If a test sample cannot be well reconstructed from its feature embedding, we are tempted to doubt the normality of its generating mechanism.

unsupervised methods often spit out a continuous score representing the abnormality of a given sample. In practice, a threshold is then needed to assist judgment of the occurrence of faults.

In the following section, we survey the relevant research and organize it according to the data type:

1. Sun et al. built a model to detect defective electro-motors from vibration
signals [66]. They applied greedy layer-wise training on the cepstrograms of vibration clips of normal conditions to learn several RBMs, and then stacked them to form an encoder- decoder-like DBN architecture. Testing samples were fed into the learned DBN, and reconstruction errors between input and output were the criteria to judge their extent of abnormality.
2. Oh and Yun used an AE to detect faults in surface mounting devices using machine sound [67]. They trained the AE with normal data to retain as much information as possible in the
bottleneck layer. The residual error between a testing sample and the output of the AE, given the testing sample as the input, was the anomalous score.
3.  To shorten the time for training and putting the anomaly detector into production, Park and Yun proposed replacing the basic fully-connected layer in an AE with a stacked LSTM layer in the same application context as above [68]. Both the number of parameters in the network and the training time were signiﬁcantly cut down at the sacriﬁce of tolerable accuracy reduction.
4.  Principi et al. compared the performance of three AEs with different building blocks: a fully-connected layer (what they called MLP), a convolutional layer and an LSTM layer [69].
With meticulous tuning of the hyperparameter, they found that AEs with a fully-connected layer or an LSTM layer outperformed, in terms of accuracy, the convolutional layer and a traditional one-class SVM algorithm.

## B. FAULT DIAGNOSIS

To return to our previous analogy, being aware of our own illness is not enough; we need to consult professionals to identify the type, localize the body part and identify the severity. By the same token, once an equipment fault is detected, steps need to be taken for fault recognition, fault localization and identiﬁcation of severity, a process called fault diagnosis.

From a machine learning point of view, diagnosis is a multi-class classiﬁcation problem,

classifying a detected fault to a certain combination of fault type, location and severity.

A typical design in the deep learning architecture is the addition of a soft-max layer to the ﬁnal layer. 

cross-entropy loss is often chosen as the loss function,  based on which the network can be trained.

After training a deep learning model, nonlinear dimensionality reduction methods, such as the t-SNE method, can be adopted to visually inspect whether the learned high-level features are discriminative

Typically used evaluation metrics include accuracy, precision, recall, ROC curve, AUC and F-score.

A confusion matrix is often employed to visually investigate the classiﬁcation results, especially to locate misclassiﬁed classes. Finding misclassiﬁcations may give a hint on the direction to take to improve the accuracy.

### 1) VIBRATION DATA:

Given this, a large part of fault diagnosis research is about learning from vibration or acoustic signals.

Depending on the integration level of the learning pipeline, we divide related work into two paradigms: **separate learning** and **end-to-end learning:**

Like many conventional machine learning tasks, separate learning consists of several independent steps, including feature extraction, feature selection and pattern recognition.

End-to-end learning builds an integrated network, taking in the raw signal, extracting discriminative feature representations and outputting the desired targets.

Numerous studies have adopted signal processing techniques. The most popular one, Fast Fourier Transform (FFT), is used to extract the frequency spectrum from original time-domain signals and forward them to a deep neural network [84]–[91].

However, the process might not work well for transient or stationary signals whose frequency components vary in time, usually the case in the real world. For non-stationary signals, it is common to transform the raw signals into the time-frequency domain using Short Time Fourier Transform
(STFT) [92]–[94], Wavelet Transform (WT) [95]–[98] or Empirical Mode Decomposition (EMD) [99], [100]. STFT adopts a window function of ﬁxed length, thus suffering from the time-frequency resolution trade-off problem.

### 2) Imagery data:

Image classiﬁcation research has progressed tremendously with the recent advancements in deep learning theory, especially the development of CNN.

One seemingly intimidating obstacle to the application of fault diagnosis from imagery data is the availability of sufﬁciently labeled samples. However, this is generally not a prerequisite. With only 40 infrared thermal videos, each 10 minutes long.

Janssens et al. successfully conducted rolling-element bearing fault diagnosis by reusing the well-known pretrained VGG-16 model [137]. They simply replaced the last layer of the architecture with a soft-max layer, restricting the number of nodes to the desired output classes, and ﬁnetuned the whole network with a limited number of samples. Although their application context differed signiﬁcantly from the scenario on which the VGG-16 was originally trained, the knowledge
learned was transferrable, leading to an accuracy of more than 95%. This type of transfer learning can markedly reduce the required number of labeled samples.

Tao et al. trained a compact CNN from scratch with only 50 raw images to diagnose metallic surface
defects [139]. With the aid of data augmentation (including random rotation, translation, zoom, shear and elastic transformation) and a segmentation step prior to classiﬁcation, they successfully augmented the number of labeled training samples. As a result, their model achieved an accuracy of 86.82%, much higher than classical models based on hand-crafted features.

Depending on the complexity of a concrete problem, using a pretrained network or data augmentation techniques may not be necessary, Jia et al. trained a CNN with only  450 images per class to diagnose nine faulty states of rolling bearings, attaining nearly 100% accuracy [143].

### 3) Time-series data:

### 4) STRUCTURED DATA:

In the literature, the most commonly adopted deep learning architectures for structured data are RBM-based and AE-based,

Other researchers have endeavored to improve the classiﬁcation accuracy by combining deep learning models with other models, such as the multi-grained cascade forest [164], ﬁsher discriminative dictionary learning [165] and deep quantum neural network [166]. One commonality is they all used the deep learning model to learn feature representations and the other model to increase discriminative power.

Data may also be subject to problems like incompleteness, heterogeneity, low signal to noise ratio, exhibition of certain topology, etc.

Chen et al. attempted to conquer the incomplete data problem caused by multi-rate sampling by using transfer learning [168]. They proposed a framework enabling a portion of the structure and parameters to be transferred between the model of structurally complete data and the model of incomplete data.

Although numerous studies have validated the superiority of adopting deep learning in fault diagnosis, they are generally restricted to laboratory data, largely because of the insufﬁciency of labeled data in real-world applications where destructive experiments are costly or not allowed.

Furthermore, the learned classiﬁer may only be sensitive to those faults that are included in the training set. In other words, its generalization capability to unhappened faults may be poor, leading to low testing accuracy in the real world.

## C. PROGNOSIS:

In prognosis, we estimate the Remaining Useful Life (RUL) of the item of interest. 

In other words, it estimates the RUL of the item **taking into account its degradation trajectory and the future operational use plan.**

From a machine learning viewpoint, **prognosis is a regression problem,** as the target value (RUL) is in the real domain. Prognosis aims to learn a function that maps the condition of an item to its RUL estimates.

As in many regression tasks, it is challenging to provide labels for training. Most research uses data from run-to-failure tests, from which the RUL labels can be derived.

The simplest way to deﬁne RUL is by calculating time to failure, i.e., subtracting the timestamp of the failure occurrence from each time step;

In prognostic tasks, the ﬁnal layer of a deep learning architecture can be a single neuron with a linear activation function [170], [184]–[186] or a sigmoid function squashing the RUL prediction to a normalized range [187], [188]

Accordingly, many loss functions can be selected for training; typical ones are Mean Absolute Percentage Error (MAPE) [174], Mean Absolute Error (MAE) [180] and Mean Squared Error (MSE) [181]. **These loss functions can also be applied to evaluate model performance in a testing set.**

It has to be noted that one unique characteristic of prognostic tasks is **the penalization of late RUL predictions** (i.e., the estimated RUL is larger than the actual RUL). Late prediction may lead to unplanned breakdown, or even catastrophic damage, whereas early prediction only causes extra maintenance cost.

To cope with this problem, the following asymmetric scoring function for evaluating model performance was proposed by [189], adopted by [182], [190], [191] and modiﬁed by [192]–[194]:

![Untitled](A%20Review%20On%20Deep%20Learning%20Application%20and%20Heath%20ma%20f9a24bdffe844c5ea1d1d3f719ac90a2/Untitled%201.png)

*m: number of testing samples.*

*di: RUL_estimated - RUL_actual.*

*a1 and a2 :  controls the degree of penalty for late predictions.*

*Some related work:*

zadeh et al. proposed a spectral subtraction method to intensify fault signatures by subtracting the WPT spectrum of a signal by its steady-state part; the obtained residuals were fed to a standard CNN for tool wear estimation [186].

To better model the degradation trend, Wang et al. proposed using bidirectional GRU to capture the temporal-dependencies among the tri-domain features of the original signal [185].

Rui et al. used CNN for feature extraction and bidirectional LSTM for sequential modeling [184]. Comparisons of traditional machine learning and deep learning models, including CNN, LSTM, AE and DBN, in tool wear prediction can be found in [197].

The PHM 2008 data challenge asked researchers to predict the RUL of NASA’s turbofan engines based on multivariate time-series measurements, also known as the C-MAPSS dataset [195]. The dataset is comprised of four sub-datasets subjecting to different operating and fault conditions.

Zhang et al. studied  the transferability of the problem among different operating conditions [191]. An interesting observation was that negative transfer occurred when transferring from a dataset of multiple operating conditions to a dataset of single operating condition.

Long et al. built a k-fold ensemble model using residual CNN; this method was similar to the bagging technique in machine learning.

Zhang et al. constructed a multiple DBN ensemble to maximize two conﬂicting objectives: accuracy and diversity. Composite models using LSTM with RBM [190] and 1DCNN [176], [182] were also investigated recently, and quite competitive performance was reported.

In one of the most researched prognostic problems, the IEEE PHM 2012 data challenge works with bearing vibration data acquired from an accelerated aging platform PROGNOSTIA. It expects participants to predict the RUL of bearings whose monitoring data are truncated [196].

Although the target is different, the data type is in line with the aforementioned fault diagnosis problem using the CWRU dataset. Therefore, we provide some details of related studies in Table 2 with the aim of comparing them to those in Table 1. *see table in paper.*

After carefully scrutinizing these studies:

- A simple modiﬁcation by replacing the ﬁnal classiﬁcation layer with a regression layer can turn a diagnostic method into a prognostic one.
- This gives an opportunity to conduct transfer learning in these two closely related but different tasks.
- Another interesting observation was that all the proposed methods in Table 2 fall into the category of separate learning, not end-to-end learning.

This subsection surveys prognostic research that aims to predict the RUL of machining tools, batteries, turbofan engines and rotating bearings. After reviewing the referenced papers, we made some interesting observations:

- Compared with fault detection and diagnosis, no imagery data were used as input in prognosis tasks. This may imply that degradation process is not evident in images in some domains. It may also indicate the potential to develop imagery data-driven prognostic applications.
- While a conﬁdence bound associated with the target RUL prediction is a desirable output, very few  researchers handle the requirement properly or report their efforts sufﬁciently. This should be addressed in future studies.
- A few benchmarking datasets, such as the C-MAPSS and the PROGNOSTIA, are heavily used for the purpose of model validation. However, researchers tend to use different metrics to evaluate their models’ accuracy, making comprehensive comparisons difﬁcult. We call for a uniﬁed evaluation metric for model assessment in future studies.

Researchers agree on the importance of capturing the temporal dependencies of data in prognostic tasks.

# IV. CHALLENGES AND OPPORTUNITIES

## A. CHALLENGES

## B. OPPORTUNITIES

### 1) TRANSFER LEARNING

### 2) DATA AUGMENTATION

### 3) END-TO-END LEARNING