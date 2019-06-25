from sqlalchemy import Column, String, LargeBinary, Text

from app.models import Base


class Profile(Base):
    __tablename__ = 'profiles'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    profile_name = Column(String(255), primary_key=True)
    admission_grade = Column(String(20))
    project_name = Column(String(255))
    profile_image = Column(LargeBinary)
    content = Column(Text)

    def __init__(self, profile_name, admission_grade, project_name, profile_image=b"", content=""):
        self.profile_name = profile_name
        self.admission_grade = admission_grade
        self.project_name = project_name
        self.profile_image = profile_image
        self.content = content
    def update_context(self, new):
        self.profile_name = new.projectName
        self.admission_grade = new.admissionGrade
        self.project_name = new.developerList
        self.profile_image = new.projectImage
        self.content = new.content

    def insert_or_update(self):
        current = Profile.query.filter_by(profile_name=self.profile_name).first()

        if current:
            current.update_context(self)
        else:
            Base.session.add(self)
        Base.session.commit()

    def as_dict(self):
        result = {x.name: getattr(self, x.name) for x in self.__table__.columns}
        try:
            result["profile_image"] = result["project_image"].decode("utf-8")
        except (AttributeError, TypeError):
            pass

        return result
