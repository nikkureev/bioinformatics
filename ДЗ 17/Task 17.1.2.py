import sqlite3

import pandas as pd

# there is a musician database which consist of great musicians names and their genres


ms = pd.read_csv('C:/Python/musicians.csv', sep=' ', header=None)
musicians = [(i[0], str(i[1]), str(i[2]), i[3]) for i in ms.itertuples(index=False)]

gs = pd.read_csv('C:/Python/genres_new.csv', sep=' ')
genres = [(i[0], str(i[1])) for i in gs.itertuples(index=False)]

# now we have the folloing:

# musicians = [(1, 'wolfgang', 'Mozart', 101),
#            (2, 'Joseph', 'Haydn', 101),
#            (3, 'Freddie', 'Mercury', 102),
#            (4, 'Michael', 'Jackson', 102),
#            (5, 'Brian', 'Johnson', 103),
#            (6, 'Marilyn', 'Manson', 103),
#             (7, 'Daniel', 'Reynolds', 103)]

#genres = [(101, 'classic'),
#          (102, 'pop'),
#          (103, 'rock'),
#          (104, 'indie')]

connection = sqlite3.connect('music_range.db')

# tried to connect genres distribution in musicians table with genres table
# using CASCADE with UPDATE to modify with a new parent key

connection.execute('''CREATE TABLE IF NOT EXISTS musicians (
                                                            musician_id INTEGER PRIMARY KEY,
                                                            first_name TEXT,
                                                            last_name TEXT,
                                                            genre TEXT,
                                                            
                                                            FOREIGN KEY (genre) references genres(genre_id)
                                                            
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
