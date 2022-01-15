import psycopg2


connection_name = "postgres://postgres:banana_2@localhost:5432/postgres"

#dogs

dogs_commands = ("""
UPDATE dogs SET bred_for = "Unkown" WHERE bred_for ='';
UPDATE dogs SET bred_for = "Unkown" WHERE bred_for IS NULL;
""")


#animals
animals_commands = ("""
UPDATE animals SET reproductive_status = 'Unkown' WHERE reproductive_status IS NULL;
UPDATE animals SET gender = 'Unkown' WHERE gender is NULL;
DELETE FROM animals WHERE species != "Dog";
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
""")
#weight

weight_commands = ("""
ALTER TABLE weight DROP COLUMN unit;
ALTER TABLE weight DROP COLUMN qualifier;
""")

#duration


#age_table
age_table_commands = ("""
DELETE FROM age_table WHERE 
ALTER TABLE age_table DROP COLUMN unit;
""")

commands_list = [weight_commands, reaction_commands, drugs_commands, animals_commands, dogs_commands]


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


if __name__ == '__main__':
    cleaning()
