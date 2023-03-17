# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="firstname", middlename="middlename", lastname="last test",
                      nickname="nicktest", title="title test", company="company test",
                      address="address test", home="+7843564224", mobile="+7946545455",
                      work="+9373632923", fax="+432423", email="test@mail.ru",
                      email2="test2@yandex.ru", email3="test3@yandex.ru", homepage="homepage",
                      bday="11", bmonth="August", byear="1998", aday="13", amonth="August",
                      ayear="1999", address2="secondary address test", phone2="+373732",
                      notes="secondary notes test")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_add_empty_contact(app):
#    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="",
#                 company="", address="", home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="", bday="", bmonth="-",byear="", aday="", amonth="-",
#                 ayear="", address2="", phone2="", notes=""))
