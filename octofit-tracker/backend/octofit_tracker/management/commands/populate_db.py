from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Test data for users
        users = [
            {"email": "john.doe@example.com", "name": "John Doe"},
            {"email": "jane.smith@example.com", "name": "Jane Smith"}
        ]
        db.users.insert_many(users)

        # Test data for teams
        teams = [
            {"name": "Team Alpha", "members": ["john.doe@example.com", "jane.smith@example.com"]}
        ]
        db.teams.insert_many(teams)

        # Test data for activities
        activities = [
            {"user_id": "john.doe@example.com", "activity_type": "Running", "duration": 30},
            {"user_id": "jane.smith@example.com", "activity_type": "Cycling", "duration": 45}
        ]
        db.activity.insert_many(activities)

        # Test data for leaderboard
        leaderboard = [
            {"user_id": "john.doe@example.com", "score": 100},
            {"user_id": "jane.smith@example.com", "score": 150}
        ]
        db.leaderboard.insert_many(leaderboard)

        # Test data for workouts
        workouts = [
            {"name": "Morning Run", "description": "A quick morning run to start the day."},
            {"name": "Evening Yoga", "description": "Relaxing yoga session to end the day."}
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
