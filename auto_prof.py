import pandas_profiling
import requests
import psycopg2
import json
import pandas as pd
from init import *


def profiling(query, export_file_name):
    connection = psycopg2.connect(connection_name)
    connection.autocommit = True

    df = pd.read_sql(query, connection)

    try:
        report = pandas_profiling.ProfileReport(df)
        report.to_file(export_file_name)
    except ZeroDivisionError:
        print("Zero Division Error")
    except Exception as e:
        print("Error : {}".format(e))


def profile_tables():
    profiling("SELECT * FROM dogs LIMIT 1000000", "dogs.html")
    profiling("SELECT * FROM animals LIMIT 1000000", "animals.html")
    profiling("SELECT * FROM results LIMIT 1000000", "results.html")
    profiling("SELECT * FROM weight LIMIT 1000000", "weight.html")
    profiling("SELECT * FROM drugs LIMIT 1000000", "drugs.html")
    profiling("SELECT * FROM age_table LIMIT 1000000", "age.html")
    profiling("SELECT * FROM duration LIMIT 1000000", "duration.html")
    profiling("SELECT * FROM reactions LIMIT 1000000", "reactions.html")
    profiling("SELECT * FROM active_ingredients LIMIT 1000000", "active_ingredients.html")
    profiling("SELECT * FROM incident_ai LIMIT 1000000", "incident_ai.html")
    profiling("SELECT * FROM health_assessment_prior_to_exposure LIMIT 1000000", "health_assessment_prior_to_exposure.html")


# profile_tables()
