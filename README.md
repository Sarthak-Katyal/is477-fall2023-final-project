# is477-fall2023-final-project

## Overview
FILL ME

![Pairplot Visualization](results/iris_pairplot_visualization.png)
## Analysis
FILL ME

## Workflow
FILL ME
![Workflow Visualization](workflow_visualization_graph.png)

## Reproducing
If you would like to reproduce the contents of this project, please follow the following steps:
1. Clone this repository
2. Install Docker on your device if it has not been installed already
3. Run the following command to run all the scripts in this file:
docker run --rm -v ${PWD}:/is477 sarthakkatyal/is477-fall2023:final-project snakemake --cores 1 reproduce

## License
### Software License
I wanted a license that would allow people to easily use my software to build on their own analysis, or perhaps build on my software to create a more robust analysis. I chose the MIT License because it is simple and permissive. This means that the software I create for the length of this project can be unrestricted as long as the software is attributed to me. I like the MIT Software License specifically because it is a simple license with conditions that only require the preservation of copyright and license notices. This allows licensed works and any modifications to be distributed without the source code. The permissions on this license are commercial and private use, distribution, and modification. This also allows people to use the software and incorporate it into their closed or proprietary software, which would make it easier for them to monetize, if they wanted to do so.

### Data License
Similar to the software license, I did not want people to have a hard time accessing the data I used to conduct my analysis. This is because I would like others to have the ability to use the data I use and build on my analysis, or create some novel analysis of their own. That is why I went with the Creative Commons Attribution 4.0 (CC-BY-4.0) Data License. Unlike some of the other data licenses, this license requires attribution, but does not require share-alike. This means that anyone is free to share and adapt the data as long as they provide appropriate credit, a link to the license, and indicate if any changes were made. This license also makes sure that other people may not add legal terms or other restrictions to stop people from doing what this license permits.

## References
Fisher, R. A.. (1988). Iris. UCI Machine Learning Repository. https://doi.org/10.24432/C56C76.