from database import db


class Project(db.Model):
    __tablename__ = 'projects'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    projectName = db.Column(db.String(255), primary_key=True)
    admissionGrade = db.Column(db.String(20))
    projectImage = db.Column(db.LargeBinary)
    videoUrl = db.Column(db.String(255))
    content = db.Column(db.Text)
#    created = db.Column(db.DateTime)

    def __init__(self, project_name, admission_grade, project_image=None, video_url=None, content=None):
        self.projectName = project_name
        self.admissionGrade = admission_grade
        self.projectImage = project_image
        self.videoUrl = video_url
        self.content = content

    def __repr__(self):
        chk_image = False
        chk_video = False
        chk_content = False
        if self.projectImage:
            chk_image = True
        if self.videoUrl:
            chk_video = True
        if self.content:
            chk_content = True

        return "project_name : %s, admission_grade : %s, project_image : %s, video_url : %s, content : %s " \
               % (self.projectName, self.admissionGrade, chk_image, chk_video, chk_content)

    def as_dict(self):
        result = {x.name: getattr(self, x.name) for x in self.__table__.columns}
        result["projectImage"] = result["projectImage"].decode("utf-8")
        return result
