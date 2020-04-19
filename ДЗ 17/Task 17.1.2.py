import sqlite3


# there is a musician database which consist of great musicians names and their genres
musicians = [(1, 'wolfgang', 'Mozart', 101),
            (2, 'Joseph', 'Haydn', 101),
            (3, 'Freddie', 'Mercury', 102),
            (4, 'Michael', 'Jackson', 102),
            (5, 'Brian', 'Johnson', 103),
            (6, 'Marilyn', 'Manson', 103),
             (7, 'Daniel', 'Reynolds', 103)]

genres = [(101, 'classic'),
          (102, 'pop'),
          (103, 'rock'),
          (104, 'indie')]

connection = sqlite3.connect('music_range.db')

connection.execute('''CREATE TABLE IF NOT EXISTS musicians (
                                                            musician_id INTEGER PRIMARY KEY,
                                                            first_name TEXT,
                                                            last_name TEXT,
                                                            genre TEXT,
                                                            
                                                            # tried to connect genres distribution in musicians table with genres table
                                                            FOREIGN KEY (genre) references genres(genre_id)
                                                            
                                                            # using CASCADE with UPDATE to modify with a new parent key
                                                            ON UPDATE CASCADE
                                                            )''')

connection.execute('''CREATE TABLE IF NOT EXISTS genres (
                                                            genre_id INTEGER PRIMARY KEY,
                                                            genre_name TEXT
                                                            )''')


# implementing data to new tables 
connection.executemany('''INSERT INTO musicians VALUES (?, ?, ?, ?)''', musicians)
connection.executemany('''INSERT INTO genres VALUES (?, ?)''', genres)

# trying to change Daniels Reynolds's music genre from rock to indie 
connection.execute('''UPDATE musicians set genre = 104 where musician_id = 7''')

# adding new genre in a genres table eith id = 105
connection.execute('''INSERT INTO genres VALUES (105, 'something_new')''')

# deleting added genre cause there is noone who could be related with this one
connection.execute('''DELETE FROM genres WHERE genre_id = 105''')

connection.commit()
connection.close()
