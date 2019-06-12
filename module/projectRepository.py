import pymysql


class ProjectRepository:
    def __init__(self):
        self.url = ""

    def getProject(self, project):
        query = "SELECT * FROM " + self.table + " WHERE name = " + project
        return self.transaction(query)

    def addProject(self):
        return NotImplemented

    def transaction(self, query):
        db = pymysql.connect()
        try:
            with db.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                db.commit()
        finally:
            db.close()

        return result

