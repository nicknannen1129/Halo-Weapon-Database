#Name: Halo Weapons Database Project
#Description: this database is for the purpose of storing data on all of the
#             different weapon types in the popular video game series Halo.
#             It includes many weapons from the game and information about
#             them such as what games they appear in and what faction they
#             are made by.
#Author: Nick Nannen
#Last Date Edited: 11/18/2020

#importing the SQLite module for database creation and manipulation
import sqlite3

#establishing a connection variable to connect to the database
connection = sqlite3.connect('halo_weapons_database.db')

#creating a cursor so the python code can write to the database in SQL
cursor = connection.cursor()

#printing a welcome banner
print("")
print("_____________________________________________________________________\
_________________________")
print("")
print("W E L C O M E    T O    T H E    H A L O    W E A P O N S    D A T A \
B A S E !")
print("_____________________________________________________________________\
_________________________")
print("")
print("(For best experience, use in fullscreen)")
print("")
#status messege for creating the tables in the database
print("Creating database...")

#SQL query for creating the new table to store the weapons in with their
#attributes
cursor.execute("""CREATE TABLE weapons (
        common_name text,
        technical_name text,
        faction text,
        PRIMARY KEY (common_name),
        FOREIGN KEY (faction) REFERENCES factions(type)
    )""")

#SQL query for creating the new game_weapons table to store which games the
#weapons appear in
cursor.execute("""CREATE TABLE game_weapons (
        name text,
        weapon text,
        PRIMARY KEY (name, weapon),
        FOREIGN KEY (weapon) REFERENCES weapons(common_name)
        FOREIGN KEY (name) REFERENCES halo_games(name)
    )""")

#SQL query for creating the new table halo_games that stores each Halo game
#and some info about it
cursor.execute("""CREATE TABLE halo_games (
        name text,
        year_released integer,
        month_released text,
        day_released integer,
        PRIMARY KEY (name),
        FOREIGN KEY (name) REFERENCES game_weapons(name)
    )""")

#SQL query that creates the table for the factions
cursor.execute("""CREATE TABLE factions (
        type text
    )""")

#committing the changes to the database
connection.commit()

#confirmation message to signify that database creation is done
print("DONE")
print("")

#variable that stores all of the 'human' weapon data for later insertion
human_weapons = [('Assault Rifle', 'MA5 Assault Rifle', 'Human'),
           ('Battle Rifle', 'BR55 Battle Rifle', 'Human'),
           ('Shotgun', 'DTM Close Assault Weapon System', 'Human'),
           ('Sniper Rifle', 'SRS99 Anti-Materiel Rifle', 'Human'),
           ('Rocket Launcher', 'M41 Rocket Launcher', 'Human'),
           ('SMG', 'M7/Caseless Submachine Gun', 'Human'),
           ('Machine Gun Turret', 'M247 General Purpose Machine Gun', \
            'Human')]

#variable that stores all of the 'covenant' weapon data for later insertion
covenant_weapons = [('Plasma Pistol', 'Type-25 Directed Energy Pistol', \
                     'Covenant'),
                    ('Plasma Rifle', 'Type-25 Directed Energy Rifle', \
                     'Covenant'),
                    ('Needler', 'Type-33 Guided Munitions Launcher', \
                     'Covenant'),
                    ('Beam Rifle', 'Particle Beam Rifle', 'Covenant'),
                    ('Brute Shot', 'Type-25 Brute Shot', 'Covenant'),
                    ('Energy Sword', 'Type-1 Energy Weapon', 'Covenant'),
                    ('Brute Plasma Rifle', 'Type-25 Brute plasma rifle', \
                     'Covenant'),
                    ('Needle Rifle', 'Type-31 needle rifle', 'Covenant'),
                    ('Mauler', 'Type-52 Pistol', 'Covenant'),
                    ('Spiker', 'Type-25 Carbine', 'Covenant'),
                    ('Carbine', 'Type-51 Carbine', 'Covenant'),
                    ('Focus Rifle', 'Applications Rifle', 'Covenant'),
                    ('Plasma Repeater', ' Type-51 Directed Energy Rifle', \
                     'Covenant'),
                    ('Gravity Hammer', 'Type-2 Energy Weapon', 'Covenant'),
                    ('Plasma Turret', \
                     'Type-52 Directed Energy Support Weapon', 'Covenant'),
                    ('Fuel-Rod Gun', 'Type-33 Light Anti-Armor Weapon', \
                     'Covenant')]

