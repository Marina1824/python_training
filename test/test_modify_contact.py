
from model.contact import Contact



def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="edit", middlename="middlename", lastname="last test", nickname="nicktest",
                    title="title test", company="company test", address="address test", home="+7843564224",
                    mobile="+7946545455", work="+9373632923", fax="+432423", email="test@mail.ru",
                    email2="test2@yandex.ru",
                    email3="test3@yandex.ru", homepage="homepage", bday="11", bmonth="August", byear="1998", aday="13",
                    amonth="August", ayear="1999", address2="secondary address test", phone2="secondary home test",
                    notes="test notes test"))
    app.contact.modify_first_contact(Contact(firstname="edit", middlename="middlename", lastname="last test", nickname="nicktest",
                    title="title test", company="company test", address="address test", home="+7843564224",
                    mobile="+7946545455", work="+9373632923", fax="+432423", email="test@mail.ru",
                    email2="test2@yandex.ru",
                    email3="test3@yandex.ru", homepage="homepage", bday="11", bmonth="August", byear="1998", aday="13",
                    amonth="August", ayear="1999", address2="secondary address test", phone2="secondary home test",
                    notes="test notes test"))

def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="edit"))
    app.contact.modify_first_contact(Contact(firstname="edit"))

