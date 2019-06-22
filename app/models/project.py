from app.extension import main_db


class Project(main_db.Model):
    __tablename__ = 'projects'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    project_name = main_db.Column(main_db.String(255), primary_key=True)
    admission_grade = main_db.Column(main_db.String(20))
    developer_list = main_db.Column(main_db.Text)
    project_image = main_db.Column(main_db.LargeBinary)
    video_url = main_db.Column(main_db.String(255))
    content = main_db.Column(main_db.Text)
#    created = db.Column(db.DateTime)

    def __init__(self, project_name, admission_grade, developer_list, project_image=b"", video_url="", content=""):
        self.project_name = project_name
        self.admission_grade = admission_grade
        self.developer_list = developer_list
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

        return "project_name : %s, admission_grade : %s, developer_list: %s " \
               "project_image : %s, video_url : %s, content : %s " \
               % (self.project_name, self.admission_grade, self.developer_list, chk_image, chk_video, chk_content)

    def update_context(self, new):
        self.project_name = new.projectName
        self.admission_grade = new.admissionGrade
        self.developer_list = new.developerList
        self.project_image = new.projectImage
        self.video_url = new.videoUrl
        self.content = new.content

    def insert_or_update(self):
        current = Project.query.filter_by(projectName=self.project_name).first()

        if current:
            current.update_context(self)
        else:
            main_db.session.add(self)
        main_db.session.commit()

    def as_dict(self):
        result = {x.name: getattr(self, x.name) for x in self.__table__.columns}
        try:
            result["developer_list"] = result["developer_list"].split(":")
        except (AttributeError, TypeError):
            pass
        try:
            result["project_image"] = result["project_image"].decode("utf-8")
        except (AttributeError, TypeError):
            pass

        return result
