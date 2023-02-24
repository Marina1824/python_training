# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="firstname", middlename="middlename", lastname="last test", nickname="nicktest", title="title test", company="company test", address="address test", home="+7843564224", mobile="+7946545455", work="+9373632923", fax="+432423", email="test@mail.ru", email2="test2@yandex.ru", email3="test3@yandex.ru", homepage="homepage", bday="11", bmonth="August", byear="1998", aday="13", amonth="August", ayear="1999", address2="secondary address test", phone2="secondary home test", notes="secondary notes test"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact())
    app.session.logout()
