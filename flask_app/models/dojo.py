from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        dojos = []
        for result in results:
            dojos.append(cls(result))
        return dojos

    @classmethod
    def get_dojo(cls, id):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, {"id":id})
        print(results[0])
        return cls(results[0])

    @classmethod
    def create_dojo(cls,data):
        query = "INSERT INTO dojos (name) VALUES ( %(name)s);"
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)
