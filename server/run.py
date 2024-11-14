import os
from app import create_app, db
from app.routes import api_bp

# Create the application instance
app = create_app()

# Register blueprint for API routes
app.register_blueprint(api_bp, url_prefix='/api')

# Run the application
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5555)) 
    app.run(host="0.0.0.0", port=port, debug=True)
