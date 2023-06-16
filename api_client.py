import requests
import time

class APIClient:
    def __init__(self, api_key):
        # Initialize the API key
        self.api_key = api_key

    def get_team_info(self, team_id):
        # Retrieve team information based on the team ID
        url = f'https://api.football-data.org/v4/teams/{team_id}'
        headers = {'X-Auth-Token': self.api_key}

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            # Parse the JSON response and return the team info
            team_info = response.json()
            return team_info
        else:
            # Print an error message if the request fails and return None
            print(f'Failed to retrieve team {team_id} data:', response.status_code)
            return None
    
    def get_standings_data(self):
        # Retrieve standings data for the Premier League
        url = "http://api.football-data.org/v4/competitions/PL/standings"
        headers = {'X-Auth-Token': self.api_key}

        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            # Parse the JSON response and return the standings data
            standings_data = response.json()
            return standings_data
        else:
            # Return None if the request fails
            return None

    def delay_between_calls(self, seconds):
        # Introduce a delay between API calls
        time.sleep(seconds)
