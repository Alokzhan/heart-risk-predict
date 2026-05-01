# ❤️ Heart Risk Prediction System

## 📌 Abstract

<p>
Heart disease remains one of the most prevalent and costly health conditions today. Unfortunately, treatment costs often place the burden beyond reach of many patients. By leveraging **Machine Learning and Data Mining techniques**, we can reduce this burden through early detection and risk prediction.

This **Heart Disease Prediction System (HDPS)** analyzes medical parameters to identify risk factors before they become critical. The system processes biomedical data to uncover hidden patterns and relationships between medical factors and heart disease risk, enabling intelligent clinical decisions and reducing overall healthcare costs while improving treatment quality.

The system predicts likelihood of heart disease based on patient profiles including blood pressure, age, sex, cholesterol, blood sugar, and other clinical indicators. Performance is validated through confusion matrix calculations ensuring high accuracy and reliability.
</p>

---

## 📌 Overview
A comprehensive **Django-based web application** for heart disease prediction using Machine Learning. This platform enables patients to predict heart disease risk, connect with doctors, and maintain their health records. Administrators can manage the system, doctors, and analyze prediction data.

---

## 📖 Introduction

<p>
The healthcare industry collects massive amounts of data containing valuable hidden information critical for making effective medical decisions. Advanced data mining and machine learning techniques can extract this knowledge to improve patient outcomes.

This Heart Disease Prediction System (HDPS) utilizes the **Gradient Boosting Classifier** and **Logistic Regression** algorithms to analyze 13 medical parameters and predict heart disease risk. The system enables healthcare providers to identify complex medical conditions and make intelligent diagnostic decisions before symptoms become critical.

By automating risk assessment, HDPS helps establish important relationships between medical factors and disease, providing significant medical insights and improving diagnostic accuracy.
</p>

### 🎯 Aim
To develop an intelligent system that predicts heart disease risk according to medical parameters provided by users, utilizing machine learning on historical cardiac datasets to enable early intervention and prevention.

### 🔍 Objectives
- Develop a user-friendly heart disease prediction system accessible to patients and healthcare providers
- Discover and extract hidden knowledge from historical cardiac datasets using data mining techniques
- Build a scalable medical decision support system to assist in heart disease prediction
- Improve early detection and reduce treatment costs through risk stratification
- Provide comprehensive patient management and doctor-patient connectivity

### 📊 Project Scope
- **Accessibility**: Generic software applicable across healthcare organizations
- **Users**: Patients, doctors, and administrators
- **Features**: Risk prediction, patient records, doctor management, feedback system
- **Data**: Historical heart disease datasets with 13 medical parameters
- **Deployment**: Web-based platform with cloud deployment capability
- **Scalability**: Designed to handle growing user base and data volume

---

## 🏗️ System Analysis & Modules

### Core Modules

**Patient Management:**
- **Patient Login** - Secure authentication using credentials
- **Patient Registration** - New users enter personal details and receive credentials
- **My Details** - View and manage personal medical information
- **Disease Prediction** - Input medical parameters and receive instant risk assessment with doctor recommendations based on locality
- **Search Doctor** - Find doctors by name, address, or specialty
- **Prediction History** - Retrieve and review past prediction results
- **Feedback System** - Submit feedback and report issues to administrators

**Doctor Management:**
- **Doctor Login** - Secure authentication for medical professionals
- **Patient Details** - View patient profiles and medical history
- **Patients List** - Access to all assigned patients
- **Notifications** - Real-time alerts on system usage and disease predictions
- **Prescription Management** - Manage patient recommendations

**Admin Management:**
- **Admin Login** - Superuser authentication and access control
- **Add Doctor** - Register and manage doctor accounts with approval workflow
- **Add Dataset** - Upload CSV files for model training
- **View Doctors** - Monitor all registered doctors and their details
- **View Patients** - Analyze user base and patient demographics
- **View Predictions** - Track prediction history and system analytics
- **View Feedback** - Monitor user feedback and system issues
- **Admin Dashboard** - System statistics and overview

---

## 🚀 Key Features

