import pymysql
from AgendaPaq.Contact import Contact

class ContactMysqlDA():

    instance = None
    agendaDB = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
            cls.instance.agendaDB = pymysql.connect(host="localhost",user="root", passwd="root",db="ORSYS_FORMATION_PYTHON",cursorclass=pymysql.cursors.DictCursor)
        return cls.instance



    def insert(self, my_object):
        if not isinstance(my_object,Contact):
            raise Exception("Insert attend un object de type Contact")
        with self.agendaDB.cursor() as cursor:
        # Create a new record
            sql = "INSERT INTO `contact` (`id`,`nom`,`prenom`,`numerotel`,`email`) VALUES (NULL,%s,%s,%s,%s)"
            cursor.execute(sql, (my_object.nom, my_object.prenom,my_object.tel,my_object.email))
        self.agendaDB.commit()

    def get_all(self):
        contacts={}
        with self.agendaDB.cursor() as cursor:
            cursor.execute("SELECT * FROM contact ORDER BY id DESC LIMIT 10")
            for result in cursor.fetchall():
                contacts[result['id']] = Contact(result['nom'],result['prenom'],result['numerotel'],result['email'])
        return contacts

    def close(self):
        self.agendaDB.close()

if __name__== "__main__":
    contact=ContactMysqlDA()
    contacts=contact.get_all();
    print(contacts)