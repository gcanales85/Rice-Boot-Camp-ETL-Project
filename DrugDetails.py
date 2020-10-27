
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base

# Imports the method used to connect to DBs
from sqlalchemy import create_engine

# function to establish a session with a connected database
from sqlalchemy.orm import Session

# import func
from sqlalchemy import  func

from config import connection_string 

import pandas as pd

# a method to pull all the data from the database
def AllDataStatistics():

    

    try :

        # creates an connection object
        engine = create_engine(connection_string)

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
def AllDataStatisticsByState(resultCode, stateList):

    try :
        
        # creates an connection object
        engine = create_engine(connection_string)

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
        if (resultCode == "0") :
            opiod_abuseDf = pd.read_sql(session.query(opioid_abuse).statement, engine)
        else :
            opiod_abuseDf = pd.read_sql(session.query(opioid_abuse).filter(opioid_abuse.state.in_(stateList)).statement, engine)

        return opiod_abuseDf

    except Exception as ex :
        return null


# a method to pull all the data by state from the database
def AllDataStatisticsByYear(resultCode, yearList):

    try :
        
        # creates an connection object
        engine = create_engine(connection_string)

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
        if (resultCode == "0") :
            opiod_abuseDf = pd.read_sql(session.query(opioid_abuse).statement, engine)
        else :
            opiod_abuseDf = pd.read_sql(session.query(opioid_abuse).filter(opioid_abuse.year.in_(yearList)).statement, engine)

        return opiod_abuseDf

    except Exception as ex :
        return null



# a method to pull all the data by state and year from the database
def AllDataStatisticsByStateAndYear(stateResultCode, stateList, yearResultCode, yearList):

    try :
        from sqlalchemy import and_
        # creates an connection object
        engine = create_engine(connection_string)

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
        if ((stateResultCode == "0") and (yearResultCode == "0") ):
            opiod_abuseDf = pd.read_sql(session.query(opioid_abuse).statement, engine)
        
        if ((stateResultCode == "0") and (yearResultCode == "1")) :
            opiod_abuseDf = pd.read_sql(session.query(opioid_abuse).filter(opioid_abuse.year.in_(yearList)).statement, engine)
        
        if ((stateResultCode == "1") and (yearResultCode == "0")) :
            opiod_abuseDf = pd.read_sql(session.query(opioid_abuse).filter(opioid_abuse.state.in_(stateList)).statement, engine)
        
        if ((stateResultCode == "1") and (yearResultCode == "1") ):
            opiod_abuseDf = pd.read_sql(session.query(opioid_abuse).filter(opioid_abuse.year.in_(yearList)).filter(opioid_abuse.state.in_(stateList) ).statement, engine)

        return opiod_abuseDf

    except Exception as ex :
        return null