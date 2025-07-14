# Interpreting Black-Box Models: A Review on Explainable Artificial Intelligence

Author: Vikas Hassija
Date published: 24/08/2023
Key word: Black-box models, Explainable artiﬁcial intelligence, Interpretability, Machine Learning, Responsible AI, Transparency, XAI
Status: Not started
Task: Review Explainability and interpretability
Type of paper: review paper

Objective:

- Aiming to collate the current state-of-the-art in interpreting the black-box models, this study provides a comprehensive analysis of the explainable AI (XAI) models.
- Topic:
    - the development of XAI is reviewed.
    - A comprehensive and in-depth evaluation of the XAI frameworks and their efficacy to serve as a starting point of XAI for applied and theoretical researchers.
    - It highlights emerging and critical issues pertaining to XAI research to showcase major, model-specific trends for better explanation, enhanced transparency, and improved prediction accuracy.

Explainability is influencing AI:

- Model interpretability: There is a growing focus on developing AI models that are interpretable, meaning that their decision-making process can be understood and explained to users.
- Regulatory requirements: In some industries and regions, regulations are being introduced to require AI systems to be explainable in order to ensure accountability and transparency.
- Trust and adoption: Explainability can play a role in building trust in AI systems, which is crucial for their widespread adoption and use.
- Model validation: Explainability can help validate the decisions made by AI models, ensuring that they are free from biases and errors.
- Debugging and improvement: Explainability can provide insights into how AI models are making decisions, making it easier to identify and address sources of error or bias.

Why Explainability Matters:

- Humans generally look for reasoning rather than an incomprehensive description of the inner
workings of the algorithms and logic behind the decision-making process.
- Explanation fulfils the constant desire to innovate for more effective algorithms and sophisticated neural networks.

XAI Evaluation Framework:

Design principles for interactive XAI:

Adeptness to the User Behavior:

- XAI’s effectiveness depends on the degree of motivation it brings about in the user to interact with the AI.

Align Perception of XAI With Human Understandability:

- Developers should aim to involve the user in the early stages of the development process, which will ensure their active participation.

Collaborative Techniques Should Be Implemented More:

- An ideal explanation is one which incorporates expertise from multiple domains of knowledge.
- Human-computer interaction skills such as philosophy, psychology and cognitive science have proven their worth in the field of XAI by developing explanations that were able to stimulate the human explanation process.

Explanations Have More Dimensions Than Just Performance:

- They should be assessed along dimensions such as qualitative performance (satisfaction, trust and understanding), achievement of the end task, mitigation, and error analysis.
- Designers should aim at developing an evaluation benchmark that could measure the qualitative and quantitative ability of the explanations.

Contradictions Provide Alternative Approaches:

- The utilisation of contradictions and counterfactuals is termed as one of the vest practices that XAI designers need to involve in their development process.
- Utilising contradictions and counterfactuals in the design process can help ensure the diagnostic system is able to identify and handle rare or unusual cases which can be critical in medical diagnosis.
- For example, by providing the system with counterfactual examples of patients who have similar symptoms but different diagnoses, the system can learn to identify the unique characteristics that distinguish  one diagnosis from another.

Are Explanations Always Important?:

- *You have to ask* “Does the cost of getting an explanation outweigh its benefit”*.*

Amendments Go a Long Way:

- The process of making explainable AI is not one-off.
- Along with a strong foundation, necessary amendments with always help in adding more to the structure of XAI, which will lead to a greater impact.

Techniques For XAI implementation:

XAI expected to answer about  foundational questions:

- Why the model produced this prediction, and what are the logic and reasoning involved behind the model’s decisions?
- 1) Based on scope:
    
    Global Interpretability:
    
    Global interpretable approaches are intended to make it easier to comprehend a model’s overarching logic as well as the whole justification used to produce specific predictions.
    
    We categorise the various approaches to achieving explainability globally into the following subclasses:
    
    1. Model Extraction:
        - In order to properly mimic the black-box model’s judgments, model extraction entails training an interpretable model **(such as a linear model or a decision tree)** on the predictions of the black-box model.
        - The usually step followed to extract model:
            - A desirable dataset X is chosen, which may either be the same black-box model’s training dataset or a brand-new dataset with comparable distributions.
            - The trained black-box model generates predictions from the chosen dataset.
            - To fit the black-box model’s predictions, an interpretable
            model is chosen and trained on dataset X
        - Rule extraction and model distillation are the two strategies that are primarily used in the creation of model extraction algorithms.
            1. Rule Extraction:
                - One of the most popular methods for extracting models from highly complex black-box models is rule extraction.
                - 
            2. Model Distillation:
            
    2. Feature‑Based Methods:
        - Although model extraction was successful in providing global explanations of black-box models, researchers found compromised accuracy due to the oversimplification of the model complexity. **Hence, a method that could provide explanations as well as maintain the desired level of accuracy was needed.**
        - The method looking at the impact or significance of input  features into the algorithm
        - The proposed approach was further extended into two alternative paths, which were used to measure the input feature’s relevance:
            1. feature importance:
                - By calculating each feature’s contribution to the predictions, a model’s feature importance is calculated.
            2. feature interaction:
                - The impact of one feature depends on the value of the other if an AI algorithm bases a forecast on two features.
                - However, one potential disadvantage of this approach is that it may be computationally expensive, as it requires training and evaluating multiple models. Another disadvantage is that the approach may struggle with handling complex models, especially those with many variables or non-linear relationships.
                - The success of this work for explainability depends on the specific context and application. For some datasets and problems, this approach may provide more accurate and trustworthy explanations than other methods [110, 111].
    
    Local interpretability:
    
    - Local interpretability focuses on providing explanations separately for each choice and prediction rather than providing a detailed description of the intricate mechanism underlying the entire black-box model.
    - In these models, each input feature is associated with a weight, and the final prediction is made by taking the dot product of the input features and their corresponding weights plus a bias term. This means that the importance of each input feature can be easily determined by looking at the corresponding weight. Additionally, it is possible to understand the impact of a specific feature by holding all other features constant and varying the feature of interest.
