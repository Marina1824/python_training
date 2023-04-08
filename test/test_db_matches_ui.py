from model.group import Group
from model.contact import Contact
from timeit import timeit
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
        return Contact(id=contact.id, lastname=contact.lastname.strip().rstrip(), firstname=contact.firstname.strip().rstrip())
    db_list = map(clean, db.get_contact_list())
    #print(timeit(lambda: map(clean, db.get_contact_list()), number=1000))
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list,  key=Contact.id_or_max)
