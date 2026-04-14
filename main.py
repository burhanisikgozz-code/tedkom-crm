from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
<head>
<title>TEDKOM CRM</title>
<style>
body { font-family: Arial; background:#0f172a; color:white; padding:20px;}
.card { background:#1e293b; padding:20px; margin:10px; border-radius:10px;}
input { padding:8px; margin:5px;}
button { padding:8px; background:#3b82f6; color:white; border:none;}
</style>
</head>
<body>

<h1>TEDKOM CRM</h1>

<div class="card">
<h2>Müşteri</h2>
<input id="customer"/>
<button onclick="addCustomer()">Ekle</button>
<ul id="customers"></ul>
</div>

<div class="card">
<h2>Teklif</h2>
<input id="offer"/>
<button onclick="addOffer()">Ekle</button>
<ul id="offers"></ul>
</div>

<div class="card">
<h2>Kasa (USD)</h2>
<p id="balance">0</p>
<button onclick="addMoney()">+100$</button>
</div>

<script>
let customers=[]
let offers=[]
let balance=0

function addCustomer(){
 let v=document.getElementById("customer").value
 customers.push(v)
 render()
}

function addOffer(){
 let v=document.getElementById("offer").value
 offers.push(v)
 render()
}

function addMoney(){
 balance+=100
 render()
}

function render(){
 document.getElementById("customers").innerHTML=customers.map(c=>"<li>"+c+"</li>").join("")
 document.getElementById("offers").innerHTML=offers.map(o=>"<li>"+o+"</li>").join("")
 document.getElementById("balance").innerText=balance+" $"
}
</script>

</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def home():
    return html
