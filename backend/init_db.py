#!/usr/bin/env python3
"""
Database initialization script for MuscleUp
Creates tables and populates with sample data
"""

import os
import sys
from datetime import datetime, date
from dotenv import load_dotenv

# Add the app directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import create_app, db
from app.models import User, Exercise, WorkoutLog, NutritionLog, ProgressRecord, PoseFeedback

# Load environment variables
load_dotenv()

def create_sample_exercises():
    """Create sample exercises"""
    exercises = [
        # Core strength movements
        Exercise(name="Squat", category="Strength", muscle_group="Legs", difficulty_level="Beginner", description="Compound lower-body movement", instructions="Stand with feet shoulder-width apart and squat down then up", default_sets=3, default_reps=12, default_rest_time=60),
        Exercise(name="Deadlift", category="Strength", muscle_group="Back", difficulty_level="Intermediate", description="Posterior chain compound", instructions="Hinge at hips and lift bar to standing", default_sets=4, default_reps=5, default_rest_time=120),
        Exercise(name="Bench Press", category="Strength", muscle_group="Chest", difficulty_level="Intermediate", description="Chest pressing movement", instructions="Press barbell from chest to lockout", default_sets=4, default_reps=8, default_rest_time=90),
        Exercise(name="Pull-up", category="Strength", muscle_group="Back", difficulty_level="Intermediate", description="Vertical pulling bodyweight", instructions="Pull until chin clears bar", default_sets=3, default_reps=8, default_rest_time=90),
        Exercise(name="Overhead Press", category="Strength", muscle_group="Shoulders", difficulty_level="Intermediate", description="Standing shoulder press", instructions="Press bar overhead to full extension", default_sets=3, default_reps=8, default_rest_time=75),
        # Added requested movements
        Exercise(name="Incline Bench Press", category="Strength", muscle_group="Chest", difficulty_level="Intermediate", description="Upper-chest pressing", instructions="Press from an incline bench", default_sets=4, default_reps=8, default_rest_time=90),
        Exercise(name="Leg Curl", category="Strength", muscle_group="Hamstrings", difficulty_level="Beginner", description="Hamstring isolation", instructions="Curl pad toward glutes on machine", default_sets=3, default_reps=12, default_rest_time=60),
        Exercise(name="Lateral Raises", category="Strength", muscle_group="Shoulders", difficulty_level="Beginner", description="Medial delt isolation", instructions="Raise dumbbells to sides", default_sets=3, default_reps=12, default_rest_time=60),
        Exercise(name="Leg Press", category="Strength", muscle_group="Legs", difficulty_level="Beginner", description="Sled leg press", instructions="Press sled by extending knees", default_sets=4, default_reps=10, default_rest_time=90),
        Exercise(name="Tricep Pushdown", category="Strength", muscle_group="Triceps", difficulty_level="Beginner", description="Cable triceps isolation", instructions="Extend elbows with rope/bar attachment", default_sets=3, default_reps=12, default_rest_time=60),
        Exercise(name="Lat Pull Down", category="Strength", muscle_group="Back", difficulty_level="Beginner", description="Vertical pulling on cable", instructions="Pull bar to upper chest", default_sets=3, default_reps=10, default_rest_time=75),
        Exercise(name="Arnold Press", category="Strength", muscle_group="Shoulders", difficulty_level="Intermediate", description="Rotational dumbbell press", instructions="Rotate wrists during press", default_sets=3, default_reps=10, default_rest_time=75),
        Exercise(name="Face Pull", category="Strength", muscle_group="Rear Delts", difficulty_level="Beginner", description="Rear delt cable pull", instructions="Pull rope to face with elbows high", default_sets=3, default_reps=15, default_rest_time=60),
        Exercise(name="Shrugs", category="Strength", muscle_group="Traps", difficulty_level="Beginner", description="Upper trap isolation", instructions="Elevate shoulders while holding weight", default_sets=3, default_reps=12, default_rest_time=60),
        Exercise(name="Back Extension", category="Strength", muscle_group="Lower Back", difficulty_level="Beginner", description="Hyperextension accessory", instructions="Extend trunk over bench with neutral spine", default_sets=3, default_reps=12, default_rest_time=60),
        Exercise(name="Bent Over Row", category="Strength", muscle_group="Back", difficulty_level="Intermediate", description="Horizontal barbell row", instructions="Row bar to torso while hinged", default_sets=4, default_reps=8, default_rest_time=90),
        Exercise(name="Bicep Curl", category="Strength", muscle_group="Biceps", difficulty_level="Beginner", description="Elbow flexion", instructions="Curl barbell/dumbbells without swinging", default_sets=3, default_reps=12, default_rest_time=60),
    ]

    for exercise in exercises:
        existing = Exercise.query.filter_by(name=exercise.name).first()
        if not existing:
            db.session.add(exercise)

    db.session.commit()
    print(f"✅ Created {len(exercises)} sample exercises")

