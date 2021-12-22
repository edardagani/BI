import psycopg2
import json
import requests


def etl():
    connection = psycopg2.connect("postgres://postgres:e26519982@localhost:5432/postgres")
    connection.autocommit = True
    crs = connection.cursor()

    insert_q = """    INSERT INTO raw (unique_aer_id_number, raw_data) VALUES(%s, %s)
    """
    for page in fetch_data():
        for result in page:
            crs.execute(insert_q, (result.get("unique_aer_id_number"), json.dumps(result)))


def fetch_data():
    url = 'https://api.fda.gov/animalandveterinary/event.json?limit=50'
    response = requests.get(url)
    #print(url)
    yield response.json().get("results")

    while response.links.get("next") is not None:
        url = response.links.get('next').get("url")
        response = requests.get(url)
        yield response.json().get("results")


if __name__ == '__main__':
    etl()


