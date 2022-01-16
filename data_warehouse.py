import psycopg2

connection_name = "postgres://postgres:banana_2@localhost:5432/postgres"

temperament_commands = ("""
CREATE TABLE temperament
(
  name TEXT NOT NULL,
  char1 TEXT,
  char2 TEXT,
  char3 TEXT,
  char4 TEXT,
  char5 TEXT,
  char6 TEXT,
  PRIMARY KEY (name)
);

INSERT INTO temperament (name, char1, char2, char3, char4, char5, char6)
SELECT name
     ,split_part(temperament, ',', 1) AS col1
     ,split_part(temperament, ',', 2) AS col2
     ,split_part(temperament, ',', 3) AS col3
     ,split_part(temperament, ',', 4) AS col4
     ,split_part(temperament, ',', 5) AS col5
     ,split_part(temperament, ',', 6) AS col6
FROM dogs;
""")

commands_list = [temperament_commands]


def data_mart():
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


def age():
    connection = psycopg2.connect("postgres://postgres:banana_2@localhost:5432/postgres")
    connection.autocommit = True

    crs = connection.cursor()

    crs.execute("SELECT * FROM raw LIMIT 1000000")

    records = crs.fetchall()

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


if __name__ == '__main__':
    data_mart()
