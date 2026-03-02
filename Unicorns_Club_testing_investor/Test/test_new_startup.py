import time
import pytest
from selene import browser
from pages.login_page import LoginPage
from pages.new_startup_page_required_fields import NewStartupPage
from config import BASE_URL
from datetime import datetime


class TestCreateStartup:

    def test_create_startup_only_mandatory_fields(self):
        """Заполнение только обязательных полей и публикация профиля"""

        # 1. Сначала логинимся
        login_page = LoginPage()
        login_page.login_as('valya15fenichco.com@mail.ru', 'ZXqwcver1029')  # введи реальный пароль
        time.sleep(10)

        # 2. Теперь открываем страницу создания стартапа
        #    (после логина мы уже авторизованы)
        page = NewStartupPage().open()

        # 3. Заполняем обязательные поля
        page.fill_name("Test Startup")
        time.sleep(1)

        page.fill_ceo_name("John Doe")
        time.sleep(1)

        page.select_main_industry("Aerospace")
        time.sleep(2)  # дольше, потому что дропдаун

        page.select_headquarters("United States")
        time.sleep(2)

        page.select_background("AI")
        time.sleep(2)

        #page.select_today_date('#startDateNewProfilePage')  # выбираем сегодня
        #time.sleep(2)

        #page.select_traction_today_date('#startRevenueNewProfilePage')  # выбираем сегодня
        #time.sleep(2)

        page.select_readiness_level("4")
        time.sleep(2)

        page.fill_short_intro_what("aerospace company")
        time.sleep(2)

        page.fill_short_intro_for("government agencies")
        time.sleep(2)

        page.fill_short_intro_help("reduce launch costs")
        time.sleep(2)

        page.fill_short_intro_with("reusable rockets")
        time.sleep(2)

        page.select_funding_round("Seed")
        time.sleep(2)

        page.fill_email("test@example.com")
        time.sleep(2)

        page.publish()
        time.sleep(2)

    def test_create_startup_only_mandatory_fields1(self):
        """Заполнение только обязательных полей (без дат) и публикация профиля"""

        # 1. Сначала логинимся
        login_page = LoginPage()
        login_page.login_as('valya15fenichco.com@mail.ru', 'ZXqwcver1029')
        time.sleep(5)

        # 2. Открываем страницу создания стартапа
        page = NewStartupPage().open()
        time.sleep(2)

        # 3. Заполняем обязательные поля (кроме дат)
        print("Заполняем название...")
        page.fill_name("Test Startup")
        time.sleep(1)

        print("Заполняем CEO...")
        page.fill_ceo_name("John Doe")
        time.sleep(1)

        print("Выбираем индустрию...")
        page.select_main_industry("Aerospace")
        time.sleep(2)

        print("Выбираем штаб-квартиру...")
        page.select_headquarters("Afghanistan")
        time.sleep(2)

        print("Выбираем бэкграунд...")
        page.select_background("Asian Founders")
        time.sleep(2)

        print("Выбираем уровень готовности...")
        page.select_readiness_level("4")
        time.sleep(2)

        print("Заполняем short intro...")
        page.fill_short_intro_what("aerospace company")
        page.fill_short_intro_for("government agencies")
        page.fill_short_intro_help("reduce launch costs")
        page.fill_short_intro_with("reusable rockets")
        time.sleep(2)

        print("Выбираем раунд...")
        page.select_funding_round("Seed")
        time.sleep(2)

        print("Заполняем email...")
        page.fill_email("test@example.com")
        time.sleep(2)

        # Даты пока пропускаем
        # page.select_today_date('#startDateNewProfilePage')
        # page.select_today_date('#startRevenueNewProfilePage')

        print("Публикуем...")
        page.publish()
        time.sleep(3)

        print("Тест завершен!")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        browser.driver().save_screenshot(f"startup_created_{timestamp}.png")
        print(f"✅ Скриншот сохранён: startup_created_{timestamp}.png")