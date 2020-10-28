# ETL Proposal
Aggregating data regarding opiate prescriptions from multiple sources, primarily comparing number of prescriptions vs. overdose cases or overdose deaths.
Data should be relatable by both State as well as year.

## Project Work breakdown by File Order
 * Readme.md (you are here)
 1. opioid_prescription_webscrape.ipynb (extraction source 1)
 2. ETL_Project.ipynb (extraction source 2)
 3. Transformation_PartII.ipynb (extraction source 3)
 4. Transformation_PartIII.ipynb (transformation)
 5. DrugDetails.py (Loading part 1)
 6. DrugPrescription.py (Loading part 2, sets up html page)
 7. Final Report.md (Final report)



# Rice-Boot-Camp-ETL-Project
Rice-Boot-Camp-ETL Project

Considerations regarding proposal:
- A link to your team’s github repo
- Datasets you intend to use
- What useful investigation could be done with the final database
- Whether final database will be relational or non-relational. Why?



# PROJECT REQUIREMENTS
Data Sources:
- At least 2 (or more) sources
  * Source 1: https://healthdata.gov/dataset/vsrr-provisional-drug-overdose-death-counts (JSON format available, satisfies API requirement)
  * ~~Source 2: https://www.kaggle.com/apryor6/us-opiate-prescriptions~~ Deemed redundant and replaced
  * Source 2: https://www.cdc.gov/drugoverdose/maps/rxrate-maps.html (data is presented in web tables, will have to perform webscraping to solve)
  * Source 3: https://catalog.data.gov/dataset/nchs-drug-poisoning-mortality-by-state-united-states-dc4ee/resource/537c480c-051a-419f-b727-336cb6930e81 
- If possible, try to incorporate a web API as one of your data sources.
  > Source 1 is available as an API, but downloading the JSON should be fine?
ETL Process:
- Within Jupyter, build out the ETL process to extract your data from their sources, apply some level of transformation, and
load the resulting data to a database (relational or non-relational)
  > Generic steps to perform with the data sources that we have collated so far:
  > 1) aggregate data by state
  > 2) drop any non-useful columns
  > 3) combine data sources based on a common key (state?)
  > Final database will likely be relational

Flask API:
- Build a Flask application that has a route that will execute a query to your database and return the results in JSON format.
Final Report:
- Write up a short report that details your 3 ETL steps.
- More details on a later slide.
Github Repo:
- Store all of your project files in a well-organized project repository
- Each member of your team will submit a link to your project repo to BCS by the end of class Tuesday



FINAL REPORT REQUIREMENTS
-What data sources you chose, and why?
-Detailing the process of the extraction, transformation, and loading steps
- Explain why you have performed the types of transformation you did
- Why you chose the type of final database
- Schema of the tables/collections in the final database
- Hypothetical use case(s) for your database

Questions to consider in your ETL
- Is my data redundant?
- Is there a way to normalize this data?
- Can I accomplish the same thing with less code?
- Is my code maintainable? If I let someone else read it, would they
understand it?
- Why would someone want to use my final dataset?

