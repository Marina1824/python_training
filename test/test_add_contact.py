# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return clear(prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]))

def random_numbers(prefix, maxlen):
    number = string.digits *10
    return prefix + "".join([random.choice(number) for i in range(random.randrange(maxlen))])

def clear(s):
    return " ".join(s.split()) if s is not None else None

testdata = [Contact(firstname="", middlename="", lastname="",
                      nickname="", title="", company="", address="",
                      home="", mobile="", work="", fax="", email="",
                      email2="", email3="", homepage="",
                      bday="", bmonth="-", byear="", aday="", amonth="-",
                      ayear="", address2="", phone2="",
                      notes="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 20),
            lastname=random_string("lastname", 20), nickname=random_string("nickname", 20),
            title=random_string("title", 10), company=random_string("company", 20),
            address=random_string("address", 20), home=random_numbers("+", 10), mobile=random_numbers("+", 10),
            work=random_numbers("+", 10), fax=random_numbers("+", 10), email=random_string("email", 20),
            email2=random_string("email2", 20), email3=random_string("email3", 20),
            homepage=random_string("homepage", 10), bday="11", bmonth="August", byear="1998",
            aday="13", amonth="August", ayear="1999", address2=random_string("address2", 20),
            phone2=random_numbers("+", 10))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
