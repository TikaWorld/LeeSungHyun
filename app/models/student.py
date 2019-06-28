from sqlalchemy import Column, String, LargeBinary, Text

from app.models import Base


class Student(Base):
    __tablename__ = 'students'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    student_name = Column(String(255), primary_key=True)
    admission_grade = Column(String(20))
    project_name = Column(String(255))
    student_image = Column(LargeBinary)
    content = Column(Text)

    def __init__(self, student_name, admission_grade, project_name, student_image=b"", content=""):
        self.student_name = student_name
        self.admission_grade = admission_grade
        self.project_name = project_name
        self.student_image = student_image
        self.content = content

    def as_dict(self):
        result = {x.name: getattr(self, x.name) for x in self.__table__.columns}
        try:
            result["student_image"] = result["student_image"].decode("utf-8")
        except (AttributeError, TypeError):
            pass

        return result
