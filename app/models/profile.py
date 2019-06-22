from app.extension import main_db


class Profile(main_db.Model):
    __tablename__ = 'profiles'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    profile_name = main_db.Column(main_db.String(255), primary_key=True)
    admission_grade = main_db.Column(main_db.String(20))
    project_name = main_db.Column(main_db.String(255))
    profile_image = main_db.Column(main_db.LargeBinary)
    content = main_db.Column(main_db.Text)

    def __init__(self, profile_name, admission_grade, project_name, profile_image=b"", content=""):
        self.profile_name = profile_name
        self.admission_grade = admission_grade
        self.project_name = project_name
        self.profile_image = profile_image
        self.content = content

    def __repr__(self):
        chk_image = False
        chk_content = False
        if self.profile_image:
            chk_image = True
        if self.content:
            chk_content = True

        return "profile_name : %s, admission_grade : %s, project_name: %s " \
               "profile_image : %s, content : %s " \
               % (self.profile_name, self.admission_grade, self.project_name, chk_image, chk_content)

    def update_context(self, new):
        self.profile_name = new.projectName
        self.admission_grade = new.admissionGrade
        self.project_name = new.developerList
        self.profile_image = new.projectImage
        self.content = new.content

    def insert_or_update(self):
        current = Profile.query.filter_by(projectName=self.profile_name).first()

        if current:
            current.update_context(self)
        else:
            main_db.session.add(self)
        main_db.session.commit()

    def as_dict(self):
        result = {x.name: getattr(self, x.name) for x in self.__table__.columns}
        try:
            result["profile_image"] = result["project_image"].decode("utf-8")
        except (AttributeError, TypeError):
            pass

        return result
