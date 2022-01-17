import psycopg2



# def etl_dog_api():
#     connection = psycopg2.connect("postgres://postgres:banana_2@localhost:5432/postgres")
#     connection.autocommit = True
#     crs = connection.cursor()
#
#     insert_q = """
#      INSERT INTO raw_dog (raw_data)
#        SELECT j FROM jsonb_array_elements((%s)::jsonb) AS j;
#     """
#
#     crs.execute(insert_q, fetch_data_dog_api())

def common_breeds():
    breeds_list = []
    connection = psycopg2.connect("postgres://postgres:banana_2@localhost:5432/postgres")
    connection.autocommit = True

    crs = connection.cursor()

    crs.execute("SELECT * FROM raw LIMIT 2000")

    records = crs.fetchall()
    # print(records)

    for record in records:
        try:
            animal = record[1].get("animal")
            breed = animal['breed']['breed_component']
            # print(breed)

            breeds_list.append(breed)
        except Exception as e:
                print(e)
    return breeds_list
        # finally:
        #     return column_list


def common_reactions():
    reactions_list = []
    connection = psycopg2.connect("postgres://postgres:banana_2@localhost:5432/postgres")
    connection.autocommit = True

    crs = connection.cursor()

    crs.execute("SELECT * FROM reactions LIMIT 10000")
    records = crs.fetchall()
    for record in records:
        try:
            reaction = record[3]
            # print(reaction)

            reactions_list.append(reaction)
        except Exception as e:
                print(e)
    return reactions_list
        # finally:
        #     return column_list

# common_reactions()

def common_active_ingredients():
    active_ingredients_list = []
    connection = psycopg2.connect("postgres://postgres:banana_2@localhost:5432/postgres")
    connection.autocommit = True

    crs = connection.cursor()

    crs.execute("SELECT * FROM raw LIMIT 2000")

    records = crs.fetchall()
    # print(records)

    for record in records:
        try:
            active_ingredients = record[1].get("drug")
            active_ingredients = active_ingredients[0]["active_ingredients"]
            active_ingredients = active_ingredients[0]["name"]
            # print(active_ingredients)
            active_ingredients_list.append(active_ingredients)
        except Exception as e:
                print(e)
    return active_ingredients_list
        # finally:
        #     return column_list


def duration():
    duration_list = []
    connection = psycopg2.connect("postgres://postgres:banana_2@localhost:5432/postgres")
    connection.autocommit = True

    crs = connection.cursor()

    crs.execute("SELECT * FROM duration LIMIT 10000")
    records = crs.fetchall()
    for record in records:
        try:
            duration = record[1]
            # print(reaction)

            duration_list.append(duration)
        except Exception as e:
                print(e)
    return duration_list
        # finally:
        #     return column_list


def age():
    age_list = []
    connection = psycopg2.connect("postgres://postgres:banana_2@localhost:5432/postgres")
    connection.autocommit = True

    crs = connection.cursor()

    crs.execute("SELECT * FROM age_table LIMIT 10000")
    records = crs.fetchall()
    for record in records:
        try:
            duration = record[1]
            # print(reaction)

            age_list.append(duration)
        except Exception as e:
                print(e)
    return age_list
        # finally:
        #     return column_list
# duration()

# test =common_active_ingredients()
# print(test)
# common_breeds()

# def insert_to_column():
#
#     connection = psycopg2.connect("postgres://postgres:banana_2@localhost:5432/postgres")
#     connection.autocommit = True
#     crs = connection.cursor()
#
#     insert_q = """
#      INSERT INTO data_warehouse (breed)
#        SELECT j FROM unnest((%s)::text[]) AS j;
#     """
#     data = set_column()
#     data = str(data)
#     for d in data:
#         crs.execute(insert_q, d)
#
#
# insert_to_column()
#

# set_column()
# print(column_list)
# if __name__ == '__main__':
#
#     connection = psycopg2.connect("postgres://postgres:banana_2@localhost:5432/postgres")
#     connection.autocommit = True
#
#     crs = connection.cursor()
#
#     crs.execute("SELECT * FROM raw_dog LIMIT 200")
#
#     records = crs.fetchall()
# #
# #     # insert_q = """
# #     #  INSERT INTO raw_dog (raw_data)
# #     #    SELECT j FROM jsonb_array_elements((%s)::jsonb) AS j;
# #     # """
# #     #
# #     # crs.execute(insert_q, response)
# #
#     for record in records:
#         try:
# #             # my_data = record[0], record[1].get('primary_reporter'),  record[2].get('lot_number')
#             data = record[0]
#             print(data)
# #             #
#             animal = record[1].get('animal')
#             print(animal)
            # breed = animal['breed']['breed_component']
            # species = animal['species']
            # print(species)
#             breed = animal['breed']['breed_component']
#             print(breed)
#             str(breed)
#             # crs.execute(insert_q, breed)
#
#             # original_receive_date = record[1].get("original_receive_date")
#             # print(original_receive_date)
#             #
#             # reaction = record[1].get("reaction")
#             # reaction = reaction[0].get("veddra_term_name")
#             # print(reaction)
#             #
#             # active_ingredients = record[1].get("drug")
#             # active_ingredients = active_ingredients[0]["active_ingredients"]
#             # active_ingredients = active_ingredients[0]["name"]
#             # print(active_ingredients)
#             #
#             #
#             #
#             # animal = record[1].get("animal")
#             # weight = animal['weight']['min']
#             # print(weight)
#             #
#             animal = record[1].get("animal")
#             # print(animal)
#             # species = animal['species']
#             # gender = animal['gender']
#             age = animal["age"]
#             min = age.get("min")
#             print(type(min))
            # print(animal)
            #     results = record[1].get("original_receive_date")
            #     print(results)
#             # reproductive_status = animal.get('reproductive_status')
#             # # print(reproductive_status)
#             # print("Gender: {} | Species: {} | Reproductive Status : {}".format(gender, species, reproductive_status))
#             #
#             # geography = record[1].get("receiver")
#             # city = geography["city"]
#             # print(city)
#             #
#             # time_between_exposure_and_onset = record[1].get("time_between_exposure_and_onset")
#             # print(time_between_exposure_and_onset)
#
#             #brand name
#             #age
#             #dose
#             #used_according_to_label
#             #duration
#             #outcome
#         except Exception as e:
#             print(e)
# #
