# Командный проект по курсу «Профессиональная работа с Python»

---
VKinder - это чат-бот, который ищет потенциальных собеседников на основе предпочтений пользователя, используя данные из ВКонтакте (VK).
---
### Начало работы
Чтобы начать работу с VKinder, выполните следующие действия:
---
Необходимые условия
```
- Python
- PostgreSQL
- vk_api
```
---
### Установка
#### Чтобы установить VKinder, выполните следующие шаги:

##### Клонируйте репозиторий на вашу локальную машину.

```bash
git clone git@github.com:Warswat/adpy-team-diplom.git
cd adpy-team-diplom
```
#####  Создайте виртуальную среду и активируйте ее.

```bash
python3 -m venv venv
env/bin/activate
```
#####  Установите необходимые пакеты.

```bash
pip install -r requirements.txt
```
---
####  Получение токенов пользователя и группы
_Чтобы получить USER_TOKEN_:

- Перейдите на сайт https://vkhost.github.io/ и нажмите на "vk.com"
- Скопируйте токен из адресной строки.

_Чтобы получить GROUP_TOKEN_:

- Перейдите по адресу https://vk.com/@vksoftred-kak-poluchit-token-soobschestva-vkontakte.
- Следуйте инструкциям на странице для получения токена.
---
### Запуск и использование
1. Переименуйте файл .env-examlpe в .env
2. Создайте БД
2. Пропишите в файле .env все необходимые доступы (к Базе данных, токены)
3. Запустите main.py.

```bash
python main.py
```
---
#### Функционал бота
- Для навигации по чат боту можно воспользоваться меню бота в чате
    - Чтобы начать подбор потенциальных знакомст нужно воспользоваться кнопками **"Подобрать"** или **"Автоподбор"**
    - Чтобы добавить в кандидата в избранное нужно нажать кнопку **"Избранное"**    
        - Чтобы посмотреть список избранных нужно нажать кнопку **"Показать избранных"**
    - Чтобы заблокировать кандидата нужно нажать кнопку **"Заблокировать"**
        - Чтобы посмотреть заблокированых **"Показать заблокированных"**
    - Чтобы посмотреть следующего кандидата нужно нажать кнопку **"Следующий"**
    - Так же бот предусматривает возможность поставить лайк и дизлайк(в меню присутствуют одноименные кнопки)
    - Для выхода из поиска нужно нажать кнопку **"Выйти"**

  ### Команда проекта:
  А. Владимир
  Б. Дмитрий Трубянов
  В. Дмитрий Корольков