#variable that stores all of the 'forerunner' weapon data for later insertion
forerunner_weapons = [('Lightrifle', 'Z-250 Lightrifle', 'Forerunner'),
                      ('Boltshot', 'Z-110 Boltshot', 'Forerunner'),
                      ('Suppressor', 'Z-130 Suppressor', 'Forerunner'),
                      ('Binary Rifle', 'Z-750 Binary Rifle', 'Forerunner'),
                      ('Scattershot', 'Z-180 Scattershot', 'Forerunner'),
                      ('Incineration Cannon', 'Z-390 Incineration Cannon', \
                       'Forerunner'),
                      ('Splinter Turret', \
                       'Z-520 Encounter-Mitigation System', 'Forerunner'),
                      ('Sentinal Beam', 'Gold Aggressor Sentinel Beam', \
                       'Forerunner')]

#status message for inserting the weapons into their table
print("Loading Halo weapons...")

#SQL insertion statements for insertion of the weapon entities
cursor.executemany("INSERT INTO weapons VALUES (?,?,?)", human_weapons)
cursor.executemany("INSERT INTO weapons VALUES (?,?,?)", covenant_weapons)
cursor.executemany("INSERT INTO weapons VALUES (?,?,?)", forerunner_weapons)

#confirmation message that signals insertion of weapons is complete
print("DONE")
print("")

#variable that stores all of the 'Halo CE' weapon/game data for later
#insertion
weapon_games_CE = [('Halo CE', 'Assault Rifle'),
                   ('Halo CE', 'Shotgun'),
                   ('Halo CE', 'Sniper Rifle'),
                   ('Halo CE', 'Rocket Launcher'),
                   ('Halo CE', 'Plasma Pistol'),
                   ('Halo CE', 'Plasma Rifle'),
                   ('Halo CE', 'Needler'),
                   ('Halo CE', 'Fuel-Rod Gun')]

#variable that stores all of the 'Halo 2' weapon/game data for later
#insertion
weapon_games_2 = [('Halo 2', 'Battle Rifle'),
                  ('Halo 2', 'Shotgun'),
                  ('Halo 2', 'Sniper Rifle'),
                  ('Halo 2', 'Rocket Launcher'),
                  ('Halo 2', 'Machine Gun Turret'),
                  ('Halo 2', 'SMG'),
                  ('Halo 2', 'Plasma Pistol'),
                  ('Halo 2', 'Plasma Rifle'),
                  ('Halo 2', 'Brute Plasma Rifle'),
                  ('Halo 2', 'Needler'),
                  ('Halo 2', 'Beam Rifle'),
                  ('Halo 2', 'Brute Shot'),
                  ('Halo 2', 'Energy Sword'),
                  ('Halo 2', 'Carbine'),
                  ('Halo 2', 'Plasma Turret'),
                  ('Halo 2', 'Sentinal Beam')]

