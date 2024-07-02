import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    # Query 1: Select all fields for the studio table
    query1 = "SELECT studio_id, studio_name FROM studio"
    cursor.execute(query1)
    studios = cursor.fetchall()
    print("\n-- DISPLAYING Studio RECORDS --")
    for studio in studios:
        print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

    # Query 2: Select all fields for the genre table
    query2 = "SELECT genre_id, genre_name FROM genre"
    cursor.execute(query2)
    genres = cursor.fetchall()
    print("\n-- DISPLAYING Genre RECORDS --")
    for genre in genres:
        print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

    # Query 3: Select movie names and runtime for those movies that have a run time of less than two hours
    query3 = "SELECT film_name, film_runtime FROM film WHERE film_runtime < 120"
    cursor.execute(query3)
    short_films = cursor.fetchall()
    print("\n-- DISPLAYING Short Film RECORDS --")
    for film in short_films:
        print("Film Name: {}\nRuntime: {}\n".format(film[0], film[1]))

    # Query 4: Get a list of film names and directors ordered by director
    query4 = "SELECT film_name, film_director FROM film ORDER BY film_director"
    cursor.execute(query4)
    film_directors = cursor.fetchall()
    print("\n-- DISPLAYING Director RECORDS in ORDER --")
    for film_director in film_directors:
        print("Film Name: {}\nDirector: {}\n".format(film_director[0], film_director[1]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)

finally:
    cursor.close()
    db.close()