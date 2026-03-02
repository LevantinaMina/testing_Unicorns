import time
from selene import browser
from selene.support.conditions import be
from selene.support.conditions import have
from config import BASE_URL


class NewStartupPage:
    # --- Обязательные поля ---
    NAME_INPUT = '#startupName'
    CEO_NAME_INPUT = '#ceoName'
    MAIN_INDUSTRY_INPUT = '#mainIndustry'
    HEADQUARTERS_INPUT = '#country_registration'
    HEADQUARTERS_DROPDOWN = '#country_registration-dropdown'
    BACKGROUND_INPUT = '#foundingTeamBackground'
    START_DATE_INPUT = '#startDateNewProfilePage'
    TRACTION_START_DATE_INPUT = '#startRevenueNewProfilePage'
    STARTUP_READINESS_LEVEL = '#SRLevel'
    SHORT_INTRO_WHAT = '#shortIntro'
    SHORT_INTRO_FOR = '#shortIntroFor'
    SHORT_INTRO_HELP = '#shortIntroHelp'
    SHORT_INTRO_WITH = '#shortIntroWith'
    CURRENT_FUNDING_ROUND = '#FundingRounds'
    EMAIL_ADDRESS = '#email'

    PUBLISH_BUTTON = '#create-new-profile-page-button'

    # --- Календарь ---
    DATEPICKER = 'div.absolute.top-10.z-50.block.pt-2'
    TODAY_BUTTON = f'{DATEPICKER} button[data-value="Today"]'

    def open(self):
        browser.open_url(f'{BASE_URL}/new-startup')
        return self

    # --- Методы для заполнения полей ---
    def fill_name(self, value):
        browser.element(self.NAME_INPUT).type(value)
        return self

    def fill_ceo_name(self, value):
        browser.element(self.CEO_NAME_INPUT).type(value)
        return self

    def select_main_industry(self, value):
        browser.element(self.MAIN_INDUSTRY_INPUT).type(value)
        browser.element(self.MAIN_INDUSTRY_INPUT).press_enter()
        return self

    def select_headquarters(self, value):
        """Выбирает страну штаб-квартиры из выпадающего списка"""

        # Вводим значение
        browser.element(self.HEADQUARTERS_INPUT).type(value)
        time.sleep(1)

        # Ждем дропдаун
        browser.element(self.HEADQUARTERS_DROPDOWN).should(be.visible, timeout=5)
        time.sleep(1)

        # Кликаем по нужной стране
        option_xpath = f'{self.HEADQUARTERS_DROPDOWN}//button[contains(text(), "{value}")]'
        browser.element(option_xpath).click()
        time.sleep(1)

        return self

    def select_background(self, value):
        browser.element(self.BACKGROUND_INPUT).type(value)
        browser.element(self.BACKGROUND_INPUT).press_enter()
        return self


    def select_today_date(self, field_input):
        """Выбирает сегодняшнюю дату через календарь"""

        # 1. Ждем, что поле даты вообще существует и кликабельно
        browser.element(field_input).with_(timeout=10).should(be.clickable)
        time.sleep(1)

        # 2. Кликаем на поле даты, чтобы открылся календарь
        browser.element(field_input).click()
        time.sleep(2)  # ждем появления календаря

        # 3. Ждем, пока календарь появится
        browser.element(self.DATEPICKER).with_(timeout=10).should(be.visible)
        time.sleep(1)

        # 4. Ищем кнопку Today разными способами
        today_selectors = [
            f'{self.DATEPICKER} button[data-value="Today"]',
            f'{self.DATEPICKER} button:has-text("Today")',
            f'{self.DATEPICKER} button:has-text("Сегодня")'
        ]

        today_button = None
        for selector in today_selectors:
            try:
                today_button = browser.element(selector)
                if today_button.with_(timeout=2).matching(be.visible):
                    break
            except:
                continue

        if not today_button or not today_button.matching(be.visible):
            # Если не нашли кнопку Today, попробуем кликнуть на сегодняшнее число
            print("Кнопка Today не найдена, пробуем кликнуть на сегодняшнее число")
            # Обычно сегодняшнее число имеет класс 'active' или 'selected'
            today_cell = browser.element(f'{self.DATEPICKER} .active, {self.DATEPICKER} .selected')
            today_cell.with_(timeout=5).should(be.visible).click()
        else:
            today_button.click()

        time.sleep(2)  # ждем, пока дата выберется и календарь закроется

        return self

    def select_traction_today_date(self, field_input):
        """Выбирает сегодняшнюю дату для поля Traction"""
        # 1. Кликаем на поле даты, чтобы открылся календарь
        browser.element(field_input).click()
        time.sleep(1)  # ждем появления календаря

        # 2. Ждем, пока календарь появится
        browser.element(self.DATEPICKER).should(be.visible)
        time.sleep(1)

        # 3. Ищем кнопку Today
        # Сначала пробуем найти по data-value (как в первом календаре)
        today = browser.element(f'{self.DATEPICKER} button[data-value="Today"]')

        # Если не нашли, ищем по тексту (как во втором календаре)
        if not today.matching(be.visible):
            today = browser.element(f'{self.DATEPICKER} button:has-text("Today")')

        # 4. Кликаем Today
        today.click()
        time.sleep(1)  # ждем, пока дата выберется и календарь закроется

        return self

    def select_readiness_level(self, level_value):
        """Выбирает уровень готовности стартапа по value (1-9)"""

        # Открываем выпадающий список
        browser.element(self.STARTUP_READINESS_LEVEL).click()
        time.sleep(1)

        # Выбираем нужный уровень по value
        browser.element(f'#SRLevel option[value="{level_value}"]').click()
        time.sleep(1)

        return self

    def fill_short_intro_what(self, value):
        browser.element(self.SHORT_INTRO_WHAT).type(value)
        return self

    def fill_short_intro_for(self, value):
        browser.element(self.SHORT_INTRO_FOR).type(value)
        return self

    def fill_short_intro_help(self, value):
        browser.element(self.SHORT_INTRO_HELP).type(value)
        return self

    def fill_short_intro_with(self, value):
        browser.element(self.SHORT_INTRO_WITH).type(value)
        return self

    def select_funding_round(self, round_value):
        """Выбирает раунд финансирования по value"""

        # Открываем выпадающий список
        browser.element(self.CURRENT_FUNDING_ROUND).click()
        time.sleep(1)

        # Выбираем нужный раунд по value
        browser.element(f'#FundingRounds option[value="{round_value}"]').click()
        time.sleep(1)

        return self

    def fill_email(self, value):
        browser.element(self.EMAIL_ADDRESS).type(value)
        return self

    # --- Действия ---
    def publish(self):
        browser.element(self.PUBLISH_BUTTON).click()
        return self

    # --- Очистка (если нужна) ---
    def clear_name(self):
        browser.element(self.NAME_INPUT).clear()
        return self