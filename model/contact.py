from sys import maxsize
class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None,
                 company=None, address=None, home=None, mobile=None, work=None, fax=None, email=None,
                 email2=None, email3=None, homepage=None, bday=None, bmonth=None,byear=None, aday=None, amonth=None,
                 ayear=None, group=None, address2=None, phone2=None, notes=None, id=None, all_phones_from_home_page=None,
                 all_emails_from_home_page=None, fullname=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.group = group
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.fullname = fullname

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (self.id, self.lastname, self.firstname, self.address, self.all_phones_from_home_page, self.all_emails_from_home_page)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and \
               self.firstname == other.firstname and self.address == other.address and self.all_phones_from_home_page == other.all_phones_from_home_page \
               and self.all_emails_from_home_page


    def id_or_max(gr):
        if gr.id:
            return int(gr.id)
        else:
            return maxsize
