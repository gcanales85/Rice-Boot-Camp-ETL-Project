
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base

# Imports the method used to connect to DBs
from sqlalchemy import create_engine

# function to establish a session with a connected database
from sqlalchemy.orm import Session

# import func
from sqlalchemy import  func

from config import connectionstring

import pandas as pd

# a method to pull all the data from the database
def AllDataStatistics():

    

    try :

        # creates an connection object
        engine = create_engine(connectionstring)

        #establish the connection
        connection = engine.connect()

        # build the relationships from the database
        Base = automap_base()
        Base.prepare(engine, reflect=True)

        # establish the session
        session = Session(bind=engine)

        # map the class
        opioid_abuse = Base.classes.opioid_abuse

        # query the table and pull all the resultsets
        opiod_abuseDf = pd.read_sql(session.query(opioid_abuse).statement, engine)

        return opiod_abuseDf

    except Exception as ex :
        return null



    


# a method to pull all the data by state from the database
def AllDataStatisticsByState(stateList):

    try :
        
         # creates an connection object
         engine = create_engine(connectionstring)

         #establish the connection
         connection = engine.connect()

         # build the relationships from the database
         Base = automap_base()
         Base.prepare(engine, reflect=True)

         # establish the session
         session = Session(bind=engine)

         # map the class
         opioid_abuse = Base.classes.opioid_abuse

         # query the table and pull all the resultsets
         opiod_abuseDf = pd.read_sql(session.query(opioid_abuse).filter(opioid_abuse.state.in_(stateList)).statement, engine)

         return opiod_abuseDf

    except Exception as ex :
        return null



