#import project dependencies
import numpy as np
import os

from flask import Flask, jsonify,render_template

import DrugDeathStatistics as ds
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
@app.route('/DeathStatistics')
def DrugDeathStatistics():
    drugDeathStatistics = ds.AllDataStatistics()
    drugJson = json.dumps(json.loads(drugDeathStatistics.to_json(orient='records')), indent=0)
    return (drugJson)



# add the route for drug abuse statistics
@app.route('/DeathStatisticsByState/<state>')
def DeathStatisticsByState(state):
    try :
        substring ="state="
        if state.startswith(substring):
            state = state.replace(substring, '')            
        else :
            return(f"Incorrect format should be state=stateAbbr seperated by commas")     
        stateList = state.split(",")
    except ValueError:
        return(f"Incorrect format should be state=stateAbbr seperated by commas")

    drugDeathStatisticsByState = ds.AllDataStatisticsByState(stateList)
    drugJson = json.dumps(json.loads(drugDeathStatisticsByState.to_json(orient='records')), indent=0)
    return (drugJson)



if __name__ == '__main__':
    app.run(debug=True)
