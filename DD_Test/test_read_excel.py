import time
import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Locators.Locators import Locators
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://demo.automationtesting.in/Register.html")
driver.implicitly_wait(10)


first_name = driver.find_element(By.XPATH, Locators.first_name)
last_name = driver.find_element(By.XPATH, Locators.last_name)
address = driver.find_element(By.XPATH, Locators.address)
email_address = driver.find_element(By.XPATH, Locators.email_address)
phone_number  = driver.find_element(By.XPATH, Locators.phone_number)


gender = driver.find_element(By.NAME, Locators.gender)
hobby = driver.find_element(By.ID, Locators.hobby)
language_dropdown = driver.find_element(By.ID, Locators.language_dropdown)
Skill = driver.find_element(By.ID, Locators.select_skill)

country = driver.find_element(By.ID, Locators.country)
DOB_year = driver.find_element(By.ID, Locators.DOB_year)
# DOB_month = driver.find_element(By.ID, '//*[@id="basicBootstrapForm"]/div[11]/div[2]/select')
DOB_date = driver.find_element(By.ID, Locators.DOB_date)
set_password = driver.find_element(By.ID, Locators.set_password)
confirm_password = driver.find_element(By.ID, Locators.confirm_password)
submit_button = driver.find_element(By.XPATH, Locators.submit_button)


workbook = xlrd.open_workbook("../Datafile.xlsx")
sheet = workbook.sheet_by_name("login")

#get total number of rows
rowCount = sheet.nrows
colCount = sheet.ncols
print(rowCount)
print(colCount)

for curr_row in range(1, rowCount):
    FirstName = sheet.cell_value(curr_row, 0)
    LastName  = sheet.cell_value(curr_row, 1)
    Address = sheet.cell_value(curr_row, 2)
    Email = sheet.cell_value(curr_row, 3)
    PhoneNumber = sheet.cell_value(curr_row, 4)
    Gender = sheet.cell_value(curr_row, 5)
    Hobby = sheet.cell_value(curr_row, 6)
    language = sheet.cell_value(curr_row, 7)
    Skills = sheet.cell_value(curr_row, 8)
    Country = sheet.cell_value(curr_row, 9)
    DOB = sheet.cell_value(curr_row, 10)
    Password = sheet.cell_value(curr_row, 11)
    C_Password = sheet.cell_value(curr_row, 12)


    def enter_values():
        first_name.clear()
        first_name.send_keys(FirstName), time.sleep(1)

        last_name.clear()
        last_name.send_keys(LastName), time.sleep(1)

        address.clear()
        address.send_keys(Address), time.sleep(1)

        email_address.clear()
        email_address.send_keys(Email), time.sleep(1)

        phone_number.clear()
        phone_number.send_keys(str(PhoneNumber)), time.sleep(1)

        gender.click(), time.sleep(2)
        hobby.click()



    enter_values()


    # def select_language_dropdown():
    #     language_dropdown.clear()
    #     language_dropdown = driver.find_element(By.ID, "msdd")
    #     language_dropdown.click()
    #     drop_list = driver.find_elements(By.CSS_SELECTOR, 'a.ui-corner-all')
    #     for ele in drop_list:
    #         print(ele.text)
    #         if ele.text == 'English':
    #             ele.click()
    #             break
    #         for ele in drop_list:
    #             print(ele.text)
    #             if ele.text == 'Arabic':
    #                 ele.click()
    #                 break
    #
    # select_language_dropdown()
    #
    #
    # def select_skills():
    #     Skill = driver.find_element(By.ID, 'Skills')
    #     select1 = Select(Skill)
    #     select1.select_by_index(2)
    #     time.sleep(2)
    # select_skills()
    #
    # def select_country():
    #     dropdown = driver.find_element(By.ID, 'countries')
    #     select2 = Select(dropdown)
    #     select2.select_by_visible_text("Australia")
    #     time.sleep(2)
    # select_country()
    #
    #
    # def select_dob():
    #     element1 = driver.find_element_by_id('yearbox')
    #     ele = Select(element1)
    #     ele.select_by_visible_text("1991")
    #
    #     element1 = driver.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[11]/div[2]/select')
    #     sel = Select(element1)
    #     sel.select_by_visible_text("November")
    #
    #     element1 = driver.find_element(By.ID, 'daybox')
    #     sel = Select(element1)
    #     sel.select_by_index(14)
    # select_dob()

    def enter_password():

        set_password.clear()
        set_password.send_keys(str(Password)), time.sleep(2)

        confirm_password.clear()
        confirm_password.send_keys(str(C_Password))

    enter_password()
    submit_button.click()
    time.sleep(2)





