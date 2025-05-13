// Initialize the MongoDB database and collections
db = db.getSiblingDB('octofit_db');

// Drop existing collections if they exist
db.users.drop();
db.teams.drop();
db.activity.drop();
db.leaderboard.drop();
db.workouts.drop();

// Create collections
db.createCollection('users');
db.createCollection('teams');
db.createCollection('activity');
db.createCollection('leaderboard');
db.createCollection('workouts');

// Create indexes for each collection
db.users.createIndex({ "email": 1 }, { unique: true });
db.teams.createIndex({ "name": 1 }, { unique: true });
db.activity.createIndex({ "activity_id": 1 }, { unique: true });
db.leaderboard.createIndex({ "leaderboard_id": 1 }, { unique: true });
db.workouts.createIndex({ "workout_id": 1 }, { unique: true });
