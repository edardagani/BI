import psycopg2

if __name__ == '__main__':

    connection = psycopg2.connect("postgres://postgres:banana_2@localhost:5432/postgres")
    connection.autocommit = True

    crs = connection.cursor()

    crs.execute("SELECT * FROM raw LIMIT 20000")

    records = crs.fetchall()

    for record in records:

        # my_data = record[0], record[1].get('primary_reporter'),  record[2].get('lot_number')
        # print(my_data)

        # animal = record[1].get("animal")
        # breed = animal['breed']['breed_component']
        # print(breed)

        # date = record[1].get("original_receive_date")
        # print(date)

        # reaction = record[1].get("reaction")
        # reaction = reaction[0].get("veddra_term_name")
        # print(reaction)

        # active_ingredients = record[1].get("drug")
        # active_ingredients = active_ingredients[0]["active_ingredients"]
        # active_ingredients = active_ingredients[0]["name"]
        # print(active_ingredients)

        # animal = record[1].get("animal")
        # weight = animal['weight']['min']
        # print(weight)

        # animal = record[1].get("animal")
        # species = animal['species']
        # gender = animal['gender']
        # reproductive_status = animal.get('reproductive_status')
        # # print(reproductive_status)
        # print("Gender: {} | Species: {} | Reproductive Status : {}".format(gender, species, reproductive_status))
        #
        # geography = record[1].get("receiver")
        # city = geography["city"]
        # print(city)

        time_between_exposure_and_onset = record[1].get("time_between_exposure_and_onset")
        print(time_between_exposure_and_onset)
