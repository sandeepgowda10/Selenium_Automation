from selenium import webdriver
import pytest
import time


@pytest.yield_fixture()  # decorator which is mandatory while working on pytest mdoule.
def setupclass():  # defining a class which work as setup and teardown method.
    global driver  # defining global which should be available to different methods.
    # calling geckodriver which is responsible for opening a firefox browser
    # Note: Other browsers can also be used by downloading the webdrivers
    driver = webdriver.Firefox(executable_path='D:\python material\geckodriver.exe')

    # below code is used to open gmail sign in.
    driver.get(
        'https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    driver.maximize_window()  # maximise_window is used for maximizing the browser windows
    yield
    # after performing every activity 19th and 20th line will be executed which is even a teardown method
    time.sleep(10)
    # 21st line is used to close the browser once the required activity is performed.
    driver.close()


# below function is used to login to the gmail
def test_gmail_login(setupclass):
    # below line is used for enterning the email id .
    driver.find_element_by_name('identifier').send_keys('your email ID ')
    # below line will be used to click on next button
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span').click()
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/span/span')
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[3]/div/div[2]')
    driver.find_element_by_name('password').send_keys('Your password')
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span').click()
    time.sleep(30)


# below function is used for dropping a email for the given recipients
def test_gmail_drop_mail(setupclass):
    driver.find_element_by_xpath('//*[@id=":l5"]/div/div').click()
    driver.find_element_by_xpath('//*[@id=":ql"]').send_keys('recipients email id')
    driver.find_element_by_name('subjectbox').send_keys('subject')
    driver.find_element_by_xpath('//*[@id=":rd"]/div[2]').send_keys('your email')
    driver.find_element_by_xpath('//*[@id=":q0"]').click()
    time.sleep(30)


# once the mail has been sent below code will be executed for logging out.
def test_gmail_logout(setupclass):
    driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[3]/div[1]/div[2]/div[1]/div/img').click()
    driver.find_element_by_xpath('//*[@id="gb_71"]').click()
