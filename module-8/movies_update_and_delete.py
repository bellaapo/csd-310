import mysql.connector

# Establish a connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="movies_user",
    password="popcorn",
    database="movies"
)

# Create a cursor object
cursor = db.cursor()

def show_films(cursor, title):
    # Method to execute an inner join on all tables,
    # iterate over the dataset and output the results to the terminal window

    # Inner join query
    cursor.execute("select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")

    # Get the results from the cursor object
    films = cursor.fetchall()

    print("\n-- {} --".format(title))

    # Iterate over the film dataset and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

# Display films initially
show_films(cursor, "DISPLAYING FILMS")

# Insert a new film record
cursor.execute("""
    INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
    VALUES ('Gone Girl', '2014', '149', 'David Fincher', 
        (SELECT studio_id FROM studio WHERE studio_name = '20th Century Fox'), 
        (SELECT genre_id FROM genre WHERE genre_name = 'Drama'))
""")
db.commit()

# Display films after insert
show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

# Update the genre of the film "Alien" to "Horror"
cursor.execute("""
    UPDATE film
    SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror')
    WHERE film_name = 'Alien'
""")
db.commit()

# Display films after update
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

# Delete the film "Gladiator"
cursor.execute("""
    DELETE FROM film
    WHERE film_name = 'Gladiator'
""")
db.commit()

# Display films after delete
show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

# Close the cursor and database connection
cursor.close()
db.close()