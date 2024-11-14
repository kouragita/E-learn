from app import create_app, db  # Import create_app and db correctly
from app.models import (
    User, UserProfile, UserLearningPath, Role, Resource, Rating, Quiz,
    Progress, Module, LearningPath, Comment, Badge, Achievement
)
from werkzeug.security import generate_password_hash  # Ensure correct hashing method

# Initialize the app and push an application context
app = create_app()

with app.app_context():
    # Drop all tables and recreate them
    db.drop_all()
    db.create_all()

    # Seed roles
    if not Role.query.first():
        roles = [
            Role(name="Admin", description="Platform administrator"),
            Role(name="Contributor", description="Can create and share resources"),
            Role(name="Learner", description="Can access learning paths"),
        ]
        db.session.add_all(roles)
        db.session.commit()
    
    # Seed users with password hashing
    if not User.query.first():
        users = [
            User(username="Daniel Watoro", password=generate_password_hash("password12", method='pbkdf2:sha256'), role_id=1),
            User(username="Wilson Mwangi", password=generate_password_hash("password34", method='pbkdf2:sha256'), role_id=1),
            User(username="David Wekesa", password=generate_password_hash("password56", method='pbkdf2:sha256'), role_id=3),
            User(username="Bakari Bubu", password=generate_password_hash("password78", method='pbkdf2:sha256'), role_id=2),
            User(username="Mercy Nzau", password=generate_password_hash("password90", method='pbkdf2:sha256'), role_id=3),
            User(username="Winnie Nyambura", password=generate_password_hash("password09", method='pbkdf2:sha256'), role_id=3)
        ]
        db.session.add_all(users)
        db.session.commit()
      
    # Seed profiles
    if not UserProfile.query.first():
        profiles = [
            UserProfile(user_id=1, points=500, xp=1000, bio="Admin user"),
            UserProfile(user_id=2, points=300, xp=600, bio="Admin user"),
            UserProfile(user_id=3, points=100, xp=200, bio="Learner user"),
            UserProfile(user_id=4, points=250, xp=400, bio="Contributor user"),
            UserProfile(user_id=5, points=150, xp=300, bio="Learner user"),
            UserProfile(user_id=6, points=50, xp=100, bio="Learner user")
        ]
        db.session.add_all(profiles)
        db.session.commit()

    # Seed learning paths
    if not LearningPath.query.first():
        learning_paths = [
            LearningPath(title="Data Science Basics", description="Introduction to data science", contributor_id=2),
            LearningPath(title="Web Development", description="Learn to build websites", contributor_id=2),
            LearningPath(title="Machine Learning", description="Introduction to ML concepts", contributor_id=2),
            LearningPath(title="Data Visualization", description="Visualizing data", contributor_id=4),
            LearningPath(title="React Basics", description="Introduction to React", contributor_id=4),
            LearningPath(title="Python Programming", description="Basics of Python", contributor_id=5)
        ]
        db.session.add_all(learning_paths)
        db.session.commit()
    
    # Seed modules
    if not Module.query.first():
        modules = [
            Module(title="Intro to Data Science", description="Learn the basics of data science", learning_path_id=1),
            Module(title="HTML & CSS Basics", description="Learn HTML and CSS", learning_path_id=2),
            Module(title="Intro to ML", description="Basics of machine learning", learning_path_id=3),
            Module(title="Intro to Data Visualization", description="Data visualization basics", learning_path_id=4),
            Module(title="React Components", description="Learn about React components", learning_path_id=5),
            Module(title="Python Variables", description="Learn Python variables", learning_path_id=6)
        ]
        db.session.add_all(modules)
        db.session.commit()

    # Seed resources
    if not Resource.query.first(): 
        resources = [
            Resource(title="Data Science", type="Video", url="https://youtu.be/X3paOmcrTjQ?si=A0x11b_cokxWXkTa", description="Data Science Introduction", module_id=1),
            Resource(title="HTML Tutorial", type="Article", url="https://www.w3schools.com/html/", description="Learn HTML", module_id=2),
            Resource(title="Machine Learning Guide", type="Article", url="https://www.geeksforgeeks.org/machine-learning/", description="ML basics", module_id=3),
            Resource(title="Data Visualization Tips", type="Article", url="https://www.coursera.org/articles/data-visualization?msockid=19480a2c2cad66f8351419342d516787", description="Visualization techniques", module_id=4),
            Resource(title="React Handbook", type="PDF", url="https://flaviocopes.pages.dev/books/react-handbook.pdf", description="React basics", module_id=5),
            Resource(title="Python Basics", type="Video", url="https://youtu.be/kqtD5dpn9C8?si=xln65I405xnPdMKg", description="Intro to Python", module_id=6)
        ]
        db.session.add_all(resources)
        db.session.commit()

    # Seed ratings
    ratings = [
        Rating(value=5, user_id=1, resource_id=1),
        Rating(value=4, user_id=2, resource_id=2),
        Rating(value=3, user_id=3, resource_id=3),
        Rating(value=5, user_id=4, resource_id=4),
        Rating(value=4, user_id=5, resource_id=5),
        Rating(value=3, user_id=6, resource_id=6)
    ]
    db.session.add_all(ratings)
    db.session.commit()

    # Seed quizzes
    quizzes = [
        Quiz(question="What is Data Science?", options='["A. Study of algorithms", "B. Analysis of data", "C. Cooking techniques"]', correct_answer="B", module_id=1),
        Quiz(question="What does HTML stand for?", options='["A. Hyper Text Markup Language", "B. High Text Marking Language", "C. Home Tool Markup Language"]', correct_answer="A", module_id=2),
        Quiz(question="What is Machine Learning?", options='["A. A programming language", "B. A set of rules", "C. A field of AI focused on algorithms that learn from data"]', correct_answer="C", module_id=3),
        Quiz(question="What is Data Visualization?", options='["A. The practice of representing data graphically", "B. A tool for managing data", "C. A data storage method"]', correct_answer="A", module_id=4),
        Quiz(question="What is a React Component?", options='["A. A Python module", "B. A building block of a React app", "C. A CSS framework"]', correct_answer="B", module_id=5),
        Quiz(question="What is a variable in Python?", options='["A. A fixed value", "B. A container for storing data values", "C. A type of function"]', correct_answer="B", module_id=6),
        Quiz(question="What is JavaScript?", options='["A. A type of database", "B. A programming language for web development", "C. A data storage format"]', correct_answer="B", module_id=2),
        Quiz(question="What does CSS stand for?", options='["A. Cascading Style Sheets", "B. Creative Style Systems", "C. Computer Style Syntax"]', correct_answer="A", module_id=2),
        Quiz(question="Which language is used for web development?", options='["A. Python", "B. JavaScript", "C. SQL"]', correct_answer="B", module_id=2),
        Quiz(question="What is Python used for?", options='["A. Data analysis", "B. Web development", "C. All of the above"]', correct_answer="C", module_id=6),
        Quiz(question="What is an API?", options='["A. Application Programming Interface", "B. Application Public Internet", "C. Advanced Protocol Integration"]', correct_answer="A", module_id=1),
        Quiz(question="What is SQL?", options='["A. Structured Query Language", "B. Simple Query Language", "C. Server Query Language"]', correct_answer="A", module_id=3),
        Quiz(question="What is a module in programming?", options='["A. A small device", "B. A reusable piece of code", "C. A variable type"]', correct_answer="B", module_id=1),
        Quiz(question="What is Git used for?", options='["A. Data storage", "B. Version control", "C. API management"]', correct_answer="B", module_id=5),
        Quiz(question="What is React primarily used for?", options='["A. Styling web pages", "B. Building user interfaces", "C. Managing databases"]', correct_answer="B", module_id=5),
        Quiz(question="In HTML, what tag is used for paragraphs?", options='["A. <div>", "B. <p>", "C. <section>"]', correct_answer="B", module_id=2),
        Quiz(question="Which symbol is used for comments in Python?", options='["A. //", "B. #", "C. <!-- -->"]', correct_answer="B", module_id=6),
        Quiz(question="What is the purpose of CSS?", options='["A. Add functionality to websites", "B. Style web pages", "C. Store data"]', correct_answer="B", module_id=2),
        Quiz(question="What is a dataset?", options='["A. A collection of data", "B. A code structure", "C. A web tool"]', correct_answer="A", module_id=1),
        Quiz(question="In Python, what keyword is used to define a function?", options='["A. func", "B. function", "C. def"]', correct_answer="C", module_id=6),
        Quiz(question="What does ML stand for?", options='["A. Markup Language", "B. Machine Learning", "C. Manual Learning"]', correct_answer="B", module_id=3),
        Quiz(question="What is a CSS selector?", options='["A. A tool to select files", "B. A rule to apply styles to elements", "C. A JavaScript command"]', correct_answer="B", module_id=2),
        Quiz(question="What does JSON stand for?", options='["A. Java Syntax Object Notation", "B. JavaScript Object Notation", "C. JavaScript Organized Notation"]', correct_answer="B", module_id=1),
        Quiz(question="What does IDE stand for?", options='["A. Integrated Development Environment", "B. Interactive Design Engine", "C. Internet Development Emulator"]', correct_answer="A", module_id=6),
        Quiz(question="What is the purpose of React's useState hook?", options='["A. Add style to components", "B. Manage state within components", "C. Handle form submissions"]', correct_answer="B", module_id=5),
        Quiz(question="Which symbol is used for assignment in Python?", options='["A. =", "B. ==", "C. ->"]', correct_answer="A", module_id=6),
        Quiz(question="What type of variable is 'True' in Python?", options='["A. Integer", "B. String", "C. Boolean"]', correct_answer="C", module_id=6),
        Quiz(question="Which tag is used for a hyperlink in HTML?", options='["A. <link>", "B. <a>", "C. <href>"]', correct_answer="B", module_id=2),
        Quiz(question="What does the flex property in CSS do?", options='["A. Manages layout", "B. Adds animations", "C. Adjusts font size"]', correct_answer="A", module_id=2),
        Quiz(question="Which programming language is known for its readability?", options='["A. Java", "B. Python", "C. C++"]', correct_answer="B", module_id=6),
        Quiz(question="What is the purpose of the `return` keyword in Python?", options='["A. Loops through data", "B. Exits a function", "C. Outputs a result from a function"]', correct_answer="C", module_id=6),
        Quiz(question="Which framework is popular for building single-page applications?", options='["A. React", "B. Django", "C. SQLAlchemy"]', correct_answer="A", module_id=5),
        Quiz(question="What is JSX in React?", options='["A. JavaScript Extension", "B. JavaScript XML", "C. JSON Extension"]', correct_answer="B", module_id=5),
        Quiz(question="What is the purpose of `useEffect` in React?", options='["A. Update CSS", "B. Side effects management", "C. API creation"]', correct_answer="B", module_id=5),
        Quiz(question="What does SQL stand for?", options='["A. Simple Query Language", "B. Structured Query Language", "C. Standard Query Line"]', correct_answer="B", module_id=3),
        Quiz(question="What is a dataset in data science?", options='["A. A code snippet", "B. A collection of data", "C. A machine learning tool"]', correct_answer="B", module_id=1),
        Quiz(question="What is the main purpose of pandas in Python?", options='["A. Data analysis", "B. API management", "C. Web development"]', correct_answer="A", module_id=1),
        Quiz(question="Which HTML tag is used to create an ordered list?", options='["A. <ol>", "B. <ul>", "C. <li>"]', correct_answer="A", module_id=2),
        Quiz(question="In CSS, what does 'padding' refer to?", options='["A. Space outside an element", "B. Space inside an element", "C. Elements font size"]', correct_answer="B", module_id=2),
        Quiz(question="Which function would you use to create a simple plot in Python?", options='["A. plt.scatter", "B. plt.line", "C. plt.plot"]', correct_answer="C", module_id=4),
        Quiz(question="What is a 'div' element in HTML?", options='["A. Used to style fonts", "B. Container for content", "C. Used for linking"]', correct_answer="B", module_id=2),
    ]

    db.session.add_all(quizzes)
    db.session.commit()  

    # Seed progress
    progresses = [
        Progress(user_id=1, module_id=1, completed=True),
        Progress(user_id=2, module_id=2, completed=False),
        Progress(user_id=3, module_id=3, completed=False),
        Progress(user_id=4, module_id=4, completed=True),
        Progress(user_id=5, module_id=5, completed=False),
        Progress(user_id=6, module_id=6, completed=False)
    ]
    db.session.add_all(progresses)
    db.session.commit()

    # Seed comments
    comments = [
        Comment(content="Great resource!", user_id=1, resource_id=1),
        Comment(content="Very informative.", user_id=2, resource_id=2),
        Comment(content="Needs more details.", user_id=3, resource_id=3),
        Comment(content="Helpful content.", user_id=4, resource_id=4),
        Comment(content="Good for beginners.", user_id=5, resource_id=5),
        Comment(content="Could be clearer.", user_id=6, resource_id=6)
    ]
    db.session.add_all(comments)
    db.session.commit()

    # Seed badges
    badges = [
        Badge(name="Beginner", description="Completed 1 module", points_required=100),
        Badge(name="Intermediate", description="Completed 5 modules", points_required=500),
        Badge(name="Advanced", description="Completed 10 modules", points_required=1000),
        Badge(name="Expert", description="Completed 20 modules", points_required=2000),
        Badge(name="Master", description="Completed 30 modules", points_required=3000),
        Badge(name="Legend", description="Completed 50 modules", points_required=5000)
    ]
    db.session.add_all(badges)
    db.session.commit()

    # Seed achievements
    achievements = [
        Achievement(user_id=1, badge_id=1),
        Achievement(user_id=2, badge_id=2),
        Achievement(user_id=3, badge_id=3),
        Achievement(user_id=4, badge_id=4),
        Achievement(user_id=5, badge_id=5),
        Achievement(user_id=6, badge_id=6)
    ]
    db.session.add_all(achievements)
    db.session.commit()

    # Seed user learning paths
    user_learning_paths = [
        UserLearningPath(user_id=1, learning_path_id=1),
        UserLearningPath(user_id=2, learning_path_id=2),
        UserLearningPath(user_id=3, learning_path_id=3),
        UserLearningPath(user_id=4, learning_path_id=4),
        UserLearningPath(user_id=5, learning_path_id=5),
        UserLearningPath(user_id=6, learning_path_id=6)
    ]
    db.session.add_all(user_learning_paths)
    db.session.commit()

    # # Commit the changes
    # db.session.commit()

print("Database seeded successfully.")