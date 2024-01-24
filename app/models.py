from sqlalchemy import Table, Column, Integer, String, Date
from config import metadata

author = Table(
    "author",
    metadata,
    Column("authorId", Integer, primary_key=True, autoincrement=True),
    Column("firstName", String(50), nullable=False),
    Column("lastName", String(50), nullable=False),
    Column("bio", String(250), nullable=True),
    Column("birthDate", Date, nullable=True)
)