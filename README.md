## Проект ABC-forum

ABC-forum - свободный форум для общения по самым разным темам. 
Проект доступен по адресу [https://abc-forum.didns.ru](https://abc-forum.didns.ru).

### Автор проекта:

Фуллстек-разработка и дизайн: Ильдар Аюпов, 2023 г., e-mail: ildarbon@gmail.com, Telegramm: @ildarbonn

### Техническое описание проекта:

Основные библиотеки и технологии:
- Бэкенд: Python, Django, PostgreSQL, pillow, sorl-thumbnail.
- Фронтенд: Bootstrap, HTML, CSS, Javascript.  
- Деплой: Docker, Gunicorn, NGINX, Continuous Deployment (GitHub Actions).

Реализованы такие вещи как:
- переопределена стандартная модель user, добавлены новые поля
- переопределены Class Based Views из django.contrib.auth.views
- отслеживание активности пользователей через middleware
- восстановление пароля по электронной почте
- пользовательские теги, фильтры (для контроля форм, подсчета количества сообщений, определения последнего сообщения и перевода даты и времени под часовой пояс пользователя)
- пагинация
- загрузка изображений для аватаров пользователей, в сообщения пользователей, отображение их в виде миниатюр или в полноразмерном виде
- ввод смайликов в сообщениях
- возможность цитирования сообщений других авторов

### Развернуть проект на локальной машине:

- Установить Docker, Docker Compose:
```
sudo apt update
sudo apt install curl
curl -fSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh
sudo apt-get install docker-compose-plugin
```

- Клонировать репозиторий:
```
git clone git@github.com:ildar-aiupov/abc-forum.git
```

- В корне проекта переименовать файл .env.example (настройки Джанго и подключения к базе данных) в файл .env (команда `mv .env.example .env`). Данные настройки приведены для примера, они не соответствуют реальным настройкам сайта в продакшене. Часть этих настроек (настройки электронной почты) необходимо переопределить, чтобы можно было запустить проект на локальной машине. 

- Находясь в корневой папке проекта, запустить его сборку:
```
sudo docker compose up -d
```

- При сборке проекта для демонстрации его работы сразу автоматически создается база данных из множества тем, сообщений, нескольких пользователей, одного суперпользователя. Суперпользователь (логин `admin`, пароль `admin`) необходим для работы с админ-панелью.

- Точки входа в проект:
```
Главная страница проекта: http://localhost:8000/

Админ-панель: http://localhost:8000/admin/
```

- Для остановки контейнеров Docker:
```
sudo docker compose down -v      # с их удалением (также удалаяется все хранилища данных проекта)
sudo docker compose stop         # просто остановка без удаления
```
