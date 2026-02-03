#!/usr/bin/env python3
"""
MuscleUp Backend Server
Flask application entry point
"""

import os
from dotenv import load_dotenv
from app import create_app

# Load environment variables
load_dotenv()

# Create Flask app instance
app = create_app()

if __name__ == '__main__':
    # Get configuration from environment
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 5001))  # Changed to 5001 to avoid AirPlay conflict
    debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    
    print(f"🚀 Starting MuscleUp Backend Server...")
    print(f"📍 Server running on http://{host}:{port}")
    print(f"🔧 Debug mode: {debug}")
    
    app.run(host=host, port=port, debug=debug)
