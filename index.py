import requests
import time
from dotenv import dotenv_values
from pymongo import MongoClient

config = dotenv_values('.env')

# API configuration
api_key = config['API_KEY']
cluster_link = config['MONGODB_CLUSTER_LINK']

# MongoDB configuration
client = MongoClient(cluster_link)
db = client['Database'] 
team_data_collection = db['Team Data'] 

#Id of different EPL teams
team_ids = [57, 58, 61, 62, 63, 64, 65, 66, 67, 73, 76, 338, 340, 341, 351, 354, 397, 402, 563, 1044]

for team_id in team_ids:
    url = f'https://api.football-data.org/v4/teams/{team_id}'
    headers = {'X-Auth-Token': api_key}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        team_info = response.json()
        
        #Retrieve the coach and player information
        name = team_info.get('name')
        coach = team_info.get('coach', {})
        coach_name = [[coach.get('name'), coach.get('nationality')]] if coach.get('name') and coach.get('nationality') else []

        players_names = []
        squad = team_info.get('squad', [])
        for player in squad:
            player_name = player.get('name')
            player_nationality = player.get('nationality')
            player_position = player.get('position')
            if player_name and player_nationality and player_position:
                players_names.append([player_name, player_nationality, player_position])

        team_data = {
            'name': name,
            'coach': coach_name,
            'team': players_names
        }

        result = team_data_collection.insert_one(team_data)
        print('Team data stored in MongoDB with document ID:', result.inserted_id)

        time.sleep(10)  # Introduce a 10-second delay between API calls

    else:
        print(f'Failed to retrieve team {team_id} data:', response.status_code)
