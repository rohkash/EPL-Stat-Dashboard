from dotenv import dotenv_values
from api_client import APIClient
from data_storage import DataStorage
from team_staff_processor import TeamInfoProcessor
from team_season_metrics import SeasonMetricsUpdater

config = dotenv_values('.env')

# Configure API and MongoDB settings
api_key = config['API_KEY']
cluster_link = config['MONGODB_CLUSTER_LINK']

# Id of different EPL teams
team_ids = [57, 58, 61, 62, 63, 64, 65, 66, 67, 73, 76, 338, 340, 341, 351, 354, 397, 402, 563, 1044]

# Create instances of classes
api_client = APIClient(api_key)
data_storage = DataStorage(cluster_link, 'Database', 'teamData')
team_info_processor = TeamInfoProcessor(api_client, data_storage)
team_season_metrics = SeasonMetricsUpdater(api_client, data_storage)

# Process teams and store data
data_storage.delete_all_documents()
team_info_processor.process_team_information(team_ids)
team_season_metrics.update_season_metrics()



