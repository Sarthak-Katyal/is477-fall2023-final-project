# An Analysis of the UC Irvine Iris Dataset for IS477
## Overview
The purpose of this repository is to apply the knowledge and central concepts of IS477 through a comprehensive and end-to-end reproducible analysis of UC Irvine's Iris dataset. This dataset is composed of 5 variables (sepal length, sepal width, petal length, petal width, and class) and explores the 3 species of the Iris plant (Setosa, Virginica, Versicolor) with 50 data points per species. The dataset itself was retrieved from the UC Irvine Machine Learning Repository and is protected by a Creative Commons Attribution 4.0 International (CC-BY-4.0) License.

The purpose of this analysis was to identify differences across the variables of these 3 species and how their different measures could differentiate them. The analysis itself consisted of creating summary statistics and a pairplot and utilizing the ydata-profiling Python package to create a profiling report.

The summary statistics reveal that petal width tends to be quite small for the Iris plants while the petal length tends to be comparatively larger and more varied. The same can be said for sepal width and sepal length, although there is considerably less variability for sepals in comparison to petals. The pairplot demonstrates a positive correlation between petal length and width and no distinct correlation between sepal length and width, while illustrating the similarity in size between Iris-versicolor and Iris-virginica. The profiling report stated the class variable to be a normal distribution and illustrated that the lengths and widths variables have a high correlation with the and class variable.

## Analysis
Summary Statistics for the Dataset: 
- Sepal Length ranges from 4.30 to 7.90 with an average of 5.84 and standard deviation of 0.83
- Sepal Width ranges from 2.00 to 4.40 with an average of 3.05 and standard deviation of 0.43
- Petal Length ranges from 1.00 to 6.90 with an average of 3.76 and standard deviation of 1.76
- Petal Width ranges from 0.10 to 2.50 with an average of 1.20 and standard deviation of 0.76

These statistics reveal that petal and sepal width tends to be smaller than petal and sepal length, but petal length and width have comparatively more variability than sepal length and width. Additionally, sepals tend to be larger than petals.

The pairplot visualizes the positive correlation between petal length and width and the lack of a clear correlation between sepal length and width. It also highlights that Iris-versicolor and Iris-virginica tend to be similar in size and are larger than Iris-setosa.

The profiling report indicates there are 2 duplicate rows and zero missing values. It also says the variable class is uniformly distributed and the various lengths and widths have an overall high correlation with class.

## Workflow
![Workflow Visualization](workflow_visualization_graph.png)

## Reproducing
If you would like to reproduce the contents of this project, please follow the following steps:
1. Clone this repository
2. Install Docker on your device if it has not been installed already
3. Run the following command to run all the scripts in this file:\
docker run --rm -v ${PWD}:/is477 sarthakkatyal/is477-fall2023:final-project snakemake --cores 1 reproduce

## License
### Software License
The software license for this project is the MIT License, which was chosen because it is simple and permissive. This license only requires the preservation of copyright and license notices; it grants permission to anyone to copy, modify, merge, publish, distribute, sell, or sublicense the software. The actual copyright notice can be found in the LICENSE portion of this repository. Additionally, the MIT license can protect developers from legal liabilities since it does not provide warranties.

### Data License
The data license chosen is the Creative Commons Attribution 4.0 (CC-BY-4.0) Data License. This license requires attribution, but not share-alike. This license allows people to share and adapt the data as they would like as long as they provide the appropriate credit, a link to the license, and indicate if any changes were made. This license also ensures that others may not add legal terms or other restrictions that would stop other parties from doing what this license permits. 

This license was chosen because it facilitates collaboration and allows for easy access to data for analysis and perhaps generates novel analyses and interpretations.

## References
Fisher, R. A.. (1988). Iris. UCI Machine Learning Repository. https://doi.org/10.24432/C56C76.