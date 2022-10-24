from datetime import datetime

from sqlalchemy import create_engine, MetaData, Column, Integer, Table, String, Text, Boolean, DateTime
from sqlalchemy.orm import sessionmaker, mapper, declarative_base

engine = create_engine('sqlite:///python.db')
Session = sessionmaker(engine)
session = Session()

Base = declarative_base(engine)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(16), nullable=False)
    email = Column(String(60))
    login = Column(String(50), nullable=False)

    def __repr__(self):
        return f"{self.name}, {self.email}, {self.login}"

    @classmethod
    def get_all_users(cls):
        return session.query(User).all()


Base.metadata.create_all()

print(User.get_all_users())
# metadata = MetaData(engine)
# blog = Table('blog', metadata,
#              Column('id', Integer(), primary_key=True),
#              Column('post_title', String(200), nullable=False),
#              Column('post_slug', String(200), nullable=False),
#              Column('content', Text(), nullable=False),
#              Column('published', Boolean(), default=False),
#              Column('created_on', DateTime(), default=datetime.now),
#              Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now))
#
#
# class Blog:
#     def __init__(self, post_title, post_slug, content, published, created_on, updated_on):
#         self.post_title = post_title
#         self.post_slug = post_slug
#         self.content = content
#         self.published = published
#         self.created_on = created_on
#         self.updated_on = updated_on
#
#     def __repr__(self):
#         return f"{self.post_title}, {self.post_slug}, {self.content}, {self.published}, {self.published}, " \
#                f"{self.created_on}, {self.updated_on}"
#
#
# mapper(Blog, blog)
#
# b = Blog('test', 'test', 'test', True, datetime.now(), datetime.now())
# metadata.create_all(engine)
