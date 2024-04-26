    exoplanets_data = [
        (1, 'Proxima b', 'Transit', 2016, 4.24, 1),
        (2, 'HD 209458 b', 'Transit', 1999, 153, 2),
        (3, 'Kepler-186f', 'Transit', 2014, 582, 3),
        (4, 'TRAPPIST-1d', 'Transit', 2017, 39.6, 4),
        (5, 'Gliese 581g', 'Radial Velocity', 2010, 20.3, 5),
        (6, 'WASP-121b', 'Transit', 2016, 900, 6),
        (7, 'TOI-700d', 'Transit', 2020, 101.4, 7),
        (8, 'Kepler-22b', 'Transit', 2011, 620, 8),
        (9, 'GJ 1214 b', 'Transit', 2009, 42.4, 9),
        (10, '51 Pegasi b', 'Radial Velocity', 1995, 50.9, 10)
    ]
    cursor.executemany("INSERT INTO Starborn_Exoplanets (exoplanet_id, exoplanet_name, discovery_method, discovery_year, distance_from_earth, host_star_id) VALUES (:1, :2, :3, :4, :5, :6)", exoplanets_data)
