#!D:/bin/Python/Python311/python.exe

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# get anime name from user
# TODO: Maybe have a local database of all the anime in pahe and let you search throught that.
anime_name = input("Enter the FULL Anime Name: ")
# anime_name = "Non Non Biyori"


# setup firefox webdriver
driver = webdriver.Firefox()
driver.install_addon("C:/Users/ahmed/AppData/roaming/Mozilla/Firefox/profiles/0zslsgan.Momoyon/extensions/uBlock0@raymondhill.net.xpi")
driver.implicitly_wait(30)
driver.set_page_load_timeout(30)

# goto animepahe
driver.get("https://animepahe.com")

ogWindow = driver.current_window_handle

# search for the anime
searchbox = driver.find_element(By.CLASS_NAME, 'input-search')
searchbox.click()
searchbox.send_keys(anime_name)

# click on the first result
first_result = driver.find_element(By.CLASS_NAME, 'result-title')
first_result.click()

episodes = driver.find_elements(By.CLASS_NAME, "play")

print("List of Episodes of {} : {}" .format(anime_name, len(episodes)))


for ep in episodes:
    if (len(driver.window_handles) > 1):
        driver.switch_to.window(ogWindow)
    ep.click()
    driver.find_element(By.ID, 'downloadMenu').click()
    for link in driver.find_elements(By.CLASS_NAME, 'dropdown-item'):
        if (link.get_attribute("target")):
            link.click()
            break
    # switch to the dl link tab
    for window in driver.window_handles:
        if (window != ogWindow):
            driver.switch_to.window(window)
            break    
    redirect = driver.find_element(By.CLASS_NAME, 'btn btn-primary btn-block redirect')
    print("Redirect Text : {}".format(redirect.text))
break
        
driver.quit()
