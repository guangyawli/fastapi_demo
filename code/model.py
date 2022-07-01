# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from db import Base
from db import ENGINE


class FileInfoTable(Base):
    __tablename__ = 'fileinfo'

    id = Column(Integer, primary_key=True, autoincrement=True)
    file_name = Column(String(50), nullable=False)
    file_path = Column(String(100), nullable=False)
    file_size = Column(String(10), nullable=False)
    file_type = Column(String(50), nullable=False)


class FileInformation(BaseModel):
    id: int
    file_name: str
    file_path: str
    file_size: str
    file_type: str


def main():
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main()
