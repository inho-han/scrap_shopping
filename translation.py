
import time

from selenium import webdriver
from path_file import Chrome_Path

# input : 번역하기 전 언어
# output : 번역한 후 언어
# sentence : 번역 할 언어
def Translation_Module(input, output, sentence):
    start_time = time.time()
    # papagoUrl = 'https://papago.naver.com/'
    papagoUrl = 'https://papago.naver.com/?sk=' +input+ '&tk=' +output+ '&st=' +sentence

    # 아래 headless 옵션 설정을 통해 크롬 창이 뜨지않고 백그라운드에서 돈다.
    # options = ChromeOptions_init()
    # driver = webdriver.Chrome(r'C:\Users\Master\Desktop\chromedriver_win32\chromedriver.exe', chrome_options=options)
    driver = webdriver.Chrome(Chrome_Path)

    driver.get(papagoUrl)
    driver.implicitly_wait(3)

    #번역대는 속도에 대한 페이지 대기시간
    # time.sleep(1)

    traduction = driver.find_element_by_id('txtTarget').text
    print(traduction)
    print("--- %s seconds ---" % (time.time() - start_time))

    return traduction
