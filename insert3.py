import cx_Oracle

try:
    # Establish a connection to the Oracle database
    con = cx_Oracle.connect('system/oracle_1234@localhost:1521/xe')
    cursor = con.cursor()

    # Insert data into the Stars table
    stars_data = [
        (1, 'Sun'),
        (2, 'Cassiopeiae'),
        (3, 'Achernar'),
        (4, 'Botein'),
        (5, 'Castor'),
        (6, 'Ceibo'),
        (7, 'Chara'),
        (8, 'Citadelle'),
        (9, 'Copernicus'),
        (10, 'Cujam')
    ]
    cursor.executemany("INSERT INTO Stars (star_id, star_name) VALUES (:1, :2)", stars_data)

    # Insert data into the Spacecrafts table

    spacecraft_data = [
         (1, 'SpaceX Dragon', 'SpaceX', '2010-12-08'),
    (2, 'Soyuz', 'Roscosmos', '1966-11-28'),
    (3, 'Chang\'e 5', 'CNSA', '2007-10-24'),
    (4, 'Viking', 'NASA', '1975-08-20'),
    (5, 'Pioneer', 'NASA', '1972-03-02'),
    (6, 'Cassini', 'NASA', '1997-10-15'),
    (7, 'New Horizons', 'NASA', '2006-01-19'),
    (8, 'Hubble Space Telescope', 'NASA', '1990-04-24'),
    (9, 'Saturn V', 'NASA', '1967-11-09'),
    (10, 'Apollo Lunar Module', 'NASA', '1966-02-10'),
        # Add more spacecraft data as needed
    ]
    cursor.executemany("INSERT INTO Spacecrafts (spacecraft_id, spacecraft_name, manufacturer, inaugural_date) VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'))", spacecraft_data)

    # Insert data into the Missions table
   

    # Insert data into the Astronauts table
    astronauts_data = [
        (1, 'Neil Armstrong', 'American', '1930-08-05'),
        (2, 'Yuri Gagarin', 'Russian', '1934-03-09'),
        (3, 'Buzz Aldrin', 'American', '1930-01-20'),
        (4, 'Sally Ride', 'American', '1951-05-26'),
        (5, 'Valentina Tereshkova', 'Russian', '1937-03-06'),
        (6, 'John Glenn', 'American', '1921-07-18'),
        (7, 'Kalpana Chawla', 'Indian', '1961-03-17'),
        (8, 'Chris Hadfield', 'Canadian', '1959-08-29'),
        (9, 'Mae Jemison', 'American', '1956-10-17'),
        (10, 'Guion Bluford', 'American', '1942-11-22')
    ]
    cursor.executemany("INSERT INTO Astronauts (astronaut_id, astronaut_name, nationality, birth_date) VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'))", astronauts_data)

    # Insert data into the Planets table
    planets_data = [
        (1, 'Mercury', 4879, 0.39, 0),
        (2, 'Venus', 12104, 0.72, 0),
        (3, 'Earth', 12756, 1.0, 1),
        (4, 'Mars', 6792, 1.52, 2),
        (5, 'Jupiter', 139822, 5.2, 79),
        (6, 'Saturn', 116464, 9.58, 82),
        (7, 'Uranus', 50724, 19.22, 27),
        (8, 'Neptune', 49244, 30.05, 14),
        (9, 'Pluto', 2376, 39.48, 5),
        (10, 'Eris', 2326, 67.66, 1)
    ]
    cursor.executemany("INSERT INTO Planets (planet_id, planet_name, diameter, distance_from_sun, number_of_moons,host_star) VALUES (:1, :2, :3, :4, :5)", planets_data)

    # Insert data into the Exoplanets table
    exoplanets_data = [
        (1, 'Proxima b', 'Transit', 2016, 4.24, 2),
        (2, 'HD 209458 b', 'Transit', 1999, 153, 2),
        (3, 'Kepler-186f', 'Transit', 2014, 582, 3),
        (4, 'TRAPPIST-1d', 'Transit', 2017, 39.6,4),
        (5, 'Gliese 581g', 'Radial Velocity', 2010, 20.3,4),
        (6, 'WASP-121b', 'Transit', 2016, 900, 5),
        (7, 'TOI-700d', 'Transit', 2020, 101.4, 5),
        (8, 'Kepler-22b', 'Transit', 2011, 620,5),
        (9, 'GJ 1214 b', 'Transit', 2009, 42.4, 5),
        (10, '51 Pegasi b', 'Radial Velocity', 1995, 50.9, 6)
    ]
    cursor.executemany("INSERT INTO Exoplanets (exoplanet_id, exoplanet_name, discovery_method, discovery_year, distance_from_earth, host_star_id) VALUES (:1, :2, :3, :4, :5, :6)", exoplanets_data)

    # Insert data into the Launch_Sites table
    launch_sites_data = [
        (1, 'Kennedy Space Center', 'USA', 28.5721, -80.648),
        (2, 'Baikonur Cosmodrome', 'Russia', 45.965, 63.305),
        (3, 'Guiana Space Centre', 'France', 5.239, -52.768),
        (4, 'Vostochny Cosmodrome', 'Russia', 51.857, 128.333),
        (5, 'Wenchang Spacecraft Launch Site', 'China', 19.614, 110.951),
        (6, 'Tanegashima Space Center', 'Japan', 30.385, 130.967),
        (7, 'Satish Dhawan Space Centre', 'India', 13.733, 80.235),
        (8, 'Alcantara Space Center', 'Brazil', -2.373, -44.396),
        (9, 'Spaceport America', 'USA', 32.990, -106.974),
        (10, 'Mojave Air and Space Port', 'USA', 35.059, -118.151)
    ]
    cursor.executemany("INSERT INTO Launch_Sites (launch_site_id, launch_site_name, country, latitude, longitude) VALUES (:1, :2, :3, :4, :5)", launch_sites_data)

    # Insert data into the Space_Events table
    space_events_data = [
        (1, 'Mars Rover Landing', '2021-02-18', 'Successful'),
        (2, 'Chandrayaan-2 Mission', '2019-07-22' ,'Partial Success'),
        (3, 'Crew Dragon Demo-2 Launch', '2020-05-30', 'Successful'),
        (4, 'Hubble Space Telescope Launch', '1990-04-24', 'Successful'),
        (5, 'Mars InSight Landing', '2018-11-26', 'Successful'),
        (6, 'Voyager 1 Launch', '1977-09-05', 'Successful'),
        (7, 'Apollo 11 Moon Landing', '1969-07-20', 'Successful'),
        (8, 'Sputnik 1 Launch', '1957-10-04', 'Successful'),
        (9, 'Cassini-Huygens Mission', '1997-10-15', 'Successful'),
        (10, 'SpaceX Starship Test Flight', '2021-12-09','Successful')
    ]
    cursor.executemany("INSERT INTO Space_Events (event_id, event_name, event_date, description) VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), :4)", space_events_data)

    # Insert data into the Space_Agencies table
    space_agencies_data = [
        (1, 'NASA', 'USA', 1958),
        (2, 'Roscosmos', 'Russia', 1955),
        (3, 'ESA', 'Europe', 1975),
        (4, 'ISRO', 'India', 1969),
        (5, 'CNSA', 'China', 1993),
        (6, 'JAXA', 'Japan', 2003),
        (7, 'AEB', 'Brazil', 1994),
        (8, 'Virgin Galactic', 'USA', 2004),
        (9, 'SpaceX', 'USA', 2002),
        (10, 'Blue Origin', 'USA', 2000)
    ]
    cursor.executemany("INSERT INTO Space_Agencies (agency_id, agency_name, country, establishment_year) VALUES (:1, :2, :3, :4)", space_agencies_data)

    # Insert data into the Space_Exploration_Budgets table
    budgets_data = [
        (1, 1, 25000000000),
        (2, 2, 10000000000),
        (3, 3, 15000000000),
        (4, 4, 2000000000),
        (5, 5, 8000000000),
        (6, 6, 3000000000),
        (7, 7, 500000000),
        (8, 8, 1000000000),
        (9, 9, 12000000000),
        (10, 10, 5000000000)
    ]
    missions_data = [
        (1, 'Apollo 11', '1969-07-16', 'Moon', 8, 'Completed', 1,1),
        (2, 'Vostok 1', '1961-04-12', 'Low Earth Orbit', 1, 'Completed', 2,2),
        (3, 'SpaceX CRS-1', '2012-10-08', 'International Space Station', 23, 'Completed', 1,1),
        (4, 'Chang\'e 5', '2020-11-23', 'Moon', 23, 'Completed', 3,3),
        (5, 'Viking 1', '1975-08-20', 'Mars', 6, 'Completed', 4,4),
        (6, 'Pioneer 10', '1972-03-02', 'Jupiter', 21, 'Completed', 5,5),
        (7, 'Cassini-Huygens', '1997-10-15', 'Saturn', 20, 'Completed', 6,6),
        (8, 'New Horizons', '2006-01-19', 'Pluto', 9, 'Completed', 7,7),
        (9, 'Hubble Space Telescope', '1990-04-24', 'Low Earth Orbit', 31, 'Active', 8,8),
        (10, 'Apollo 13', '1970-04-11', 'Moon', 6, 'Failed', 9,9)
    ]
    cursor.executemany("INSERT INTO Missions (mission_id, mission_name, launch_date, destination, duration, mission_status, spacecraft_id) VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), :4, :5, :6, :7)", missions_data)
    cursor.executemany("INSERT INTO Space_Exploration_Budgets (mission_id, agency_id, budget_amount) VALUES (:1, :2, :3)", budgets_data)

    # Commit the changes to the database
    con.commit()
    print("Data inserted into tables successfully.")

except cx_Oracle.DatabaseError as e:
    error, = e.args
    print("Oracle Error encountered:", error.code)
    print(error.message)

finally:
    # Ensure the cursor and connection are closed properly
    if cursor:
        cursor.close()
    if con:
        con.close()
    print("Oracle connection is closed")
