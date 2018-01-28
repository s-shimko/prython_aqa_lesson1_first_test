# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from contact import Contact
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def login(self, wd, username="admin", password="secret"):
        wd.find_element_by_name("user").click()
        el = wd.find_element_by_name("user")
        el.clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def create_contact_page(self, wd, contact):
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").send_keys(contact.notes)

    def return_contact_page(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def open_add_contact_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_add_contact_page(wd)
        self.create_contact_page(wd, Contact(firstname="firstname", middlename="middlename",
                                             lastname="lastname", nickname="nickname",
                                             title="title", company="company", address="address",
                                             home="home", mobile="mobile", work="work",
                                             fax="fax", email="email", homepage="homepage",
                                             address2="address2", phone2="phone2", notes="notes"))
        self.return_contact_page(wd)
        self.logout(wd)


    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
