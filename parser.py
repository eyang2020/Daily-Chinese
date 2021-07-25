import codecs
from selenium import webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

def get_results(search_term):

    chrome_options = Options()

    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")

    full_package = []  # [char, definition_list, pinyin, english, sentence]
    full_package.append(search_term)
    url = "http://ce.linedict.com/#/cnen/home"
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get(url)

    # wait until elements load before trying to fetch them
    browser.implicitly_wait(1);

    search_box = browser.find_element_by_class_name("ac_input")
    search_box.send_keys(search_term)
    search_box.submit()

    # return top hit
    first_result = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="autocplt_wrap"]/ul[1]/li/span/a[1]'))
    )
    first_result.click()

    # return Pinyin
    new_pinyin = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.prnc_area>span'))
    )
    pinyin = new_pinyin.text
    full_package.append(pinyin)

    # return definition_list
    new_definition_list = WebDriverWait(browser, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'ol.lst_defin>li span.cn'))
    )

    synonym_list = []

    for eachY in new_definition_list:
        synonym_list.append(eachY.text)

    full_package.append(synonym_list)

    # return sample sentence
    sentence_list = []

    # char
    new_sentence_char = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.exam> p.stc'))
    )
    sentence_list.append(new_sentence_char.text.strip())

    # Pinyin
    new_sentence_pinyin = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.exam> p.pinyin'))
    )
    sentence_list.append(new_sentence_pinyin.text.strip())

    # English
    new_sentence_english = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.exam> p.trans'))
    )
    sentence_list.append(new_sentence_english.text.strip())

    full_package.append(sentence_list)

    # return all data
    browser.close()
    # return full package
    #print(full_package)

    message1 = "Good morning! Today's character is " + full_package[0] + ".<br><br>" + "Pinyin: " + full_package[1] + "<br><br>" + "Definitions: <br>"
    message2 = ""
    for eachDef in full_package[2]:
        message2 += "  " + "-" + eachDef + "<br>"
    message3 = message1 + message2 + "<br>" + "Sample Sentence:<br>"
    for eachSection in full_package[3]:
        message3 += eachSection + "<br>"
    full_message = message3 + "<br>" + "If you liked today's character, feel free to forward it along! As always, shoot me an email if there's anything I can help with!"

    # write email template
    with codecs.open('emailtemplates.txt', 'a', encoding='utf-8') as emailtemps:
        emailtemps.write(full_message + "\n")

# for each character, append result
with codecs.open('grabchars.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
content = [x.strip() for x in content]

for eachChar in content:
    get_results(eachChar)

# clear grabchars.txt
codecs.open('grabchars.txt', 'w').close()