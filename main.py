from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

customers = []
offers = []

def render_page():
    return f"""
    <html>
    <body style='background:#0f172a;color:white;padding:20px;font-family:Arial'>

    <h1>TEDKOM CRM</h1>

    <h2>Müşteri</h2>
    <form method="post" action="/add_customer">
    <input name="name"/>
    <button>Ekle</button>
    </form>
    <ul>{"".join([f"<li>{c}</li>" for c in customers])}</ul>

    <h2>Teklif</h2>
    <form method="post" action="/add_offer">
    <input name="name"/>
    <button>Ekle</button>
    </form>
    <ul>{"".join([f"<li>{o}</li>" for o in offers])}</ul>

    </body>
    </html>
    """

@app.get("/", response_class=HTMLResponse)
def home():
    return render_page()

@app.post("/add_customer", response_class=HTMLResponse)
def add_customer(name: str = Form(...)):
    customers.append(name)
    return render_page()

@app.post("/add_offer", response_class=HTMLResponse)
def add_offer(name: str = Form(...)):
    offers.append(name)
    return render_page()