#variable that stores all of the 'Halo 3' weapon/game data for later
#insertion
weapon_games_3 = [('Halo 3', 'Assault Rifle'),
                  ('Halo 3', 'Battle Rifle'),
                  ('Halo 3', 'Shotgun'),
                  ('Halo 3', 'SMG'),
                  ('Halo 3', 'Sniper Rifle'),
                  ('Halo 3', 'Rocket Launcher'),
                  ('Halo 3', 'Machine Gun Turret'),
                  ('Halo 3', 'Plasma Pistol'),
                  ('Halo 3', 'Plasma Rifle'),
                  ('Halo 3', 'Needler'),
                  ('Halo 3', 'Brute Plasma Rifle'),
                  ('Halo 3', 'Beam Rifle'),
                  ('Halo 3', 'Brute Shot'),
                  ('Halo 3', 'Energy Sword'),
                  ('Halo 3', 'Mauler'),
                  ('Halo 3', 'Spiker'),
                  ('Halo 3', 'Carbine'),
                  ('Halo 3', 'Gravity Hammer'),
                  ('Halo 3', 'Plasma Turret'),
                  ('Halo 3', 'Fuel-Rod Gun'),
                  ('Halo 3', 'Sentinal Beam')]

#variable that stores all of the 'Halo Reach' weapon/game data for later
#insertion
weapon_games_reach = [('Halo Reach', 'Assault Rifle'),
                      ('Halo Reach', 'Shotgun'),
                      ('Halo Reach', 'Sniper Rifle'),
                      ('Halo Reach', 'Rocket Launcher'),
                      ('Halo Reach', 'Machine Gun Turret'),
                      ('Halo Reach', 'Plasma Pistol'),
                      ('Halo Reach', 'Needler'),
                      ('Halo Reach', 'Brute Shot'),
                      ('Halo Reach', 'Energy Sword'),
                      ('Halo Reach', 'Needle Rifle'),
                      ('Halo Reach', 'Spiker'),
                      ('Halo Reach', 'Focus Rifle'),
                      ('Halo Reach', 'Plasma Repeater'),
                      ('Halo Reach', 'Gravity Hammer'),
                      ('Halo Reach', 'Plasma Turret'),
                      ('Halo Reach', 'Fuel-Rod Gun')]

#variable that stores all of the 'Halo 4' weapon/game data for later
#insertion
weapon_games_4 = [('Halo 4', 'Assault Rifle'),
                  ('Halo 4', 'Battle Rifle'),
                  ('Halo 4', 'Shotgun'),
                  ('Halo 4', 'Sniper Rifle'),
                  ('Halo 4', 'Rocket Launcher'),
                  ('Halo 4', 'Plasma Pistol'),
                  ('Halo 4', 'Needler'),
                  ('Halo 4', 'Beam Rifle'),
                  ('Halo 4', 'Energy Sword'),
                  ('Halo 4', 'Carbine'),
                  ('Halo 4', 'Gravity Hammer'),
                  ('Halo 4', 'Fuel-Rod Gun'),
                  ('Halo 4', 'Lightrifle'),
                  ('Halo 4', 'Boltshot'),
                  ('Halo 4', 'Suppressor'),
                  ('Halo 4', 'Binary Rifle'),
                  ('Halo 4', 'Scattershot'),
                  ('Halo 4', 'Incineration Cannon')]

#variable that stores all of the 'Halo 5: Guardians' weapon/game data for
#later insertion
weapon_games_5 = [('Halo 5: Guardians', 'Assault Rifle'),
                  ('Halo 5: Guardians', 'Battle Rifle'),
                  ('Halo 5: Guardians', 'Shotgun'),
                  ('Halo 5: Guardians', 'Sniper Rifle'),
                  ('Halo 5: Guardians', 'Rocket Launcher'),
                  ('Halo 5: Guardians', 'SMG'),
                  ('Halo 5: Guardians', 'Plasma Pistol'),
                  ('Halo 5: Guardians', 'Needler'),
                  ('Halo 5: Guardians', 'Beam Rifle'),
                  ('Halo 5: Guardians', 'Energy Sword'),
                  ('Halo 5: Guardians', 'Brute Plasma Rifle'),
                  ('Halo 5: Guardians', 'Carbine'),
                  ('Halo 5: Guardians', 'Gravity Hammer'),
                  ('Halo 5: Guardians', 'Fuel-Rod Gun'),
                  ('Halo 5: Guardians', 'Lightrifle'),
                  ('Halo 5: Guardians', 'Boltshot'),
                  ('Halo 5: Guardians', 'Suppressor'),
                  ('Halo 5: Guardians', 'Binary Rifle'),
                  ('Halo 5: Guardians', 'Scattershot'),
                  ('Halo 5: Guardians', 'Incineration Cannon'),
                  ('Halo 5: Guardians', 'Splinter Turret'),
                  ('Halo 5: Guardians', 'Sentinal Beam')]

