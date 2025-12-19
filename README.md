📌 Возможности
- CRUD для Постов
- Комментарии
- Права доступа: редактировать может только автор
- Аутентификация JWT
- Swagger документация (SPECTACULAR)

🚀 Как запустить

### 1. Клонировать проект
git clone <repo_url>

### 2. Установить зависимости
pip install -r requirements.txt

### 3. Применить миграции
python manage.py migrate

### 4. Создать суперпользователя
python manage.py createsuperuser

### 5. Запустить сервер
python manage.py runserver
🔑 JWT
POST /api/v1/token/  
POST /api/v1/token/refresh/

 📚 Документация
Swagger:  
`/api/docs/`

OpenAPI schema:  
`/api/schema/`

## 🛠 Используемый стек
- Python 3.12
- Django 5+
- DRF
- SimpleJWT
- drf-spectacular
- SQLite/PostgreSQL
