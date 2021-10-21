# REST_API_survey_system

### _Документация API (автодокументирование на swagger (drf-yasg) доступно по адресу http://127.0.0.1:8000/swagger/ )

## ТЗ:

##### _Функционал для администратора системы:_
- авторизация в системе (регистрация не нужна)
- добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

##### _Функционал для пользователей системы:_
- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя


## Окружение проекта:
  * python 3.8
  * Django 2.2.10
  * djangorestframework

Склонируйте репозиторий с помощью git

    https://github.com/Bekbo01/REST_API_survey_system.git
Перейти в папку:
```bash
cd REST_API_survey_system
```
Создать и активировать виртуальное окружение Python.

Установить зависимости из файла **requirements.txt**:
```bash
pip install -r requirements.txt
```

* Команда для создания миграций приложения для базы данных
```bash
python manage.py makemigrations
python manage.py migrate
```
* Создание суперпользователя
```bash
python manage.py createsuperuser
```

* Команда для запуска приложения
```bash
python manage.py runserver
```
* Приложение будет доступно по адресу: http://127.0.0.1:8000/



### Чтобы получить токен пользователя: 
```
curl --location --request GET 'http://localhost:8000/api/login/' \
--form 'username=%username' \
--form 'password=%password'
```

### Чтобы создать опрос:
* Request method: POST
* URL: http://localhost:8000/api/poll/create/
```
curl --location --request POST 'http://localhost:8000/api/poll/create/' \
--header 'Authorization: Token %userToken' \
--form 'title=%title' \
--form 'start_date=%start_date' \
--form 'end_date=%end_date \
--form 'description=%description'
```

### Обновить опрос:
* Request method: PATCH
* URL: http://localhost:8000/api/poll/update/[pk]/

```
curl --location --request PATCH 'http://localhost:8000/api/poll/update/[pk]/' \
--header 'Authorization: Token %userToken' \
--form 'title=%title' \
--form 'end_date=%end_date \
--form 'description=%description'
```

### Удалить опрос:
* Request method: DELETE
* URL: http://localhost:8000/api/poll/update/[pk]
```
curl --location --request DELETE 'http://localhost:8000/api/poll/update/[pk]/' \
--header 'Authorization: Token %userToken'
```

### Посмотреть все опросы:
* Request method: GET
* URL: http://localhost:8000/api/poll/view/
```
curl --location --request GET 'http://localhost:8000/api/poll/view/' \
--header 'Authorization: Token %userToken'
```

### Просмотр текущих активных опросов:
* Request method: GET
* URL: http://localhost:8000/api/poll/view/active/
```
curl --location --request GET 'http://localhost:8000/api/poll/view/active/' \
--header 'Authorization: Token %userToken'
```

### Создаем вопрос:
* Request method: POST
* URL: http://localhost:8000/api/question/create/
```
curl --location --request POST 'http://localhost:8000/api/question/create/' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type \
```

### Обновляем вопрос:
* Request method: PATCH
* URL: http://localhost:8000/api/question/update/[pk]/
```
curl --location --request PATCH 'http://localhost:8000/api/question/update/[pk]/' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type \
```

### Удаляем вопрос:
* Request method: DELETE
* URL: http://localhost:8000/api/question/update/[pk]/
```
curl --location --request DELETE 'http://localhost:8000/api/question/update/[pk]/' \
--header 'Authorization: Token %userToken' \
--form 'poll=%pol' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type \
```

### Создаем выбор:
* Request method: POST
* URL: http://localhost:8000/api/option/create/
```
curl --location --request POST 'http://localhost:8000/api/option/create/' \
--header 'Authorization: Token %userToken' \
--form 'question=%question' \
--form 'option_text=%option_text'
```

### Обновляем выбор:
* Request method: PATCH
* URL: http://localhost:8000/api/option/update/[pk]/
```
curl --location --request PATCH 'http://localhost:8000/api/option/update/[pk]/' \
--header 'Authorization: Token %userToken' \
--form 'question=%question' \
--form 'option_text=%option_text'
```

### Удаляем выбор:
* Request method: DELETE
* URL: http://localhost:8000/api/option/update/[pk]/
```
curl --location --request DELETE 'http://localhost:8000/api/option/update/[pk]/' \
--header 'Authorization: Token %userToken' \
--form 'question=%question' \
--form 'option_text=%option_text'
```

### Создаем ответ:
* Request method: POST
* URL: http://localhost:8000/api/answer/create/
```
curl --location --request POST 'http://localhost:8000/api/answer/create/' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question=%question' \
--form 'option=%option \
--form 'option_text=%option_text'
```

### Обновляем ответ:
* Request method: PATCH
* URL: http://localhost:8000/api/answer/update/[pk]/
```
curl --location --request PATCH 'http://localhost:8000/api/answer/update/[pk]' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question=%question' \
--form 'option=%option \
--form 'option_text=%option_text'
```

### Удаляем ответ:
* Request method: DELETE
* URL: http://localhost:8000/api/answer/update/[pk]/
```

### Просматриваем ответы:
* Request method: GET
* URL: http://localhost:8000/api/answer/view/[pk]/
```
curl --location --request GET 'http://localhost:8000/api/answer/view/[pk]' \
--header 'Authorization: Token %userToken'