#status message for insertion of weapon/game data
print("Applying Halo games to weapons...")

#SQL statements for inserting weapon/game data into the table
cursor.executemany("INSERT INTO game_weapons VALUES (?,?)", weapon_games_CE)
cursor.executemany("INSERT INTO game_weapons VALUES (?,?)", weapon_games_2)
cursor.executemany("INSERT INTO game_weapons VALUES (?,?)", weapon_games_3)
cursor.executemany("INSERT INTO game_weapons VALUES (?,?)", \
                    weapon_games_reach)
cursor.executemany("INSERT INTO game_weapons VALUES (?,?)", weapon_games_4)
cursor.executemany("INSERT INTO game_weapons VALUES (?,?)", weapon_games_5)

#confirmation message that weapon/game data has finished inserting
print("DONE")
print("")

#variable for storing Halo games for later insertion
halo_games = [('Halo CE', '2001', 'November', '15'),
              ('Halo 2', '2004', 'November', '9'),
              ('Halo 3', '2007', 'September', '25'),
              ('Halo Reach', '2010', 'September', '14'),
              ('Halo 4', '2012', 'November', '6'),
              ('Halo 5: Guardians', '2015', 'October', '27')]

#status message for the insertion of the halo games into their desagnated
#table
print("Loading Halo game data...")

#SQL for inserting the halo games into their database
cursor.executemany("INSERT INTO halo_games VALUES (?,?,?,?)", halo_games)

#confirmation message showing that insertion was successful
print("DONE")
print("")

#status message for inserting the factions
print("Loading factions...")

#SQL code for inserting each faction into its desagnated table
cursor.execute("INSERT INTO factions VALUES ('Human')")
cursor.execute("INSERT INTO factions VALUES ('Covenant')")
cursor.execute("INSERT INTO factions VALUES ('Forerunner')")

#confiramtion message indecating that insertion of factions is complete
print("DONE")
print("")

#commiting the changes we have made to the database
connection.commit()

#confirmation message that the database has finished being rendered and is
#now ready to be used
print("D a t a b a s e   i s   r e a d y   f o r   u s e !")
print("_____________________________________________________________________\
_________________________")
#formatting rules for functions so user does not get confused on how to
#operate the variaous funcitons included with this database
print("")
print("DATABASE FORMATTING RULES:")
print("")
print("  - All function arguements should be input as strings ('...')")
print("")
print("  - Any arguement for the game that a Halo weapon is in should be \
input")
print("    as a tuple, even if there is only one arguement \
(ex: ('Halo 3',))")
print("")
print("  - For a full list of availible functions, use the function \
'display_functions()'")
print("_____________________________________________________________________\
_________________________")
print("")

#closing the connection to the database since initial database modification
#is done 
connection.close()

