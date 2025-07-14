# Data and model aggregation for radiomics applications: Emerging trend and open challenges

Author: Antonella Guzzo
Score: ⭐️⭐️⭐️⭐️⭐️
Key word: Data fusion, Federated learning, Model fusion, Radiomics, forward feature selection
Status: Not started
Task: radiomics review
Journal Name: information fusion indexed in science direct
Type of paper: tool review

Objective:

- What Information Fusion methods and techniques have been
adopted in the last 5 for years for the Radiomics applications?
- How to categorize the process of Fusion that are performed
in Radiomic and which kind of such processes were subject to
more attention in the literature?
- What are the main challenges in Information Fusion when
applied to the Radiomic domain?

Task:

- talk about radiomics pipeline
- talk about issue of radiomics

Radiomics issue:

- The first critical issue originates from the fact that there is no standard method for image acquisition.
- The second critical issue is related to the segmentation step, which is focused on identifying which parts of an image have to be further analyzed to extract meaningful and useful information.
- 

Quote:

- The term of radiomics was first introduced in 2012 by [3] as a set of combined methods aim at quantifying major diseases such as tumors by extracting many quantitative features from available medical images. Differently from traditional imaging research that mainly extract morphological features of tumors qualitatively and semi-quantitatively, these methods over time have proven to be more effective in predicting the heterogeneity of tumors [4–6].
- Radiomics is in particular very popular nowadays in the field of
oncology. Approaches based on Artificial Intelligence tools and methods have been proven to be quite effective in this context, by enabling advanced forms of diagnostic/prognostic approaches with the ability of precisely characterizing a number of multifaced pathophysiological processes, ranging from oncological to cardiac and other diseases [7]. **In fact, specialized algorithms can provide unforeseen and useful information from medical images. For instance, single biopsy-based molecular and histological analysis does not suffice for conducting spatial/temporal assessments, and multiple biopsies are needed to check for some supposed prostate malignancy. Advanced approaches to medical imaging could, instead, provide valuable information by** non-invasive examination, even following a longitudinal observation in presence/absence of therapeutic interventions that change truthfully tumor biology bulk (delta-radiomics) [8,9].

- Moreover, it is straightforward to share a huge amount of data among numerous institutes to
translate radiomics from bench (imaging research) to bedside (patients application).

- when dealing with images coming from different devices or different manufacturers (using different acquisition and reconstruction techniques [24]), if images have to be analyzed numerically/algorithmically to extract meaningful and relevant data, it is easy to envisage that even small variations in the acquisition chain can lead to introduce bias that can lead to undesired result [1].
- the ‘‘black box’’ approach which characterize Deep Learning algorithms, that is, the fact that the models learned via these algorithms are not suited for human inspection and they are typically not interpretable, is an important point that limits their practical applicability.
- these methods provide high accuracy values and are able to extract all relevant features from the diagnostic data, including those that the naked eye of the greatest expert cannot see [26].
- Deep Learning approaches typically require very large datasets for training and testing. If this could be a secondary issue in many application domains (such as insurance companies, sales, or customer relationship management), in the case of healthcare there are obvious limitations to share data because of privacy regulamentation and requirements.
- Up to now, most of the studies in the literature about radiomics have been carried out in a single institutional structure, which was mandatory in order not to run into legal, ethical, administrative and technical problems. However, if a radiomics model is trained by considering training sets that belong to a single legal entity, then the quality of the model might be rather poor because it might lack the ability to generalize over other settings, by incurring in overfitting [26].