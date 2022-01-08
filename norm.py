import psycopg2
import requests
import psycopg2
import json


connection = psycopg2.connect("postgres://postgres:banana_2@localhost:5432/postgres")
connection.autocommit = True

crs = connection.cursor()

crs.execute("SELECT * FROM raw LIMIT 2000")

records = crs.fetchall()


def common_active_ingredients():
    # Active Ingredients
    active_ingredients_to_insert = []
    for record in records:
        for drugs_data in record[1].get('drug'):
            for active_ingredient in drugs_data.get('active_ingredients'):
                active_ingredients_to_insert.append(active_ingredient.get('name', 'Unknown'))

    insert_q = """
        INSERT INTO active_ingredients (active_ingredient)
        VALUES (%s)
        ON CONFLICT DO NOTHING
        """

    for active_ingredient_to_insert in active_ingredients_to_insert:
        crs.execute(insert_q, (active_ingredient_to_insert,))


def active_ingrediends_per_incident():
    for record in records:
        try:
            for drugs_data in record[1].get('drug'):
                for active_ingredient in drugs_data.get('active_ingredients'):

                    crs.execute(f"""
                    SELECT id FROM active_ingredients
                    WHERE active_ingredient = '{active_ingredient.get('name', 'Unknown')}'
                    """)

                    ai_to_insert = crs.fetchone()

                    crs.execute("""
                    INSERT INTO incident_ai (unique_aer_id_number,ai_id,numenator,numerator_unit,denominator,denominator_unit)
                    VALUES (%s,%s,%s,%s,%s,%s)
                    ON CONFLICT DO NOTHING 
                    """, (record[0], ai_to_insert[0], active_ingredient.get('dose').get('numerator'),
                        active_ingredient.get('dose').get('numerator'), active_ingredient.get('dose').get('denominator'),
                        active_ingredient.get('dose').get('denominator_unit')))
        except Exception as E:
            print("Error: {}".format(E))


def animals():
    for record in records:
        try:

            # for animal_data in record[1].get('animal'):
                animal_data = record[1].get("animal")
                print(animal_data['breed']['breed_component'])
                print(animal_data['species'])
                crs.execute(f"""
                INSERT INTO animals(unique_aer_id_number, species, gender, reproductive_status, 
                female_animal_physiological_status, type_of_information)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT DO NOTHING
                """, (record[0], animal_data.get('species'), animal_data.get('gender'), animal_data.get('reproductive_status'),
                     animal_data.get('female_animal_physiological_status'), animal_data.get('type_of_information')))

        except Exception as E:
            print("Error: {}".format(E))


def age():
    for record in records:
        try:
            animal_data = record[1].get("animal")
            age = animal_data["age"]
            print(age)
            min = age.get("min")
            print(min)
            crs.execute(f"""
            INSERT INTO age_table(unique_aer_id_number, min, unit, qualifier)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT DO NOTHING
            """, (record[0], age.get("min"), age.get("unit"), age.get("qualifier")))
        except Exception as E:
            print("Error: {}".format(E))


def results():
    for record in records:
        try:
            results = record[1]
            original_receive_date = results.get("original_receive_date")
            primary_reporter = results.get("primary_reporter")
            number_of_animals_treated = results.get("number_of_animals_treated")
            onset_date = results.get("onset_date")
            report_id = results.get("report_id")
            crs.execute(f"""
            INSERT INTO results(unique_aer_id_number, original_receive_date, primary_reporter, onset_date, report_id)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT DO NOTHING
            """, (record[0], original_receive_date, primary_reporter, onset_date, report_id))
            # print(report_id)
            # print(onset_date)
            # print(number_of_animals_affected)
            # print(number_of_animals_treated)
            # print(onset_date)
            # print(primary_reporter)
            # print(report_id)
        except Exception as E:
            print("Error: {}".format(E))


def dogs():
    connection = psycopg2.connect("postgres://postgres:banana_2@localhost:5432/postgres")
    connection.autocommit = True

    crs = connection.cursor()

    crs.execute("SELECT * FROM raw_dog LIMIT 2000")

    records = crs.fetchall()
    for record in records:
        try:
            id  = record[0].get("id")
            name = record[0].get("name")
            life_span = record[0].get("life_span")
            weight = record[0].get("weight")["metric"] + " kg"
            height = record[0].get("height")["metric"] + " cm"
            temperament = record[0].get("temperament")
            # print(id)
            # print(weight)
            # print(height)
            print(temperament)
            crs.execute("""
            INSERT INTO dogs(id, name, life_span, weight, height, temperament)
            VALUES (%s,%s, %s, %s, %s, %s)
            ON CONFLICT DO NOTHING
            """, (id, name, life_span, weight, height, temperament))
        except Exception as E:
            print("Error: {}".format(E))



if __name__ == "__main__":
    # common_active_ingredients()
    # results()
    dogs()
