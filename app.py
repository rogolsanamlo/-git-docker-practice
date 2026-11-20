import os
from flask import Flask

app = Flask(__name__)

# اسم رو از متغیر محیطی می‌خونیم. اگر نبود، "دنیا" استفاده می‌شه.
NAME = os.environ.get("NAME", "دنیا")

# شمارنده بازدید (در حافظه نگه داشته می‌شه)
visits = 0


@app.route("/")
def home():
    global visits
    visits += 1
    return f"سلام {NAME}! به نسخه جدید برنامه خوش آمدی. بازدید: {visits}"


@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/visits")
def show_visits():
    return {"visits": visits}

if __name__ == "__main__":
    # host=0.0.0.0 یعنی از بیرون کانتینر هم بشه بهش وصل شد
    app.run(host="0.0.0.0", port=5000)
