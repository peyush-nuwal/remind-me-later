
# Remind me later


A simple web app that allows users to set reminders with a message. The app supports storing reminders in a database and will later support sending reminders via SMS or email.



---



## 🚀 Features

- 🗓️ **Create reminders** by sending a POST request with message, date, time, and reminder type.
- 🛠️ **Basic validation** for required fields like message, date, and time.
- 💾 **Store reminders** in a PostgreSQL database using Supabase as the database provider.
- 🔒 **CSRF protection** with Django's CSRF middleware, disabled for API requests using the `@csrf_exempt` decorator.
- ⚙️ **Easy-to-use API** for future extension with more reminder types and features.

## 🧰 Tech Stack

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)




## Screenshots

![App Screenshot](/ss/ss-1.png)

![App Screenshot](/ss/ss-2.png)

![App Screenshot](/ss/ss-3.png)







## 🛠 Installation & Setup

To run this app locally, follow these steps:

1. **Clone the repository**
```bash
git clone https://github.com/peyush-nuwal/remind-me-later.git
cd remind-me-later
```

2. **Set up a virtual environment**
```bash
python -m venv venv
```

3. **Activate the virtual environment**
 on Windows
```bash
venv\Scripts\activate

```
on macOS/Linux
```bash
source venv/bin/activate

```

4. **Install the required dependencies**
```bash
pip install -r requirements.txt

```

5. **Set up the database and migrations**
```bash
python manage.py migrate


```

6. **Run the development server**
```bash
python manage.py runserver


```

7. **The application will be running at**
```bash
http://127.0.0.1:8000/

```

## 📬 Contact

-Portfolio [peyush-nuwal-portfolio.vercel.app](https://peyush-nuwal-portfolio.vercel.app/)
- LinkedIn: [linkedin.com/in/peyush-nuwal](https://linkedin.com/in/peyush-nuwal)
- Email: piyushnawal19@gmail.com

