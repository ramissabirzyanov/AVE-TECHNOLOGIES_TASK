**Задача**

Необходимо разработать RESTful сервис с использованием Fast API и Redis.
Эндпоинты  (ручки)
•   	Запись и обновление данных
•   	Phone
•   	Address
•   	Получение данных
•   	Phone

Примеры использования сервиса: 

Получение данных по телефону:
GET /check_data?phone=89090000000
Сервис ищет адрес по номеру телефона в Redis и возвращает его в ответе.
Запись новых данных:
POST /write_data
{
  "phone": "89090000000",
  "address": "г. Москва, ул. Примерная, д. 1"
}
Сервис сохраняет данные в Redis по ключу phone.
Обновление адреса:

POST /write_data
{
  "phone": "89090000000",
  "address": "г. Москва, ул. Новая, д. 5"
}
Сервис перезаписывает адрес по тому же номеру.

**Выполнено:**
- Все поставленные задачи
- Интеграционные тесты
- Контейнеризация
