#import project dependencies
import numpy as np
import os

from flask import Flask, jsonify,render_template

import DrugDetails as ds
import DrugPrescription as dp
import json

# Flask Setup
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# add the default route
@app.route("/")
def index():
    return render_template('index.html')


# add the route for drug abuse statistics
@app.route('/DrugDetails')
def DrugDeathStatistics():
    drugDeathStatistics = ds.AllDataStatistics()

    # if data result  is empty return 
    if (drugDeathStatisticsByState.empty) :
        return ("Data not found")

    # return the json dataset
    drugJson = json.dumps(json.loads(drugDeathStatistics.to_json(orient='records')), indent=0)
    return (drugJson)



# add the route for drug abuse statistics by state
@app.route('/DrugDetailsByState/<state>')
def DeathStatisticsByState(state):
    try :

        # parse the input parameter
        resultCode, result = ParseStateList(state)

        #if input parameter does not match the format return error message
        if (resultCode  == "-1" ):
            return (result)  
        
        # call the method to pull the statistics by state
        drugDeathStatisticsByState = ds.AllDataStatisticsByState(resultCode, result)

        # if data result  is empty return 
        if (drugDeathStatisticsByState.empty) :
            return ("Data not found for queried states")

        # return the json dataset
        drugJson = json.dumps(json.loads(drugDeathStatisticsByState.to_json(orient='records')), indent=0)
        return (drugJson)

    except Exception as ex :
        return (ex) 


# add the route for drug abuse statistics by year
@app.route('/DrugDetailsByYear/<year>')
def DeathStatisticsByYear(year):
    try :

        # parse the input parameter
        resultCode, result = ParseYearList(year)

        #if input parameter does not match the format return error message
        if (resultCode  == "-1" ):
            return (result)  
        # call the method to pull the statistics by year
        drugDeathStatisticsByYear = ds.AllDataStatisticsByYear(resultCode, result)

        # if data result  is empty return 
        if (drugDeathStatisticsByYear.empty) :
            return ("Data not found for queried years")

        # return the json dataset
        drugJson = json.dumps(json.loads(drugDeathStatisticsByYear.to_json(orient='records')), indent=0)
        return (drugJson)

    except Exception as ex :
        return (ex) 


# add the route for drug abuse statistics by year and state
@app.route('/DrugDetailsByStateAndYear/<state>/<year>')
def DeathStatisticsByStateAndYear(state, year):
    try :

        # parse the input parameter
        stateResultCode, stateResult = ParseStateList(state)

        #if input parameter does not match the format return error message
        if (stateResultCode  == "-1" ):
            return (stateResult)  

        # parse the input parameter
        yearResultCode, yearResult = ParseYearList(year)

        #if input parameter does not match the format return error message
        if (yearResultCode  == "-1" ):
            return (yearResult)   
      
        # call the method to pull the statistics by state and year
        drugDeathStatisticsByStateYear = ds.AllDataStatisticsByStateAndYear(stateResultCode, stateResult, yearResultCode, yearResult)

        # if data result  is empty return 
        if (drugDeathStatisticsByStateYear.empty) :
            return ("Data not found for queried state and years")

        # return the json dataset
        drugJson = json.dumps(json.loads(drugDeathStatisticsByStateYear.to_json(orient='records')), indent=0)
        return (drugJson)

    except Exception as ex :
        return (ex) 


# add the route for drug abuse statistics
@app.route('/DrugPrescriptionDetails')
def DrugPrescriptionStatistics():
    
    # call the method to pull the prescription statistics
    drugPrescriptionStatistics = dp.AllPrescriptionStatistics()
    
    # if data result  is empty return 
    if (drugPrescriptionStatistics.empty) :
        return ("Data not found")
    
    # return the json dataset
    drugJson = json.dumps(json.loads(drugPrescriptionStatistics.to_json(orient='records')), indent=0)
    return (drugJson)

