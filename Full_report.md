# Full Report

## Chapter 1: Introduction
## Chapter 2: Data
## Chapter 3: Methodology
## Chapter 4: Results
## Chapter 5: Discussion
## Chapter 6: Conclusion


# Introduction

The question city planners and municipal bodies often ask is: Why do people want to live in certain neighborhoods? That can make planning and development of cities more holistic and sustainable. 

Economic opportunities in the area, availability of residential locations, professional and educational opportunities all seem like great candidates determining the sustained popularity of a neighborhood. Some of these factors include a number of aspects. For example, residence could be owned or rented. Or average income of a neighborhood may be a factor in people staying in a location due to higher overall quality of life or people moving away due to excessive rents. Existing population density could be a draw or a put off for a neighborhood. 

Here we try to understand using a framework as simple as possible, if we can predict the population density and change in population (people moving in or out of neighborhoods) based on some of these factors.

For the clustering of neighborhoods in Toronto we already collected and organized data on the neighborhoods of Toronto, grouped by their postal code and we added information regarding their location.

I have used Foursquare data on venues to collect the number of venues in broad categories for each postal code. These broad categories are:

•    Professional
•    Food
•    Shops
•    Arts
•    Travel
•    Outdoor
•    Residential
       
The number of venues in each such category in a postal code gives us some information regarding the location and its suitability for people living there.

In addition, we need other population metrics. These are: population density, average income of people living there, fraction of people that rent or commute to work etc. For this information me use:

https://en.wikipedia.org/wiki/Demographics_of_Toronto_neighbourhoods


With this collocated data, we proceed to understand the population statistics of the different neighborhoods.

Finally, we use some of these factors to model the population density and whether people tend to move in or out of these neighborhoods.

Further exploration of the data is provided in the “Data_sources.md” file.


# Data

Analyzing population density in the various neighborhoods of Toronto

From https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M we could create a database which was grouped by the postal code and listed all the neighborhoods according to the postal code: starting from M1A to M9Z.

Then http://cocl.us/Geospatial_data allows us to add information regarding the latitude and longitude of each Postal code to our data frame.

With FS, I can explore venues listed in a postal code by its geographical location and its approximate radius (approximated using its area). These venues are then categorized broadly into:

•    Professional
•    Food
•    Shops
•    Arts
•    Travel
•    Outdoor
•    Residential

These categories provide a comprehensive view of the economic, residential, and entertainment opportunities in a neighborhood.

Finally, I need to understand the population dynamics of a postal code. I employ population data such as population density, average income of people living there, fraction of people that rent or commute to work etc. from https://en.wikipedia.org/wiki/Demographics_of_Toronto_neighbourhoods

And then map these data onto the postal code associated with each neighborhood.

The methodologies to extract the data, clean it, preprocess it and model it are presented next.


# Methodology

We start with the same approach as when we were clustering the neighborhoods. Using the neighbourhood information with the location information allows us to create a database of postal codes with assoicated neighborhoods and their geographical location.

Next we want more location information from https://en.wikipedia.org/wiki/Demographics_of_Toronto_neighbourhoods 

Extracting the tables from this webpage allows us to access information such as population density, average income of people living there, fraction of people that rent or commute to work etc for each neighborhood. Please note quantities such as population density are not additive in the sense that the Population density of the post code is not the sum of Population densities of the associated neighborhoods. Hence we calculate variables where the value for the postal code is equal to the sum of values from the nieghborhoods included in it.

## Grouping 
We transform average income to total neighbor hood income, % change in population (from 2001 to 2006) to absolute change in population,  % commuting to total commuting and  % renting to total people renting. These new variables can now be grouped by postal code. Finally once we have the values by postal code and values of total area and total population associated with the postal code, we can calculate these variable back for the postal code.

Finally we have a table which list postal codes with its associated latittude and longitude and its area along with other information.

