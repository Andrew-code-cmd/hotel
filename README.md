## О чем проект?

Это портфолио-лендинг для гостиницы с Django-бэкендом и чистым ванильным фронтом.
Просто приятный, быстрый сайт, который легко поддерживать и ещё легче обновлять через встроенную админку.

## Стек

**Backend** | Python, Django |
**Frontend** | HTML5, CSS3, Vanilla JS |
**Библиотеки** | Swiper.js |
**БД** | SQLite (для локалки) |

## Что внутри

Приятный, адаптивный дизайн
Плавная карусель на Swiper.js
Django админка, готовая к бою 



## Как запустить? 

```bash
git clone https://github.com/Andrew-code-cmd/hotel.git
cd hotel

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
```
