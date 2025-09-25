
import random
from faker import Faker
from app import create_app, db
from app.models import (
    User, UserProfile, Role, LearningPath, Module, Resource, Quiz,
    Progress, Comment, Rating, Badge, Achievement, UserLearningPath
)
from werkzeug.security import generate_password_hash

fake = Faker()

def seed_roles():
    """Seeds the roles table."""
    if Role.query.first():
        return  # Roles already seeded

    print("Seeding roles...")
    roles = [
        {"name": "Admin", "description": "Platform administrator with full access."},
        {"name": "Contributor", "description": "Can create, edit, and manage their own learning content."},
        {"name": "Learner", "description": "Can enroll in and consume learning content."}
    ]
    for role_data in roles:
        role = Role(**role_data)
        db.session.add(role)
    db.session.commit()
    print("Roles seeded.")

def seed_users(num_users=20):
    """Seeds users with different roles."""
    if User.query.count() > 1:
        return

    print(f"Seeding {num_users} users...")
    admin_role = Role.query.filter_by(name="Admin").first()
    contributor_role = Role.query.filter_by(name="Contributor").first()
    learner_role = Role.query.filter_by(name="Learner").first()

    # Create a specific admin for easy login
    admin_user = User(
        username="admin",
        email="admin@elearn.com",
        password=generate_password_hash("admin", method='pbkdf2:sha256'),
        role_id=admin_role.id
    )
    db.session.add(admin_user)
    db.session.commit()
    user_profile = UserProfile(user_id=admin_user.id, bio="E-learn Platform Administrator", points=100, xp=200)
    db.session.add(user_profile)

    # Create other users
    for i in range(num_users - 1):
        role = random.choices(
            [admin_role, contributor_role, learner_role],
            weights=[0.1, 0.3, 0.6],
            k=1
        )[0]
        
        username = fake.unique.user_name()
        user = User(
            username=username,
            email=fake.unique.email(),
            password=generate_password_hash("password", method='pbkdf2:sha256'),
            role_id=role.id
        )
        db.session.add(user)
        db.session.commit() # Commit to get user ID for profile
        
        user_profile = UserProfile(
            user_id=user.id,
            bio=fake.sentence(nb_words=10),
            points=random.randint(0, 1000),
            xp=random.randint(0, 5000)
        )
        db.session.add(user_profile)

    db.session.commit()
    print("Users and profiles seeded.")

def seed_learning_content(num_paths=5, modules_per_path=4, resources_per_module=3):
    """Seeds learning paths, modules, resources, and quizzes."""
    if LearningPath.query.first():
        return

    print("Seeding learning content...")
    contributors = User.query.join(Role).filter(Role.name == "Contributor").all()
    if not contributors:
        print("No contributors found to create content. Aborting content seeding.")
        return

    for _ in range(num_paths):
        path = LearningPath(
            title=fake.catch_phrase(),
            description=fake.paragraph(nb_sentences=3),
            contributor_id=random.choice(contributors).id,
            category=random.choice(["Tech", "Business", "Arts", "Science", "Health"]),
            difficulty_level=random.choice(["Beginner", "Intermediate", "Advanced"])
        )
        db.session.add(path)
        db.session.commit()

        for i in range(modules_per_path):
            module = Module(
                title=f"Module {i+1}: {fake.sentence(nb_words=4)}",
                description=fake.paragraph(nb_sentences=2),
                learning_path_id=path.id,
                order_index=i
            )
            db.session.add(module)
            db.session.commit()

            for j in range(resources_per_module):
                resource = Resource(
                    title=fake.sentence(nb_words=5),
                    description=fake.paragraph(nb_sentences=1),
                    type=random.choice(["Video", "Article", "PDF"]),
                    url=fake.url(),
                    module_id=module.id,
                    order_index=j
                )
                db.session.add(resource)

            # Add a quiz to each module
            quiz = Quiz(
                question=f"What is the key concept of Module {i+1}?",
                options='["Concept A", "Concept B", "Concept C"]',
                correct_answer="Concept B",
                module_id=module.id
            )
            db.session.add(quiz)

    db.session.commit()
    print("Learning paths, modules, resources, and quizzes seeded.")

