from selenium import webdriver
import json
import time


def check(my_driver):
    if my_driver.current_url.find('https://wappass.baidu.com/') >= 0:
        return True
    else:
        return False


f = open('keyword.txt', 'r', encoding='utf-8')
keylist = []
for line in f.readlines():
    keylist.append(line.strip())
print(keylist)
url = 'http://m.baidu.com/s?word='
driverPath = 'E:\\webdriver\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driverPath)
key_pass = []
key_no_pass = []
for i in keylist:
    while 1:
        driver.get(url + i)
        if check(driver):
            driver.get(url)
            continue
        else:
            try:
                result = driver.find_elements_by_class_name("c-result")
                if not result:
                    raise Exception
                else:
                    print('\n------------------检测关键词------------------\n')
                    print(i)

                    for n in result:
                        key_dict = json.loads(n.get_attribute('data-log'))
                        if key_dict['mu'].find('9game.cn') >= 0 and key_dict['mu'].find('a.9game.cn') == -1:
                            print(key_dict['mu'], '检测到九游.......')
                            key_no_pass.append(i)
                    print('\n--------------------------------------------\n')
                    break
            except:
                time.sleep(1)
                continue
for i in keylist:
    if i not in key_no_pass:
        key_pass.append(i)
print('\n--------------------------------------------\n')
print("可写的关键词")
for i in key_pass:
    print(i)
print('\n--------------------------------------------\n')
print("九游已有关键词")
for i in key_no_pass:
    print(i)