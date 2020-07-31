from selenium import webdriver

browser = webdriver.Chrome(r"C:\chrome_driver\chromedriver.exe")

browser.get("https://github.com")

signin_link = browser.find_element_by_link_text("Sign in")

signin_link.click()


username_box = browser.find_element_by_id("login_field")
username_box.send_keys("Aman-Kesarwani")  # replace with username

password_box = browser.find_element_by_id("username")
password_box.send_keys("password")  # replace with password

password_box.submit()

assert "username" in browser.page_source

#profile_link = browser.find_elements_by_class_name("user-profile-link")
#link_label = profile_link.getattribute("innerHTML")
