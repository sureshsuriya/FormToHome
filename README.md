# 🏡 FormToHome

FormToHome is an online platform that allows users to submit and manage service request forms. It is designed to connect service providers with users in a seamless and efficient manner.

## 🚀 Features
- 🗉️ **Service Request Form Submission** – Users can submit forms online.
- 🍔 **Vegetable Seller Integration** – Sellers can list vegetables with price and location.
- 📍 **Location Tracking** – Users can view seller locations and collect items.
- 🔐 **User Authentication** – Secure login and registration system.
- 📊 **Data Management** – Backend processing with MongoDB.

## 🛠️ Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** MongoDB
- **Version Control:** Git & GitHub

## 📂 Folder Structure
```
FormToHome/
│── env/                     # Virtual environment
│── static/                  # Static files (CSS, JS)
│── templates/               # HTML templates
│── app/                     # Django App
│   ├── models.py            # Database models
│   ├── views.py             # Views logic
│   ├── urls.py              # URL routing
│── manage.py                # Django project manager
│── README.md                # Project documentation
```

## 🛠️ Setup Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/sureshsuriya/FormToHome.git
   ```
2. Navigate into the project directory:
   ```sh
   cd FormToHome
   ```
3. Create a virtual environment and activate it:
   ```sh
   python -m venv env
   source env/bin/activate  # On macOS/Linux
   env\Scripts\activate     # On Windows
   ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Run the development server:
   ```sh
   python manage.py runserver
   ```

## 📌 How to Contribute
1. Fork the repository.
2. Create a new branch:
   ```sh
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```sh
   git commit -m "Added new feature"
   ```
4. Push to GitHub:
   ```sh
   git push origin feature-branch
   ```
5. Open a **Pull Request**.

## 🐟 License
This project is licensed under the **MIT License**.

---