#Name: add_new_weapon
#Description: adds a new weapon entity to the database in both the weapons
#             table as well as updating the game_weapons table to reflect
#             the changes.
#Parameters:
#       common_name: the commonly known name for the weapon
#       technical_name: the technical name for the weapon
#       faction: the faction who made the weapon
#       halo_games: a tuple of all of the Halo games the weapon has appeared
#                   in
#Output: adds a new weapon to the weapons and game_weapons tables
#Author: Nick Nannen
def add_new_weapon(common_name, technical_name, faction, halo_games):
    
    #connecting to the database and creating a cursor
    connect = sqlite3.connect('halo_weapons_database.db')
    curs = connect.cursor()

    #executing SQL code to check if the weapon name is already in the
    #database and therefore would cause duplicate data to be inserted
    curs.execute("SELECT COUNT(*) FROM weapons WHERE common_name = (?)", \
                 (common_name,))
    #the resulting tuple is stored in the result variable
    result = (curs.fetchall())[0]

    #if statement determines if the weapon is in the database already.
    if (result[0] <= 0):

        #SQL code executes if the weapon is not already in the database
        curs.execute("INSERT INTO weapons VALUES (?,?,?)", (common_name, \
                                                            technical_name, \
                                                            faction))

        #for loop iterates through the Halo games that the weapon is a part
        #of in the tuple parameter
        for game in halo_games:

            #SQL code executes to insert the weapon/game data into the
            #game_weapons table
            curs.execute("INSERT INTO game_weapons VALUES (?,?)", \
                         (game, common_name))

        #confirmation message for when insertion is successful
        print("")
        print("You have successfully added the " + common_name + " to the \
database!")
        print("")

    #condition executes when the weapon is already in the database
    else:
        print("")
        print("This weapon is already in the database")
        print("")

    #committing the changes made to the database and closing the connection
    #to the database
    connect.commit()
    connect.close()
    
#Name: remove_weapon
#Description: removes a weapon from both the weapons table as well as the
#             game_weapons table
#Parameters:
#       common_name: the commonly known name for the weapon
#Output: removes a weapon from the weapons and game_weapons tables
#Author: Nick Nannen
def remove_weapon(common_name):
    
    #connecting to the database and creating a cursor
    connect = sqlite3.connect('halo_weapons_database.db')
    curs = connect.cursor()

    #executing SQL code to check if the weapon name is in the
    #database for removal
    curs.execute("SELECT COUNT(*) FROM weapons WHERE common_name = (?)", \
                 (common_name,))

    #the resulting tuple is stored in the result variable
    result = (curs.fetchall())[0]

    #if statement executes if the weapon name isn't in the database
    if (result[0] <= 0):

        #prints message that the weapon isn't found in the database
        print("")
        print("This weapon does not exist in this database")
        print("")

        #returns from the function to prevent deletion
        return

    #SQL statements executes to delete the specified weapon
    curs.execute("DELETE from weapons WHERE common_name = (?)", \
                 (common_name,))
    curs.execute("DELETE from game_weapons WHERE weapon = (?)", \
                 (common_name,))

    #confirmation message shows that weapon was successfully
    #deleted
    print("")
    print("You have successfully deleted the " + common_name)
    print("")

    #committing the changes made to the database and closing the
    #connection to the database
    connect.commit()
    connect.close()

#Name: display_by_game
#Description: displays all of the weapons in a specified Halo game
#Parameters:
#       game: the the game whose weapons you want displayed
#Output: displays to the user a table of weapons and their
#        attributes in the specified game
#Author: Nick Nannen
def display_by_game(game):
    
    #connecting to the database and creating a cursor
    connect = sqlite3.connect('halo_weapons_database.db')
    curs = connect.cursor()

    #string formatting for title and column headers for the output table
    print("")
    print(game + ":")
    print("_________________________________________________________________\
_____________________________")
    print("Common Name:" + "\t\t\t" + "Technical Name:" + "\t\t\t\t" + "Fact\
ion:")
    print("-----------------------------------------------------------------\
-----------------------------")

    #SQL code executes to find all weapons that are associated with the
    #specified game in the game_weapons table
    curs.execute("SELECT weapon FROM game_weapons WHERE name = (?)", (game,))
    
    #tuples are stored in the variable 'weapons'
    weapons = curs.fetchall()

    #for loop iterates through all of the tuples in the weapons variable
    for weapon in weapons:

        #SQL retrieves all of the weapon tuples in the weapons table
        curs.execute("SELECT * FROM weapons WHERE common_name = (?)", \
                     (weapon))
        disp_weapons = curs.fetchall()

        #for loop prints out each weapon to the user
        for item in disp_weapons:
            print(item[0] + "\t\t\t" + item[1] + "\t\t\t" + item[2])

    #seperator line
    print("")
    print("_________________________________________________________________\
_____________________________")
    print("")

    #committing the changes made to the database and closing the connection
    #to the database
    connect.commit()
    connect.close()

