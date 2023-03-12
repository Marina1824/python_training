from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from model.contact import Contact
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("localhost/addressbook/")):
            wd.find_element_by_link_text("home").click()

    def change_select_value(self,field_name,text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def change_field_value(self,field_name,text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname",contact.firstname)
        self.change_field_value("middlename",contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title",contact.title)
        self.change_field_value("company",contact.company)
        self.change_field_value("address",contact.address)
        self.change_field_value("home",contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3",contact.email3)
        self.change_field_value("homepage",contact.homepage)
        self.change_select_value("bday",contact.bday)
        self.change_select_value("bmonth",contact.bmonth)
        self.change_field_value("byear",contact.byear)
        self.change_select_value("aday", contact.aday)
        self.change_select_value("amonth", contact.amonth)
        self.change_field_value("ayear",contact.ayear)
        self.change_field_value("address2",contact.address2)
        self.change_field_value("phone2",contact.phone2)
        self.change_field_value("notes",contact.notes)

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.open_home()
        self.select_first_contact()
        #open modification form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        # submit group creation
        wd.find_element_by_name("update").click()
        self.open_home()

    def create(self, contact):
        wd = self.app.wd
        self.open_home()
        wd.find_element_by_link_text("add new").click()
        # fill group creation
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.open_home()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home()
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.msgbox")))
        self.open_home()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        self.open_home()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_home()
        contacts = []
        for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
            tds = element.find_elements(By.TAG_NAME, "td")
            lastname = tds[1].text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(lastname=lastname, id=id))
        return contacts
