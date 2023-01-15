from flask import Flask, render_template,request,jsonify,send_file
from utils.upi_qr_code_generator import generateUPIQR
app = Flask(__name__)

@app.route("/")
def home():
    return "QR code generator app"

@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}!"

@app.route("/upi-qr")
def getQR():
    amount = request.args.get("amount")
    upi_address = request.args.get("adr")
    user_name = request.args.get("name")
    imageData = generateUPIQR(upi_address,amount,user_name)
    return send_file('upi_qr.png', mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
