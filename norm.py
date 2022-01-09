import psycopg2
import requests
import psycopg2
import json


connection = psycopg2.connect("postgres://postgres:banana_2@localhost:5432/postgres")
connection.autocommit = True

crs = connection.cursor()

crs.execute("SELECT * FROM raw LIMIT 1000000")

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
                INSERT INTO animals(unique_aer_id_number, species, gender, breed, reproductive_status)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT DO NOTHING
                """, (record[0], animal_data.get('species'), animal_data.get('gender'), animal_data['breed']['breed_component'],
                      animal_data.get('reproductive_status')))

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
            breed_group = record[0].get("breed_group")
            bred_for = record[0].get("bred_for")
            # print(id)
            # print(weight)
            # print(height)
            print(temperament)
            crs.execute("""
            INSERT INTO dogs(id, name, life_span, weight, height, temperament, breed_group, bred_for)
            VALUES (%s,%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT DO NOTHING
            """, (id, name, life_span, weight, height, temperament, breed_group, bred_for))
        except Exception as E:
            print("Error: {}".format(E))


def reactions():
    for record in records:
        try:
            results = record[1]
            reaction = results.get("reaction")
            veddra_version = reaction["veddra_version"]
            veddra_term_code = reaction["veddra_term_code"]
            veddra_term_name = reaction["veddra_term_code"]
            crs.execute(f"""
            INSERT INTO reactions(unique_aer_id_number, veddra_version, veddra_term_code, veddra_term_name)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT DO NOTHING
            """, (record[0], veddra_version, veddra_term_code, veddra_term_name))
            # print(veddra_version)
            # print(veddra_term_code)
            # print(veddra_term_name)
        except Exception as E:
            print("Error: {}".format(E))


def weight():
    for record in records:
        try:
            animal_data = record[1].get("animal")
            weight = animal_data["weight"]
            print(age)
            min = weight.get("min")
            print(min)
            crs.execute(f"""
            INSERT INTO weight(unique_aer_id_number, min, unit, qualifier)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT DO NOTHING
            """, (record[0], weight.get("min"), weight.get("unit"), weight.get("qualifier")))
        except Exception as E:
            print("Error: {}".format(E))


def drugs():
    for record in records:
        try:
            drugs = record[1].get("drug")
            used_according_to_label = drugs[0].get("used_according_to_label")
            print(used_according_to_label)
            previous_exposure_to_drug = drugs[0].get("previous_exposure_to_drug")
            brand_name = drugs[0].get("brand_name")
            dosage_form = drugs[0].get("dosage_form")
            atc_vet_code = drugs[0].get("atc_vet_code")
            crs.execute(f"""
            INSERT INTO drugs(unique_aer_id_number, used_according_to_label, previous_exposure_to_drug, brand_name, dosage_form, atc_vet_code)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT DO NOTHING
            """, (record[0], used_according_to_label, previous_exposure_to_drug,
                  brand_name, dosage_form, atc_vet_code))
        except Exception as E:
            print("Error: {}".format(E))

def health_assessment_prior_to_exposure():
    for record in records:
        try:
            results = record[1].get("results")
            health_assessment_prior_to_exposure = results["health_assessment_prior_to_exposure"]
            print(health_assessment_prior_to_exposure)
            condition = health_assessment_prior_to_exposure.get("condition")
            assessed_by = health_assessment_prior_to_exposure.get("assessed_by")
            print(assessed_by)
            crs.execute(f"""
            INSERT INTO age_table(unique_aer_id_number, condition, assessed_by)
            VALUES (%s, %s)
            ON CONFLICT DO NOTHING
            """, (record[0], condition, assessed_by))
        except Exception as E:
            print("Error: {}".format(E))


def duration():
    for record in records:
        try:
            results = record[1].get("results")
            duration = results["duration"]
            print(duration)
            value = duration.get("value")
            unit = duration.get("unit")
            print(unit)
            crs.execute(f"""
            INSERT INTO age_table(unique_aer_id_number, value, unit)
            VALUES (%s, %s)
            ON CONFLICT DO NOTHING
            """, (record[0], value, unit))
        except Exception as E:
            print("Error: {}".format(E))



if __name__ == "__main__":
    # common_active_ingredients()
    # results()
    # animals()
    dogs()
    # age()
    # weight()
    # drugs()