### For Patients
- ✅ **Heart Disease Prediction** - Input medical parameters to get instant risk assessment
- ✅ **Secure Authentication** - Register and login system with validation
- ✅ **Prediction History** - Track all previous predictions with timestamps
- ✅ **Profile Management** - Edit personal details and medical information
- ✅ **Doctor Search & Connection** - Find and contact certified doctors
- ✅ **Feedback System** - Submit feedback about the platform

### For Doctors
- ✅ **Doctor Dashboard** - Manage patient interactions
- ✅ **Patient Management** - View and manage patient records
- ✅ **Approval System** - Need admin approval to access the platform
- ✅ **Doctor Profiles** - Display expertise and contact information
- ✅ **Patient Search** - Find and view patient predictions

### For Administrators
- ✅ **Admin Dashboard** - Overview of system statistics
- ✅ **Doctor Management** - Approve/manage doctor registrations
- ✅ **Patient Management** - View and manage all patients
- ✅ **CSV Data Upload** - Bulk import health data
- ✅ **Feedback Monitoring** - View user feedback and issues
- ✅ **System Analytics** - Track predictions, users, and activities

---

## 🤖 Machine Learning Model Training

### Model Implementation
The prediction system uses a **Gradient Boosting Classifier** trained on the UCI Heart Disease Dataset with 13 medical features.

### Training Code
```python
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

def predict_heart_disease(list_data):
    """
    Predict heart disease risk based on medical parameters
    
    Parameters:
    list_data: List of 13 medical parameters in order
    
    Returns:
    accuracy: Model accuracy percentage
    prediction: 0 (No disease) or 1 (Disease present)
    """
    # Load training data
    csv_file = Admin_Helath_CSV.objects.get(id=1)
    df = pd.read_csv(csv_file.csv_file)
    
    # Feature selection - EXACT order must be maintained
    X = df[['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']]
    y = df['target']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=0.8, random_state=0
    )
    
    # Model training
    nn_model = GradientBoostingClassifier(
        n_estimators=100,
        learning_rate=1.0,
        max_depth=1,
        random_state=0
    )
    nn_model.fit(X_train, y_train)
    
    # Make prediction
    pred = nn_model.predict([list_data])
    accuracy = nn_model.score(X_test, y_test) * 100
    
    print(f"Model Accuracy: {accuracy:.2f}%")
    print(f"Prediction: {pred}")
    
    return accuracy, pred
```

### Input Features (13 Parameters)
1. **Age** - Patient age in years
2. **Sex** - Gender (0=Female, 1=Male)
3. **CP** - Chest pain type (0-3)
4. **Trestbps** - Resting blood pressure (mm Hg)
5. **Chol** - Serum cholesterol (mg/dl)
6. **Fbs** - Fasting blood sugar > 120 mg/dl (0/1)
7. **Restecg** - Resting electrocardiographic results (0-2)
8. **Thalach** - Maximum heart rate achieved
9. **Exang** - Exercise induced angina (0/1)
10. **Oldpeak** - ST depression
11. **Slope** - ST segment slope (0-2)
12. **Ca** - Vessels count (0-4)
13. **Thal** - Thalassemia type (0-3)

### Model Performance
- **Algorithm**: Gradient Boosting Classifier
- **Training Dataset Size**: 303 samples
- **Accuracy**: ~85% (varies with data quality)
- **Cross-validation**: 80% train, 20% test split

---

## 🛠️ Technology Stack

### Languages
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)

