from model.group import Group
from model.contact import Contact
from timeit import timeit
import re
def test_group_list(app, db):
    print(timeit(lambda: app.group.get_group_list(), number=1))
    def clean(group):
        return Group(id=group.id, name=group.name.strip().rstrip())
    print(timeit(lambda: map(clean, db.get_group_list()), number=1000))
    assert False #sorted(ui_list, key=Group.id_or_max) == sorted(db_list,  key=Group.id_or_max)



def test_contact_list(app, db):
    ui_list = app.contact.get_contact_list()
    #print(timeit(lambda: app.contact.get_contact_list(), number=1))
    def clean(contact):
        return Contact(id=contact.id, lastname=contact.lastname.strip().rstrip(), firstname=contact.firstname.strip().rstrip(),
                       address=contact.address, all_phones_from_home_page=merge_phones_like_on_home_page(contact),
                       all_emails_from_home_page=merge_emails_like_on_home_page(contact))

    db_list = map(clean, db.get_contact_list())
    #print(timeit(lambda: map(clean, db.get_contact_list()), number=1000))
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list,  key=Contact.id_or_max)

def clear(s):
    return re.sub("[() -]", "", s)
def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: x, filter(lambda x: x is not None,
                                                           [contact.email, contact.email2, contact.email3]))))