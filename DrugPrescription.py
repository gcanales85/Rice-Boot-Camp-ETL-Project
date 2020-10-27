#import modules

import pymongo
import pandas as pd


# a method to pull all the data from the database
def AllPrescriptionStatistics():

    #establish a client to mongodb server
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    # connect to opioid database
    db = client.opioidabuse_db

    # map to collections
    prescriptionCollection = db.opioidabuse_prescription
    populationCollection = db.opioidabuse

    # filter the data from collections
    prescriptions = prescriptionCollection.find()
    population = populationCollection.find()

    #convert the collection to data frame
    prescriptionsDF = pd.DataFrame(list(prescriptions))
    populationDF = pd.DataFrame(list(population))
   
    
    #merge the Crime data and housing census data
    mergedDF = pd.merge(prescriptionsDF, populationDF, on = ['state', 'year'], how='inner' )
    
    # select the columns for output
    outputDF = mergedDF[['state', 'state abbr', 'year', 'prescribing rate', 'sex',  'age_group', 'race_and_hispanic_origin',\
                                'deaths', 'population', 'crude_death_rate', 'standard_error_for_crude_rate', \
                                'lower_confidence_limit_for_crude_rate', 'upper_confidence_limit_for_crude_rate',\
                                'age_adjusted_rate', 'standard_error_for_age_adjusted_rate', 'lower_confidence_limit_for_age_adjusted_rate',\
                                'upper_confidence_limit_for_age_adjusted_rate', 'state_crude_rate_in_range', 'us_crude_rate',\
                                'us_age_adjusted_rate', 'unit']]


    #return the output
    return (outputDF)

   
# a method to pull all the data from the database filtered by years
def AllPrescriptionStatisticsByYear(yearList):

   #establish a client to mongodb server
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    # connect to opioid database
    db = client.opioidabuse_db

    # map to collections
    prescriptionCollection = db.opioidabuse_prescription
    populationCollection = db.opioidabuse

    # filter the data from collections
    prescriptions = prescriptionCollection.find()
    population = populationCollection.find()    
        
    #build the data frame
    prDF = pd.DataFrame(list(prescriptions))
    ppDF = pd.DataFrame(list(population))


    # filter the prescriptions dataframe with year
    prescriptionsDF = pd.DataFrame(prDF.loc[prDF['year'].isin(yearList)])
    if (prescriptionsDF.empty) :
        return ("1", prescriptionsDF)
    

    # filter the prescriptions dataframe with year
    populationDF = pd.DataFrame(ppDF.loc[ppDF['year'].isin(yearList)])

    if (populationDF.empty) :
        return ("2", populationDF)
    
    #filter the index before merge
    prescriptionsDF = prescriptionsDF.reset_index(drop = True)
    populationDF = populationDF.reset_index(drop = True)

    # merge the dataframes
    mergedDF = pd.merge(prescriptionsDF, populationDF, on = ['state', 'year'], how='left' )


    # retrieve selected columns
    outputDF = mergedDF[['state', 'state abbr', 'year', 'prescribing rate', 'sex',  'age_group', 'race_and_hispanic_origin',\
                                'deaths', 'population', 'crude_death_rate', 'standard_error_for_crude_rate', \
                                'lower_confidence_limit_for_crude_rate', 'upper_confidence_limit_for_crude_rate',\
                                'age_adjusted_rate', 'standard_error_for_age_adjusted_rate', 'lower_confidence_limit_for_age_adjusted_rate',\
                        
                        'upper_confidence_limit_for_age_adjusted_rate', 'state_crude_rate_in_range', 'us_crude_rate',\
                                'us_age_adjusted_rate', 'unit']]
    print(outputDF)

    return ("0", outputDF)



