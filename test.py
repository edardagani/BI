import psycopg2

def common_active_ingredients():
    active_ingredients_list = []
    connection = psycopg2.connect("postgres://postgres:e26519982@localhost:5432/postgres")
    connection.autocommit = True

    crs = connection.cursor()

    crs.execute("SELECT * FROM raw LIMIT 2000")

    records = crs.fetchall()

    for record in records:
        try:
            active_ingredients = record[1].get("drug")
            active_ingredients = active_ingredients[0]["active_ingredients"]
            active_ingredients = active_ingredients[0]["name"]
            active_ingredients_list.append(active_ingredients)
        except Exception as e:
                print(e)
    return active_ingredients_list



def life_span():
    life_span_list = []
    connection = psycopg2.connect("postgres://postgres:e26519982@localhost:5432/postgres")
    connection.autocommit = True

    crs = connection.cursor()

    crs.execute("SELECT * FROM dogs LIMIT 10000")
    records = crs.fetchall()
    for record in records:
        try:
            life_span = record[2]

            life_span_list.append(life_span)
        except Exception as e:
                print(e)
    return life_span_list


def weight():
    weight_list = []
    connection = psycopg2.connect("postgres://postgres:e26519982@localhost:5432/postgres")
    connection.autocommit = True

    crs = connection.cursor()

    crs.execute("SELECT * FROM dogs LIMIT 10000")
    records = crs.fetchall()
    for record in records:
        try:
            weight = record[3]
            # print(reaction)

            weight_list.append(weight)
        except Exception as e:
                print(e)
    return weight_list


def names_of_dogs():
    name_list = []
    connection = psycopg2.connect("postgres://postgres:e26519982@localhost:5432/postgres")
    connection.autocommit = True

    crs = connection.cursor()

    crs.execute("SELECT * FROM dogs LIMIT 10000")
    records = crs.fetchall()
    for record in records:
        try:
            name = record[1]

            name_list.append(name)
        except Exception as e:
                print(e)
    return name_list



def master_function(query, index):
    list = []
    connection = psycopg2.connect("postgres://postgres:e26519982@localhost:5432/postgres")
    connection.autocommit = True

    crs = connection.cursor()

    crs.execute(query)
    records = crs.fetchall()
    for record in records:
        try:
            value = record[index]

            list.append(value)
        except Exception as e:
            print(e)
    return list
