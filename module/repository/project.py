from app import db

class Project(db.model):
    __tablename__ = 'projects'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    project_name = db.Column(db.String(255), primary_key=True)
    admission_grade = db.Column(db.String(20))
    project_image = db.Column(db.LargeBinary)
    video_url = db.Column(db.String(255))
    content = db.Column(db.Text)
    created = db.Column(db.DateTime)

    def __init__(self, project_name, admission_grade, project_image, video_url, content):
        self.project_name = project_name
        self.admission_grade = admission_grade
        self.project_image = project_image
        self.video_url = video_url
        self.content = content