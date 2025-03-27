from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Koyeb वर सर्व्हर चालू आहे!"  # Health Check साठी हा route गरजेचा आहे!

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)  # 0.0.0.0 आणि पोर्ट 8080 हे नक्की करा!
