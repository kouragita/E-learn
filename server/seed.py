import os
import random
import argparse
from faker import Faker
from app import create_app, db

# Ensure the instance folder exists before other imports
instance_path = os.path.join(os.path.dirname(__file__), 'instance')
if not os.path.exists(instance_path):
    os.makedirs(instance_path)

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
        {"id": 1, "name": "Admin", "description": "Platform administrator with full access."},
        {"id": 2, "name": "Contributor", "description": "Can create, edit, and manage their own learning content."},
        {"id": 3, "name": "Learner", "description": "Can enroll in and consume learning content."}
    ]
    for role_data in roles:
        role = Role(**role_data)
        db.session.add(role)
    db.session.commit()
    print("Roles seeded.")

def seed_users():
    """Seeds specific, predictable users for admin, contributor, and learner roles."""
    if User.query.count() > 0:
        print("Users table is not empty, skipping user seeding.")
        return

    print("Seeding predictable users (admin, contributor, learner)...")
    admin_role = Role.query.filter_by(name="Admin").first()
    contributor_role = Role.query.filter_by(name="Contributor").first()
    learner_role = Role.query.filter_by(name="Learner").first()

    users_to_create = [
        {
            'username': 'admin', 'email': 'admin@elearn.com',
            'password': 'password', 'role_id': admin_role.id
        },
        {
            'username': 'contributor', 'email': 'contributor@elearn.com',
            'password': 'password', 'role_id': contributor_role.id
        },
        {
            'username': 'learner', 'email': 'learner@elearn.com',
            'password': 'password', 'role_id': learner_role.id
        }
    ]

    for user_data in users_to_create:
        user = User(
            username=user_data['username'],
            email=user_data['email'],
            password=generate_password_hash(user_data['password'], method='pbkdf2:sha256'),
            role_id=user_data['role_id']
        )
        db.session.add(user)
        db.session.commit()
        user_profile = UserProfile(user_id=user.id, bio=f"Default bio for {user_data['username']}.")
        db.session.add(user_profile)
    
    db.session.commit()
    print("Predictable users and profiles seeded.")

def seed_learning_content(num_paths=5, modules_per_path=4, resources_per_module=3):
    """Seeds learning paths and assigns them to the specific contributor user."""
    if LearningPath.query.first():
        return

    print("Seeding learning content...")
    contributor = User.query.filter_by(username="contributor").first()
    if not contributor:
        print("Could not find the 'contributor' user. Aborting content seeding.")
        return

    for _ in range(num_paths):
        path = LearningPath(
            title=fake.catch_phrase(),
            description=fake.paragraph(nb_sentences=3),
            contributor_id=contributor.id,
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

            quiz = Quiz(
                question=f"What is the key concept of Module {i+1}?",
                options='["Concept A", "Concept B", "Concept C"]',
                correct_answer="Concept B",
                module_id=module.id
            )
            db.session.add(quiz)

    db.session.commit()
    print("Learning paths, modules, resources, and quizzes seeded.")

def seed_enrollments_and_progress():
    """Seeds enrollments and progress for the specific learner user."""
    if UserLearningPath.query.first():
        return

    print("Seeding enrollments and progress for the learner user...")
    learner = User.query.filter_by(username="learner").first()
    paths = LearningPath.query.all()

    if not learner or not paths:
        print("Learner or Learning Paths not found. Aborting enrollment seeding.")
        return

    paths_to_enroll = random.sample(paths, min(len(paths), 3))
    for path in paths_to_enroll:
        enrollment = UserLearningPath(user_id=learner.id, learning_path_id=path.id)
        db.session.add(enrollment)
        db.session.commit()

        modules_in_path = Module.query.filter_by(learning_path_id=path.id).all()
        if not modules_in_path:
            continue
            
        num_modules_to_complete = random.randint(0, len(modules_in_path))
        completed_modules = random.sample(modules_in_path, num_modules_to_complete)

        for module in completed_modules:
            progress = Progress(
                user_id=learner.id,
                module_id=module.id,
                completed=True,
                completion_date=fake.date_time_this_year()
            )
            db.session.add(progress)
    
    db.session.commit()
    print("Learner enrollments and progress seeded.")

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

    users = User.query.all()
    first_module_badge = Badge.query.filter_by(name="First Steps").first()
    for user in users:
        if Progress.query.filter_by(user_id=user.id, completed=True).count() > 0:
            if not Achievement.query.filter_by(user_id=user.id, badge_id=first_module_badge.id).first():
                db.session.add(Achievement(user_id=user.id, badge_id=first_module_badge.id))

    db.session.commit()
    print("Badges and achievements seeded.")

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
    parser.add_argument('--full', action='store_true', help='Run the full seed, wiping the database.')

    args = parser.parse_args()

    seed_map = {
        'roles': seed_roles,
        'users': seed_users,
        'content': seed_learning_content,
        'enrollments': seed_enrollments_and_progress,
        'social': seed_social_features,
        'gamification': seed_gamification
    }

    if args.full:
        run_full_seed()
    elif args.seed:
        if args.seed in seed_map:
            run_specific_seed(seed_map[args.seed])
        else:
            print(f"Error: Seeder '{args.seed}' not found. Available seeders: {list(seed_map.keys())}")
    else:
        print("No operation chosen. Use --seed <name> for a specific seeder or --full to wipe and seed everything.")