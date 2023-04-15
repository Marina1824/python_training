from selenium.webdriver.common.by import By
from model.group import Group
from model.contact import Contact
from random import randrange

def test_del_contact_from_group(app, orm, db, check_ui):
    groups = app.wd.find_element_by_name("group").find_elements(By.TAG_NAME, "option")
    index = randrange(len(groups))
    group = groups[index]
    group_id = group.get_attribute("value")
    app.contact.change_select_value_by_index("group", index)
    if app.contact.count_contacts_on_page() == 0:
        app.contact.create(Contact(lastname="lastname", firstname="firstname", group=group_id))
        app.contact.change_select_value_by_index("group", index)
    contact = app.wd.find_elements_by_name("selected[]")[0]
    contact_id = contact.get_attribute("id")
    contact.click()
    app.wd.find_element_by_name("remove").click()
    contacts = orm.get_contacts_in_group(Group(id=group_id))
    contact_found = False
    for c in contacts:
        if c.id == contact_id:
            contact_found = True
    assert not contact_found, f"contact {contact_id} exists in group {group_id}"
