from dataclasses import dataclass
from typing import Optional


@dataclass
class BaseAuthorSchema:
    name: str
    biography: str


@dataclass
class AuthorSchema(BaseAuthorSchema):
    id: int


@dataclass
class BaseCategorySchema:
    title: str
    description: str


@dataclass
class CategorySchema(BaseCategorySchema):
    id: int
