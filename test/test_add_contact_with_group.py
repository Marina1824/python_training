# -*- coding: utf-8 -*-

from model.contact import Contact
from model.group import Group
def test_add_contact_with_group(app, db, orm, json_contacts):
    contact = json_contacts
    group_id = app.contact.create(contact)
    new_contacts = orm.get_contact_list()
    contact_id = sorted(new_contacts, key=Contact.id_or_max)[-1].id
    if group_id !="":
        contacts = orm.get_contacts_in_group(Group(id=group_id))
        contact_found = False
        for c in contacts:
            if c.id == contact_id:
                contact_found = True
        assert contact_found