# a method to pull all the data from the database
def AllPrescriptionStatisticsByState(stateResultCode, stateAbbrList):

    #establish a client to mongodb server
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    # connect to opioid database
    db = client.opioidabuse_db

    # map to collections
    prescriptionCollection = db.opioidabuse_prescription
    populationCollection = db.opioidabuse

    # pull the statenames for the abbrevations
    stateAbbrList = [x.upper() for x in stateAbbrList] 
    stateList =  (prescriptionCollection.find({"state abbr":{ "$in": stateAbbrList  }},{"state" : 1})).distinct("state")


    # filter the data from collections
    prescriptions = prescriptionCollection.find()
    population = populationCollection.find()    

    #build the data frame
    prDF = pd.DataFrame(list(prescriptions))
    ppDF = pd.DataFrame(list(population))

    # filter the prescriptions dataframe with state name
    prescriptionsDF = pd.DataFrame(prDF.loc[prDF['state'].isin(stateList)])
    # filter the prescriptions dataframe with state name
    populationDF = pd.DataFrame(ppDF.loc[ppDF['state'].isin(stateList)])

    
    #if prescription data is empty return 
    if (prescriptionsDF.empty) :
        return ("1", prescriptionsDF)

    #if population data is empty return 
    if (populationDF.empty) :
        return ("2", populationDF)
    
    #reset the index before merge
    prescriptionsDF = prescriptionsDF.reset_index(drop = True)
    populationDF = populationDF.reset_index(drop = True)

    # merge the dataframes
    mergedDF = pd.merge(prescriptionsDF, populationDF, on = ['state', 'year'], how='left' )


    # retrieve selected columns
    outputDF = mergedDF[['state', 'state abbr', 'year', 'prescribing rate', 'sex',  'age_group', 'race_and_hispanic_origin',\
                                'deaths', 'population', 'crude_death_rate', 'standard_error_for_crude_rate', \
                                'lower_confidence_limit_for_crude_rate', 'upper_confidence_limit_for_crude_rate',\
                                'age_adjusted_rate', 'standard_error_for_age_adjusted_rate', 'lower_confidence_limit_for_age_adjusted_rate',\
                                'upper_confidence_limit_for_age_adjusted_rate', 'state_crude_rate_in_range', 'us_crude_rate',\
                                'us_age_adjusted_rate', 'unit']]
    print(outputDF)

    return ("0", outputDF)

# a method to pull all the data from the database by state and year
def AllPrescriptionStatisticsByStateAndYear(stateResultCode, stateAbbrList, yearResultCode, yearList):

    #establish a client to mongodb server
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    # connect to opioid database
    db = client.opioidabuse_db

    # map to collections
    prescriptionCollection = db.opioidabuse_prescription
    populationCollection = db.opioidabuse

    # pull the statenames for the abbrevations
    stateAbbrList = [x.upper() for x in stateAbbrList] 
    stateList =  (prescriptionCollection.find({"state abbr":{ "$in": stateAbbrList  }},{"state" : 1})).distinct("state")


    # query the table and pull all the resultsets
    if ((stateResultCode == "0") and (yearResultCode == "0") ):
        prescriptions = prescriptionCollection.find()
        population = populationCollection.find()
        
    if ((stateResultCode == "0") and (yearResultCode == "1")) :
        prescriptions = prescriptionCollection.find({ "year": { "$in": yearList } })
        population = populationCollection.find({ "year" : { "$in": yearList } })
        
    if ((stateResultCode == "1") and (yearResultCode == "0")) :
        prescriptions = prescriptionCollection.find({ "state": { "$in": stateList } })
        population = populationCollection.find({ "state": { "$in": stateList } })
        
    if ((stateResultCode == "1") and (yearResultCode == "1") ):
        prescriptions = prescriptionCollection.find({ "$and": [{"state" : { "$in": stateList }}, {"year": { "$in": yearList }}] })
        population = populationCollection.find({'$and': [ {"state" : { "$in": stateList }} , {"year" : { "$in": yearList }}]})

    #convert the collection to data frame
    prescriptionsDF = pd.DataFrame(list(prescriptions))
    populationDF = pd.DataFrame(list(population))

    # if no results for prescription then return
    if (prescriptionsDF.empty):
        return (f"1", prescriptionsDF)

    # if no results for popultation then return
    if (populationDF.empty) :
        return (f"2", populationDF)  

    #merge the Crime data and housing census data
    mergedDF = pd.merge(prescriptionsDF, populationDF, on = ['state', 'year'], how='inner' )
    
    # select the required columns
    outputDF = mergedDF[['state', 'state abbr', 'year', 'prescribing rate', 'sex',  'age_group', 'race_and_hispanic_origin',\
                                'deaths', 'population', 'crude_death_rate', 'standard_error_for_crude_rate', \
                                'lower_confidence_limit_for_crude_rate', 'upper_confidence_limit_for_crude_rate',\
                                'age_adjusted_rate', 'standard_error_for_age_adjusted_rate', 'lower_confidence_limit_for_age_adjusted_rate',\
                                'upper_confidence_limit_for_age_adjusted_rate', 'state_crude_rate_in_range', 'us_crude_rate',\
                                'us_age_adjusted_rate', 'unit']]
    


    #return the output
    return ("0", outputDF)




