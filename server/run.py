import os
from app import create_app, db

# Create the application instance
app = create_app()

# Run the application
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5555)) 
    app.run(host="0.0.0.0", port=port, debug=True)
