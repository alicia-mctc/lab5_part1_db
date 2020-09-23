import sqlite3

with sqlite3.connect('lab5_Sqlite_part1_db.sqlite') as conn:

    conn.execute('Create table record(name text, country text, number int ')

    name = input('Enter new record:  ')
    country = input('Enter country:  ')
    number = int(input('Enter number of catches: ')

    conn.execute('insert into record values  (?, ?, ?)', (name, country, number))


con.close()