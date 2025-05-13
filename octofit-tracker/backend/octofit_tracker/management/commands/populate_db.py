from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        try:
            self.stdout.write('Clearing existing data...')
            # Clear Django models
            User.objects.all().delete()
            Team.objects.all().delete()
            Activity.objects.all().delete()
            Leaderboard.objects.all().delete()
            Workout.objects.all().delete()

            self.stdout.write('Creating users...')
            # Create users with superhero usernames
            users = [
                User(_id=ObjectId(), username='thundergod', email='thundergod@mhigh.edu', password='thundergodpassword'),
                User(_id=ObjectId(), username='metalgeek', email='metalgeek@mhigh.edu', password='metalgeekpassword'),
                User(_id=ObjectId(), username='zerocool', email='zerocool@mhigh.edu', password='zerocoolpassword'),
                User(_id=ObjectId(), username='crashoverride', email='crashoverride@mhigh.edu', password='crashoverridepassword'),
                User(_id=ObjectId(), username='sleeptoken', email='sleeptoken@mhigh.edu', password='sleeptokenpassword')
            ]
            users = User.objects.bulk_create(users)
            self.stdout.write(f'Created {len(users)} users')

            self.stdout.write('Creating teams...')
            # Create teams
            blue_team = Team(_id=ObjectId(), name='Blue Team')
            blue_team.save()
            gold_team = Team(_id=ObjectId(), name='Gold Team')
            gold_team.save()

            # Add members to teams
            for user in users[:3]:
                blue_team.members.add(user)
            for user in users[3:]:
                gold_team.members.add(user)
            self.stdout.write('Created teams and added members')

            self.stdout.write('Creating activities...')
            # Create activities
            activities = []
            for i, (user, activity_type, duration) in enumerate([
                (users[0], 'Cycling', timedelta(hours=1)),
                (users[1], 'Crossfit', timedelta(hours=2)),
                (users[2], 'Running', timedelta(hours=1, minutes=30)),
                (users[3], 'Strength', timedelta(minutes=30)),
                (users[4], 'Swimming', timedelta(hours=1, minutes=15))
            ]):
                activity = Activity(
                    _id=ObjectId(),
                    activity_id=str(ObjectId()),  # Generate unique ID for each activity
                    user=user,
                    activity_type=activity_type,
                    duration=duration
                )
                activities.append(activity)
            # Create all activities at once
            activities = Activity.objects.bulk_create(activities)
            self.stdout.write(f'Created {len(activities)} activities')

            self.stdout.write('Creating leaderboard entries...')
            # Create leaderboard entries with corresponding scores
            leaderboard_entries = [
                Leaderboard(_id=ObjectId(), user=users[0], score=100),  # thundergod
                Leaderboard(_id=ObjectId(), user=users[1], score=90),   # metalgeek
                Leaderboard(_id=ObjectId(), user=users[2], score=95),   # zerocool
                Leaderboard(_id=ObjectId(), user=users[3], score=85),   # crashoverride
                Leaderboard(_id=ObjectId(), user=users[4], score=80),   # sleeptoken
            ]
            Leaderboard.objects.bulk_create(leaderboard_entries)
            self.stdout.write(f'Created {len(leaderboard_entries)} leaderboard entries')

            self.stdout.write('Creating workouts...')
            # Create workout programs
            workouts = [
                Workout(_id=ObjectId(), name='Cycling Training', description='Training for a road cycling event'),
                Workout(_id=ObjectId(), name='Crossfit', description='Training for a crossfit competition'),
                Workout(_id=ObjectId(), name='Running Training', description='Training for a marathon'),
                Workout(_id=ObjectId(), name='Strength Training', description='Training for strength'),
                Workout(_id=ObjectId(), name='Swimming Training', description='Training for a swimming competition'),
            ]
            Workout.objects.bulk_create(workouts)
            self.stdout.write(f'Created {len(workouts)} workouts')

            self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))
            raise
