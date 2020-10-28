## FINAL REPORT
# Aggregating Data Relating Opioid Prescriptions and Overdose Deaths

This project focused on pulling together aggregated information relating opioid prescriptions to opioid overdose deaths. Broadly speaking, painkiller overdose has been steadily rising within the United States for several years. Is there any relation of overdose deaths when compared to prescription rates? The aim of the project is to set up a useable site for a researcher to look into these two sets of data already related to each other.

## Extraction: Source 1) U.S. Opioid Prescribing Rate Maps 
(https://www.cdc.gov/drugoverdose/maps/rxrate-maps.html)

The Center for Disease Control (CDC) presents summary statistics aggregated from many health related industries throughout the country, though the raw collected data isn't available. As such, web scraping had to be performed to pull the data together in a useable analytical format. Each table of data is stored separately in different pages by year, so the web scraping script had to be performed multiple times before being collated together. As the tables themselves were stored in an HTML table, using Pandas inset ability to pull and store table data was the most sensible tool to use. Unfortunately, the last two years of tables organized their tables slightly differently and could not be aggregated together until some manual data cleanup was performed to get the tables in alignment with each other. Ultimately this was successfully put together in a single dataframe, then exported out to a consumable .csv file.

## Extraction: Source 2) VSRR Provisional Drug Overdose Death Counts
(https://healthdata.gov/dataset/vsrr-provisional-drug-overdose-death-counts)

The CDC also collates and releases data related to drug overdoses as collected from the Vital Statistics Rapid Release (VSRR) program. For the purposes of this project, deaths related to drug overdose were of primary interest. This is available in a referrable API, but a downloadable JSON containing the specific dataset is pubicly available. This data source collects information related to drug overdoses from ALL sources of drugs, not just prescription opioids. As such one of the data extraction challenges was to pull out only the specific data for opioids only. To accomplish this, JSON was ported to a consumable SQL database using a Jupyter notebook as the querying and filtering intermediary.

## Extraction: Source 3) NCHS - Drug Poisoning Mortality by State: United States
(https://catalog.data.gov/dataset/nchs-drug-poisoning-mortality-by-state-united-states-dc4ee/resource/537c480c-051a-419f-b727-336cb6930e81)

The National Center for Health Statistics collates an incredible amount of information related to death sources by state, moreso than source 2. Overall, this ended up being a more extensive version of source 2, though the source being an extensive JSON file as well, the same procedures to consume the file were applied as in source 2.

## Transformation

Once the sources were collected in a consumable format, the next task was to attempt to relate them together within a useable database. Sources were transformed into useable python dictionaries, with the intention of converting to JSON that can be referred to via Python API flask. Though the extraction process cleaned up the the majority of the datasets, some miscellaneous data that ended up being outside the scope of analysis had to be dropped. Ultimately since the datasets were a mix of qualitative and quantitative data, the transformations worked best as **semi-relational,** with some common columns between datasets available; datasets were imported into a Mongo database for ease of use. Additionally this database was designed with *flexibility* in mind (in case more and more sources would be added over time), so a non-relational database would be ideal for this task.

## Loading

Python scripts using the API Flask module were used to export the final database into browsable HTML page. **Six filtered** APIs were set up with different queries in mind, but ultimately were of the same dataset. Please see the Final Schema section for detailed breakdown. 

## Final Schema

 * state
 * state abbr
 * year
 * prescribing rate
 * sex
 * age_group
 * race_and_hispanic_origin
 * deaths
 * population
 
 *Secondary columns schema, likely not necessary for final analysis but left in if a researcher wants it*
 * crude_death_rate
 * standard_error_for_crude_rate
 * lower_confidence_limit_for_crude_rate
 * upper_confidence_limit_for_crude_rate
 * age_adjusted_rate
 * standard_error_for_age_adjusted_rate
 * lower_confidence_limit_for_age_adjusted_rate
 * upper_confidence_limit_for_age_adjusted_rate
 * state_crude_rate_in_range
 * us_crude_rate
 * us_age_adjusted_rate
 * unit
 
## Using the Database

A researcher looking to relate legal drug prescriptions against overdose deaths would be the primary user of this database. The data can be related together via State and/or year. As there is a chronological element, they would be able to analyse trends over time, or map out a heat map showing all the states related together.


