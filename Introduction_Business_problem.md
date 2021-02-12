Introduction/ Business Problem

The question city planners and municipal bodies often ask is: Why do people want to live in certain neighborhoods? That can make planning and develolment of cities more holistic and sustainable. 

Economic opportunities in the area, availability of residential locations, professional and educational opportunities all seem like great candidates determining the sustained popularity of a neighborhood. Some of these factors include a number of aspects. For example, residence could be owned or rented. Or average income of a neighborhood may be a factor in people staying in a location due to higher overall quality of life or people moving away due to excessive rents. Existing population density could be a draw or a put off for a neighborhood. 

Here I try to understand using a framework as simple as possible, if we can predict the population density and change in population (people moving in or out of neighborhoods) based on some of these factors.

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


