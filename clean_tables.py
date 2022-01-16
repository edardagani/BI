import psycopg2


connection_name = "postgres://postgres:banana_2@localhost:5432/postgres"

#dogs

dogs_commands = ("""
UPDATE dogs SET bred_for = 'Unkown' WHERE bred_for ='';
UPDATE dogs SET bred_for = 'Unkown' WHERE bred_for IS NULL;
UPDATE dogs SET breed_group = 'Unkown' WHERE breed_group ='';
UPDATE dogs SET breed_group = 'Unkown' WHERE breed_group IS NULL;
UPDATE dogs SET temperament = 'Unkown' WHERE temperament IS NULL;
UPDATE dogs SET temperament = 'Unkown' WHERE temperament ='';
""")


#animals
animals_commands = ("""
UPDATE animals SET reproductive_status = 'Unkown' WHERE reproductive_status IS NULL;
UPDATE animals SET gender = 'Unkown' WHERE gender is NULL;
DELETE FROM animals WHERE species != 'Dog';

""")


#drugs
drugs_commands = ("""
UPDATE drugs SET used_according_to_label = 'Unkown' WHERE used_according_to_label IS NULL;
UPDATE drugs SET previous_exposure_to_drug = 'Unkown' WHERE previous_exposure_to_drug IS NULL;
UPDATE drugs SET dosage_form = 'Unkown' WHERE dosage_form IS NULL;
UPDATE drugs SET brand_name = 'Unkown' WHERE brand_name IS NULL;
""")


#reactions
reaction_commands = ("""
UPDATE reactions SET veddra_version = 'Unknown' WHERE veddra_version = '';
UPDATE reactions SET veddra_term_code = 'Unknown' WHERE veddra_term_code = '';
UPDATE reactions SET veddra_term_name = 'Unknown' WHERE veddra_term_name = '';
""")

#weight

weight_commands = ("""
DELETE FROM weight WHERE min IS NULL;
ALTER TABLE weight DROP COLUMN qualifier;
ALTER TABLE weight DROP COLUMN unit;
""")

#duration
duration_commands = ("""
DELETE FROM duration WHERE unit IS NULL;
DELETE FROM duration WHERE unit != 'Day' or unit != 'Week' or unit != 'Month';
ALTER TABLE duration DROP COLUMN unit;
""")

#age_table
age_table_commands = ("""
SELECT EXISTS (SELECT 1 
FROM information_schema.columns 
WHERE table_name='age_table' AND column_name='unit');
DELETE FROM age_table WHERE unit !='Year';
DELETE FROM age_table WHERE unit IS NULL;
ALTER TABLE age_table DROP COLUMN unit;
ALTER TABLE age_table DROP COLUMN qualifier;
""")

commands_list = [dogs_commands]


def cleaning():
    try:
        connection = psycopg2.connect(connection_name)
        connection.autocommit = True
        crs = connection.cursor()

        for command in commands_list:
            crs.execute(command)
            # close communication with the PostgreSQL database server
            crs.close()
            # commit the changes
            connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# def dogs_clean():
#     connection = psycopg2.connect("postgres://postgres:banana_2@localhost:5432/postgres")
#     connection.autocommit = True
#
#     crs = connection.cursor()
#
#     crs.execute("SELECT * FROM dogs LIMIT 500")
#
#     records = crs.fetchall()
#
#     for record in records:
#         try:
#             dog_life_span = record[2][:2]
#             print(dog_life_span)
#             weight = record[3][:2]
#             print(weight)
#             height = record[4][:2]
#             print(height)
#             crs.execute(f"""
#             INSERT INTO age_table(unique_aer_id_number, min, unit, qualifier)
#             VALUES (%s, %s, %s, %s)
#             ON CONFLICT DO NOTHING
#             """, (record[0], age.get("min"), age.get("unit"), age.get("qualifier")))
#         except Exception as E:
#             print("Error: {}".format(E))
#


if __name__ == '__main__':
    cleaning()