- 2) Stage Based:
    - Ante‑Hoc Interpretability:
        - Ante Hoc interpretability techniques mostly consist of traditional AI practices. Designed with the idea of keeping an uncomplicated structure so that complexity is limited
        to a certain extent, such techniques are termed glass box techniques.
        - Intrinsic:
    - Post Hoc:
        
        Contradictory to ante hoc methods, post hoc interpretability refers to the class of techniques which involve the research and development of black-box models post their training.
        
        - Model specific :
        - Model Agnostic:
- 3) Example Based:
    
    Counterfactual:
    
    Influential Instances:
    
    Adversarial:
    
    Prototype-Criticism:
    

Quote:

- Human beings have been defeated for the first time in related open challenges
[3] (e.g., ImageNet image-classification [4], COCO object-detection [5]) since the introduction of AlexNet [6].
- One of the significant milestones was witnessed in 2016 when an AI player AlphaGo [9, 10], was
able to defeat the human world champion Sedol Lee in a game of Go.
- Consequently, the proliferation of AI has made people think, “How comfortable are we trusting blindly on these AI-generated predictions and results? Who will be held accountable when things go wrong?”
- It is essential to note that the highly efficient predictions of AI models are derived from Deep Neural Networks (DNNs) which originate from extremely complex non-linear statistical models and innumerable parameters, thus compromising the aforementioned algorithms’ transparency [16, 17]. Due to this, AI algorithms suffer from opacity i.e., the situation in which a system is unable to offer any reason or suitable explanation involved behind its decisions, commonly
referred to as “the black-box problem.” A black-box nature is poorly understandable by humans. Entrusting crucial decisions to a black-box model creates a necessary need for
AI algorithms to be explainable for their decision-making process [18].
- The topic of how to explain ML predictions has generated a lot of discussions [19]
- explainable artificial intelligence (XAI). The field seeks to develop AI systems that not only provide accurate predictions but also provide explicit and interpretable explanations for their decisions and actions, thereby making them more trustworthy for human users.
- XAI aims to equip engineers with extensive resources to understand the elusive black-box nature of AI, emphasising transparency and the interpretability of AI models employed to reach conclusions. [20].
- A black-box model in XAI refers to a machine learning model that operates as an opaque system where the internal workings of the model are not easily accessible or interpretable.
- This lack of transparency makes it strenuous for users to understand the model’s behavior, detect potential biases or errors, or hold the model accountable for its decisions.
- When ML models are utilised in a product, interpretable systems are frequently a decisive element.
- **In machine learning, interpretability is a crucial component. Nevertheless, it is still unclear how to quantify it.** Because of this ambiguity, academics frequently conflate the terms “interpretability” and “explainability.”
- **An incorrect prediction’s interpretation aids in determining its root cause.**
- SHAP is a procedure that can be applied to any machine learning model in order to provide
explanations for specific predictions.
- Using SHAP, the researchers were able to identify the most influential factors influencing the model’s predictions for each patient.
- **By providing these explanations to clinicians, the researchers hoped to increase the accuracy and reliability of the model’s predictions and to identify potential errors or biases in the underlying data.**
- With approximately 70% accuracy, the interpretable version of the model was able to identify patients who were more likely to benefit from escitalopram.
- Using readily understandable and explainable features can make the model more interpretable, whereas using complex or abstract features can make it more challenging to comprehend.
- Humans generally look for reasoning
rather than an incomprehensive description of the inner
workings of the algorithms and logic behind the decision-
making process.
- **It is important to note that interpretability and explainability are challenging and active areas of research, and there is no one-size-fits-all solution. The effectiveness and success of any interpretability method will depend on the specific context and**
- In XAI, KNN can be considered an interpretable algorithm as it provides a clear explanation for its predictions.