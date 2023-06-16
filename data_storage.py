from pymongo import MongoClient

class DataStorage:
    def __init__(self, cluster_link, database_name, collection_name):
        try:
            # Initialize the MongoDB client, database, and collection
            self.client = MongoClient(cluster_link)
            self.db = self.client[database_name]
            self.collection = self.db[collection_name]
        except Exception as e:
            print("An error occurred while initializing the MongoDB client:", str(e))

    def store_team_data(self, team_data):
        try:
            # Store team data in MongoDB
            result = self.collection.insert_one(team_data)
            print('Team data stored in MongoDB with document ID:', result.inserted_id)
        except Exception as e:
            print("An error occurred while storing team data in MongoDB:", str(e))
    
    def update_season_metrics(self, team_name, season_metrics):
        try:
            # Update the season metrics for a specific team
            self.collection.update_one(
                {"name": team_name},
                {"$set": {"season_metrics": season_metrics}}
            )
        except Exception as e:
            print("An error occurred while updating season metrics in MongoDB:", str(e))
          
    def delete_all_documents(self):
        try:
            # Delete all documents in the collection
            deletion_result = self.collection.delete_many({})
            print(f"{deletion_result.deleted_count} documents deleted.")
        except Exception as e:
            print("An error occurred while deleting documents in MongoDB:", str(e))
