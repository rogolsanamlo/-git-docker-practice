# پروژه تمرین Git و Docker

یک برنامه خیلی کوچک Flask که یک صفحه سلام نشون می‌ده.
هدف این پروژه یاد گرفتن Git و Docker است، نه خود برنامه.

## فایل‌ها

| فایل | کارش |
|------|------|
| `app.py` | خود برنامه Flask |
| `requirements.txt` | لیست پکیج‌های پایتون |
| `Dockerfile` | دستور ساخت ایمیج داکر |
| `.dockerignore` | فایل‌هایی که وارد ایمیج نشن |
| `.gitignore` | فایل‌هایی که وارد گیت نشن |

---

## بخش اول: Git

داخل پوشه پروژه:

```bash
git init
git add .
git commit -m "اولین کامیت: برنامه Flask"
```

برای گذاشتن روی GitHub (اول یک ریپوی خالی در GitHub بساز):

```bash
git branch -M main
git remote add origin https://github.com/USERNAME/git-docker-practice.git
git push -u origin main
```

### تمرین‌های پیشنهادی گیت

1. یک شاخه (branch) جدید بساز: `git checkout -b feature/greeting`
2. در `app.py` یک مسیر جدید مثل `/about` اضافه کن.
3. کامیت کن و به شاخه main ادغام (merge) کن:
   ```bash
   git checkout main
   git merge feature/greeting
   ```
4. با `git log --oneline` تاریخچه رو ببین.
5. یک اشتباه عمدی بکن و با `git restore` یا `git revert` برگردون.

---

## بخش دوم: Docker

### ساخت ایمیج

```bash
docker build -t git-docker-practice .
```

### اجرای کانتینر

```bash
docker run -p 5000:5000 git-docker-practice
```

حالا در مرورگر برو به: http://localhost:5000

### اجرا با متغیر محیطی

```bash
docker run -p 5000:5000 -e NAME=رقیه git-docker-practice
```

### اجرا در پس‌زمینه و مدیریت

```bash
docker run -d -p 5000:5000 --name myapp git-docker-practice
docker ps                # کانتینرهای در حال اجرا
docker logs myapp        # لاگ‌ها
docker stop myapp        # توقف
docker rm myapp          # حذف کانتینر
```

### تمرین‌های پیشنهادی داکر

1. پورت بیرونی رو عوض کن: `-p 8080:5000`
2. متن صفحه رو در `app.py` عوض کن، دوباره build کن و ببین چه تغییری کرد.
3. داخل کانتینر برو: `docker exec -it myapp bash`
4. با `docker images` اندازه ایمیج رو ببین.
5. بعداً یک `docker-compose.yml` اضافه کن.


This project is for learning Git and Docker.