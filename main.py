from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import psycopg2
import os

app = FastAPI()

# Render environment variable
DATABASE_URL = os.environ.get("DATABASE_URL")

conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

# tablolar
cur.execute("CREATE TABLE IF NOT EXISTS customers (id SERIAL PRIMARY KEY, name TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS offers (id SERIAL PRIMARY KEY, name TEXT)")
conn.commit()


def render_page():
    cur.execute("SELECT name FROM customers ORDER BY id DESC")
    customers = "".join([f"<li>{c[0]}</li>" for c in cur.fetchall()])

    cur.execute("SELECT name FROM offers ORDER BY id DESC")
    offers = "".join([f"<li>{o[0]}</li>" for o in cur.fetchall()])

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title>TEDKOM CRM</title>
    </head>
    <body style='background:#0f172a;color:white;padding:20px;font-family:Arial'>

    <h1>TEDKOM CRM</h1>

    <h2>Müşteri</h2>
    <form method="post" action="/add_customer">
    <input name="name" placeholder="Müşteri adı"/>
    <button>Ekle</button>
    </form>
    <ul>{customers}</ul>

    <h2>Teklif</h2>
    <form method="post" action="/add_offer">
    <input name="name" placeholder="Teklif"/>
    <button>Ekle</button>
    </form>
    <ul>{offers}</ul>

    </body>
    </html>
    """


@app.get("/", response_class=HTMLResponse)
def home():
    return render_page()


@app.post("/add_customer", response_class=HTMLResponse)
def add_customer(name: str = Form(...)):
    cur.execute("INSERT INTO customers (name) VALUES (%s)", (name,))
    conn.commit()
    return render_page()


@app.post("/add_offer", response_class=HTMLResponse)
def add_offer(name: str = Form(...)):
    cur.execute("INSERT INTO offers (name) VALUES (%s)", (name,))
    conn.commit()
    return render_page()
