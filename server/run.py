from app import create_app, db

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
from app import create_app, db
from app.routes import api_bp

app = create_app()
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5555))  # Use environment variable or default to 5555
    app.run(host="0.0.0.0", port=port, debug=True)
