# KapkandexDisk
# KapkaYandex Market
KapkaYandex_Products

![test and deploy](https://github.com/kapkaevandrey/KapkandexDisk/actions/workflows/disk_workflow.yml/badge.svg)

### _Описание проекта_
> ***Linus Torvalds***
>>Большинство хороших программистов делают свою работу не потому, что ожидают оплаты или признания, а потому что получают удовольствие от программирования.
>>
Бэкенд для веб-сервиса сравнения цен на товары. Учебный проект в рамках проектного задания для поступления в Школу бэкенд-разработки Яндекс.

Пример запущенного сервиса https://bonus-2051.usr.yandex-academy.ru/ 

### _Технологии_
 - __[Python 3.10.1](https://docs.python.org/3/)__
 - __[Fast API 0.82](https://fastapi.tiangolo.com/)__
 - __[SQLAlchemy 1.4.41](https://www.sqlalchemy.org/)__
 - __[Alembic 1.8.1](https://alembic.sqlalchemy.org/en/latest/)__
 - __[Pydantic 1.10.2](https://alembic.sqlalchemy.org/en/latest/)__
 - __[Uvicron 0.18.3](https://www.uvicorn.org/)__
 - __[pytest 7.1.3](https://docs.pytest.org/en/7.1.x/)__
 - __[dateutil 2.8.2](https://dateutil.readthedocs.io/en/stable/)__
 - __[Poetry 1.2.0](https://python-poetry.org/)__
 - __[Docker](https://www.docker.com/)__


## _Как запустить проект_:
________________________________________
________________________________________

### _Локальный запуск_
________________________________________
Клонировать репозиторий и перейти в него в командной строке:
```shell
https://github.com/kapkaevandrey/KapkandexDisk.git
```

```shell
cd KapkandexDisk
```

#### Используйте Poetry (предпочтительный способ)
Если poetry не установлен, то просто следуйте официальной __[инструкции](https://python-poetry.org/docs/)__ 

Что бы в дальнейшем poetry создавал виртуально окружение прямо в папке с проектом выполните:

```shell
poetry config virtualenvs.in-project true
```

Посмотреть полный список настроек:
```shell
poetry config --list
```

Следующая команд создаст виртуальное окружение и установит все зависимости из файла __pyproject.toml__
```shell
poetry install
```

#### Виртуальное окружение через requirements.txt
Данный способ не является приоритетным т.к. автор может просто забыть добавить что-то в requirements во время
разработки, чего не происходить если вы работаете в среде __poetry__ (Это не реклама)

Cоздать и активировать виртуальное окружение:

```bash
python3 -m venv venv
```

```shell
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```shell
python3 -m pip install --upgrade pip
```

```shell
python3 pip install -r requirements.txt
```

Заполните файл __.env__, предварительно создав его в главной директории проекта. Для примера в директории проекта есть файл ```example.env```

Пример заполнения для локального запуска
```dotenv
APP_TITLE=Market                            # название приложения
APP_DESCRIPTION=application for             # описание приложения
DATABASE_URL=sqlite+aiosqlite:///./disk.db  # данные для подключения к БД
SECRET=My Big Super Puper Secret            # секретный ключ вашего приложения
```
☑️ ___Примечание___: в приведённом выше примере в качестве БД используется **[SQLite](https://www.sqlite.org/index.html)** 
с асинхронным драйвером **[aiosqlite](https://pypi.org/project/aiosqlite/)**, драйвер присутствует в списке зависимостей (для реализации тестирования).


Выполните миграции Alembic
```shell
alembic upgrade head
```
Запустите приложение
```shell
uvicorn app.main:app
```
в режиме автоматического отслеживания изменений. Внимание работает **[watchgod](https://pypi.org/project/watchgod/)**
```shell
uvicorn app.main:app --reload
```
Документация к проекту будет доступна по адресу http://127.0.0.1:8000/docs или http://127.0.0.1:8000/redoc
### _Запуск в контейнере Docker_ 
________________________________________
__Внимание:__ контейнеры использую **poetry**

Установите Docker, просто следуйте [инструкции](https://docs.docker.com/desktop/linux/install/) на официальном сайте.
Изучите файл [docker-compose.yml](https://github.com/kapkaevandrey/KapkaYandex_Products/blob/main/docker-compose.yml) в репозитории проекта. 

Обратите внимание, что сборка контейнера осуществляется с использованием 
готового образа ([15052016/disk:latest](https://hub.docker.com/r/15052016/disk)) расположенного на DockerHub. 

В проекте настроено __CI__ так что образ обновляется при каждом обновлении в репозитории. 
Подробности в файле [disk_workflow](https://github.com/kapkaevandrey/KapkandexDisk/blob/main/.github/workflows/disk_workflow.yml)

#### _Запуск с использованием готового образа_
Дополните файл __.env__ данными для создания базы данных PostgreSQL
```dotenv
POSTGRES_DB=disk.db         # имя базы данных
POSTGRES_USER=postrges      # имя пользователя
POSTGRES_PASSWORD=postgres  # пароль пользователя
POSTGRES_PORT=5432          # порт доступа
```
Имя хоста в данном случае совпадает с именем контейнера **_db_**

В итоге в файле __.env__ имя переменной ```DATABASE_URL``` должно выглядеть примерно следующим образом:
```dotenv
DATABASE_URL==postgresql+asyncpg://db:postgres@postgres:5432/disk.db
```
Выполните из директории с проектом команду:
```shell
docker-compose up
```
Документация к проекту будет доступна по адресу http://127.0.0.1/docs или http://127.0.0.1/redoc

#### _Запуск с использованием образа собранного из исходных файлов проекта_
Для такого подхода вам придётся изменить файл `docker-compose.yaml`
>Замените
>```yaml
> image: 15052016/disk:latest
>```
>на
> ```yaml
> build: .
>```
В данном случае образ будет собран по образу `Dockerfile` в директории проекта.

Выполните из директории с проектом команду:
```shell
docker-compose up
```
Документация к проекту будет доступна по адресу http://127.0.0.1/docs или http://127.0.0.1/redoc
### _Описание работы сервиса_:
__________________________________________
Сервис позволяет создавать файлы и папки образуя иерархическую древовидную структуру.
Каждый файл может быть прикреплён к определённой папке и, в свою очередь,
каждая папка может быть прикреплена к другой папке. Сервис позволяет отслеживать изменение размера 
как определённого файла,
так и определённой папки. Размер папки отображает суммарный размер всех файлов находящихся 
в этой папке и во всех подпапках в глубину.
При удалении файлов или папок, размеры обновляются автоматически.

### _Набор доступных эндпоинтов_:
* ```/imports``` - (_POST_) Импортирует элементы файловой системы. Элементы импортированные повторно обновляют текущие. 
Изменение типа элемента с папки на файл и с файла на папку не допускается. Порядок элементов в запросе является произвольным.
* ```/nodes/{id}``` - (_GET_) Получить информацию об элементе по идентификатору. При получении информации о папке также предоставляется информация о её дочерних элементах.
* ```/delete/{id}``` - (_DELETE_) Удалить элемент по идентификатору. При удалении папки удаляются все дочерние элементы. Доступ к истории обновлений удаленного элемента невозможен.
### _Набор эндпоинтов в разработке (deprecated)_:
* ```/updates``` - (_GET_) Получение списка файлов, которые были обновлены за последние 24 часа включительно от времени переданном в запросе.
    * ```date``` - _QUERY PARAMETERS_ - Дата и время запроса. __required__ Example: date=2022-05-28T21:12:01.000Z
* ```/node/{id}/history/``` - (_GET_) Получение истории обновлений по элементу за заданный полуинтервал [from, to). История по удаленным элементам недоступна.
    * ```dateStart``` - _QUERY PARAMETERS_ - Дата и время начала интервала, для которого считается история. Example: ```dateStart=2022-05-28T21:12:01.000Z```
    * ```dateStart``` - _QUERY PARAMETERS_ - Дата и время конца интервала, для которого считается история. Example: ```dateEnd=2022-05-28T21:12:01.000Z```

### _Примеры запросов_:
_________________________________
## _Примеры выполнения запросов_:
##### Импортируем объекты
`/imports`
>
>request body
> ```json
> {
>  "items": [
>    {
>      "id": "root1",
>      "url": null,
>      "parentId": null,
>      "size": null,
>      "type": "FOLDER"
>    },
>    {
>      "id": "file1_1",
>      "url": "/file/1_1",
>      "parentId": "root1",
>      "size": 15,
>      "type": "FILE"
>    }
>  ],
>  "updateDate": "2022-05-28T21:12:01.000Z"
> }
>```
>Response sample (status code = 200)

##### Получаем данные об объекте
`/nodes/root1` *id=root1*
>
> Response sample (status code = 200)
> ```json
> {
>  "id": "root1",
>  "url": null,
>  "parentId": null,
>  "type": "FOLDER",
>  "size": 15,
>  "date": "2022-05-28T21:12:01Z",
>  "children": [
>    {
>      "id": "root1_1",
>      "url": null,
>      "parentId": "root1",
>      "type": "FOLDER",
>      "size": null,
>      "date": "2022-05-28T21:12:01Z",
>      "children": []
>    },
>    {
>      "id": "file1_1",
>      "url": "/file/1_1",
>      "parentId": "root1",
>      "type": "FILE",
>      "size": 15,
>      "date": "2022-05-28T21:12:01Z",
>      "children": null
>    }
>  ]
> }
>```

________________________________

### Автор проекта:
#### Андрей ***Lucky*** Капкаев
#### email: kapkaew@yandex.ru
>*Улыбайтесь - это всех раздражает :relaxed:.*