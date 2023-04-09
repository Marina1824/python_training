
from model.group import Group
from random import randrange


def test_modify_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test321"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = old_groups[index]
    new_group = Group(name="New group4324")
    new_group.id = group.id
    app.group.modify_group_by_id(group.id, new_group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = new_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
#def test_modify_group_header(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    app.group.modify_first_group(Group(header="edit header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)