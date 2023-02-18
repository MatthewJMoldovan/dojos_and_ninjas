from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo import Dojo

class Ninja:
    def __init__(self,data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def get_ninja_with_dojo(cls):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        dojo_w_ninjas = []

        for row in results:
            dojo = Dojo(row)
            ninja_data = {
                **row,
                'id' : row['ninjas.id'],
                'created_at' : row['ninjas.created_at'],
                'updated_at' : row['ninjas.updated_at']
            }
            ninja = Ninja(ninja_data)
            ninja.dojo = dojo
            dojo_w_ninjas.append(ninja)
            
        print(dojo_w_ninjas)
        return dojo_w_ninjas

    @classmethod
    def create_ninja(cls,data):
        query = """INSERT INTO ninjas (first_name, last_name, age, dojo_id) 
        VALUES (%(first_name)s, %(last_name)s,%(age)s,%(dojo_id)s );"""
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)
