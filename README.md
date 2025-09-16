# outpost-welltech-CFDI-form

Quick start (Replit via GitHub)

Import this repo into Replit (Connect GitHub → select repo).

In Replit, add Secrets (Environment Variables):

SMTP_HOST (e.g., smtp.gmail.com)

SMTP_PORT (e.g., 587)

SMTP_USER (SMTP username / from-address)

SMTP_PASS (SMTP password or app password)

MAIL_TO = anca@outpostnow.com

Click Run. The app listens on $PORT (default 8080). Share the public URL.

Local dev (optional)
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # edit values
python app.py

App runs at http://localhost:8080.
