
class NewStartupPage:
    NAME_INPUT = '#startupName'
    # --- Аватар стартапа ---
    LOGO_TOOLTIP = # TODO: добавить ID для тултипов
    AVATAR_INPUT = '#startupAvatar'  # скрытый input
    AVATAR_UPLOAD_BUTTON = '#startupAvatar-upload-button'  # видимая кнопка
    AVATAR_REMOVE_BUTTON = '#startupAvatar-remove-button'  # появляется после загрузки
    AVATAR_PREVIEW = '#avatar'  # контейнер с превью

    CEO_NAME_INPUT = '#ceoName'
    CEO_LINKEDIN_INPUT = '#ceoLinkedin'

    # --- Фото СЕО ---
    CEO_PHOTO_INPUT = '#ceoPhoto'  # сам input type="file" (скрытый)
    CEO_PHOTO_UPLOAD_BUTTON = '#ceoPhoto-upload-button'  # видимая кнопка "Загрузка"
    CEO_PHOTO_REMOVE_BUTTON = '#ceoPhoto-remove-button'  # кнопка "Удалить" (появляется после загрузки)
    CEO_PHOTO_PREVIEW = '#ceoPhoto-avatar'  # div с превью фото

    MAIN_INDUSTRY_INPUT = '#mainIndustry'
    MAIN_INDUSTRY_DROPDOWN = '#mainIndustry-dropdown'

    RELEVANT_INDUSTRIES_INPUT = '#relevantIndustries'
    RELEVANT_INDUSTRIES_DROPDOWN = '#relevantIndustries-dropdown'

    WEBSITE_INPUT = '#startupWebsite'
    NO_WEBSITE_CHECKBOX = '#noWebsite'

    HEADQUARTERS_INPUT = '#country_registration'
    HEADQUARTERS_DROPDOWN = '#country_registration-dropdown'

    FOUNDERS_BASED_INPUT = '#team_location'
    FOUNDERS_BASED_DROPDOWN = '#team_location-dropdown'
    FOUNDERS_BASED_TOOLTIP = # TODO: добавить ID для тултипов

    BACKGROUND_INPUT = '#foundingTeamBackground'
    BACKGROUND_DROPDOWN = '#foundingTeamBackground-dropdown'
    BACKGROUND_NOT_APPLICABLE_CHECKBOX = '#preferNotToDiscloseTeamBackground'

    START_DATE_INPUT = 'startDateNewProfilePage'
    START_DATEPICKER_CALENDAR = # TODO: добавить ID для календаря
    #❓в календаре мы выписываем все атрибуты сетки❓

    TRACTION_START_DATE_INPUT = '#startRevenueNewProfilePage'
    TRACTION_START_DATEPICKER_CALENDAR = # TODO: добавить ID для календаря
    NO_REVENUE_YET_CHECKBOX = '#Still pre-revenue and pre-users' # TODO: исправить ID (убрать пробелы)

    INCOME_FOR_THE_YEAR = '#InputCommittedMoney'

    STARTUP_READINESS_LEVEL = '#SRLevel' #❓надо ли здесь перечислять уровни❓

    # --- Short Intro
    SHORT_INTRO_WHAT = '#shortIntro'  # компания/продукт (что делают)
    SHORT_INTRO_FOR = '#shortIntroFor'  # целевая аудитория (для кого)
    SHORT_INTRO_HELP = '#shortIntroHelp'  # проблема/решение (что делают)
    SHORT_INTRO_WITH = '#shortIntroWith'  # технология/метод (с помощью чего)
    # ----
    INDUSTRY_SOLUTION = '#solution'
    INDUSTRY_SOLUTION_TOOLTIP = # TODO: добавить ID для тултипов

    DEMO_VIDEO_YOUTUBE_ONLY = '#demoVideo'
    DEMO_VIDEO_YOUTUBE_ONLY_TOOLTIP = # TODO: добавить ID для тултипов

    # --- PRESENTATION
    PITCH_DECK_INPUT = '#pitchDeck'  # вероятно скрытая кнопка
    PITCH_DECK_UPLOAD_BUTTON = '#pitchDeck-upload-button'  # видимая кнопка, по которой кликаем
    PITCH_DECK_DELETE_BUTTON = '#pitchDeck-delete-button'
    PITCH_DECK_NAME_FILE = '#pitchDeck-file'
    PITCH_DECK_TOOLTIP = # TODO: добавить ID для тултипов
    # ----
    CURRENT_FUNDING_ROUND = '#FundingRounds' #❓надо ли здесь перечислять раунды❓

    ROUND_SUZE = '#roundSize'
    TOTAL_INVESTMENTS = '#InputPreviousInvestments'
    EMAIL_ADDRESS = '#email'

    # Текст тултипа (одинаков для всех полей)
    SPARKS_TOOLTIP_TEXT = 'Fill this field now and get extra sparks'

    PUBLISH_BUTTON = '#create-new-profile-page-button'


    # --- ERROR_MESSAGES
    # TODO: добавить ID для ошибок
    ERROR_CONTAINER = 'div.bg-[rgba(254,67,236,0.10)]'  # розовый контейнер с ошибками
    ERROR_TITLE = f'{ERROR_CONTAINER} p.font-bold'  # заголовок "Вам не хватает..."

    # --- Ошибки валидации (найденные ID) ---
    STARTUP_NAME_ERROR = '#startupName-error'
    CEO_LINKEDIN_ERROR = '#ceoLinkedin-error'
    STARTUP_WEBSITE_ERROR = '#startupWebsite-error'
    DEMO_VIDEO_YOUTUBE_ERROR = '#demoVideo-error'
    EMAIL_ERROR = '#email-error'

    # TODO: добавить уникальные ID для всех сообщений об ошибках под обязательными полями
    # --- empty field errors (нужны ID от разработчика)
    CEO_NAME_ERROR =  # для #ceoName
    MAIN_INDUSTRY_ERROR =  # для #mainIndustry
    HEADQUARTERS_ERROR =  # для #country_registration
    FOUNDERS_BACKGROUND_ERROR =  # для #foundingTeamBackground
    START_DATE_ERROR =  # для #startDateNewProfilePage
    TRACTION_DATE_ERROR =  # для #startRevenueNewProfilePage
    STARTUP_READINESS_ERROR =  # для #SRLevel
    FUNDING_ROUND_ERROR =  # для #FundingRounds

    # TODO: Short intro — обязательное поле, но сейчас нет текстового сообщения об ошибке.
    # Валидация показывается только красной рамкой вокруг пустых инпутов.
    INPUT_ERROR_CLASS = 'border-[#B41A88]'