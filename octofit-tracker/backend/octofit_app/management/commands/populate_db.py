from django.core.management.base import BaseCommand
from pymongo import MongoClient
import sys

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        try:
            client = MongoClient('localhost', 27017)
            db = client['octofit_db']
            
            self.stdout.write('Clearing existing data...')
            # Clear existing data
            db.users.delete_many({})
            db.teams.delete_many({})
            db.activity.delete_many({})
            db.leaderboard.delete_many({})
            db.workouts.delete_many({})
            
            self.stdout.write('Inserting users...')
            # Test data for users
            users = [
                {"email": "student1@school.edu", "name": "Student One", "password": "password123"},
                {"email": "student2@school.edu", "name": "Student Two", "password": "password123"},
                {"email": "coach1@school.edu", "name": "Coach Smith", "password": "password123", "is_coach": True}
            ]
            result = db.users.insert_many(users)
            self.stdout.write(f'Inserted {len(result.inserted_ids)} users')

            self.stdout.write('Inserting teams...')
            # Test data for teams
            teams = [
                {
                    "name": "Track Stars",
                    "members": ["student1@school.edu", "student2@school.edu"],
                    "coach": "coach1@school.edu"
                }
            ]
            result = db.teams.insert_many(teams)
            self.stdout.write(f'Inserted {len(result.inserted_ids)} teams')

            self.stdout.write('Inserting activities...')
            # Test data for activities
            activities = [
                {
                    "user_id": "student1@school.edu",
                    "activity_type": "Running",
                    "duration": 30,
                    "distance": 5.0,
                    "date": "2025-05-13"
                },
                {
                    "user_id": "student2@school.edu",
                    "activity_type": "Swimming",
                    "duration": 45,
                    "distance": 1.5,
                    "date": "2025-05-13"
                }
            ]
            result = db.activity.insert_many(activities)
            self.stdout.write(f'Inserted {len(result.inserted_ids)} activities')

            self.stdout.write('Inserting leaderboard entries...')
            # Test data for leaderboard
            leaderboard = [
                {"user_id": "student1@school.edu", "score": 150, "rank": 1},
                {"user_id": "student2@school.edu", "score": 120, "rank": 2}
            ]
            result = db.leaderboard.insert_many(leaderboard)
            self.stdout.write(f'Inserted {len(result.inserted_ids)} leaderboard entries')

            self.stdout.write('Inserting workouts...')
            # Test data for workouts
            workouts = [
                {
                    "name": "Beginner Running Plan",
                    "description": "30-minute easy jog with 5-minute warm-up and cool-down",
                    "difficulty": "beginner"
                },
                {
                    "name": "Advanced Swimming",
                    "description": "45-minute swimming session with mixed strokes",
                    "difficulty": "advanced"
                }
            ]
            result = db.workouts.insert_many(workouts)
            self.stdout.write(f'Inserted {len(result.inserted_ids)} workouts')

            self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))
            sys.exit(1)
