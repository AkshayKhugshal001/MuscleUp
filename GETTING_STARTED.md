# 🏋️‍♂️ MuscleUp - Getting Started Guide

Welcome to MuscleUp, your comprehensive fitness tracking application with AI-powered pose analysis!

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)

```bash
# Run the setup script
./setup.sh
```

### Option 2: Manual Setup

#### 1. Backend Setup

```bash
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp env.example .env
# Edit .env with your database credentials

# Initialize database
python init_db.py
```

#### 2. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install
```

## 🗄️ Database Configuration

### MySQL Setup

1. Install MySQL 8.0+
2. Create a database:
   ```sql
   CREATE DATABASE muscleup_db;
   ```
3. Update `backend/.env` with your credentials:
   ```
   DB_HOST=localhost
   DB_PORT=3306
   DB_NAME=muscleup_db
   DB_USER=your_username
   DB_PASSWORD=your_password
   ```

## 🏃‍♂️ Running the Application

### Start Backend Server

```bash
cd backend
source venv/bin/activate
python run.py
```

Backend will run on http://localhost:5000

### Start Frontend Development Server

```bash
cd frontend
npm start
```

Frontend will run on http://localhost:3000

## 🔑 Demo Login

Use these credentials to test the application:

- **Email:** demo@muscleup.com
- **Password:** demo123

## 📱 Features Overview

### 🏋️‍♂️ Workout Tracking

- Log exercises with sets, reps, weight, and duration
- Track rest times and add notes
- Filter workouts by exercise, date range
- View workout statistics and recent sessions

### 🍎 Nutrition Tracking

- Daily calorie and macro tracking
- Set calorie targets
- Track protein, carbs, fats, fiber, sugar, sodium
- Monitor water intake
- Visual progress indicators

### 📈 Progress Monitoring

- Record personal records for exercises
- Track body measurements (weight, body fat, muscle mass)
- Body measurements (chest, waist, arm, thigh)
- Visual progress charts
- Historical data analysis

### 📸 AI Pose Analysis

- Upload exercise images for form analysis
- Get AI-powered feedback using MediaPipe
- Receive improvement suggestions
- Track form scores over time
- Support for squats, push-ups, and more exercises

### 👤 User Management

- Secure JWT-based authentication
- User profile management
- Fitness goals and experience level tracking
- Password change functionality

## 🛠️ Technology Stack

### Backend

- **Flask** - Web framework
- **SQLAlchemy** - ORM
- **JWT** - Authentication
- **MediaPipe** - Pose estimation
- **OpenCV** - Image processing
- **MySQL** - Database

### Frontend

- **React.js** - UI framework
- **Tailwind CSS** - Styling
- **Recharts** - Data visualization
- **React Router** - Navigation
- **Axios** - API communication

## 📁 Project Structure

```
MuscleUp/
├── backend/                 # Flask API server
│   ├── app/
│   │   ├── models/         # Database models
│   │   ├── routes/         # API endpoints
│   │   └── __init__.py
│   ├── requirements.txt
│   ├── init_db.py         # Database initialization
│   └── run.py             # Server entry point
├── frontend/               # React application
│   ├── src/
│   │   ├── components/     # Reusable components
│   │   ├── pages/          # Page components
│   │   ├── services/       # API services
│   │   └── contexts/       # React contexts
│   └── package.json
├── setup.sh               # Automated setup script
└── README.md
```

## 🔧 API Endpoints

### Authentication

- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `GET /api/auth/profile` - Get user profile
- `PUT /api/auth/profile` - Update profile

### Workouts

- `GET /api/workouts` - Get user workouts
- `POST /api/workouts` - Create workout
- `PUT /api/workouts/:id` - Update workout
- `DELETE /api/workouts/:id` - Delete workout

### Nutrition

- `GET /api/nutrition` - Get nutrition logs
- `POST /api/nutrition` - Create nutrition log
- `PUT /api/nutrition/:id` - Update nutrition log

### Progress

- `GET /api/progress` - Get progress records
- `POST /api/progress` - Create progress record
- `GET /api/progress/personal-records` - Get personal records

### Pose Analysis

- `POST /api/pose-feedback/analyze` - Analyze exercise image
- `GET /api/pose-feedback` - Get pose feedbacks

## 🎯 Supported Exercises for Pose Analysis

Currently supports pose analysis for:

- **Squats** - Analyzes knee angle, back position, depth
- **Push-ups** - Analyzes elbow angle, body alignment
- **Generic** - Basic pose detection for other exercises

## 🚀 Deployment

### Backend Deployment

1. Set up a cloud database (AWS RDS, Google Cloud SQL)
2. Configure environment variables
3. Deploy to Heroku, AWS, or similar platform

### Frontend Deployment

1. Build the React app: `npm run build`
2. Deploy to Vercel, Netlify, or similar platform

## 🐛 Troubleshooting

### Common Issues

1. **Database Connection Error**

   - Check MySQL is running
   - Verify credentials in `.env`
   - Ensure database exists

2. **MediaPipe Installation Issues**

   - Update pip: `pip install --upgrade pip`
   - Install with: `pip install mediapipe`

3. **Frontend Build Errors**
   - Clear node_modules: `rm -rf node_modules && npm install`
   - Check Node.js version (16+ required)

## 📞 Support

For issues or questions:

1. Check the troubleshooting section
2. Review the API documentation
3. Check the console for error messages

## 🎉 Enjoy Your Fitness Journey!

MuscleUp is designed to help you track your fitness progress with precision and get AI-powered feedback to improve your form. Start logging your workouts, tracking your nutrition, and analyzing your exercise form today!
