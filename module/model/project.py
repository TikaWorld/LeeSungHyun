from database import db


class Project(db.Model):
    __tablename__ = 'projects'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    projectName = db.Column(db.String(255), primary_key=True)
    admissionGrade = db.Column(db.String(20))
    developerList = db.Column(db.Text)
    projectImage = db.Column(db.LargeBinary)
    videoUrl = db.Column(db.String(255))
    content = db.Column(db.Text)
#    created = db.Column(db.DateTime)

    def __init__(self, project_name, admission_grade, developer_list, project_image=b"", video_url="", content=""):
        self.projectName = project_name
        self.admissionGrade = admission_grade
        self.developerList = developer_list
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

        return "project_name : %s, admission_grade : %s, developer_list: %s " \
               "project_image : %s, video_url : %s, content : %s " \
               % (self.projectName, self.admissionGrade, self.developerList, chk_image, chk_video, chk_content)

    def update_context(self, new):
        self.projectName = new.projectName
        self.admissionGrade = new.admissionGrade
        self.developerList = new.developerList
        self.projectImage = new.projectImage
        self.videoUrl = new.videoUrl
        self.content = new.content

    def insert_or_update(self):
        current = Project.query.filter_by(projectName=self.projectName).first()

        if current:
            current.update_context(self)
        else:
            db.session.add(self)
        db.session.commit()

    def as_dict(self):
        result = {x.name: getattr(self, x.name) for x in self.__table__.columns}
        try:
            result["developerList"] = result["developerList"].split(":")
        except (AttributeError, TypeError):
            pass
        try:
            result["projectImage"] = result["projectImage"].decode("utf-8")
        except (AttributeError, TypeError):
            pass

        return result
