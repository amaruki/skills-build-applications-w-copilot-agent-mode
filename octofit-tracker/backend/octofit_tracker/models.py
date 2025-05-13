from pymongo import MongoClient

# MongoDB connection setup
client = MongoClient('localhost', 27017)
db = client['octofit_db']

# Models for MongoDB collections
class User:
    collection = db['users']

class Team:
    collection = db['teams']

class Activity:
    collection = db['activity']

class Leaderboard:
    collection = db['leaderboard']

class Workout:
    collection = db['workouts']