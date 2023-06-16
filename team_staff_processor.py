class TeamInfoProcessor:
    def __init__(self, api_client, data_storage):
        try:
            # Initialize the API client and data storage
            self.api_client = api_client
            self.data_storage = data_storage
        except Exception as e:
            print("An error occurred while initializing the TeamStaffProcessor:", str(e))

    def process_team_information(self, team_ids):
        try:
            # Process team staff for each team ID
            for team_id in team_ids:
                # Get team information from the API client
                team_info = self.api_client.get_team_info(team_id)
                if team_info:
                    # Create a dictionary to store team data
                    team_data = {
                        'name': team_info.get('name')
                    }
                    # Get coach information
                    self.get_coach_info(team_info, team_data)
                    # Get player information
                    self.get_player_info(team_info, team_data)
                    # Get additional information
                    self.get_additional_club_info(team_info, team_data)

                    # Store team data in the data storage
                    self.data_storage.store_team_data(team_data)
                    self.api_client.delay_between_calls(10)  # Introduce a 10-second delay between API calls
        except Exception as e:
            print("An error occurred while processing team staff:", str(e))

    def get_coach_info(self, team_info, team_data):
        try:
            # Extract coach information and add it to the team data
            coach = team_info.get('coach')
            coach_name = [[coach.get('name'), coach.get('dateOfBirth'), coach.get('nationality')]]
            team_data['coach'] = coach_name
        except Exception as e:
            print("An error occurred while getting coach info:", str(e))

    def get_player_info(self, team_info, team_data):
        try:
            # Extract player information and add it to the team data
            players_names = []
            squad = team_info.get('squad')
            for player in squad:
                player_name = player.get('name')
                player_nationality = player.get('nationality')
                player_position = player.get('position')
                if player_name and player_nationality and player_position:
                    players_names.append([player_name, player_nationality, player_position])
            team_data['team'] = players_names
        except Exception as e:
            print("An error occurred while getting player info:", str(e))

    def get_additional_club_info(self, team_info, team_data):
        try:
            # Extract additional information and add it to the team data
            club_colors = team_info.get('clubColors')
            date_founded = team_info.get('founded')
            venue = team_info.get('venue')
            address = team_info.get('address')
            website = team_info.get('website')
            crest = team_info.get('crest')

            team_data['club_colors'] = club_colors
            team_data['date_founded'] = date_founded
            team_data['venue'] = venue
            team_data['address'] = address
            team_data['website'] = website
            team_data['crest'] = crest
        except Exception as e:
            print("An error occurred while getting additional club info:", str(e))
