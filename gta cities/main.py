import sqlite3

connection = sqlite3.connect("gta.db")
cursor = connection.cursor() # In charge of all our communication with out DB. 

# Create table of gta cities.
cursor.execute("create table gta (release_year integer, release_name text, city text)") #text means string here

release_list = [
    (1997, "Grand Theft Auto", "state of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos")
]

cursor.executemany("insert into gta values (?,?,?)", release_list) # Specify template, and the actual data.

#print database rows
for row in cursor.execute("select * from gta"):
	print(row)

#print specific rows 
print("************************************")
cursor.execute("select * from gta where city=:c", {"c": "Liberty City"})
gta_search = cursor.fetchall() # to do the above.
print(gta_search)



# Create table of gta cities, and its real inspiration city
cursor.execute("create table cities (gta_city text, real_city text)")
cursor.execute("insert into cities values (?,?)", ("Liberty City", "New York")) # This is just one row of data btw.
cursor.execute("select * from cities where gta_city=:c", {"c": "Liberty City"})
cities_search = cursor.fetchall()
print(cities_search)


# manipulate gta_search database data
# Replace (and print out) every instance of "Liberty City" with actual city, "New York"
print("************************************")
for i in gta_search:
	adjusted = [cities_search[0][1] if value==cities_search[0][0] else value for value in i]
	print(adjusted)

connection.close()

#https://www.youtube.com/watch?v=Ohj-CqALrwk