import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

# TODO: Ask the user how much assignments they want through loop through
untilLooped = input("Enter the amount of assignments you want to loop through: ")
startingNum = 1

# TODO: Initialize chromedriver and open the zybooks url
browser = webdriver.Chrome('/Users/jesusperez/Downloads/chromedriver')
browser.get('https://learn.zybooks.com/signin')
browser.implicitly_wait(20)  # Gives an implicit wait for the functions to run 25 seconds apart

actions = ActionChains(browser)


# TODO: Click the Sign In field, enter sign in credentials
emailField = browser.find_element_by_css_selector('input[type=email]')
emailField.send_keys('jpereza6@calstatela.edu')

passField = browser.find_element_by_css_selector('input[type=password]')
passField.send_keys('Jayp01242001')
passField.send_keys(Keys.ENTER)


# TODO: Find the html with the name of course, click on it
courseName = browser.find_element_by_class_name('zybook-header-img')
courseName.click()

# TODO: Find the assignment button and click on it
assignmentButton = browser.find_element_by_css_selector('.tabs *:nth-child(3)')
assignmentButton.click()
time.sleep(3)

# TODO: Find the assignment text and click on it
assignment = browser.find_element_by_class_name('section-title')
assignment.click()


# TODO: Find the fieldsets, iterate through each child div and click on them
labels = browser.find_elements_by_tag_name('label')

# TODO: Click each radio button on the web page
def clickPoints(containerList):
    for labelButton in containerList:
        labelButton.click()
    time.sleep(3)  # Once the loop has exited, wait three seconds until the next thing

clickPoints(labels)  # Call the loop

while(startingNum < untilLooped):
    # TODO: Scroll down to the bottom of the web page
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # TODO: Go onto the next section once finished with the loop above
    nextSection = browser.find_element_by_class_name('nav-link ember-view')
    nextSection.click()

    time.sleep(5)  # Wait for five seconds until the web page loads

    clickPoints(labels)  # Call the loop for the new web page

    startingNum += 1  # Increment the starting num
