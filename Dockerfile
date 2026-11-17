# ۱) ایمیج پایه: پایتون سبک
FROM python:3.12-slim

# ۲) پوشه کاری داخل کانتینر
WORKDIR /app

# ۳) اول فقط requirements رو کپی و نصب می‌کنیم
#    تا اگر کد عوض شد، نصب پکیج‌ها دوباره انجام نشه (کش داکر)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ۴) بعد بقیه کد رو کپی می‌کنیم
COPY . .

# ۵) پورتی که برنامه روش اجرا می‌شه
EXPOSE 5000

# ۶) دستور اجرای برنامه
CMD ["python", "app.py"]
