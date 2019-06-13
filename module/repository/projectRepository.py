import pymysql


class ProjectRepository:
    def __init__(self):
        self.url = "localhost"
        self.port = 3306
        self.user = "root"
        self.password = ""
        self.db = "leepository"
        self.table = "projects"

    def getProject(self, project):
        query = "SELECT * FROM %s WHERE projectName = '%s'" % (self.table, project)
        return self.transaction(query)

    def addProject(self):
        return NotImplemented

    def transaction(self, query):
        db = pymysql.connect(host=self.url, port=self.port, user=self.user, passwd=self.password, db=self.db)
        try:
            with db.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                db.commit()
        finally:
            db.close()

        return result

