# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
sbis_site = 'https://sbis.ru/'
sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'

try:
    driver.maximize_window()
    driver.get(sbis_site)
    sleep(1)
    print('Проверить адрес сайта и заголовок страницы')
    assert driver.current_url == sbis_site, 'Неверный адрес сайта'
    assert driver.title == sbis_title, 'Неверный заголовок сайта'

    print('Проверка наличия раздела контакты')
    contacts_txt = 'Контакты'
    contacts_btn = driver.find_element(By.CSS_SELECTOR, '[href="/contacts"]')
    assert contacts_btn.text == contacts_txt

    print('Переход в раздел Контакты')
    contacts_btn.click()

    print('Проверка наличия банера Тензор')
    tensor_banner_title = 'tensor.ru'
    tensor_banner = driver.find_element(By.CSS_SELECTOR, '[class="sbisru-Contacts__logo-tensor mb-8"]')
    assert tensor_banner.get_attribute('title') == tensor_banner_title

    print('Переход на tensor.ru')
    tensor_site = 'https://tensor.ru/'
    sleep(1)
    tensor_banner.click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == tensor_site, 'Неверный адрес tensor.ru'

    print('Проверка наличия блока Сила в людях')
    peopl_blok_header_text = 'Сила в людях'
    peopl_blok = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content')
    peopl_blok_header = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-Index__card-title')
    assert peopl_blok_header.text == peopl_blok_header_text, f'Текст заголовка не {peopl_blok_header_text}'

    print('Проверка наличия блока Подробнее')
    more_blok_people_text = 'Подробнее'
    more_blok_people = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content [href="/about"]')
    assert more_blok_people.text == more_blok_people_text, 'Неверный текст у блока Подробнее'

    print('Переход в подробнее')
    more_site = 'https://tensor.ru/about'
    sleep(1)
    more_blok_people.location_once_scrolled_into_view
    sleep(1)
    more_blok_people.click()
    sleep(1)
    assert driver.current_url == more_site, f'Адрес страницы подробнее не {more_site}'
finally:
    driver.quit()