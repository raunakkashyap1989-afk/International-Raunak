from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head><title>Raunak Kashyap - Kreative.</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
    body{background:#0f0f0f;color:white;text-align:center;font-family:Arial;padding:20px}
    h1{font-size:32px} h1 em{color:#ffcc00;font-style:normal}
    .btn{display:inline-block;background:#25D366;color:white;padding:14px 22px;border-radius:30px;text-decoration:none;font-weight:bold;margin:10px}
    .card{background:#1c1c1c;border-radius:16px;padding:20px;margin:15px auto;max-width:400px;text-align:left}
    .price{font-size:28px;color:#ffcc00;font-weight:bold}
    </style></head>
    <body>
    <h2>K. Kreative.</h2>
    <p>Budget me bada idea</p>
    <h1>Digital duniya me<br><em>apni pehchaan</em> banao.</h1>
    <p>Website ho, APK ho ya chhota kaam - <b>Rs.500 ke andar</b></p>
    <a class="btn" href="https://wa.me/916388866390?text=Namaste! Mujhe website banwani hai">Apna Idea Bhejein</a>

    <div class="card"><h3>Personal Website</h3><p>Apni identity online dikhaiye</p><div class="price">Rs.299</div><a class="btn" href="https://wa.me/916388866390?text=Mujhe Website banwani hai">Baat Karein</a></div>
    <div class="card"><h3>Simple APK</h3><p>Aapke idea ke liye Android App</p><div class="price">Rs.499</div><a class="btn" href="https://wa.me/916388866390?text=Mujhe APK banwana hai">Baat Karein</a></div>
    <div class="card"><h3>Small Changes</h3><p>Website me updates, buttons</p><div class="price">Rs.99+</div><a class="btn" href="https://wa.me/916388866390?text=Mujhe Small Changes karwane hai">Baat Karein</a></div>

    <h2>WhatsApp - 6388866390</h2>
    <a class="btn" href="https://wa.me/916388866390">WhatsApp Par Baat Karein</a>
    <p>Made by Raunak Kashyap</p>
    </body></html>
    """

if __name__ == '__main__':
    app.run(debug=True)
