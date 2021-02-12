Data sources

Analyzing population density in the various neighborhoods of Toronto

From https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M we could create a database which was grouped by the postal code and listed all the neighborhoods according to the postal code: starting from M1A to M9Z.

Then http://cocl.us/Geospatial_data allow us to add information regarding the latitude and longitude of each Postal code to our data frame.

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

And then map these data onto the postal code associated with each neighborhood

An explanation of the methodologies to extract the data, clean it, preprocess it and model it will be provided in the ipython notebooks for the solution


