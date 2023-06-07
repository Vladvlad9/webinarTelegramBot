from datetime import datetime

from pydantic import BaseModel


class BotSchema(BaseModel):
    TOKEN: str
    ADMINS: list[int]


class CourseSchema(BaseModel):
    NAME: str
    DESCRIPTION: str
    KW1: str
    KW2: str
    KW3: str
    DT: str
    LINK: str


class ConfigSchema(BaseModel):
    BOT: BotSchema
    ADDCOURSE: CourseSchema
    DATABASE: str
