# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from contactapp import Contactapp

@pytest.fixture
def app(request):
    fixture = Contactapp()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="firstname", middlename="middlename", lastname="last test", nickname="nicktest", title="title test", company="company test", address="address test", home="+7843564224",mobile="+7946545455", work="+9373632923", fax="+432423", email="test@mail.ru", email2="test2@yandex.ru", email3="test3@yandex.ru", homepage="homepage", bday="11", bmonth="August", byear="1998", aday="13", amonth="August", ayear="1999", address2="secondary address test",  phone2="secondary home test", notes="secondary notes test"))
    app.logout()

def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="", bday="", bmonth="-", byear="", aday="", amonth="-", ayear="", address2="",  phone2="", notes=""))
    app.logout()