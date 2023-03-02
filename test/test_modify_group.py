
from model.group import Group



def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="edit name"))

def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="edit header"))