from datetime import datetime

from sqlalchemy import create_engine, MetaData, Column, Integer, Table, String, Text, Boolean, DateTime
from sqlalchemy.orm import sessionmaker, mapper

engine = create_engine('sqlite:///python.db')
Session = sessionmaker(engine)
session = Session()

metadata = MetaData(engine)

blog = Table('blog', metadata,
             Column('id', Integer(), primary_key=True),
             Column('post_title', String(200), nullable=False),
             Column('post_slug', String(200), nullable=False),
             Column('content', Text(), nullable=False),
             Column('published', Boolean(), default=False),
             Column('created_on', DateTime(), default=datetime.now),
             Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now))


class Blog:
    def __init__(self, post_title, post_slug, content, published, created_on, updated_on):
        self.post_title = post_title
        self.post_slug = post_slug
        self.content = content
        self.published = published
        self.created_on = created_on
        self.updated_on = updated_on

    def __repr__(self):
        return f"{self.post_title}, {self.post_slug}, {self.content}, {self.published}, {self.published}, " \
               f"{self.created_on}, {self.updated_on}"


metadata.create_all(engine)

print(type(blog))