# add the route for drug abuse statistics filtered by state
@app.route('/DrugPrescriptionDetailsByState/<state>')
def DrugPrescriptionStatisticsByState(state):

    try :
        # parse the input parameter
        stateResultCode, stateResult = ParseStateList(state)

        #if input parameter does not match the format return error message
        if (stateResultCode  == "-1" ):
            return (stateResult) 
       
       # call the method to pull the prescription statistics
        resultcode, drugPrescriptionStatisticsByState = dp.AllPrescriptionStatisticsByState(stateResultCode, stateResult)

        # if prescription/population is empty then let user know 
        if (resultcode.startswith("1") ):
            return (f"prescription statistics empty")
        if (resultcode.startswith("2")) :
            return ("population statistics details empty")

        # if data result  is empty return 
        if (drugPrescriptionStatisticsByState.empty) :
            return ("Data not found for queried states")

        # return the json dataset
        drugJson = json.dumps(json.loads(drugPrescriptionStatisticsByState.to_json(orient='records')), indent=0)
        return (drugJson)

    except Exception as ex :
        return (ex)
    

# add the route for drug abuse statistics filtered by state
@app.route('/DrugPrescriptionDetailsByYear/<year>')
def DrugPrescriptionStatisticsByYear(year):

    try :

        # parse the input parameter
        yearResultCode, yearResult = ParseYearList(year)

        #if input parameter does not match the format return error message
        if (yearResultCode  == "-1" ):
            return (yearResult) 

       # call the method to pull the prescription statistics
        resultcode, drugPrescriptionStatisticsByYear = dp.AllPrescriptionStatisticsByYear(yearResult)

        # if prescription/population is empty then let user know 
        if (resultcode.startswith("1") ):
            return (f"prescription statistics empty")
        if (resultcode.startswith("2")) :
            return ("population statistics details empty")

        # if data result  is empty return
        if (drugPrescriptionStatisticsByYear.empty) :
            return ("Data not found for queried years")

        # return the json dataset
        drugJson = json.dumps(json.loads(drugPrescriptionStatisticsByYear.to_json(orient='records')), indent=0)
        return (drugJson)

    except Exception as ex :
        return (ex)

# add the route for drug abuse statistics
@app.route('/DrugPrescriptionDetailsByStateAndYear/<state>/<year>')
def DrugPrescriptionStatisticsByStateAndYear(state, year):

    try :

        # parse the input parameter
        stateResultCode, stateResult = ParseStateList(state)
        #if input parameter does not match the format return error message
        if (stateResultCode  == "-1" ):
            return (stateResult)  

        # parse the input parameter
        yearResultCode, yearResult = ParseYearList(year)
        #if input parameter does not match the format return error message
        if (yearResultCode  == "-1" ):
            return (yearResult) 

        # call the method to pull the prescription statistics
        resultcode, drugPrescriptionStatisticsByStateAndYear = dp.AllPrescriptionStatisticsByStateAndYear(stateResultCode, stateResult, yearResultCode, yearResult)

        # if prescription/population is empty then let user know 
        if (resultcode.startswith("1") ):
            return (f" prescription statistics empty")
        if (resultcode.startswith("2")) :
            return ("population statistics details empty")

        # if data result  is empty return
        if (drugPrescriptionStatisticsByStateAndYear.empty) :
            return ("Data not found for queried state and years")

        # return the json dataset
        drugJson = json.dumps(json.loads(drugPrescriptionStatisticsByStateAndYear.to_json(orient='records')), indent=0)
        return (drugJson)

    except Exception as ex :
        return (ex)


# a method to input state parameter and parse them to list
def ParseStateList(state):
    try :
        stateList = []
        substring ="state="
        if state.lower().startswith(substring):
            state = state.replace(substring, '')                                 
        else :
            return("-1", "Incorrect format should be state=stateAbbr seperated by commas")     
        if (state.lower().find("all") != -1) :
            stateList.append("all")
            return ("0", stateList ) 
        
        stateList = state.split(",")
        return ("1", stateList)
        
    except ValueError as ex:
        return("-1", "Incorrect format should be state=stateAbbr seperated by commas")

# a method to input year parameter and parse them to list
def ParseYearList(year):
    try :
        yearList = []
        substring ="year="
        if year.lower().startswith(substring):
            year = year.replace(substring, '')                                 
        else :
            return("-1", "Incorrect format should be year=year seperated by commas")     
        if (year.lower().find("all") != -1) :
            yearList.append("all")
            return ("0", yearList ) 
        
        yearList = year.split(",")
        return ("1", yearList)
        
    except ValueError as ex:
        return("-1", "Incorrect format should be year=year seperated by commas")

if __name__ == '__main__':
    app.run(debug=True)
