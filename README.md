# Race, Faces, and Fairness
## Gender and Race Disparity in Commerical Face Recognition Systems
"Race, Faces, and Fairness" was my final project for the Spring 2019 course "Proseminar in Audiovisual Machine Learning" at Wesleyan's Quantitative Analysis Center, taught by Jielu Yao. 

This repository holds the code and paper submitted for completion of the course. The summary notebook is located at `code/rff_analysis.ipynb`.

The inspiration for this work includes both my work in using data science to breakdown racial disparities in criminal justice, as well as the work done by the Algorithmic Justice League.

My intention is to archive and document my work, as well as to establish the foundation for which I will continue using data and computer science to research social inequity. 

## Abstract
Recent literature concerning artificial intelligence demon-
strate that machine learning algorithms have race and gen-
der discrimination. In this work, we conduct a status quo
check by evaluating two commercial gender classification
systems - Amazon Rekognition and Sightengine - using the
large-scale UTKFace Dataset to ascertain intersectional
gender and race disparities in these systems, i.e. if these
systems can accurately identify the perceived gender of
a labelled Asian, Black, or White face. Our results show
that both of these classification systems exhibit bias towards
non-white female faces, assigning disproportionately higher
male confidence values. We also observe frequent errors in
both classifiers identifying non-white male faces, with either
higher-than-normal female confidence values assigned or
the classifier not even being able to identify a face. By audit-
ing these two classifiers with an intersectional approach, we
hope to pinpoint precise flaws and identify what ought to be
corrected in machine learning algorithms in the future.