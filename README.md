# CarZone — Second-Hand Car Marketplace

A full-stack web application where customers can list their used cars for sale, and buyers can browse, search, and send inquiries. An admin reviews and approves all listings before they go public.

---

## Features

- **User Registration & Login** — Secure authentication using Django's built-in auth system
- **Post a Car** — Logged-in users can submit car listings with photos and full details
- **Admin Approval Workflow** — Every submission is reviewed by admin before going live
- **Search & Filter** — Filter cars by keyword, model, city, year, body style, and price range
- **Inquiry System** — Buyers can send inquiries on any car listing; admin gets email notification
- **User Dashboard** — Users can track their own listings (with approval status) and their past inquiries
- **Featured Cars** — Admin can spotlight selected cars on the homepage

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10 |
| Framework | Django 3.0.7 |
| Database | SQLite (development) / PostgreSQL (production) |
| Frontend | HTML, CSS, Bootstrap 4, jQuery |
| Rich Text Editor | django-ckeditor |
| Image Handling | Pillow |
| Static Files | Whitenoise |
| Auth | Django built-in authentication |

---

## Project Structure

```
carzone/
├── carzone/          # Project config (settings, root URLs)
├── pages/            # Public pages: Home, About, Services, Contact
├── cars/             # Core app: listings, search, post, approval
├── accounts/         # User auth: register, login, logout, dashboard
├── contacts/         # Inquiry system
├── templates/        # All HTML templates
├── static/           # CSS, JS, fonts, images
├── media/            # User-uploaded car photos (not tracked in git)
└── db.sqlite3        # SQLite database (not tracked in git)
```

---

## Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/pranayreddy-08/carzone.git
cd carzone
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Create a superuser (admin account)
```bash
python manage.py createsuperuser
```

### 6. Run the development server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## Usage

### As a Customer
1. Register at `/accounts/register`
2. Log in and click **"Post a Car"** in the top bar
3. Fill in car details and upload photos → submit for approval
4. Track your listing status in your **Dashboard**

### As Admin
1. Log in at `/admin/` with superuser credentials
2. Go to **Cars** → filter by **"Pending Approval"**
3. Select listings and use **"Approve selected cars"** action
4. Approved cars appear immediately on the public site

### Searching Cars
- Use the search bar on the homepage or visit `/cars/search`
- Filter by model, city, year, body style, or price range

---

## Database Models

### Car
| Field | Description |
|---|---|
| `car_title` | Listing title |
| `model`, `year`, `color`, `condition` | Basic info |
| `price` | Asking price |
| `state`, `city` | Location |
| `engine`, `transmission`, `fuel_type` | Specs |
| `features` | Multi-select (AC, Airbags, Cruise Control, etc.) |
| `car_photo` + 4 extras | Upload photos |
| `description` | Rich text description |
| `is_featured` | Show on homepage spotlight |
| `is_approved` | Admin must approve before going public |
| `owner` | FK to User — who submitted the listing |

### Contact (Inquiry)
Stores every buyer inquiry: `car_id`, `user_id`, `name`, `email`, `phone`, `message`

### Team
Team members displayed on the About page.

---

## URL Reference

| URL | Description |
|---|---|
| `/` | Homepage |
| `/cars/` | All approved listings |
| `/cars/<id>` | Car detail page |
| `/cars/search` | Search with filters |
| `/cars/post` | Post a car (login required) |
| `/accounts/register` | Register |
| `/accounts/login` | Login |
| `/accounts/dashboard` | My listings & inquiries (login required) |
| `/admin/` | Admin panel (superuser only) |

---

## Screenshots

> Add screenshots here after running the project locally.

---

## Author

**Pranay Reddy** — [GitHub](https://github.com/pranayreddy-08)
