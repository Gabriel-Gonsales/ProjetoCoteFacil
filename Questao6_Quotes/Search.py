import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

def get_element_text(driver, locator):
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator)).text

def extract_author_info(driver):
    author_title = get_element_text(driver, (By.CLASS_NAME, 'author-title'))
    birth = get_element_text(driver, (By.CLASS_NAME, 'author-born-date'))
    born_location = get_element_text(driver, (By.CLASS_NAME, 'author-born-location'))
    author_description = get_element_text(driver, (By.CLASS_NAME, 'author-description'))[:200]

    return {
        "name": author_title,
        "birth_date": birth,
        "birth_location": born_location,
        "description": f'{author_description} ...'
    }

def quotesQ6(search_author):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        link = "http://quotes.toscrape.com/"
        navegador.get(link)

        author_locator = (By.XPATH, f'//small[@class="author" and contains(text(), "{search_author}")]')
        WebDriverWait(navegador, 10).until(EC.presence_of_all_elements_located(author_locator))

        about = navegador.find_element(By.XPATH, f'//small[@class="author" and contains(text(), "{search_author}")]/following-sibling::a[@href]')
        link_about = about.get_attribute('href')
        navegador.get(link_about)

        author_info = extract_author_info(navegador)
        author_content = {"author": author_info, "quotes": []}

        while True:
            quotes = navegador.find_elements(By.XPATH, f"//span[@class='text' and following-sibling::span/small[@class='author' and contains(text(), '{search_author}')]]")
            quotes_tags = navegador.find_elements(By.XPATH, f"//span[./small[@class='author' and contains(text(), '{search_author}')]]/following-sibling::div[@class='tags']/a[@class='tag']")

            for quote_text, tags in zip(quotes, quotes_tags):
                quote_text_conteudo = quote_text.text
                tags_text = tags.text

                new_tag = {"text": quote_text_conteudo, "tags": [tags_text]}
                author_content["quotes"].append(new_tag)

            next_button = navegador.find_element(By.XPATH, '//li[@class="next"]/a')
            if 'disabled' in next_button.get_attribute('class'):
                break
            next_button.click()

    finally:
        navegador.quit()

    return author_content

print(json.dumps(quotesQ6("J.K. Rowling"), indent=2, ensure_ascii=False))
