# MuscleUp - Fitness Tracking App

A comprehensive mobile fitness tracking application that allows users to log workouts, track nutrition, and receive pose-based feedback on their exercise form.

## 🏗️ Project Structure

```
MuscleUp/
├── backend/                 # Flask API server
│   ├── app/
│   │   ├── models/         # SQLAlchemy models
│   │   ├── routes/         # API endpoints
│   │   ├── services/       # Business logic
│   │   ├── utils/          # Helper functions
│   │   └── __init__.py
│   ├── requirements.txt
│   └── run.py
├── frontend/               # React.js application
│   ├── src/
│   │   ├── components/     # Reusable components
│   │   ├── pages/          # Page components
│   │   ├── services/       # API calls
│   │   ├── utils/          # Helper functions
│   │   └── App.js
│   ├── package.json
│   └── public/
└── README.md
```

## 🚀 Features

- **User Authentication**: JWT-based login/registration
- **Workout Logging**: Track exercises, sets, reps, and weights
- **Nutrition Tracking**: Monitor calories and macronutrients
- **Pose Feedback**: AI-powered form analysis using MediaPipe
- **Progress Visualization**: Charts and analytics for fitness progress
- **Cross-Platform**: React.js frontend with Flask backend

## 🛠️ Tech Stack

### Frontend

- React.js
- Tailwind CSS
- Chart.js/Recharts
- Axios for API calls

### Backend

- Flask (Python)
- SQLAlchemy ORM
- JWT Authentication
- MediaPipe for pose estimation
- OpenCV for image processing
- MySQL database

## 📋 Getting Started

### Prerequisites

- Node.js (v16+)
- Python (v3.8+)
- MySQL (v8.0+)

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
python run.py
```

### Frontend Setup

```bash
cd frontend
npm install
npm start
```

## 🗄️ Database Schema

The app uses a MySQL database with the following main entities:

- **USER**: User profiles and preferences
- **EXERCISE**: Exercise definitions and categories
- **WORKOUT_LOG**: Individual workout sessions
- **NUTRITION_LOG**: Daily nutrition tracking
- **PROGRESS_RECORD**: Personal records and progress
- **POSE_FEEDBACK**: AI-generated form feedback

## 🔐 Authentication

JWT-based authentication with secure password hashing using bcrypt.

## 📱 API Endpoints

- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `GET /api/workouts` - Get user workouts
- `POST /api/workouts` - Log new workout
- `GET /api/nutrition` - Get nutrition logs
- `POST /api/nutrition` - Log nutrition entry
- `POST /api/pose-feedback` - Upload image for pose analysis

## 🚀 Deployment

- Frontend: Vercel/Netlify
- Backend: AWS/Render
- Database: MySQL on cloud provider
- Storage: AWS S3 for images