def create_sample_user():
    """Create a sample user for testing"""
    # Check if user already exists
    existing_user = User.query.filter_by(email="demo@muscleup.com").first()
    if existing_user:
        print("✅ Sample user already exists")
        return existing_user
    
    user = User(
        name="Demo User",
        email="demo@muscleup.com",
        password="demo123",
        age=25,
        gender="male",
        fitness_goal="gain_muscle",
        experience_level="intermediate"
    )
    
    db.session.add(user)
    db.session.commit()
    print("✅ Created sample user: demo@muscleup.com / demo123")
    return user

def create_sample_data(user):
    """Create sample workout and nutrition data"""
    # Get some exercises
    squat = Exercise.query.filter_by(name="Squat").first()
    pushup = Exercise.query.filter_by(name="Push-up").first()
    deadlift = Exercise.query.filter_by(name="Deadlift").first()
    
    if not squat or not pushup or not deadlift:
        print("❌ Required exercises not found")
        return
    
    # Sample workout logs
    workout_logs = [
        WorkoutLog(
            user_id=user.user_id,
            exercise_id=squat.exercise_id,
            date=date.today(),
            sets=3,
            reps=12,
            weight=60.0,
            rest_time=60,
            duration=30,
            notes="Good form, felt strong"
        ),
        WorkoutLog(
            user_id=user.user_id,
            exercise_id=pushup.exercise_id,
            date=date.today(),
            sets=3,
            reps=15,
            weight=0,
            rest_time=45,
            duration=20,
            notes="Bodyweight exercise"
        ),
        WorkoutLog(
            user_id=user.user_id,
            exercise_id=deadlift.exercise_id,
            date=date.today(),
            sets=4,
            reps=5,
            weight=100.0,
            rest_time=120,
            duration=45,
            notes="New PR! Felt great"
        ),
    ]
    
    for log in workout_logs:
        existing = WorkoutLog.query.filter_by(
            user_id=log.user_id,
            exercise_id=log.exercise_id,
            date=log.date
        ).first()
        if not existing:
            db.session.add(log)
    
    # Sample nutrition log
    nutrition_log = NutritionLog(
        user_id=user.user_id,
        date=date.today(),
        calorie_target=2500,
        calories_consumed=2200,
        protein=150.0,
        carbs=250.0,
        fats=80.0,
        fiber=35.0,
        sugar=50.0,
        sodium=2000.0,
        water_intake=3.0,
        notes="Good day of eating, hit protein target"
    )
    
    existing_nutrition = NutritionLog.query.filter_by(
        user_id=user.user_id,
        date=date.today()
    ).first()
    if not existing_nutrition:
        db.session.add(nutrition_log)
    
    # Sample progress record
    progress_record = ProgressRecord(
        user_id=user.user_id,
        exercise_id=deadlift.exercise_id,
        date=date.today(),
        personal_record=100.0,
        body_weight=75.0,
        body_fat_percentage=15.0,
        muscle_mass=65.0,
        chest_measurement=100.0,
        waist_measurement=80.0,
        arm_measurement=35.0,
        thigh_measurement=60.0,
        notes="New deadlift PR! Feeling stronger"
    )
    
    existing_progress = ProgressRecord.query.filter_by(
        user_id=user.user_id,
        exercise_id=deadlift.exercise_id,
        date=date.today()
    ).first()
    if not existing_progress:
        db.session.add(progress_record)
    
    db.session.commit()
    print("✅ Created sample workout, nutrition, and progress data")

def main():
    """Main initialization function"""
    print("🚀 Initializing MuscleUp Database...")
    
    # Create Flask app
    app = create_app()
    
    with app.app_context():
        # Create all tables
        db.create_all()
        print("✅ Database tables created")
        
        # Create sample data
        create_sample_exercises()
        user = create_sample_user()
        create_sample_data(user)
        
        print("🎉 Database initialization complete!")
        print("\n📋 Sample Login Credentials:")
        print("   Email: demo@muscleup.com")
        print("   Password: demo123")
        print("\n🔗 You can now start the application:")
        print("   Backend: python run.py")
        print("   Frontend: npm start (in frontend directory)")

if __name__ == "__main__":
    main()
