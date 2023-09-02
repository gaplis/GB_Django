"""
Семинар 1

Задание 1:
● Подготовить среду для разработки проекта с помощью команд терминала.
● Создать каталог для Django задач в рамках семинаров.
● Развернуть в каталоге виртуальное окружение.
● Установить фреймворк Django

Задание 2:
● Создайте проект и приложение Django.
● Подключите приложение к проекту.
● Убедитесь, что встроенный Django сервер работает.

Задание 3:
● Настройте работу сервера в вашей локальной сети.
● Убедитесь что при запуске на ПК, сайт можно посмотреть в
браузере другого устройства локальной сети: другой ПК, ноутбук, телефон и т.п.

Задание 4:
● Создайте представление “Привет, мир!” внутри вашего
первого приложения.
● Настройте маршруты

Задание 5:
● Создайте новое приложение. Подключите его к проекту.
В приложении должно быть три простых представления, возвращающих HTTP ответ:
● Орёл или решка
● Значение одной из шести граней игрального кубика
● Случайное число от 0 до 100
● Пропишите маршруты

Задание 6:
Добавьте логирование в проект.
● Настройте возможность вывода в файл и в терминал.
● Устраните возможные ошибки.
● *Форматирование настройте по своему желанию. Объясните что вы выводите в логи

Задание 7:
● Доработайте задачи 5 и 6.
● Сохраняйте в логи значения, которые генерирует каждое из представлений.


Семинар 2

Задание 1:
● Создайте модель для запоминания бросков монеты: орёл или решка.
● Также запоминайте время броска


Задание 2:
● Доработаем задачу 1.
● Добавьте статический метод для статистики по n последним броскам монеты.
● Метод должен возвращать словарь с парой ключейзначений, для орла и для решки.

Задание 3:
● Создайте модель Автор. Модель должна содержать следующие поля:
○ имя до 100 символов
○ фамилия до 100 символов
○ почта
○ биография
○ день рождения
● Дополнительно создай пользовательское поле “полное имя”, которое возвращает имя и фамилию.

Задание 4:
● Создайте модель Статья (публикация).
Авторы из прошлой задачи могут писать статьи.
У статьи может быть только один автор.
У статьи должны быть следующие обязательные поля:
○ заголовок статьи с максимальной длиной 200 символов
○ содержание статьи
○ дата публикации статьи
○ автор статьи с удалением связанных объектов при удалении автора
○ категория статьи с максимальной длиной 100 символов
○ количество просмотров статьи со значением по умолчанию 0
○ флаг, указывающий, опубликована ли статья со значением по умолчанию False

Задание 5:
● Доработаем задачу 4.
● Создай четыре функции для реализации CRUD в модели Django Article (статья).
● *Используйте Django команды для вызова функций.

Задание 6:
● Создайте модель Комментарий.
● Авторы могут добавлять комментарии к своим и чужим статьям. Т.е. у комментария может быть один автор.
● И комментарий относится к одной статье. У модели должны быть следующие поля
○ автор
○ статья
○ комментарий
○ дата создания
○ дата изменения

Задание 7:
● Создайте функции для работы с базой данных:
○ Поиск всех статей автора по его имени
○ Поиск всех комментариев автора по его имени
○ Поиск всех комментариев по названию статьи
● Каждая из трёх функций должна иметь возможность сортировки и ограничение выборки по количеству.
"""