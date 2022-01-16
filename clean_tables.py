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
ALTER TABLE drugs DROP COLUMN brand_name;
ALTER TABLE drugs DROP COLUMN atc_vet_code;
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
DELETE FROM duration WHERE unit = 'Year';
DELETE FROM duration WHERE unit = 'Hour';
DELETE FROM duration WHERE unit = 'Minute';
DELETE FROM duration WHERE unit = 'Second';
DELETE FROM duration WHERE unit = '';
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

health_assessment_prior_to_exposure_commands = ("""
UPDATE health_assessment_prior_to_exposure SET conditions = 'Unknown' WHERE conditions='';
DELETE FROM health_assessment_prior_to_exposure WHERE conditions IS NULL;
""")


results_commands = ("""
UPDATE results SET onset_date = 'Unkown' WHERE onset_date IS NULL;
UPDATE results SET onset_date = 'Unkown' WHERE onset_date = '';
UPDATE results SET primary_reporter = 'Unkown' WHERE primary_reporter IS NULL;
UPDATE results SET primary_reporter = 'Unkown' WHERE primary_reporter = '';
UPDATE results SET original_receive_date = 'Unkown' WHERE original_receive_date IS NULL;
UPDATE results SET original_receive_date = 'Unkown' WHERE original_receive_date = '';
""")



commands_list = [reaction_commands]


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
