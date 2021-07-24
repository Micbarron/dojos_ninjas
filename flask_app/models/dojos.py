from flask_app.config.mysqlconnection import connectToMySQL

class Dojo():

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES ( %(dojo_name)s);"

        new_dojo_id = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

        return new_dojo_id



    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos"

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)

        dojos = []
        for item in results:
            dojos.append(cls(item))

        return dojos

    @classmethod
    def get_dojo_id(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        dojo = Dojo(results[0])

        return dojo



