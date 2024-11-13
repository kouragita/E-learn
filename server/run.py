from app import create_app, db

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
from app import create_app, db
from app.routes import api_bp

app = create_app()
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
