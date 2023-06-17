# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import Keys, ActionChains

driver = webdriver.Chrome()
sbis_site = 'https://fix-sso.sbis.ru/auth-online/'
sbis_title = 'Вход в личный кабинет'

try:
    driver.maximize_window()
    driver.get(sbis_site)
    sleep(1)
    print('Проверить адрес сайта и заголовок страницы')
    assert driver.current_url == sbis_site, 'Неверный адрес сайта'
    assert driver.title == sbis_title, 'Неверный заголовок сайта'

    print('Авторизация')
    user_login, user_password = 'test_cont', 'test_cont1'
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(user_login, Keys.ENTER)
    assert login.get_attribute('value') == user_login
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password, Keys.ENTER)
    sleep(3)

    print('Переход в реестр Контакты')
    contact_ac = driver.find_element(By.CSS_SELECTOR, '[name="item-contacts"]')
    contact_ac.click()
    sleep(3)
    contact = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle')
    contact.click()
    sleep(3)

    print('Создание диалога')
    plus = driver.find_element(By.CSS_SELECTOR, '.controls-Button__icon.controls-BaseButton__icon.icon-RoundPlus')
    plus.click()
    sleep(3)

    print('Поиск адресата')
    user = 'Пользователь Автотеста'
    search = driver.find_element(By.CSS_SELECTOR, '.controls-StackTemplate__top-area-content .controls-Field')
    search.send_keys(user, Keys.ENTER)
    sleep(3)

    print('Выбор пользователя')
    addressee = driver.find_element(By.CSS_SELECTOR, '[class="msg-addressee-item"]')
    addressee.click()
    sleep(3)

    print('Написание сообщения')
    message = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    message_text = "Мой второй автотест"
    message.send_keys(message_text, Keys.ENTER)
    sleep(3)
    button_ent = driver.find_element(By.CSS_SELECTOR, '[data-qa = "msg-send-editor__send-button"]')
    button_ent.click()
    sleep(3)

    print('Проверка, что сообщение отправлено')
    sender = driver.find_element(By.CSS_SELECTOR, '[data-qa = "msg-dialogs-item__addressee"]')
    message_send_text = driver.find_element(By.CSS_SELECTOR, '.msg-entity-expander')
    assert sender.text == user, 'ФИО пользователя не совпадает'
    assert message_send_text.text == message_text, 'Текст сообщения не совпадает'

    print('Удаление')
    mess = driver.find_element(By.CSS_SELECTOR, '.controls-ListView__item_default-topPadding_s')
    action_chains = ActionChains(driver)
    action_chains.move_to_element(mess)
    action_chains.perform()

    button_delete = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]')
    action_chains.click(button_delete)
    action_chains.perform()
    sleep(3)

    print('Проверка, что сообщение удалено')
    no_message = driver.find_element(By.CSS_SELECTOR, '.hint-Template__text_message')
    assert no_message.text == 'В этой папке нет сообщений', 'Неверный текст в заглушке'


finally:
    driver.quit()

