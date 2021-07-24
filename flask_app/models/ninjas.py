
from flask_app.config.mysqlconnection import connectToMySQL


class Ninja():
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']


    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"

        new_ninja_id = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

        return new_ninja_id

    @classmethod
    def get_all_ninjas(cls,data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(id)s"

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

        ninjas = []
        for item in results:
            ninjas.append(cls(item))

        return ninjas