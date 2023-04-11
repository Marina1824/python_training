from selenium.webdriver.common.by import By
import random
from model.contact import Contact
from random import randrange

def test_del_contact_from_group(app, db, check_ui):
    groups = app.wd.find_element_by_name("group").find_elements(By.TAG_NAME, "option")
    index = randrange(len(groups))
    group = groups[index]
    group_id = group.get_attribute("value")
    print(group_id)
    print(app.contact.count_contacts_on_page())
    app.contact.change_select_value_by_index("group", index)
    if app.contact.count_contacts_on_page() == 0:
        app.contact.create(Contact(lastname="lastname", firstname="firstname", group=group_id))
    #if contact in groups:
