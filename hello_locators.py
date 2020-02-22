from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.support.ui import Select

email= 'eeewa@ewaa.com'
firstname= 'Ewa'
lastname= 'Nowak'
password= "ddd"
birthday='16'
birthmonth='10'
birthyear='1986'

class APRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.com/index.php')


    def testCorrectRegistration(self):
        driver = self.driver
        #Odnajdz Sign in
        sign_in = driver.find_element_by_class_name('login')
        #1.Kliknij
        sign_in.click()
        #2.wpisz adres email
        email_input = driver.find_element_by_id('email_create')
        email_input.send_keys(email)
        #3.kliknij "Create an account"
        driver.find_element_by_id('SubmitCreate').click()
        sleep(2)
        #4.wybierz tytul
        driver.find_element_by_id('id_gender2').click()
        # #5.wpisz imie
        driver.find_element_by_name('customer_firstname').send_keys(firstname)
        driver.find_element_by_name('customer_lastname').send_keys(lastname)
        #sprawdz poprawnosc maila
        email_text = driver.find_element_by_id('email').get_attribute('value')
        assert email_text == email
        #wpisz niepoprawne haslo
        driver.find_element_by_name('passwd').send_keys(password)
        #data ur
        day_of_birth_webelement=driver.find_element_by_id('days')
        day_of_birth_select=Select(day_of_birth_webelement)
        day_of_birth_select.select_by_value(birthday)

        birthmonth=Select(driver.find_element_by_id('months'))
        birthmonth.select_by_visible_text('November ')

        Select(driver.find_element_by_id('years')).select_by_value(birthyear)

        #sprawdz imie
        name_presented = driver.find_element_by_id('firstname').get_attribute('value')
        assert firstname == name_presented
        self.assertEqual(firstname, name_presented, 'zle imie!!!')
        sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=2)