#Name: update_weapon
#Description: updates the fields of a weapon entity to reflect the changes
#             specifed by the user
#Parameters:
#       old_common_name: the previous common_name value for a weapon
#       new_common_name: the updated name that will replace the
#                        old_common_name in the weapon entity
#       technical_name: the technical name for the weapon
#       faction: the faction who made the weapon
#       games: a tuple of all of the Halo games the weapon has appeared
#              in
#Output: updates the weapon entities specified by the user
#Author: Nick Nannen
def update_weapon(old_common_name, new_common_name, technical_name, \
                  faction, games):
    
    #connecting to the database and creating a cursor
    connect = sqlite3.connect('halo_weapons_database.db')
    curs = connect.cursor()

    #SQL code executes and updates the weapons table with the new information
    curs.execute("""UPDATE weapons SET common_name = (?),
                                       technical_name = (?),
                                       faction = (?)
                 WHERE common_name = (?)""", \
                 (new_common_name, technical_name, faction, old_common_name))

    
    for game in games:
        print("")
        print("Checking for duplicate data...")
        print("")

        #executing SQL code to check if the weapon name is already in the
        #database for updating or if a new entity needs to be created
        curs.execute("SELECT COUNT(*) FROM game_weapons WHERE weapon = (?) \
AND name = (?)", (old_common_name, game))

        #the resulting tuple is stored in the result variable
        result = (curs.fetchall())[0]
        curs.execute("SELECT COUNT(*) FROM game_weapons WHERE weapon = (?) \
AND name = (?)", (new_common_name, game))
        dup_check = (curs.fetchall())[0]

        if (result[0] <= 0 and dup_check[0] <= 0):
            curs.execute("INSERT INTO game_weapons VALUES (?,?)", \
                         (game, new_common_name))
        elif (dup_check[0] <= 0):
            curs.execute("""UPDATE game_weapons SET weapon = (?)
                            WHERE weapon = (?) AND name = (?)""", \
                         (new_common_name, old_common_name, game))
        else:
            curs.execute("SELECT name, weapon FROM game_weapons WHERE \
weapon = (?) AND name = (?)", (new_common_name, game))
            dup_game_info = (curs.fetchall())[0]

            print("")
            print("This game and weapon information for the " + \
                  dup_game_info[1] + " in " + dup_game_info[0] + \
                  " is already in the database")
            return

    print("")
    print("Information for the " + new_common_name + \
              " updated successfully!")
    print("")
    print("_____________________________________________________________\
_________________________________")

    #committing the changes made to the database and closing the connection
    #to the database
    connect.commit()
    connect.close()

#Name: add_game
#Description: adds a game specified by the user to the database
#Parameters:
#       game_title: the title of the Halo game being inserted into the
#                   database
#       release_year: the year the game was released
#       release_month: the month the game was released
#       release_day: the day that the game was released
#Output: adds a game to the database
#Author: Nick Nannen
def add_game(game_title, release_year, release_month, release_day):

    #connecting to the database and creating a cursor
    connect = sqlite3.connect('halo_weapons_database.db')
    curs = connect.cursor()

    #executing SQL code to check if the game name is already in the
    #database and therefore would cause duplicate data to be inserted
    curs.execute("SELECT COUNT(*) FROM halo_games WHERE name = (?)", \
                 (game_title,))

    #the resulting tuple is stored in the result variable
    result = (curs.fetchall())[0]

    if (result[0] <= 0):
            curs.execute("INSERT INTO halo_games VALUES (?,?,?,?)", \
                         (game_title, release_year, release_month, \
                          release_day))

            print("")
            print("You have successfully added " + game_title + \
                  " to the database!")
            print("")
    else:
        print("")
        print("This game is already in the database")
        print("")

    #committing the changes made to the database and closing the connection
    #to the database
    connect.commit()
    connect.close()

