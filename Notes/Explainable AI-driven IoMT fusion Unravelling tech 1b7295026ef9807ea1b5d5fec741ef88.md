# Explainable AI-driven IoMT fusion: Unravelling techniques, opportunities, and challenges with Explainable AI in healthcare

Author: Niyaz Ahmed Wani
Score: ⭐️⭐️⭐️
DataSet: Private
Date published: 16/05/2024
Key word: Artificial intelligence (AI), Deep Learning, Explainability, Explainable Artificial intelligence (XAI), Healthcare, Internet of medical things, Internet of things, Interpretability
Status: Not started
Task: Explainability and interpretability
Type: Journal
Journal Name: information fusion
Optimization : No
Explainability : No
Features selection : No
Muti-central Data: True
Transfer learning: No
Type of paper: systematic review
list of features: No
Mentioned: Not yet
Multimodal: No

1.3. Explainable artificial intelligence (XAI)  and internet of medical things:

- XAI  propose a shift from black box to transparent AI to address this issue by devising various ways to create more intelligible models with high accuracy.
- XAI is the ability to explain the judgment made by a black box, or internal working mechanism, in a way that a human can comprehend.
- Van Lent et al. coined the term in 2004 as “The capacity of a system/model to describe the behavior of AI-controlled entities in simulation games”.
- The output of XAI may be represented in several ways, including mathematical equations, visuals, scatter plots, etc.
- The Internet of medical things (IoMT) is a subset of the internet of things (IoT) that specifically deals with the integration and interoperability of medical equipment. It is designed to be a strong tool in the healthcare industry. Moreover, it offers exceptional prospects for gathering, examining, and sharing biological data, revolutionizing the provision of healthcare services. Medical care has become more more individualized and precise in the internet of medical things.

1.3.1. Need of explainable artificial intelligence:

1. Explain to defend.
2. Explain to control.
3. Explain to upgrade.
4. Explain to discover.

1.3.2 Explainability scope:

- Global: This form of scope aids understanding of the entire model or attempts to describe the model’s behavior as a whole on several conceivable outcome.
- Local: Individual contributions of each attribute type are given for a single occurrence in this type of explanation.

1.3.3 Trade off between accuracy and transparency:

- According to studies, explainability or interpretability diminished as one’s accuracy rate improves.
- In most  tasks, the current deep learning algorithms perform best  in prediction or accuracy, but they are the least explainable, which is unacceptable in some of their applications.
- As massive datasets become more widely available, the benefits of implementation sophisticated models become more apparent, necessitating the approximate implementation may allow for a better balanced between forecasts and explainability of more sophisticated models.
1. Explainable artificial intelligence in healthcare:
    
    Classification of the many explainable artificial intelligence techniques:
    
    1. model-based and post hoc explanations.
    2. scope-based explanations.
    3. model-related explanations.

 4.1 model-based and post hoc explanation:

1. Model-based (Ante-hoc) explanation:
    - Techniques that are easily comprehensible by design and clearly explain the connection between a model’s input and output fall into this category.
    - These are also know as translucent or white box approaches at times.
    - Example: DT, Bayesian modes, rule-based approaches, fuzzy inference system, Regression.
    
2. Post-hoc explanation:
    - These encompass the methods used on models that cannot be naturally or purposefully explained. These explanation include training a model (called a “black-box”) initially, after which explainable artificial intelligence techniques are used to provide explanation that may be local or global.

4.2 Scope related explanation:

1. Global: This explanation gives the reader a grasp of the overall correlations or logic a model has learned about how various results or outputs are produced.
    - Examples: Decision tree, Anchors, Deep-Shap, ELI5, Bayesian averaging over decision tree, Generalized Additive Models.
2. Local: Techniques that explain a single result or particular decision fall under this category of explanations. 
    - Examples: SHAP, Saliency map, counterfactual explanations, features importance

4.3 Model related explanation:

1. Model-specific explanation:
    - The methods in this category are restricted to certain type or subset of machine learning algorithms.
2. Model-agnostic explanation:
    - This explanation category is further divided into four subcategories:
        - Visualization:  Which includes surrogate models, and partial Dependence Plot.
        - Knowledge extraction: Which includes Rule extraction and model distillation
        - Influence method: features importance and layer-wise relevance propagation
        - Example based explanation: counterfactuals and prototypes.