from sqlalchemy import Column, String, Text, LargeBinary

from app.models import Base


class Project(Base):
    __tablename__ = "projects"
    __table_args__ = {"mysql_collate": "utf8_general_ci"}

    project_name = Column(String(255), primary_key=True)
    admission_grade = Column(String(20))
    developer_list = Column(Text)
    project_image = Column(LargeBinary)
    video_url = Column(String(255))
    content = Column(Text)
    #    created = db.Column(db.DateTime)

    def __init__(
        self,
        project_name,
        admission_grade,
        developer_list,
        project_image=b"",
        video_url="",
        content="",
    ):
        self.project_name = project_name
        self.admission_grade = admission_grade
        self.developer_list = developer_list
        self.project_image = project_image
        self.video_url = video_url
        self.content = content

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
