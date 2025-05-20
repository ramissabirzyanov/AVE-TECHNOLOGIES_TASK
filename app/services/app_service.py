from app.services.redis_service import RedisService


# Хотя в рамках этой задачи слой Service может выглядеть избыточным,
# он изолирует бизнес-логику и работу с Redis,
# не допуская прямого обращения к БД из контроллеров.
# Это улучшает архитектуру и упрощает тестирование.


class AppService:
    def __init__(self):
        self.redis = RedisService()

    async def write_data(self, data):
        await self.redis.write_data(data)

    async def chekc_data_by_phone(self, phone):
        data = await self.redis.check_data_by_phone(phone)
        return data
