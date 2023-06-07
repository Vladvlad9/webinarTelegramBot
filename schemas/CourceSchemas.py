from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, validator


class CourseSchema(BaseModel):
    user_id: Optional[int] = Field(ge=1)
    name: Optional[str]
    description: str
    KeywordsOne: str = Field(default="Нету Ключевого слова 1")
    KeywordsTwo: str = Field(default="Нету ключевого слова 2")
    KeywordsThree: str = Field(default="Нету ключевого слова 3")
    date_course: datetime
    link: str

    @validator('name')
    def name_must_contain_space(cls, name):
        if name == '':
            raise ValueError('Не введено название курса')
        return name.title()

    @validator('description')
    def name_must_contain_space(cls, description):
        if description == '':
            raise ValueError('Не введено описание курса')
        return description.title()


class CourseInDBSchema(CourseSchema):
    id: int = Field(ge=1)
