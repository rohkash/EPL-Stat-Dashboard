const express = require('express');
const { MongoClient } = require('mongodb');
const app = express();
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

// MongoDB connection URL
const url = process.env.MONGODB_CLUSTER_LINK;

// MongoDB database and collection names
const dbName = process.env.DB_NAME;
const collectionName = process.env.COLLECTION_NAME;

// Connect to MongoDB
MongoClient.connect(url, (err, client) => {
  if (err) {
    console.error('Error connecting to MongoDB:', err);
    return;
  }

  // Get a reference to the MongoDB database
  const db = client.db(dbName);

  // ... (previous code omitted for brevity) ...

const { ObjectId } = require('mongodb');

app.get('/documents/:id', async (req, res) => {
  const documentId = req.params.id;

  try {
    // Convert the document ID to an ObjectId
    const objectId = ObjectId(documentId);

    // Query the MongoDB collection to retrieve the document with the given ID
    const document = await db.collection(collectionName).findOne({ _id: objectId });

    if (document) {
      res.json(document);
    } else {
      res.status(404).json({ error: 'Document not found' });
    }
  } catch (error) {
    console.error('Error retrieving document:', error);
    res.status(500).json({ error: 'An error occurred' });
  }
});

// ... (remaining code omitted for brevity) ...


  // Start the server
  const port = 3000;
  app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
  });
});
