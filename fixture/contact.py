from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from model.contact import Contact
import re
class ContactHelper:

    def __init__(self, app):
        self.app = app


    def change_field_value(self,field_name,text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    contact_cache = None

    def open_home(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("localhost/addressbook/")):
            wd.find_element_by_link_text("home").click()

    def change_select_value(self,field_name,text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)


    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname",contact.firstname)
        self.change_field_value("middlename",contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("company",contact.company)
        self.change_field_value("title",contact.title)
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

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_home()
        #open modification form
        pens = wd.find_elements_by_xpath("//img[@alt='Edit']")
        pens[index].click()
        self.fill_contact_form(new_contact_data)
        # submit group creation
        wd.find_element_by_name("update").click()
        self.open_home()
        self.contact_cache = None

    def create(self, contact):
        wd = self.app.wd
        self.open_home()
        wd.find_element_by_link_text("add new").click()
        # fill group creation
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.open_home()
        self.contact_cache = None

    def select_contact_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self,index):
        wd = self.app.wd
        self.open_home()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.msgbox")))
        self.open_home()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        self.open_home()
        return len(wd.find_elements_by_name("selected[]"))

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()


    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                cells = element.find_elements(By.TAG_NAME, "td")
                lastname = cells[1].text
                firstname = cells[2].text
                id = cells[0].find_element(By.TAG_NAME, "input").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       home=home, work=work, mobile=mobile,
                       phone2=phone2)

    def get_contact_from_view_page(self,index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, work=work, mobile=mobile,
                       phone2=phone2)


