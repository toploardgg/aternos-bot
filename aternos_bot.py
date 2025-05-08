import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# === ТВОИ НАСТРОЙКИ ===
BOT_TOKEN = '7121189704:AAFjgU0n6ylB0hB9Cie9SumEwrIKkvTpfTE'
ATERNOS_USERNAME = 'Zapyck'
ATERNOS_PASSWORD = '12345lol12345'
ATERNOS_SERVER_NAME = 'Toploardgg.aternos.me:39466'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

async def start_aternos_server():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://aternos.org/go/")
        await asyncio.sleep(2)

        driver.find_element(By.ID, "user").send_keys("Zapyck")
        driver.find_element(By.ID, "password").send_keys("12345lol12345")
        driver.find_element(By.CLASS_NAME, "login-button").click()
        await asyncio.sleep(5)

        driver.get("https://aternos.org/server/")
        await asyncio.sleep(5)

        start_button = driver.find_element(By.CLASS_NAME, "start")
        start_button.click()
        await asyncio.sleep(5)

        return "Сервер запускається!"

    except Exception as e:
        return f"Ошибка: {e}"
    finally:
        driver.quit()

@dp.message_handler(commands=["start"])
async def handle_start_server(message: types.Message):
    await message.reply("Запускаю сервер Aternos...")
    result = await start_aternos_server()
    await message.reply(result)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)