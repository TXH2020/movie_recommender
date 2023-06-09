import psycopg2
conn=psycopg2.connect(host='localhost',user='postgres',password='mysecretpassword',dbname='moviegeek')
c=conn.cursor()
csv_loc='/opt/'
c.execute("COPY collector_log FROM '"+csv_loc+"log.csv'  WITH DELIMITER ',' CSV HEADER;")
c.execute("COPY moviegeeks_genre FROM '"+csv_loc+"movggenre.csv'  WITH DELIMITER ',' CSV HEADER;")
c.execute("COPY moviegeeks_movie FROM '"+csv_loc+"movgmov.csv'  WITH DELIMITER ',' CSV HEADER;")
c.execute("COPY analytics_rating FROM '"+csv_loc+"rating.csv'  WITH DELIMITER ',' CSV HEADER;")
c.execute("COPY movie_genre FROM '"+csv_loc+"movgenre.csv'  WITH DELIMITER ',' CSV HEADER;")
c.execute("COPY movie_description FROM '"+csv_loc+"desc.csv'  WITH DELIMITER ',' CSV HEADER;")
c.execute("COPY seeded_recs FROM '"+csv_loc+"seeded_recs.csv'  WITH DELIMITER ',' CSV HEADER;")
c.execute("COPY analytics_cluster FROM '"+csv_loc+"analytics_cluster.csv'  WITH DELIMITER ',' CSV HEADER;")
c.execute("COPY similarity FROM '"+csv_loc+"similarity.csv'  WITH DELIMITER ',' CSV HEADER;")
c.execute("COPY lda_similarity FROM '"+csv_loc+"lda_similarity.csv'  WITH DELIMITER ',' CSV HEADER;")
conn.commit()
c.close()
conn.close()

