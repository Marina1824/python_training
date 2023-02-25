
from model.group import Group



def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="edit name", header="edit header", footer="edit footer"))
    app.session.logout()