#Name: remove_game
#Description: removes the specified game form the database
#Parameters:
#       game_title: the title of the game being deleted from the
#                   database
#Output: removes a game from the database
#Author: Nick Nannen
def remove_game(game_title):

    #connecting to the database and creating a cursor
    connect = sqlite3.connect('halo_weapons_database.db')
    curs = connect.cursor()

    #executing SQL code to check if the game name is in the database
    #for removal
    curs.execute("SELECT COUNT(*) FROM halo_games WHERE name = (?)", \
                 (game_title,))

    #the resulting tuple is stored in the result variable
    result = (curs.fetchall())[0]

    if (result[0] <= 0):
        print("")
        print("This game does not exist in this database")
        print("")
        return

    curs.execute("DELETE FROM halo_games WHERE name = (?)", (game_title,))
    curs.execute("DELETE FROM game_weapons WHERE name = (?)", (game_title,))

    print("")
    print("You have successfully deleted " + game_title + \
          " from the database")
    print("")

    #committing the changes made to the database and closing the connection
    #to the database
    connect.commit()
    connect.close()

#Name: add_faction
#Description: adds a faction specified by the user to the database
#Parameters:
#       faction_name: the name of the faction that is being added
#                     to the database
#Output: adds a faction to the database
#Author: Nick Nannen
def add_faction(faction_name):

    #connecting to the database and creating a cursor
    connect = sqlite3.connect('halo_weapons_database.db')
    curs = connect.cursor()

    #executing SQL code to check if the faction name is already in the
    #database and therefore would cause duplicate data to be inserted
    curs.execute("SELECT COUNT(*) FROM factions WHERE type = (?)", \
                 (faction_name,))

    #the resulting tuple is stored in the result variable
    result = (curs.fetchall())[0]

    if (result[0] <= 0):
            curs.execute("INSERT INTO factions VALUES (?)", (faction_name,))

            print("")
            print("You have successfully added the " + faction_name + \
                  " faction to the database!")
            print("")
    else:
        print("")
        print("This faction is already in the database")
        print("")

    #committing the changes made to the database and closing the connection
    #to the database
    connect.commit()
    connect.close()

#Name: remove_faction
#Description: removes a faction from the database
#Parameters:
#       faction_name: the name of the faction to be removed from the
#                     database
#Output: removes a faction from the database
#Author: Nick Nannen
def remove_faction(faction_name):

    #connecting to the database and creating a cursor
    connect = sqlite3.connect('halo_weapons_database.db')
    curs = connect.cursor()

    #executing SQL code to check if the faction name is in the
    #database for removal
    curs.execute("SELECT COUNT(*) FROM factions WHERE type = (?)", \
                 (faction_name,))

    #the resulting tuple is stored in the result variable
    result = (curs.fetchall())[0]

    if (result[0] <= 0):
        print("")
        print("This faction does not exist in this database")
        print("")
        return

    curs.execute("DELETE from factions WHERE type = (?)", (faction_name,))

    print("")
    print("You have successfully deleted the " + faction_name + " faction")
    print("")

    #committing the changes made to the database and closing the connection
    #to the database
    connect.commit()
    connect.close()

#Name: display_all_weapons
#Description: displays a table to the user that displays all of the weapons
#             that are currently in the database
#Parameters: none
#Output: displays all weapons currently in the database
#Author: Nick Nannen
def display_all_weapons():

    #connecting to the database and creating a cursor
    connect = sqlite3.connect('halo_weapons_database.db')
    curs = connect.cursor()

    print("_________________________________________________________________\
_____________________________")
    print("Common Name:" + "\t\t\t" + "Technical Name:" + "\t\t\t\t" + \
          "Faction:")
    print("-----------------------------------------------------------------\
-----------------------------")

    curs.execute("SELECT * FROM weapons ORDER BY faction DESC")
    weapons = curs.fetchall()

    for weapon in weapons:
        print(weapon[0] + "\t\t\t" + weapon[1] + "\t\t\t" + weapon[2])

    print("")
    print("_________________________________________________________________\
_____________________________")
    print("")

    #committing the changes made to the database and closing the connection
    #to the database
    connect.commit()
    connect.close()

