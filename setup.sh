#!/bin/bash

# MuscleUp Setup Script
# This script sets up the complete MuscleUp application

set -e  # Exit on any error

echo "🏋️‍♂️ MuscleUp Setup Script"
echo "=========================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Check if required tools are installed
check_requirements() {
    print_info "Checking system requirements..."
    
    # Check Python
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 is not installed. Please install Python 3.8 or higher."
        exit 1
    fi
    print_status "Python 3 found: $(python3 --version)"
    
    # Check Node.js
    if ! command -v node &> /dev/null; then
        print_error "Node.js is not installed. Please install Node.js 16 or higher."
        exit 1
    fi
    print_status "Node.js found: $(node --version)"
    
    # Check npm
    if ! command -v npm &> /dev/null; then
        print_error "npm is not installed. Please install npm."
        exit 1
    fi
    print_status "npm found: $(npm --version)"
    
    # Check MySQL (optional)
    if ! command -v mysql &> /dev/null; then
        print_warning "MySQL client not found. You'll need to set up MySQL manually."
    else
        print_status "MySQL client found"
    fi
}

# Setup backend
setup_backend() {
    print_info "Setting up backend..."
    
    cd backend
    
    # Create virtual environment if it doesn't exist
    if [ ! -d "venv" ]; then
        print_info "Creating Python virtual environment..."
        python3 -m venv venv
    fi
    
    # Activate virtual environment
    print_info "Activating virtual environment..."
    source venv/bin/activate
    
    # Install Python dependencies
    print_info "Installing Python dependencies..."
    pip install --upgrade pip
    pip install -r requirements.txt
    
    # Create .env file if it doesn't exist
    if [ ! -f ".env" ]; then
        print_info "Creating .env file..."
        cp env.example .env
        print_warning "Please edit backend/.env file with your database credentials"
    fi
    
    print_status "Backend setup complete"
    cd ..
}

# Setup frontend
setup_frontend() {
    print_info "Setting up frontend..."
    
    cd frontend
    
    # Install Node.js dependencies
    print_info "Installing Node.js dependencies..."
    npm install
    
    print_status "Frontend setup complete"
    cd ..
}

# Initialize database
init_database() {
    print_info "Initializing database..."
    
    cd backend
    source venv/bin/activate
    
    # Run database initialization
    python init_db.py
    
    cd ..
    print_status "Database initialization complete"
}

# Main setup function
main() {
    echo ""
    print_info "Starting MuscleUp setup..."
    echo ""
    
    # Check requirements
    check_requirements
    echo ""
    
    # Setup backend
    setup_backend
    echo ""
    
    # Setup frontend
    setup_frontend
    echo ""
    
    # Ask about database initialization
    echo -e "${YELLOW}Do you want to initialize the database with sample data? (y/n)${NC}"
    read -r response
    if [[ "$response" =~ ^[Yy]$ ]]; then
        init_database
        echo ""
    else
        print_warning "Skipping database initialization. Run 'python backend/init_db.py' manually when ready."
        echo ""
    fi
    
    # Final instructions
    echo "🎉 Setup Complete!"
    echo ""
    echo "📋 Next Steps:"
    echo "1. Configure your database in backend/.env"
    echo "2. Start the backend server:"
    echo "   cd backend && source venv/bin/activate && python run.py"
    echo ""
    echo "3. Start the frontend development server:"
    echo "   cd frontend && npm start"
    echo ""
    echo "4. Open your browser to http://localhost:3000"
    echo ""
    echo "🔑 Demo Login Credentials:"
    echo "   Email: demo@muscleup.com"
    echo "   Password: demo123"
    echo ""
    echo "📚 For more information, check the README.md file"
}

# Run main function
main
