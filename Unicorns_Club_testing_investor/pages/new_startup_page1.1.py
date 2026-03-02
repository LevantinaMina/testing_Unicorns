class NewStartupPage:
    NAME_INPUT = '#startupName'
    AVATAR_INPUT = 'input[name="startupAvatar"]'  # вместо '#startupAvatar'
    
    #❗️есть id, можно #startupAvatar
    #❗️по аналогии с питчдеком, тоже есть кнопка AVATAR_BUTTON = '#startupAvatar-upload-button'
    #❗️я пока не работаю с контекстным окном, которое показывает ОС, просто через инпут загружаю напрямую
    
    AVATAR_REMOVE_BUTTON = '#startupAvatar-remove-button'  # вместо '#remove-button' 
    CEO_NAME_INPUT = '#ceoName'
    CEO_LINKEDIN_INPUT = '#ceoLinkedin'
    CEO_PHOTO_BUTTON = '#ceoPhoto'
    CEO_PHOTO_REMOVE_BUTTON = '#ceoPhoto-remove-button'
    MAIN_INDUSTRY_INPUT = '#mainIndustry'
    RELEVANT_INDUSTRIES_INPUT = '#relevantIndustries'
    WEBSITE_INPUT = '#startupWebsite'
    NO_WEBSITE_CHECKBOX = '#noWebsite'
    HEADQUARTERS_INPUT = '#country_registration'
    FOUNDERS_BASED_INPUT = '#team_location'
    BACKGROUND_INPUT = '#foundingTeamBackground'
    BACKGROUND_NOT_APPLICABLE_CHECKBOX = '#preferNotToDiscloseTeamBackground'
    START_DATE_INPUT = '#startDateNewProfilePage'
    TRACTION_START_DATE_INPUT = '#startRevenueNewProfilePage'
    NO_REVENUE_YET_OPTION = '#Still pre-revenue and pre-users'
    INCOME_FOR_THE_YEAR = '#InputCommittedMoney'
    STARTUP_READINESS_LEVEL = '#SRLevel'
    # --- Short Intro
    SHORT_INTRO_WHAT = '#shortIntro'  # компания/продукт (что делают)
    SHORT_INTRO_FOR = '#shortIntroFor'  # целевая аудитория (для кого)
    SHORT_INTRO_HELP = '#shortIntroHelp'  # проблема/решение (что делают)
    SHORT_INTRO_WITH = '#shortIntroWith'  # технология/метод (с помощью чего)
    # ----
    INDUSTRY_SOLUTION = '#solution'
    DEMO_VIDEO_YOUTUBE_ONLY = '#demoVideo'
    # --- PRESENTATION
    PITCH_DECK_INPUT = '#pitchDeck'  # вероятно скрытая кнопка
    PITCH_DECK_UPLOAD_BUTTON = '#pitchDeck-upload-button'  # видимая кнопка, по которой кликаем
    
    #❗️не хватает кнопки удаления загруженного файла и имени файла, который загрузился
    
    # ----
    CURRENT_FUNDING_ROUND = '#FundingRounds'  # выпадающий список
    ROUND_SUZE = '#roundSize'
    TOTAL_INVESTMENTS = '#InputPreviousInvestments'
    EMAIL_ADDRESS = '#email'
    PUBLISH_BUTTON = '#create-new-profile-page-button'
    # --- ERROR_MESSAGES
    ERROR_CONTAINER = 'div.bg-[rgba(254,67,236,0.10)]'  # розовый контейнер с ошибками
    ERROR_TITLE = f'{ERROR_CONTAINER} p.font-bold'  # заголовок "Вам не хватает..."
    
    #❗️здесь надо ставить задачу для разработчика, к таким атрибутам не будем цепляться

    # ---
    STARTUP_NAME_ERROR = '#startupName-error'
    
    #❗️остальные ошибки нужны тоже по аналогии с STARTUP_NAME_ERROR
    #❗️если у них нет к чему прицепиться, нужно их выписать, чтоб разработчик добавил атрибуты

  
#ниже скрипт для самопроверки, подсвечивает зеленым те элементы, которые перечислены (только айди)
#срабатывает только на элементы которые уже видны сейчас
#чтоб сбросить подсветку, надо просто рефрешнуть страницу
    
const selectors = [
  '#startupName',
  'input[name="startupAvatar"]',
  '#startupAvatar-remove-button',
  '#ceoName',
  '#ceoLinkedin',
  '#ceoPhoto',
  '#ceoPhoto-remove-button',
  '#mainIndustry',
  '#relevantIndustries',
  '#startupWebsite',
  '#noWebsite',
  '#country_registration',
  '#team_location',
  '#foundingTeamBackground',
  '#preferNotToDiscloseTeamBackground',
  '#startDateNewProfilePage',
  '#startRevenueNewProfilePage',
  '#Still pre-revenue and pre-users',
  '#InputCommittedMoney',
  '#SRLevel',
  '#shortIntro',
  '#shortIntroFor',
  '#shortIntroHelp',
  '#shortIntroWith',
  '#solution',
  '#demoVideo',
  '#pitchDeck',
  '#pitchDeck-upload-button',
  '#FundingRounds',
  '#roundSize',
  '#InputPreviousInvestments',
  '#email',
  '#create-new-profile-page-button',
  '#startupName-error'
];

const missing = [];

selectors.forEach(sel => {
  const el = document.querySelector(sel);

  if (el) {
    el.style.outline = '3px solid lime';
  } else {
    missing.push(sel);
  }
});

console.log('Не найдены селекторы:', missing);


#нужно еще добавить айди дропдаунов, которые выпадают при клике на поле
#просто так их не поймаешь, нужен тоже скрипт в консоль
#скрипт ниже надо запустить и кликнуть на поле, где появляется дропдаун, в консоль выведутся его атрибуты, ищем айди
#так же сработает, если навести на элемент, который показывает тултип (его тоже надо добавить, он появляется на розовой иконке спарксов)

#если у чего-то нет айди, выписываем с местонахождением элемента (если трудно объяснить, тогда скриншот)
#формат, который я ожидаю: .py файл с элементами и их айдишниками (если нет айдишника, все равно писать элемент с комментом, что разработчику нужно добавить айди)
#и отдельно ссылку на задачу для разработчика в гугл доке

const observer = new MutationObserver((mutations) => {
  mutations.forEach(mutation => {

    // 1. Новые элементы
    mutation.addedNodes.forEach(node => {
      if (node.nodeType === 1) {
        console.log('Добавлен элемент:', node);
        console.log('ID:', node.id);
        console.log('Class:', node.className);
        console.log('---');
      }
    });

    // 2. Изменение атрибутов (style, class, hidden и т.д.)
    if (mutation.type === 'attributes') {
      const el = mutation.target;

      const visible =
        el.offsetParent !== null || 
        getComputedStyle(el).visibility === 'visible';

      if (visible) {
        console.log('Элемент стал видимым:', el);
        console.log('ID:', el.id);
        console.log('Class:', el.className);
        console.log('Attributes:', [...el.attributes].map(a => `${a.name}="${a.value}"`));
        console.log('---');
      }
    }

  });
});

observer.observe(document.body, {
  childList: true,
  subtree: true,
  attributes: true,
  attributeFilter: ['style', 'class', 'hidden', 'aria-hidden']
});

console.log('Observer запущен. Наведи или кликни, чтобы появился тултип.');