def display_all_games():

    #connecting to the database and creating a cursor
    connect = sqlite3.connect('halo_weapons_database.db')
    curs = connect.cursor()

    print("_________________________________________________________________\
_____________________________")
    print("Game Title:" + "\t\t\t\t" + "Release Information:")
    print("-----------------------------------------------------------------\
-----------------------------")

    curs.execute("SELECT * FROM halo_games ORDER BY year_released DESC")
    games = curs.fetchall()

    for game in games:
        print(game[0] + "\t\t\t\t\t" + game[2] + "\t" + str(game[3]) + "\t" \
              + str(game[1]))

    print("_________________________________________________________________\
_____________________________")
    print("")

    #committing the changes made to the database and closing the connection
    #to the database
    connect.commit()
    connect.close()

def display_all_factions():

    #connecting to the database and creating a cursor
    connect = sqlite3.connect('halo_weapons_database.db')
    curs = connect.cursor()

    print("_________________________________________________________________\
_____________________________")
    print("Halo Factions")
    print("-----------------------------------------------------------------\
-----------------------------")

    curs.execute("SELECT * FROM factions ORDER BY type DESC")
    factions = curs.fetchall()

    for faction in factions:
        print(faction[0])

    print("_________________________________________________________________\
_____________________________")
    print("")

    #committing the changes made to the database and closing the connection
    #to the database
    connect.commit()
    connect.close()

def display_all():

    display_all_weapons()
    
    print("=================================================================\
=============================")
    
    display_all_games()

    print("=================================================================\
=============================")

    display_all_factions()

#Name: display_functions
#Description: displays text that shows all of the functions that are availible
#             to the user for calling
#Parameters: none
#Output: prints text to the screen showing all availible functions
#Author: Nick Nannen
def display_functions():

    print("Here are all of the availible functions associated with this \
database:")
    print("")
    print("  - add_new_weapon(common_name, technical_name, faction, \
halo_games)")
    print("       - common_name: the commonly known name of the weapon")
    print("       - technical_name: the technical designation of the weapon")
    print("       - faction: the faction that the weapon was created by")
    print("       - halo_games: a tuple of all the Halo games the weapon \
has appeared in")
    print("")
    print("  - remove_weapon(common_name)")
    print("       - common_name: the commonly known name of the weapon")
    print("")
    print("  - display_by_game(game)")
    print("       - game: the game whose weapons you would like displayed")
    print("")
    print("  - update_weapon(old_common_name, new_common_name, \
technical_name, faction, games)")
    print("       - old_common_name: the common name that the weapon was \
originally known by in the database")
    print("       - new_common_name: the new name you would like the weapon \
to be known by in the database")
    print("       - technical_name: the technical designation of the weapon")
    print("       - faction: the faction that the weapon was created by")
    print("       - games: a tuple of all the Halo games the weapon has \
appeared in")
    print("")
    print("  - add_game(game_title, release_year, release_month, \
release_day)")
    print("       - game_title: the title of the game")
    print("       - release_year: the year the game was released")
    print("       - release_month: the month the game was released")
    print("       - release_day: the day the game was released")
    print("")
    print("  - remove_game(game_title)")
    print("       - game_title: the title of the game")
    print("")
    print("  - add_faction(faction_name)")
    print("       - faction_name: the name of the faction you are adding")
    print("")
    print("  - remove_faction(faction_name)")
    print("       - faction_name: the name of the faction you are removing")
    print("")
    print("  - display_all_weapons()")
    print("")
    print("  - display_all_games()")
    print("")
    print("  - display_all_factions()")
    print("")
    print("  - display_all()")
    print("_________________________________________________________________\
_____________________________")
    print("")
