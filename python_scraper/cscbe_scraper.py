import psycopg2
import requests
import os

conn = psycopg2.connect(
    dbname=os.environ.get('POSTGRES_DB'),
    user=os.environ.get('POSTGRES_USER'),
    password=os.environ.get('POSTGRES_PASSWORD'),
    host="postgres",
    port="5432"
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS scoreboard (
        id SERIAL PRIMARY KEY,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        team_id INTEGER,
        team_name TEXT,
        score INTEGER,
        last_flag INTEGER,
        institutions TEXT
    )
""")

# Commit des changements
conn.commit()

# Récupération des données depuis l'API
response = requests.get('https://platform.cybersecuritychallenge.be/scoreboard/data?round_id=36&competition_id=7')
if response.status_code == 200:
    json_data = response.json()['scoreboard']['scores']

    for team_data in json_data:
        team_id = team_data['id']  # ID de l'équipe

        # Création d'une liste pour stocker les noms des institutions associées à l'équipe
        institutions_list = [user['institution'] for user in team_data['users']]

        # Insertion des données dans la table 'scoreboard'
        cur.execute(
            "INSERT INTO scoreboard (team_id, team_name, score, last_flag, institutions) VALUES (%s, %s, %s, %s, %s)",
            (team_id, team_data['name'], team_data['score'], team_data['last_flag'], ','.join(institutions_list))
        )

conn.commit()

cur.close()
conn.close()
