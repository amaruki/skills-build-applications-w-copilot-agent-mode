// Initialize the MongoDB database and collections
use octofit_db;

// Create collections
const collections = ['users', 'teams', 'activity', 'leaderboard', 'workouts'];
collections.forEach(collection => {
    db.createCollection(collection);
});

// Ensure unique index for users collection
// This ensures that each user has a unique email
// and creates a primary key for the user collection
db.users.createIndex({ "email": 1 }, { unique: true });
