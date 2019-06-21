from app.extension import main_db


class Profile(main_db.Model):
    __tablename__ = 'profiles'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    profileName = main_db.Column(main_db.String(255), primary_key=True)
    admissionGrade = main_db.Column(main_db.String(20))
    projectName = main_db.Column(main_db.String(255))
    profileImage = main_db.Column(main_db.LargeBinary)
    content = main_db.Column(main_db.Text)

    def __init__(self, profile_name, admission_grade, project_name, profile_image=b"", content=""):
        self.profileName = profile_name
        self.admissionGrade = admission_grade
        self.projectName = project_name
        self.profileImage = profile_image
        self.content = content

    def __repr__(self):
        chk_image = False
        chk_content = False
        if self.profileImage:
            chk_image = True
        if self.content:
            chk_content = True

        return "profile_name : %s, admission_grade : %s, project_name: %s " \
               "profile_image : %s, content : %s " \
               % (self.profileName, self.admissionGrade, self.projectName, chk_image, chk_content)

    def update_context(self, new):
        self.profileName = new.projectName
        self.admissionGrade = new.admissionGrade
        self.projectName = new.developerList
        self.profileImage = new.projectImage
        self.content = new.content

    def insert_or_update(self):
        current = Profile.query.filter_by(projectName=self.profileName).first()

        if current:
            current.update_context(self)
        else:
            main_db.session.add(self)
        main_db.session.commit()

    def as_dict(self):
        result = {x.name: getattr(self, x.name) for x in self.__table__.columns}
        try:
            result["profileImage"] = result["projectImage"].decode("utf-8")
        except (AttributeError, TypeError):
            pass

        return result
