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


Семинар 3

Задание 1:
● Изменяем задачу 8 из семинара 1 с выводом двух html страниц: главной и о себе.
● Перенесите вёрстку в шаблоны.
● Представления должны пробрасывать полезную информацию в шаблон через контекст.

Задание 2:
● Доработаем задачу 1.
● Выделите общий код шаблонов и создайте родительский шаблон base.html.
● Внесите правки в дочерние шаблоны.

Задание 3:
● Доработаем задачу 7 из урока 1, где бросали монетку, игральную кость и генерировали случайное число.
● Маршруты могут принимать целое число - количество бросков.
● Представления создают список с результатами бросков и передают его в контекст шаблона.
● Необходимо создать универсальный шаблон для вывода результатов любого из трёх представлений.

Задание 4:
● Доработаем задачи из прошлого семинара по созданию моделей автора, статьи и комментария.
● Создайте шаблон для вывода всех статей автора в виде списка заголовков.
○ Если статья опубликована, заголовок должен быть ссылкой на статью.
○ Если не опубликована, без ссылки.
● Не забываем про код представления с запросом к базе данных и маршруты.

Задание 5:
● Доработаем задачу 4.
● Создай шаблон для вывода подробной информации о статье.
● Внесите изменения в views.py - создайте представление и в urls.py - добавьте маршрут.
● *Увеличивайте счётчик просмотра статьи на единицу при каждом просмотре

Задание 6:
● Измените шаблон для вывода заголовка и текста статьи, а также всех комментариев к статье с указанием текста
комментария, автора комментария и даты обновления комментария в хронологическом порядке.
● Если комментарий изменялся, дополнительно напишите “изменено”.
● Не забывайте про представление с запросом в БД и маршруты. Проверьте, что они работают верно


Семинар 4

Задание 1:
● Доработаем задачу про броски монеты, игральной кости и случайного числа.
● Создайте форму, которая предлагает выбрать: монета, кости, числа.
● Второе поле предлагает указать количество попыток от 1 до 64

Задание 2:
● Доработаем задачу 1.
● Создайте представление, которое выводит форму выбора.
● В зависимости от переданных значений представление вызывает одно из трёх представлений,
созданных на прошлом семинаре (если данные прошли проверку, конечно же).

Задание 3:
● Продолжаем работу с авторами, статьями и комментариями.
● Создайте форму для добавления нового автора в базу данных.
● Используйте ранее созданную модель Author

Задание 4:
● Аналогично автору создайте форму добавления новой статьи.
● Автор статьи должен выбираться из списка (все доступные в базе данных авторы).

Задание 5:
● Доработаем задачу 6 из прошлого семинара.
● Мы сделали вывод статьи и комментариев. Добавьте форму ввода нового комментария в существующий шаблон.


Семинар 5

Задание 1:
● Проверьте возможность доступа к админке.
● Создайте суперпользователя и войдите в админ панель

Задание 2:
● Подключите к админ панели созданные вами в рамках прошлых семинаров модели в приложениях:
○ случайные числа,
○ блог,
○ магазин,
○ другие, если вы их создавали.

Задание 3:
● Создайте в админ панели несколько групп. Логика следующая:
● Группа определяет права внутри своего приложения
● Группа читателей может просматривать модели приложения
● Группа редакторов может читать, добавлять и изменять модели приложения
● Группа админы также может удалять модели

Задание 4:
● Создайте десяток разных пользователей.
● Помимо минимальной информации заполните дополнительные поля модели.
● Дайте пользователям права из различных групп, а также дополнительные индивидуальные разрешения.

Задание 5:
● Настройте под свои нужды вывод информации об авторах, статьях и комментариях на страницах списков.

Задание 6:
● Настройте под свои нужды вывод информации об авторах,
статьях и комментариях на страницах вывода информации об объекте.
"""