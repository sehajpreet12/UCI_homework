# Plot.ly Homework - Belly Button Biodiversity
![Image](https://uci.bootcampcontent.com/UCI-Coding-Bootcamp/uci-irv-data-pt-08-2020-u-c/raw/master/02-Homework/14-Interactive-Visualizations-and-Dashboards/Instructions/Images/bacteria.jpg)
## Instructions
In this assignment, you will build an interactive dashboard to explore the Belly Button Biodiversity dataset, which catalogs the microbes that colonize human navels.
The dataset reveals that a small handful of microbial species (also called operational taxonomic units, or OTUs, in the study) were present in more than 70% of people, while the rest were relatively rare.

## Step 1: Plotly

- Use the D3 library to read in samples.json.
- Create a horizontal bar chart with a dropdown menu to display the top 10 OTUs found in that individual.

** Use sample_values as the values for the bar chart.

** Use otu_ids as the labels for the bar chart.

** Use otu_labels as the hovertext for the chart.
![image2](https://uci.bootcampcontent.com/UCI-Coding-Bootcamp/uci-irv-data-pt-08-2020-u-c/raw/master/02-Homework/14-Interactive-Visualizations-and-Dashboards/Instructions/Images/hw01.png)
- Create a bubble chart that displays each sample.

** Use otu_ids for the x values.

** Use sample_values for the y values.

** Use sample_values for the marker size.

** Use otu_ids for the marker colors.

** Use otu_labels for the text values.
![image3](https://uci.bootcampcontent.com/UCI-Coding-Bootcamp/uci-irv-data-pt-08-2020-u-c/raw/master/02-Homework/14-Interactive-Visualizations-and-Dashboards/Instructions/Images/bubble_chart.png)
- Display the sample metadata, i.e., an individual's demographic information.
- Display each key-value pair from the metadata JSON object somewhere on the page.
![image4](https://uci.bootcampcontent.com/UCI-Coding-Bootcamp/uci-irv-data-pt-08-2020-u-c/raw/master/02-Homework/14-Interactive-Visualizations-and-Dashboards/Instructions/Images/hw03.png)
- Update all of the plots any time that a new sample is selected.
## Deployment
** Deploy your app to a free static page hosting service, such as GitHub Pages. Submit the links to your deployment and your GitHub repo.
** Ensure your repository has regular commits (i.e. 20+ commits) and a thorough README.md file
## About the Data
** Hulcr, J. et al.(2012) A Jungle in There: Bacteria in Belly Buttons are Highly Diverse, but Predictable. Retrieved from: http://robdunnlab.com/projects/belly-button-biodiversity/results-and-data/