## Leveraging Foursquare information per postal code
The latitude, longitude and area of a postal code (transformed to "radius" by assuming a circular area) is then used to explore the venues in that region. Setting the limit to 50 in the FS API call is enough to show all the venues associated with each postal code. These venues are classified according to Foursquares own classification system. These categories are:

•    Professional
•    Food
•    Shops
•    Arts
•    Travel
•    Outdoor
•    Residential
 
Events, Nightlife and College and Universities are excluded as many postal codes had neighborhoods with no such data. 
 
Knowing the venues associated with the postal code allows us to count the number of venues in that region associated with each of the categories. Since we want to model area-averaged quantitites like Population density and whther people move in or out, we need to area-average the number of venues in each postal code. The reason is it would not be fair to use a large neighborhood's number of Food places to a small neighborhoods ones without taking their respective areas into account. 
 
Finally, we want to know the distance of each postal code from downtown. For this, we calculate the average latitude and longitude of all neighbourhoods associated with downtown and use this along with the information that 1 latitude is approximately equal to 111km and 1 longitude is approximately equal to 80 km (at Toronto) to calculate the approximate distance to downtown.
 
Hence, we have the following variables for each postal code:
 
Location variable : distance to downtown
 
Relevant population variables: Population density, Average Income, Population change from 2001 to 2006, Ratio of people commuting, Ratio of people renting, 

Relevant venues: Area-averaged number of venues: "Professional", "Food","Shops","Arts","Travel","Outdoor","Residential"

Since, the idea here is to predict and not find the best model, issues such as multicollinearity (one feature variable depending on another feature variable) are nt critically important.

# Results

We want to explore the factors that play into the popularity of neighborhoods. We approach this problem from two aspects: a) modeling the population density of a postal code ( its associate neighborhoods) by other population and socio-economic factors, and b) modeling whether people move in or out of neighborhoods (comparing 2001 to 2006: the data that we have)

## Part1: Modeling Population density
As an overview, the correlation between population density and many factors were found to be substantial (magnitude >0.6)

This allows us to build a model using Python statsmodel library trying to fit a linear model (ordinary least squares). The target is the "Population density" and the fearures are number of venues divided by the area of the postal code for categories: 'Travel', 'Outdoors', 'Food', 'Arts','Shops', 'Residence', 'Professional', geographical distance to downtown ('Distance_to_Downtown [Km]')',ratio of people commuting and renting ('Ratio_commuting', 'Ratio_renting'), other resident attributes ('Average_income','Population_change_ratio')

A large amount of variance can be explained by the model (above 95 %). The coefficients are statistically significantly (at 0.05 level of significance) over zero for a number of features. 

The model suffers from multicolinearity (i.e some features depend on each other). However, since we want the model to PREDICT and not to find the best model, we used scikit-learn to fit the training data (target to the full set of features). Upon testing it for the testing data we have a quite high explained variance score of above 85 %. This means the features we selected do a decent job in predicting the population density.

## Part2: Do people move in or out of the postal code?

This is trying to model whether people move in or out of the neighborhoods based on its features. Thus, it is a binary classification problem. We try to model whether people moved in or out into the neighborhood between 2001 and 2006. We use KNN first (after standardizing the data in order to allow for fair groupings) and see that it is not much different from random chance (predicts correctly around 0.6, but has a very wide standard error). Logistic regression turns out to the best classification algorithms in this case (Decision tree being similar and SVN being too slow) with a consistent accurcy of ~ 70% for the test dataset.

# Conclusion

The purpose of this project is to try to answer the question: why do people live in or move out of different city neighborhoods? We try to answer this question for the postal codes and the associated neighborhoods on Toronto. Geographical, population, and socio-economic factors were taken into account. While the geographical and population data could be scraped from wikipedia webpages, the socio-economic data (venues of different categories) is accessed from Foursquare using API calls. The question is divided into two sub questions. First, can we model the population density of a postal code from its other attributes? It turns out we can model this reasonably well using multiple linear regression. The second question is: can we predict whether people will move in or out of neighborhoods. This problem, for this dataset is not so straightforward.


