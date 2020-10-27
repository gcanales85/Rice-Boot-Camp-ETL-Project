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
    drugJson = json.dumps(json.loads(drugDeathStatistics.to_json(orient='records')), indent=0)
    return (drugJson)



# add the route for drug abuse statistics by state
@app.route('/DrugDetailsByState/<state>')
def DeathStatisticsByState(state):
    try :
        resultCode, result = ParseStateList(state)
        if (resultCode  == "-1" ):
            return (result)  
        drugDeathStatisticsByState = ds.AllDataStatisticsByState(resultCode, result)
        if (drugDeathStatisticsByState.empty) :
            return ("Data not found for queried states")

        drugJson = json.dumps(json.loads(drugDeathStatisticsByState.to_json(orient='records')), indent=0)
        return (drugJson)
    except Exception as ex :
        return (ex) 


# add the route for drug abuse statistics by year
@app.route('/DrugDetailsByYear/<year>')
def DeathStatisticsByYear(year):
    try :
        resultCode, result = ParseYearList(year)
        if (resultCode  == "-1" ):
            return (result)  
        
        drugDeathStatisticsByYear = ds.AllDataStatisticsByYear(resultCode, result)
        if (drugDeathStatisticsByYear.empty) :
            return ("Data not found for queried years")

        drugJson = json.dumps(json.loads(drugDeathStatisticsByYear.to_json(orient='records')), indent=0)
        return (drugJson)
    except Exception as ex :
        return (ex) 


# add the route for drug abuse statistics by year and state
@app.route('/DrugDetailsByStateAndYear/<state>/<year>')
def DeathStatisticsByStateAndYear(state, year):
    try :

        stateResultCode, stateResult = ParseStateList(state)
        if (stateResultCode  == "-1" ):
            return (stateResult)  

        yearResultCode, yearResult = ParseYearList(year)
        if (yearResultCode  == "-1" ):
            return (yearResult)  
        
      
        drugDeathStatisticsByStateYear = ds.AllDataStatisticsByStateAndYear(stateResultCode, stateResult, yearResultCode, yearResult)
        if (drugDeathStatisticsByStateYear.empty) :
            return ("Data not found for queried state and years")

        drugJson = json.dumps(json.loads(drugDeathStatisticsByStateYear.to_json(orient='records')), indent=0)
        return (drugJson)
    except Exception as ex :
        return (ex) 


# add the route for drug abuse statistics
@app.route('/DrugPrescriptionDetails')
def DrugPrescriptionStatistics():
    drugPrescriptionStatistics = dp.AllPrescriptionStatistics()
    drugJson = json.dumps(json.loads(drugPrescriptionStatistics.to_json(orient='records')), indent=0)
    return (drugJson)

# add the route for drug abuse statistics filtered by state
@app.route('/DrugPrescriptionDetailsByState/<state>')
def DrugPrescriptionStatisticsByState(state):

    try :

        stateResultCode, stateResult = ParseStateList(state)
        if (stateResultCode  == "-1" ):
            return (stateResult) 
       
        resultcode, drugPrescriptionStatisticsByState = dp.AllPrescriptionStatisticsByState(stateResultCode, stateResult)
        if (resultcode.startswith("1") ):
            return (f"prescription statistics empty")
        if (resultcode.startswith("2")) :
            return ("population statistics details empty")

        if (drugPrescriptionStatisticsByState.empty) :
            return ("Data not found for queried states")

        drugJson = json.dumps(json.loads(drugPrescriptionStatisticsByState.to_json(orient='records')), indent=0)
        return (drugJson)
    except Exception as ex :
        return (ex)
    

# add the route for drug abuse statistics filtered by state
@app.route('/DrugPrescriptionDetailsByYear/<year>')
def DrugPrescriptionStatisticsByYear(year):

    try :

        yearResultCode, yearResult = ParseYearList(year)
        if (yearResultCode  == "-1" ):
            return (yearResult) 

       
        resultcode, drugPrescriptionStatisticsByYear = dp.AllPrescriptionStatisticsByYear(yearResult)
        if (resultcode.startswith("1") ):
            return (f"prescription statistics empty")
        if (resultcode.startswith("2")) :
            return ("population statistics details empty")

        if (drugPrescriptionStatisticsByYear.empty) :
            return ("Data not found for queried years")

        drugJson = json.dumps(json.loads(drugPrescriptionStatisticsByYear.to_json(orient='records')), indent=0)
        return (drugJson)
    except Exception as ex :
        return (ex)

# add the route for drug abuse statistics
@app.route('/DrugPrescriptionDetailsByStateAndYear/<state>/<year>')
def DrugPrescriptionStatisticsByStateAndYear(state, year):

    try :

        stateResultCode, stateResult = ParseStateList(state)
        if (stateResultCode  == "-1" ):
            return (stateResult)  

        yearResultCode, yearResult = ParseYearList(year)
        if (yearResultCode  == "-1" ):
            return (yearResult) 

       
        resultcode, drugPrescriptionStatisticsByStateAndYear = dp.AllPrescriptionStatisticsByStateAndYear(stateResultCode, stateResult, yearResultCode, yearResult)
        if (resultcode.startswith("1") ):
            return (f" prescription statistics empty")
        if (resultcode.startswith("2")) :
            return ("population statistics details empty")

        if (drugPrescriptionStatisticsByStateAndYear.empty) :
            return ("Data not found for queried state and years")

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
