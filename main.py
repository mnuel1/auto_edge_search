from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Create WebDriver instance with Edge options
options = webdriver.EdgeOptions()
options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
edge_driver = webdriver.Edge(options=options)


edge_driver.get('https://www.bing.com/')

# to make sure that u logged with your personal email or your targeted email account
edge_driver.get('https://www.bing.com/fd/auth/signin?action=interactive&provider=windows_live_id&return_url=https%3a%2f%2fwww.bing.com%2f%3ftoWww%3d1%26redig%3d33376853255F4F8C87D26C1737277847%26wlsso%3d1%26wlexpsignin%3d1&src=EXPLICIT&sig=0E8FE6F01AD666CE018CF56C1BC267A0')
time.sleep(5)
edge_driver.back()
time.sleep(5)
edge_driver.get('https://www.bing.com/fd/auth/signin?action=interactive&provider=windows_live_id&return_url=https%3a%2f%2fwww.bing.com%2f%3ftoWww%3d1%26redig%3d33376853255F4F8C87D26C1737277847%26wlsso%3d1%26wlexpsignin%3d1&src=EXPLICIT&sig=0E8FE6F01AD666CE018CF56C1BC267A0')
time.sleep(5)
edge_driver.back()
time.sleep(5) 

# searching 90 times 
for i in range(90):
    search_input = edge_driver.find_element(By.ID, 'sb_form_q')
    search_input.send_keys("Your search query")
    search_input.send_keys(Keys.RETURN)
    time.sleep(2) # adjust this delay as you like
    edge_driver.back()
    


# time.sleep(5)
# edge_driver.quit()
# Locate and interact with elements
# search_input = edge_driver.find_element_by_name("q")  # Replace with the appropriate locator for your webpage
# search_input.send_keys("Your search query")
# search_input.send_keys(Keys.RETURN)

# Perform further interactions as needed

# Don't quit the browser here if you want to keep it open for further interactions

# When you're done, you can close the browser
# edge_driver.quit()
