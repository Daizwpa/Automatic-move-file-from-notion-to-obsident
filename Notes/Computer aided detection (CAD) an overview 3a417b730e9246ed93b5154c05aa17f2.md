# Computer aided detection (CAD): an overview

Author: Ronald A Castellino
Date published: 13/04/2005
Key word: Breast cancer, Computer aided detection, Computer-aided diagnosis (CAD), lung cancer, observational oversights
Status: In progress
Type: Journal
Type of paper: review paper

Abstraction:

Computer aided detection (CAD) is a technology designed to decrease observational oversights—and thus the false negative rates—of physicians interpreting medical images. Prospective clinical studies have demonstrated an increase in breast cancer detection with CAD assistance. This overview brieﬂy describes the metrics that have been used to deﬁne CAD system performance.

what is CAD system:

As used in this overview, the term ‘computer-aided detection’ refers to pattern recognition software that identiﬁes suspicious features on the image and brings them to the attention of the radiologist, in order to decrease false negative readings.

How radiologists use CAD system:

The radiologist ﬁrst reviews the exam, then activates the CAD software and re-evaluates the CAD-marked areas of concern before issuing the ﬁnal report.

Different between Computer aided detection vs Computer aided diagnosis:

Computer aided diagnosis refers to software that analyses a radiographic ﬁnding to estimate the likelihood that the feature represents a speciﬁc disease process (e.g. benign versus malignant).

Objective this article:

in some applications CAD, with its associated automated software tools, has the potential to provide workﬂow efﬁciencies. This latter application is beyond the scope of this overview.

Clinical implementation of CAD:

In current practice (and as required by the FDA), the exam should ﬁrst be reviewed and interpreted in the usual fashion. Only then are the CAD marks displayed, following which the radiologist re-reviews those areas that are prompted by the CAD system.

How to evaluate a CAD system:

A CAD system can be evaluated in several ways, which includes analysis of data generated in a laboratory or test setting, and by the impact of CAD on radiologist performance in an actual clinical practice setting.

‘Stand alone’ sensitivity and speciﬁcity:

This information can be obtained by observing the
performance of a CAD system on a set of ‘truth’ cases.

Sensitivity is determined by the percentage of positive cases in which the CAD system places a mark on the disease location. *= TP/(TP+FP).*

The number of false CAD marks per normal image or case is commonly used as a surrogate for speciﬁcity. *= TP/(TP+FN)*

The results of this exercise are, of course, dependent on the case collection. Bias, intended or not, in collecting positive cases that have more conspicuous ﬁndings will result in apparent superior CAD performance compared to cases that are less conspicuous, even though the
CAD algorithm is the same. Thus, the same CAD algorithm will demonstrate varying sensitivities and speciﬁcities (false marks per case) depending on the case composition.

**A preferred method to compare CAD systems is to determine the sensitivity and false marker rates on the same set of ‘truth’ cases. These cases must be ‘unknown’ to the CAD system**, that is, they should not have been used to train the CAD algorithms. Sufﬁcient
(and often large) numbers of cases will be needed in order to establish **statistical signiﬁcance** of superiority or equivalence in performance when comparing CAD systems.

‘Laboratory’ studies of potential detection improvement:

These studies recruit radiologists (or other ‘readers’)
to evaluate a set of ‘truth’ cases to determine the
sensitivity and call back rate of the unaided reader (pre-
CAD) with that of the reader with CAD assistance.
Such studies are useful to assess the potential beneﬁt
of CAD and provide estimates of expected changes in
disease detection and workup/recall rates. However, the
test setting often compromises the performance of the
reader, in that the reader may either over or under call
the reviewed cases in a test environment.