### Frameworks & Libraries
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![DRF](https://img.shields.io/badge/Django%20REST-ff9900?style=for-the-badge&logo=django&logoColor=white)

### Machine Learning & Data Science
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

### Database & Backend
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

### Deployment & Tools
![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

### IDEs
![VS Code](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![PyCharm](https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white)

### Operating Systems
![MacOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=apple&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

### Machine Learning Algorithms
- **[Gradient Boosting Classifier](https://en.wikipedia.org/wiki/Gradient_boosting)** - Primary prediction algorithm
- **[Logistic Regression](https://en.wikipedia.org/wiki/Logistic_regression)** - Binary classification baseline
- **Decision Tree** - Model comparison
- **Random Forest** - Ensemble methods

---

---

## 🔐 Security Features
- ✅ User authentication via Django ORM
- ✅ Password hashing with PBKDF2
- ✅ SQL injection protection (ORM parameterization)
- ✅ CSRF token protection on all forms
- ✅ Role-based access control (Patient/Doctor/Admin)
- ✅ Secure file uploads with validation
- ✅ Session management and timeouts
- ✅ Input validation and sanitization

---

## 🐛 Troubleshooting

### Common Issues & Solutions

**Issue**: Port 8000 already in use
```bash
python manage.py runserver 8001
```

**Issue**: Database not found / Migration errors
```bash
python manage.py makemigrations
python manage.py migrate
```

**Issue**: Static files not loading
```bash
python manage.py collectstatic --noinput
```

**Issue**: ModuleNotFoundError for dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Issue**: Permission denied on .venv
```bash
chmod -R 755 .venv/
```

**Issue**: Superuser already exists error
```bash
python manage.py shell
>>> from django.contrib.auth.models import User
>>> User.objects.filter(username='admin').delete()
>>> exit()
# Then create superuser again
```

**Issue**: Patient registration fails
- Check duplicate username/email
- Verify all required fields are filled
- Check file upload permissions for profile image

**Issue**: Doctor not appearing in list
- Check if doctor status = 1 (approved)
- Admin must approve doctor before visibility

---

## 📂 Project Structure (Detailed)
```
heart-risk-predict/
├── db.sqlite3                      # SQLite database
├── manage.py                       # Django CLI
├── requirements.txt                # Dependencies
├── README.md                       # Documentation
│
├── health/                         # Main Django App
│   ├── __init__.py
│   ├── admin.py                   # Django admin config
│   ├── apps.py                    # App configuration
│   ├── models.py                  # Data models
│   ├── views.py                   # View functions (~500 lines)
│   ├── api_views.py               # REST API views
│   ├── serializers.py             # DRF serializers
│   ├── forms.py                   # Django forms
│   ├── choices.py                 # Model choices
│   ├── tests.py                   # Unit tests
│   │
│   ├── migrations/
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   ├── 0002_admin_helath_csv.py
│   │   ├── 0003_search_data.py
│   │   ├── 0004_feedback.py
│   │   ├── 0005_auto_20210818_2220.py
│   │   ├── 0006_search_data_craeted.py
│   │   ├── 0007_auto_20210821_0119.py
│   │   └── 0008_auto_20210821_0121.py
│   │
│   ├── static/
│   │   ├── css/
│   │   │   ├── bootstrap.css       # Bootstrap framework
│   │   │   ├── css_slider.css      # Carousel styling
│   │   │   ├── font-awesome.min.css# Font icons
│   │   │   ├── single.css
│   │   │   └── style.css           # Custom styles
│   │   ├── fonts/
│   │   │   └── [Font files]
│   │   └── images/
│   │       └── aboutheart.jfif     # Asset images
│   │
│   └── templates/ (25+ HTML files)
│       ├── index.html              # Landing page
│       ├── carousel.html           # Home carousel
│       ├── about.html              # About page
│       ├── contact.html            # Contact page
│       ├── gallery.html            # Gallery page
│       ├── login.html              # Patient/Doctor login
│       ├── admin_login.html        # Admin login
│       ├── register.html           # User registration
│       ├── change_password.html    # Password change
│       ├── patient_home.html       # Patient dashboard
│       ├── doctor_home.html        # Doctor dashboard
│       ├── admin_home.html         # Admin dashboard
│       ├── add_heartdetail.html    # Prediction form
│       ├── predict_desease.html    # Results display
│       ├── view_search_pat.html    # History view
│       ├── search_doctor.html      # Doctor search
│       ├── view_doctor.html        # Doctor list
│       ├── add_doctor.html         # Add doctor form
│       ├── edit_doctor.html        # Edit doctor form
│       ├── view_patient.html       # Patient list
│       ├── view_feedback.html      # Feedback list
│       ├── profile_doctor.html     # Doctor profile
│       ├── edit_profile.html       # Edit profile
│       ├── zip_extractor.html      # Zip utilities
│       └── [other templates]
│
├── health_desease/                 # Django Project Settings
│   ├── settings.py                # Main config
│   ├── urls.py                    # URL routing
│   ├── urls1.py                   # Alternative URLs
│   ├── api.py                     # API config
│   ├── apirep.py                  # API routing
│   ├── wsgi.py                    # WSGI config
│   ├── asgi.py                    # ASGI config (WebSocket)
│   └── routing.py                 # WebSocket routing
│
├── Machine_Learning/
│   ├── Heart prediction.ipynb     # ML Jupyter notebook
│   └── heart.csv                  # UCI Heart dataset (303 samples)
│
└── media/                         # User uploads
    ├── profiles/                  # Profile images
    └── documents/                 # Uploaded documents
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8+
- pip or conda
- Git
- Virtual environment support

### Step 1: Clone Repository
```bash
git clone https://github.com/Alokzhan/heart-risk-predict.git
cd heart-risk-predict
```

### Step 2: Create Virtual Environment
```bash
# On macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

# On Windows
python -m venv .venv
.venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install --upgrade pip
pip install Django==3.1.6 djangorestframework pandas scikit-learn numpy matplotlib seaborn whitenoise gunicorn
```

Or install from requirements file:
```bash
pip install -r requirements.txt
```

### Step 4: Apply Database Migrations
```bash
python manage.py migrate
```

### Step 5: Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```

Follow the prompts to enter:
- **Username**: Your admin username
- **Email**: Your admin email
- **Password**: Secure password

### Step 6: Create Superuser for Testing (Optional)
```bash
python manage.py shell
>>> from django.contrib.auth.models import User
>>> User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
>>> exit()
```

### Step 7: Run Development Server
```bash
python manage.py runserver
```

The application will be available at: **`http://127.0.0.1:8000/`**

---

## 🚀 Quick Access URLs

| Function | URL |
|----------|-----|
| Home Page | `http://127.0.0.1:8000/` |
| Patient/Doctor Login | `http://127.0.0.1:8000/login` |
| New User Registration | `http://127.0.0.1:8000/signup` |
| Admin Login | `http://127.0.0.1:8000/login_admin` |
| Django Admin Panel | `http://127.0.0.1:8000/admin/` |
| API Endpoints | `http://127.0.0.1:8000/api/v1/` |

---

## 🌐 Deployment

### Local Deployment
Already covered in Installation & Setup section above.

### Production Deployment (Render)
1. Push repository to GitHub
2. Connect repository to [Render.com](https://render.com)
3. Set environment variables in Render dashboard:
   ```
   DEBUG = False
   ALLOWED_HOSTS = your-domain.onrender.com
   ```
4. Configure build and start commands in Render
5. Deploy via Render dashboard

**Important Production Settings**:
- Set `DEBUG = False` in production
- Use environment variables for sensitive data
- Configure `ALLOWED_HOSTS` properly
- Use WhiteNoise for static files

---

---

## ⚠️ Important Notes & Authentication Guide

### User Types & Authentication
1. **Patient/Doctor Account**:
   - Created via the **Register** button on homepage
   - Login at `/login` with registered credentials
   - Role determined at registration (Patient or Doctor)

2. **Admin Account**:
   - Created via `python manage.py createsuperuser` command
   - **Separate** from Patient/Doctor accounts
   - Login at `/login_admin` with superuser credentials
   - Access to Django Admin at `/admin/`

3. **Doctor Approval Workflow**:
   - New doctors register with status = 2 (pending)
   - Admin must approve before doctor can login
   - After approval, status = 1 (approved)
   - Only approved doctors can access doctor dashboard

### Database & Migrations
- SQLite database (`db.sqlite3`) is auto-created on first migration
- All migrations are pre-configured in `health/migrations/`
- Run `python manage.py migrate` to apply all migrations
- Use `python manage.py makemigrations` only if model changes are made

### Feature Order - DO NOT CHANGE
The feature order for ML prediction is critical:
```python
HEART_FEATURE_ORDER = [
    'age', 'sex', 'cp', 'trestbps', 'chol',
    'fbs', 'restecg', 'thalach', 'exang',
    'oldpeak', 'slope', 'ca', 'thal'
]
```
Always use this exact order when passing data to the prediction model.

### Environment Variables (Production)
```
DEBUG=False
ALLOWED_HOSTS=your-domain.onrender.com
SECRET_KEY=your-secret-key
DATABASE_URL=postgres://user:password@host/db
```

---

## 📝 Recent Updates & Fixes (April-May 2026)

### ✅ Django 6.0 Compatibility
- Fixed deprecated template tags ({% ifequal %} → {% if %})
- Updated 9+ HTML templates for modern Django
- Removed legacy template syntax

### ✅ Authentication & Validation
- Added duplicate user validation in signup
- Username and email uniqueness checks
- Improved error messages for duplicate users
- Fixed admin login security (null check on user.is_staff)

### ✅ System Improvements
- Python 3.12.3 virtual environment support
- All ML/DL packages updated (scikit-learn, pandas, numpy)
- Database migrations fully applied
- WhiteNoise middleware for static files

### ✅ User Experience
- Responsive Bootstrap design
- Improved form validation
- Better error handling
- Enhanced navigation

---

---

## 📖 Usage Guide

### For New Patients
1. Navigate to `http://127.0.0.1:8000/`
2. Click **"Register"** and select "Patient"
3. Enter personal details (name, email, password, DOB, contact, address)
4. Upload profile image
5. Submit registration
6. Login with credentials at `/login`

### For Predictions (Patient Workflow)
1. Login as Patient
2. Go to **"Add Heart Details"** or **"Predict Disease"**
3. Enter 13 medical parameters:
   - Age, Sex, Chest Pain Type
   - Blood Pressure, Cholesterol, Blood Sugar
   - ECG, Heart Rate, Exercise Angina
   - Old Peak, Slope, Vessel Count, Thalassemia
4. Submit form
5. View instant prediction with accuracy percentage
6. Access prediction history anytime

### For Doctors
1. Register as Doctor and wait for admin approval
2. After approval, login to doctor dashboard
3. View patient list and details
4. Access patient prediction history
5. Submit notifications and updates

### For Admins
1. Login at `/login_admin` with superuser credentials
2. Access **Admin Dashboard** at `/admin_home`
   - View statistics (predictions, patients, doctors, feedback)
3. Use **Django Admin** at `/admin/`
   - Add/approve doctors
   - Upload CSV datasets
   - Manage patients and records
   - View all feedback

---

## 🔗 API Endpoints

**Base URL**: `/api/v1/`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/patients/` | GET, POST | List all patients / Create new patient |
| `/doctors/` | GET, POST | List all doctors / Create new doctor |
| `/predictions/` | GET, POST | List predictions / Submit prediction |
| `/feedback/` | GET, POST | List feedback / Submit feedback |
| `/search-data/` | GET | Get search/prediction history |

### Example API Request
```bash
# Get all patients
curl -X GET http://127.0.0.1:8000/api/v1/patients/

# Submit prediction
curl -X POST http://127.0.0.1:8000/api/v1/predictions/ \
  -H "Content-Type: application/json" \
  -d '{"patient": 1, "result": "1", "accuracy": "85.5"}'
```

---

## 📊 Database Schema

### Patient Model
```python
class Patient(models.Model):
    user = ForeignKey(User)          # Link to Django User
    contact = CharField(max_length=100)
    address = CharField(max_length=100)
    dob = DateField()                # Date of birth
    image = FileField()              # Profile image
```

### Doctor Model
```python
class Doctor(models.Model):
    user = ForeignKey(User)
    status = IntegerField()          # 1=Approved, 2=Pending
    contact = CharField(max_length=100)
    address = CharField(max_length=100)
    category = CharField(max_length=100)  # Specialty
    doj = DateField()                # Date of joining
    dob = DateField()
    image = FileField()
```

### Search_Data Model (Predictions)
```python
class Search_Data(models.Model):
    patient = ForeignKey(Patient)
    prediction_accuracy = CharField()
    result = CharField()             # 0 or 1
    values_list = CharField()        # Input parameters
    created = DateTimeField(auto_now=True)
```

### Feedback Model
```python
class Feedback(models.Model):
    user = ForeignKey(User)
    messages = TextField()
    date = DateField(auto_now=True)
```

---

## 🔐 Security Features
- ✅ User authentication via Django ORM
- ✅ Password hashing with PBKDF2
- ✅ SQL injection protection (ORM parameterization)
- ✅ CSRF token protection on all forms
- ✅ Role-based access control (Patient/Doctor/Admin)
- ✅ Secure file uploads with validation
- ✅ Session management and timeouts
- ✅ Input validation and sanitization

---

## 📈 Model Performance
- **Accuracy**: ~85% (varies with dataset quality)
- **Training Data**: UCI Heart Disease Dataset (303 samples)
- **Algorithm**: Gradient Boosting Classifier
- **Test Set**: 20% of data (~60 samples)
- **Page Load Time**: < 2 seconds
- **API Response Time**: < 500ms

---

## 🤝 Contributing

We welcome contributions from the community!

### How to Contribute
1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Contribution Guidelines
- Follow PEP 8 style guide for Python
- Add comments for complex logic
- Update README if adding new features
- Test all changes locally before pushing
- Ensure no hardcoded credentials in commits

### Report Issues
1. Go to **Issues** tab
2. Click **New Issue**
3. Describe the problem with steps to reproduce and expected behavior

---

## 📝 License

This project is open-source and available under the **MIT License**.
You are free to use, modify, and distribute this project.

---

## 🙏 Acknowledgments

- **Dataset**: UCI Machine Learning Repository (Heart Disease Dataset)
- **Framework**: Django and Django REST Framework teams
- **ML Libraries**: Scikit-learn, NumPy, Pandas communities
- **UI Framework**: Bootstrap community
- **Icons**: Font Awesome

---

## 📧 Contact & Support

### Get Help
- **Issues**: Create an issue on GitHub
- **Discussions**: Use GitHub Discussions for questions
- **Documentation**: Check README and inline code comments

### Project Links
- **GitHub Repository**: [heart-risk-predict](https://github.com/Alokzhan/heart-risk-predict)
- **UCI Dataset**: [Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/heart+Disease)
- **Django Docs**: [Django 3.1+ Documentation](https://docs.djangoproject.com/)

---

## 🎓 Educational Use

This project was developed as a **college capstone project** to demonstrate:
- Full-stack web development with Django
- Machine Learning implementation and integration
- Database design and management
- Web API development
- Healthcare domain knowledge
- Real-world application architecture

---

## 🚀 Future Enhancements

- [ ] Mobile app (iOS/Android)
- [ ] Real-time notifications using WebSockets
- [ ] Advanced analytics dashboard
- [ ] Telemedicine features
- [ ] Multi-language support
- [ ] Blockchain for medical records
- [ ] AI-powered doctor matching
- [ ] Integration with health tracking devices

---

## 📚 Resources & References

### Django
- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Django Best Practices](https://docs.djangoproject.com/en/4.0/intro/contributing/)

### Machine Learning
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Gradient Boosting Theory](https://en.wikipedia.org/wiki/Gradient_boosting)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)

### Healthcare
- [Heart Disease Statistics](https://www.cdc.gov/heartdisease/)
- [Medical Parameter Guide](https://www.heart.org/)
- [Clinical Decision Support Systems](https://en.wikipedia.org/wiki/Clinical_decision_support_system)

---

## ✅ Quick Start Checklist for New Developers

- [ ] Clone the repository
- [ ] Create virtual environment
- [ ] Install dependencies
- [ ] Run migrations
- [ ] Create superuser
- [ ] Run development server
- [ ] Test patient registration
- [ ] Test prediction feature
- [ ] Access admin panel
- [ ] Review source code

---

**Last Updated**: May 2026  
**Maintained By**: Development Team  
**Status**: Active & Under Development  

⭐ If you find this project helpful, please consider giving it a star!

---

## ⚠️ Disclaimer

This project is for educational purposes only and should not be used for real medical diagnosis.


----------

## ⭐ Contributing

Contributions are welcome! Feel free to fork this repository and submit improvements.

----------

## 📜 License

This project is open-source and free to use.


