from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import psycopg2

app = FastAPI()

conn = psycopg2.connect("postgresql://tedkom_db_user:H2QZKZMYawJpi3MH3jFS9tzpyWjSIwLy@dpg-d7f9jcd7vvec73a8a0v0-a/tedkom_db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS customers (id SERIAL PRIMARY KEY, name TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS offers (id SERIAL PRIMARY KEY, name TEXT)")
conn.commit()

html = """
<!DOCTYPE html>
<html>
<head>
<title>TEDKOM CRM</title>
</head>
<body style='background:#0f172a;color:white;padding:20px;font-family:Arial'>

<h1>TEDKOM CRM</h1>

<h2>Müşteri</h2>
<form method="post" action="/add_customer">
<input name="name"/>
<button>Ekle</button>
</form>

<ul>
%s
</ul>

<h2>Teklif</h2>
<form method="post" action="/add_offer">
<input name="name"/>
<button>Ekle</button>
</form>

<ul>
%s
</ul>

</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def home():
    cur.execute("SELECT name FROM customers")
    customers = "".join([f"<li>{c[0]}</li>" for c in cur.fetchall()])

    cur.execute("SELECT name FROM offers")
    offers = "".join([f"<li>{o[0]}</li>" for o in cur.fetchall()])

    return html % (customers, offers)


@app.post("/add_customer")
def add_customer(name: str):
    cur.execute("INSERT INTO customers (name) VALUES (%s)", (name,))
    conn.commit()
    return {"ok": True}


@app.post("/add_offer")
def add_offer(name: str):
    cur.execute("INSERT INTO offers (name) VALUES (%s)", (name,))
    conn.commit()
    return {"ok": True}
