# url_shortner
Yakunin Ivan HW3


Сервис для сокращения длинных ссылок с поддержкой регистрации пользователей, аналитики переходов, ограниченного времени жизни ссылок и кэширования.

---

## Описание API

Сервис предоставляет REST API для управления короткими ссылками. Основные возможности:

- Создание коротких ссылок (`POST /links/shorten`)
- Переход по короткой ссылке (`GET /links/{short_code}`)
- Удаление короткой ссылки (`DELETE /links/{short_code}`)
- Обновление ссылки (`PUT /links/{short_code}`)
- Получение статистики (`GET /links/{short_code}/stats`)
- Поиск по оригинальной ссылке (`GET /links/search?original_url=...`)
- Регистрация и аутентификация пользователей (`/auth/register`, `/auth/login`, `/auth/logout`)
- Автоматическая очистка просроченных и неиспользуемых ссылок (фоновая задача)


## Примеры запросов

### Пример создания короткой ссылки
![Пример POST запроса на создание короткой ссылки c ошибкой в alias](images/shorten_error.png)

![Пример POST запроса на создание короткой ссылки без ошибкой в alias](images/shortner.png)


### Переход по короткой ссылке
![Пример POST запроса для редиректа на полную ссылку](images/links_short_url.png)

### Переход по полной ссылке
![Пример POST запроса для получения корокой ссылки по полной](images/links_full_url.png)


### Получение статистики по короткой ссылки
![Пример POST запроса для получение статистики по короткой ссылки](images/url_stats.png)

### Изменение полной ссылки для короткой
![Пример POST запроса для изменение полной ссылки для короткой](images/update_url.png)

### Удалеине короткой ссылки
![Пример POST запроса для удаления короткой ссылки](images/delete_url.png)


### Регистрация нового пользователя
![Пример POST запроса для регистрации нового пользователя](images/login.png)

### Вход в существующий аккаунт
![Пример POST запроса для входа в существующий аккаунт](images/login.png)

### Выход из аккаунта
![Пример POST запроса для выхода из аккаунта](images/logout.png)


## Схема базы данных

### `urls` — таблица коротких ссылок

| Поле           | Тип данных         | Описание                                                               |
|----------------|--------------------|------------------------------------------------------------------------|
| `id`           | Integer            | Первичный ключ                                                         |
| `short_url`    | String             | Уникальный короткий код (алиас) ссылки                                 |
| `long_url`     | String             | Исходная длинная ссылка                                                |
| `times_visited`| Integer            | Количество переходов по ссылке (по умолчанию 0)                        |
| `created_at`   | DateTime           | Дата и время создания ссылки (по умолчанию `now()`)                    |
| `last_visited` | DateTime           | Дата последнего перехода (по умолчанию `now()`)                        |
| `expires_at`   | DateTime (nullable)| Дата истечения срока действия ссылки                                   |
| `owner_id`     | Integer (nullable) | ID пользователя-владельца ссылки (внешний ключ на `users.id`)          |

---

### `users` — таблица пользователей

| Поле           | Тип данных | Описание                                                                |
|----------------|------------|-------------------------------------------------------------------------|
| `id`           | Integer    | Первичный ключ                                                          |
| `email`        | String     | Email пользователя (уникальный, индексированный)                        |
| `password_hash`| String     | Хеш пароля пользователя                                                 |
| `is_active`    | Boolean    | Флаг активности пользователя (по умолчанию `True`)                      |
| `created_at`   | DateTime   | Дата регистрации (по умолчанию `now()`)                                 |

---

### `expired_urls` — таблица удалённых/просроченных ссылок

| Поле           | Тип данных         | Описание                                                                |
|----------------|--------------------|-------------------------------------------------------------------------|
| `id`           | Integer            | Первичный ключ                                                          |
| `shortUrl`     | String             | Короткая ссылка                                                         |
| `longUrl`      | String             | Исходная длинная ссылка                                                 |
| `timesVisited` | Integer            | Количество переходов по ссылке (по умолчанию 0)                         |
| `createdAt`    | DateTime           | Дата создания                                                           |
| `lastVisited`  | DateTime (nullable)| Дата последнего перехода                                                |
| `expiresAt`    | DateTime (nullable)| Дата истечения срока действия                                           |
| `deletedAt`    | DateTime           | Дата удаления (по умолчанию `now()`)                                    |
| `owner_id`     | Integer (nullable) | ID владельца (если был)                                                 |


## Инструкция по запуску (через Docker)

Выполни команду:
```bash
docker-compose up --build
```

## Инструкция по запуску (через Python)

pip install -r requirements.txt
redis-server
uvicorn main:app --reload