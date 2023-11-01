# Data Skills 2: Homework 3 - Data Visualization
### Due Tuesday November 7th before midnight

## Part 1 (50%): Line Plot

__1a)__ Go back to homework 1, and copy/paste your code for loading the BLS data (ssamatab1.xlsx) into this assignment. Modify the code to work here and to keep the "Area FIPS Code" column. Pause to reflect on this process - was it easy to copy all of your code over? Was the way you organized it in HW1 condusive to reuse and making this small change, or did it require extra work? Then, filter the data so only observations for 2005 remain, and create a column of datetime objects.

__1b)__ Load the final csv document from homework 2 provided in this repo - I have added a column to it listing FIPS codes for (most of) the MSAs. As we saw in previous assignments, merging on strings, while sometimes necessary, can also be a pain to get right! Fortunately, a lot of geographies do come with codes for matching, which we will use here. Merge this data with the data created in 1a using the FIPS codes, so each row is unique by MSA\Date, and you've added one new column - 'direct' to the four from the first part. Discard the other columns from the BRAC table (the direct column sums all of the other direct impact columns into one value).

__1c)__ Create a figure to explore this data using MatPlotLib, Seaborn, and/or Pandas. The goal is to create a line graph that has the date on the x-axis, and the unemployment rate on the y-axis.

The graph should have three lines; one for MSAs that had net gains from the 2005 BRAC round, one for MSAs that had net losses, and one for MSAs with no gains or losses. Aggregate the MSA-level data into these three groups using the mean value. Make sure your plot clearly displays the data, including using good axis labels, titles, colors and a legend.  

Add two vertical lines, one in May and one in September. Create annotations on the plot for each line, the first saying "BRAC start" and the second saying "BRAC end". Save your figure as hw3q1.png and commit it with your code.

Finally, imagine that you are now trying to apply this analysis to other BRAC rounds (there were in fact four others in 1988, 1991, 1993, and 1995). We will not be working with this data, but you should work on generalizing your function so that it could generate the same plot for data from other years, assuming that data was in the same format as the 2005 data.

__Ungraded exercise:__ Think about how you would interpret/explain this graph based on the fact that the direct military base closures and job losses do not begin for at least 6 months to 1 year from the end of the BRAC process. You do not have to write anything on this point to include with your assignment.


## Part 2 (50%): Choropleth

Our goal now is to create a spatial mapping show the direct affects of BRAC in the US.  To do this, download the MSA Shapefile Zip File directly from:

https://www2.census.gov/geo/tiger/TIGER2019/CBSA/tl_2019_us_cbsa.zip

And the state State shapefiles directly from this link:

https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_state_5m.zip

Unzip them and load these two shapefiles using geopandas.

Merge your BRAC dataframe from part 1b above (not the version merged with the BLS data) into the MSA shapefile. Unfortunately the shapefiles are using some new FIPS codes, while our BLS and BRAC data have old ones! Use the old_new dictionary below that I assembled for you to update the BRAC msa fips codes. Once you apply it, all of the observations from the BRAC data should merge. Keep only the MSAs in your geodataframe that have data from the BRAC direct affects.

From the state geodataframe, drop all places by NAME that are not part of the continental US (Alaska, Hawaii, territories except Washington DC - feel free to ask if you aren't sure which places in this list are territories, but all of them will show up in a choropleth as disconnected from the mainland).

Then plot the states with black edges and a white fill. Add to that figure the MSAs that have BRAC effects, colored by how positive or negative the effect is. Clean up your figure, label it appropriately, and save it as hw3q2.png and commit it with your code.

And finally, create a .gitignore file that excludes your shapefile folders and any zip files from being committed to your repo. Commit the .gitignore file to your repo, while making sure the shapefile data is not uploaded,  because they tend to slow things down a lot!

__EXTRA CREDIT:__ You can gain 5 percentage points (for a maximum score of 105% on the assignment) if, instead of dropping Alaska, Hawaii, and Puerto Rico, you create a figure that has one large subplot for the continental US, and three smaller subplots, one each for those four locations.  Correctly map the MSA BRAC values onto all four subplots.
