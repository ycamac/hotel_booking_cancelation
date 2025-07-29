# 🏨 Hotellingece - Hotel Booking Cancellation Predictor

A modern, modular Streamlit web application designed to help hotel administrators predict booking cancellations using AI-powered analytics.

## 🚀 Features

- **🔐 Authentication**: Secure login system for hotel administrators
- **📊 Dashboard**: Real-time analytics and performance metrics
- **📝 Booking Management**: Create and manage bookings with instant cancellation predictions
- **🔍 Advanced Filtering**: Search and filter bookings by multiple criteria
- **📈 Analytics**: Monitor cancellation rates and booking trends
- **👥 Team Information**: Learn about the team and company vision


## 🏗️ Architecture

The application is built with a **modular, component-based architecture** for better maintainability and scalability:

```
hotel_booking_cancellation_app/
├── app.py                          # Main application entry point
├── requirements.txt                 # Python dependencies
├── README.md                       # Project documentation
├── components/                     # Reusable UI components
│   ├── __init__.py
│   ├── navigation.py              # Navigation bar component
│   ├── auth.py                    # Authentication component
│   └── styling.py                 # CSS styling component
├── data/                          # Data management layer
│   ├── __init__.py
│   └── bookings_data.py           # Booking data functions
└── pages/                         # Page components
    ├── __init__.py
    ├── home_page.py               # Home page component
    ├── new_booking_page.py        # New booking form component
    ├── bookings_page.py           # Bookings list component
    ├── dashboard_page.py          # Analytics dashboard component
    └── about_page.py              # About page component
```

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd hotel_booking_cancellation_app
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

4. **Access the application:**
   - Open your browser and go to `http://localhost:8501`
   - Use demo credentials: `admin` / `password123`

## 📋 Usage

### 🔐 Authentication
- Login with demo credentials: `admin` / `password123`
- Secure session management with automatic logout

### 🏠 Home Page
- Welcome message and app introduction
- Key features overview
- "How It Works" guide

### 📊 Dashboard
- Real-time performance metrics
- Cancellation rate trends
- Hotel type distribution charts
- Model performance indicators
- Recent activity feed

### 📝 New Booking
- Comprehensive booking form with all required fields
- Instant cancellation prediction
- Progress bar visualization
- Automatic booking storage

### 📋 Bookings Management
- View all current bookings
- Advanced search and filtering
- Status badges and prediction scores
- Progress bar visualization for predictions
- Quick analytics overview

### 👥 About
- Team member profiles
- Company mission and values
- Contact information



## 🏗️ Technical Architecture

### **Modular Design**
- **Components**: Reusable UI components for navigation, authentication, and styling
- **Pages**: Separate modules for each page with focused responsibilities
- **Data Layer**: Centralized data management with booking functions
- **Main App**: Clean entry point with routing logic

### **Key Benefits**
- ✅ **Maintainability**: Easy to modify individual components
- ✅ **Scalability**: Simple to add new pages and features
- ✅ **Reusability**: Components can be reused across pages
- ✅ **Testing**: Each module can be tested independently
- ✅ **Collaboration**: Multiple developers can work on different modules

### **Component Structure**
```python
# Components
components/
├── navigation.py    # Navigation bar with menu items
├── auth.py         # Login/logout functionality
└── styling.py      # CSS styles and theming

# Pages
pages/
├── home_page.py    # Landing page with app overview
├── dashboard_page.py    # Analytics and metrics
├── new_booking_page.py # Booking form and prediction
├── bookings_page.py    # Booking management
└── about_page.py       # Team and company info

# Data
data/
└── bookings_data.py    # Booking data functions
```

## 🔧 Dependencies

- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Plotly**: Interactive charts and visualizations
- **Watchdog**: File system monitoring for development

## 🎯 Features Implemented

- ✅ **Modular Architecture**: Component-based design for scalability
- ✅ **Authentication System**: Secure login/logout functionality
- ✅ **Responsive Design**: Modern UI with custom styling
- ✅ **Data Management**: Centralized booking data functions
- ✅ **Advanced Filtering**: Search and filter capabilities
- ✅ **Real-time Analytics**: Dashboard with charts and metrics
- ✅ **Progress Visualization**: Progress bars for prediction scores
- ✅ **Form Validation**: Input validation and error handling
- ✅ **Session Management**: State management across pages

## 🚀 Future Enhancements

- **Database Integration**: Connect to real database systems
- **API Development**: RESTful API for external integrations
- **Machine Learning**: Real ML model integration
- **User Management**: Multi-user support with roles
- **Notifications**: Real-time alerts and notifications
- **Mobile App**: Native mobile application
- **Advanced Analytics**: More sophisticated reporting
- **Multi-language Support**: Internationalization

## 👥 Team

- **Francisco Meza**: Lead Data Scientist & ML Engineer
- **Yulian Cama**: Full Stack Developer & UI/UX Designer



---

**Built with ❤️ for the hospitality industry** 