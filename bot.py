import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "7844378037:AAEpS6OGCENm5qT6pQdvjsaZihsOqceBFIE"

bot = Bot(token="7844378037:AAEpS6OGCENm5qT6pQdvjsaZihsOqceBFIE")
dp = Dispatcher()

def reduce_to_digit(num):
    """Приводит число к однозначному значению (до 9)."""
    while num > 9:
        num = sum(int(digit) for digit in str(num))
    return num

def calculate_numbers(day: int, month: int, year: int, target_date: str):
    """Выполняет все расчёты чисел."""
    # Число сознания
    consciousness_number = reduce_to_digit(day)
    
    # Число миссии
    mission_number = reduce_to_digit(day + month + year)
    
    # Разбираем дату для расчёта личного года, месяца и дня
    target_day, target_month, target_year = map(int, target_date.split('.'))
    
    # Личный год
    personal_year = reduce_to_digit(day + month + target_year)
    
    # Личный месяц
    personal_month = reduce_to_digit(personal_year + target_month)
    
    # Личный день
    personal_day = reduce_to_digit(personal_month + target_day)
    
    return consciousness_number, mission_number, personal_year, personal_month, personal_day

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Привет! Введи две даты подряд в формате ДД.ММ.ГГГГ ДД.ММ.ГГГГ: сначала свою дату рождения, затем дату для расчёта")

@dp.message()
async def calculate_handler(message: Message):
    try:
        birth_date, target_date = message.text.split()
        day, month, year = map(int, birth_date.split('.'))
        
        results = calculate_numbers(day, month, year, target_date)
        response = (f"Число сознания: {results[0]}\n"
                    f"Число миссии: {results[1]}\n"
                    f"Личный год: {results[2]}\n"
                    f"Личный месяц: {results[3]}\n"
                    f"Личный день: {results[4]}")
        await message.answer(response)
    except Exception:
        await message.answer("Хм... что-то не так. Введите две даты в формате ДД.ММ.ГГГГ ДД.ММ.ГГГГ, чтобы всё сработало!")

async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())