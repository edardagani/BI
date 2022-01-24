import psycopg2
import json
import requests
from psycopg2.extras import Json

connection_name = "postgres://postgres:banana_2@localhost:5432/postgres"


raw_table = ("""
CREATE TABLE raw
(
 unique_aer_id_number TEXT NOT NULL,
 raw_data JSON,
 PRIMARY KEY (unique_aer_id_number)
);

""")

raw_dog_table = ("""
CREATE TABLE raw_dog
(
  raw_data JSON
);

""")

table_list = [raw_table, raw_dog_table]


def table_creation():
    try:
        connection = psycopg2.connect(connection_name)
        connection.autocommit = True
        crs = connection.cursor()

        for command in table_list:
            crs.execute(command)
            # close communication with the PostgreSQL database server
            # crs.close()
            # commit the changes
            connection.commit()
        crs.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def etl():
    connection = psycopg2.connect("postgres://postgres:banana_2@localhost:5432/postgres")
    connection.autocommit = True
    crs = connection.cursor()

    insert_q = """    INSERT INTO raw (unique_aer_id_number, raw_data) VALUES(%s, %s)
    """
    for page in fetch_data():
        for result in page:
            crs.execute(insert_q, (result.get("unique_aer_id_number"), json.dumps(result)))


def fetch_data():
    url = 'https://api.fda.gov/animalandveterinary/event.json?limit=1000'
    response = requests.get(url)
    print(url)
    yield response.json().get("results")

    while response.links.get("next") is not None:
        url = response.links.get('next').get("url")
        response = requests.get(url)
        yield response.json().get("results")



def etl_dog_api():
    connection = psycopg2.connect("postgres://postgres:banana_2@localhost:5432/postgres")
    connection.autocommit = True
    crs = connection.cursor()

    insert_q = """
     INSERT INTO raw_dog (raw_data)
       SELECT j FROM json_array_elements((%s)::json) AS j;
    """

    crs.execute(insert_q, fetch_data_dog_api())


def fetch_data_dog_api():
    url = 'https://api.thedogapi.com/v1/breeds/'
    response = requests.get(url)
    response = response.text
    print(response)

    return [response]


def etl_process():
    table_creation()
    etl_dog_api()
    etl()



#etl_process()


