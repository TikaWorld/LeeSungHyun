from app import db


class Project(db.Model):
    __tablename__ = 'projects'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    project_name = db.Column(db.String(255), primary_key=True)
    admission_grade = db.Column(db.String(20))
    project_image = db.Column(db.LargeBinary)
    video_url = db.Column(db.String(255))
    content = db.Column(db.Text)
#    created = db.Column(db.DateTime)

    def __init__(self, project_name, admission_grade, project_image=None, video_url=None, content=None):
        self.project_name = project_name
        self.admission_grade = admission_grade
        self.project_image = project_image
        self.video_url = video_url
        self.content = content

    def __repr__(self):
        chk_image = False
        chk_video = False
        chk_content = False
        if self.project_image:
            chk_image = True
        if self.video_url:
            chk_video = True
        if self.content:
            chk_content = True

        return "project_name : %s\n, admission_grade : %s\n, project_image : %s\n, video_url : %s\n, content : %s " \
               % (self.project_name, self.admission_grade, chk_image, chk_video, chk_content)
