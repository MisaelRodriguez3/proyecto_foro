from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .material import Material
from .challenges import Challenge
from .examples import Example
from .comments import Comment
from .posts import Post
from .topics import Topic
from .users import User
