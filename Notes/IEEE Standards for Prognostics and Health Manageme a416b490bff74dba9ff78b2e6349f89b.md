# IEEE Standards for Prognostics and Health Management

Date published: 17/09/2008
Status: Done
Type: Journal
Type of paper: review paper

IEEE AUTOTESTCON 2008
Salt Lake City, UT, 8-11 September 2008

# The reason:

Recently, operators of complex systems such as aircraft, power plants, and networks, have been emphasizing the need for online health monitoring for purposes of maximizing operational
availability and safety. The discipline of prognostics and health management (PHM) is being formalized to address the information management and prediction requirements
for addressing these needs.

# The Objective:

In this paper, we will explore how standards currently under development within the IEEE can be used to support PHM applications. Particular emphasis will be placed on the role of PHM and PHM-related standards with Department of Defense (DOD) automatic test systems-related research.

The focus of this paper is on applying the AI-ESTATE and SIMICA standards in PHM systems. 

# The Conclusion:

Two of the primary reasons for standardization are to reduce cost by improving interoperability and minimize repeated design of similar system.

The IEEE SCC20 standards focus on promoting information interoperability between components of a test or health monitoring system.

Technological advances in CBM and PHM have identified core types of information needed for health monitoring systems. What we have found is that there is a strong overlap between the type of information needed for health monitoring and the type of information used in traditional diagnosis. Therefore, the IEEE has been working to identify and expand  its existing test and diagnostic standard to address PHM requirements.

# The introduction:

the IEEE approved a project authorization request (PAR) for SCC20 to develop a new standard focusing on diagnostic systems that use techniques from the maturing field of artificial intelligence

PHM has been defined as “a maintenance and asset management approach utilizing signals, measurements, models, and algorithms to detect, assess, and track degraded health, and to predict failure progression [1].”

The focus of this paper is on applying the AI-ESTATE and SIMICA standards in PHM systems. The discussion in this paper highlights the recent results in developing these standards and focuses on how they can be used to satisfy PHM information management requirements.

# APPROACHES TO PHM

When building a PHM system, three components are necessary for prognostics to be effective (which are highlighted in Figure 1)—the ability to estimate the current state of the system, the ability to predict future state, and thereby time to fail, and the ability to determine the impact of the assessment on system performance and the need for corrective or mitigating action. In all three cases, system-specific models must also be provided. In support of these components, several approaches are being applied.

![Untitled](IEEE%20Standards%20for%20Prognostics%20and%20Health%20Manageme%20a416b490bff74dba9ff78b2e6349f89b/Untitled.png)

Physics Model-Based Methods:

POF methods focus on issues such as material deformation, fracture, fatigue, and material loss.

Perhaps the most effective method in terms of high-fidelity prediction of system degradation

Computationally prohibitive.

POF methods depend on high-resolution models but do not scale well.

Reliability-Based Methods:

Perhaps the simplest approach to predicting failure is based on statistical reliability models of component failure.

Recall that reliability is defined as the probability that a component or unit will be functioning at time t [8].

reliability predictions are used to estimate future failure based on current test results by applying a probability distribution such as the exponential distribution (i.e., P(Di) = 1 – exp[–λit]). 

One of the principal shortcomings of using the exponential distribution is that it imposes a “Markov” assumption, meaning that the future prediction of a failure is independent of the history of the unit given the current measurement.

Given the strength of this assumption, alternative reliability methods have applied the Weibull distribution for the predictions since it relaxes the assumption of constant failure rates as well as the Markov assumption [9].

Do not handle idiosyncrasies of specific systems

Data-Driven Methods:

data-driven methods such as regression models [10], time series analysis [11], and neural networks [12] are being applied. Each offer an advantage of being able to learn models based on empirical data but also suffer from the inability to learn portions of the model where no such data exists.

Probability-Based Method:

Lessons drawn from signal  processing, target tracking, and state estimation have
identified a number of probabilistic models showing promise for PHM.

Specifically dynamic Bayesian network (DBN) architectures such as hidden Markov models (HMM) [13] and Kalman filters [11] have been suggested as methods for using historical, sequential data to predict future failure.

General Note:

prognosis is an extension of fault or failure diagnosis. In addition, given the fact prognosis attempts to anticipate and predict impending failure.

the IEEE Standards Coordinating Committee 20 on Test and Diagnosis for Electronic Systems include the Signal and Test Definition standard [18], the Automatic Test Markup Language (ATML) family of standards [19], the AI-ESTATE standard [20], and the SIMICA standards [21]. Of particular interest to us are the AI-ESTATE and SIMICA standards. Within the SIMICA family are two additional standards—Test Results [22] and Maintenance Action Information [23].