def seed_enrollments_and_progress(num_enrollments=30):
    """Seeds user enrollments in learning paths and simulates progress."""
    if UserLearningPath.query.first():
        return

    print("Seeding user enrollments and progress...")
    users = User.query.all()
    paths = LearningPath.query.all()

    for _ in range(num_enrollments):
        user = random.choice(users)
        path = random.choice(paths)

        # Avoid duplicate enrollments
        if UserLearningPath.query.filter_by(user_id=user.id, learning_path_id=path.id).first():
            continue

        enrollment = UserLearningPath(user_id=user.id, learning_path_id=path.id)
        db.session.add(enrollment)
        db.session.commit()

        # Simulate progress
        modules_in_path = Module.query.filter_by(learning_path_id=path.id).all()
        if not modules_in_path:
            continue
            
        num_modules_to_complete = random.randint(0, len(modules_in_path))
        completed_modules = random.sample(modules_in_path, num_modules_to_complete)

        for module in completed_modules:
            progress = Progress(
                user_id=user.id,
                module_id=module.id,
                completed=True,
                completion_date=fake.date_time_this_year()
            )
            db.session.add(progress)
    
    db.session.commit()
    print("User enrollments and progress seeded.")

def seed_social_features(num_comments=50, num_ratings=100):
    """Seeds comments and ratings."""
    if Comment.query.first():
        return
        
    print("Seeding comments and ratings...")
    users = User.query.all()
    resources = Resource.query.all()

    for _ in range(num_comments):
        comment = Comment(
            content=fake.paragraph(nb_sentences=2),
            user_id=random.choice(users).id,
            resource_id=random.choice(resources).id
        )
        db.session.add(comment)

    for _ in range(num_ratings):
        # Avoid duplicate ratings
        user = random.choice(users)
        resource = random.choice(resources)
        if Rating.query.filter_by(user_id=user.id, resource_id=resource.id).first():
            continue
            
        rating = Rating(
            value=random.randint(1, 5),
            user_id=user.id,
            resource_id=resource.id
        )
        db.session.add(rating)

    db.session.commit()
    print("Comments and ratings seeded.")

def seed_gamification():
    """Seeds badges and awards achievements."""
    if Badge.query.first():
        return
        
    print("Seeding badges and achievements...")
    badges_data = [
        {"name": "First Steps", "description": "Complete your first module.", "points_required": 10},
        {"name": "Pathfinder", "description": "Complete your first learning path.", "points_required": 50},
        {"name": "Serial Learner", "description": "Complete 5 learning paths.", "points_required": 250},
        {"name": "Knowledgeable", "description": "Earn 1000 XP.", "points_required": 1000},
        {"name": "Community Helper", "description": "Leave 10 helpful comments.", "points_required": 100},
    ]
    for badge_data in badges_data:
        badge = Badge(**badge_data)
        db.session.add(badge)
    db.session.commit()

    # Award some achievements (basic simulation)
    users = User.query.all()
    first_module_badge = Badge.query.filter_by(name="First Steps").first()
    for user in users:
        if Progress.query.filter_by(user_id=user.id, completed=True).count() > 0:
            if not Achievement.query.filter_by(user_id=user.id, badge_id=first_module_badge.id).first():
                db.session.add(Achievement(user_id=user.id, badge_id=first_module_badge.id))

    db.session.commit()
    print("Badges and achievements seeded.")


import argparse

def run_specific_seed(seed_function):
    """Runs a specific seeding function within the app context."""
    app = create_app()
    with app.app_context():
        print(f"--- Running seeder: {seed_function.__name__} ---")
        seed_function()
        print(f"--- Seeder {seed_function.__name__} finished ---")

def run_full_seed():
    """Main function to run all seeders, wiping the database first."""
    app = create_app()
    with app.app_context():
        print("--- Starting full database seeding (WIPING DATABASE) ---")
        db.drop_all()
        db.create_all()
        
        seed_roles()
        seed_users()
        seed_learning_content()
        seed_enrollments_and_progress()
        seed_social_features()
        seed_gamification()
        
        print("--- Database seeded successfully! ---")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Seed the E-learn database.')
    parser.add_argument('--seed', type=str, help='Specify a seeder to run (e.g., roles, users). Default is full seed.')

    args = parser.parse_args()

    seed_map = {
        'roles': seed_roles,
        'users': seed_users,
        'content': seed_learning_content,
        'enrollments': seed_enrollments_and_progress,
        'social': seed_social_features,
        'gamification': seed_gamification
    }

    if args.seed:
        if args.seed in seed_map:
            run_specific_seed(seed_map[args.seed])
        else:
            print(f"Error: Seeder '{args.seed}' not found. Available seeders: {list(seed_map.keys())}")
    else:
        print("Warning: No specific seeder chosen. Running full seed, which will wipe the database.")
        if input("Are you sure you want to continue? (y/n): ").lower() == 'y':
            run_full_seed()
        else:
            print("Aborted.")
