import random

from model.contact import Contact
from random import randrange



def test_modify_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="edit", middlename="middlename", lastname="last test", nickname="nicktest",
                    title="title test", company="company test", address="address test", home="+7843564224",
                    mobile="+7946545455", work="+9373632923", fax="+432423", email="test@mail.ru",
                    email2="test2@yandex.ru",
                    email3="test3@yandex.ru", homepage="homepage", bday="11", bmonth="August", byear="1998", aday="13",
                    amonth="August", ayear="1999", address2="secondary address test", phone2="secondary home test",
                    notes="test notes test"))

    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = old_contacts[index]
    new_contact = Contact(firstname="test", middlename="middlenametest", lastname="test", nickname="nicktest",
                    title="title test", company="company test", address="address test", home="+784 3564 224",
                    mobile="+794we6545455", work="+ 9373 63292 3", fax="+432423", email="test@mail.ru",
                    email2="test2@yweandex.ru",
                    email3="test3@yanewdex.ru", homepage="homepreage", bday="11", bmonth="August", byear="1998", aday="13",
                    amonth="August", ayear="1999", address2="secorendary address test", phone2="+37 37 32",
                    notes="test notes test")
    new_contact.id = contact.id
    app.contact.modify_contact_by_id(contact.id, new_contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = new_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        for contact in new_contacts:
            contact.firstname = contact.firstname.rstrip()
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

#def test_modify_contact_firstname(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="edit"))
#    app.contact.modify_first_contact(Contact(firstname="edit"))

