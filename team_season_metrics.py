class SeasonMetricsUpdater:
    def __init__(self, api_client, data_storage):
        # Initialize the API client and data storage
        self.api_client = api_client
        self.data_storage = data_storage

    def update_season_metrics(self):
        try:
            # Get standings data
            standings_data = self.api_client.get_standings_data()

            # Check if standings data is available and extract season metrics
            if standings_data and "standings" in standings_data:
                standings = standings_data["standings"]
                if "table" in standings[0]:
                    table = standings[0]["table"]
                    for team in table:
                        team_name = team["team"]["name"]

                        try:
                            # Extract season metrics for the team
                            season_metrics = self.extract_season_metrics(team)

                            # Update season metrics for the team
                            self.data_storage.update_season_metrics(team_name, season_metrics)
                        except Exception as e:
                            print("An error occurred while extracting season metrics:", str(e))
        except Exception as e:
            print("An error occurred while updating season metrics:", str(e))

    def extract_season_metrics(self, team):
        try:
            # Extract relevant season metrics for a team
            season_metrics = {
                'games_played': team.get('playedGames'),
                'goals_scored': team.get('goalsFor'),
                'goals_allowed': team.get('goalsAgainst'),
                'goal_difference': team.get('goalDifference'),
                'points': team.get('points'),
                'position': team.get('position')
            }
            return season_metrics
        except Exception as e:
            print("An error occurred while extracting season metrics:", str(e))
            return {}
