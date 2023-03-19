

def test_lastname_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname



def test_lastname_on_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    firstname = clear(contact_from_edit_page.firstname)
    lastname = clear(contact_from_edit_page.lastname)
    assert contact_from_view_page.fullname.startswith(firstname)
    assert contact_from_view_page.fullname.endswith(lastname)


def clear(s):
    return s.lstrip()