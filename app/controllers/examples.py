from typing import List, Optional
from blacksheep.server.controllers import Controller, get, post, delete, put, patch
from blacksheep import json

from app import models
from app.schemas import (
    AuthorSchema,
    BaseAuthorSchema,
    BaseCategorySchema,
    CategorySchema,
)


class ExamplesController(Controller):
    @classmethod
    def route(cls) -> Optional[str]:
        return "/api/author"

    @classmethod
    def class_name(cls) -> str:
        return "Author"

    @get("")
    async def get_authors(self, request) -> List[AuthorSchema]:
        authors = models.Author().all()
        return json(
            [
                AuthorSchema(
                    id=author.id,
                    name=author.name,
                    biography=author.biography,
                )
                for author in authors
            ]
        )

    @post("/")
    async def create_author(self, data: BaseAuthorSchema) -> AuthorSchema:
        author = models.Author(name=data.name, biography=data.biography)
        author = author.create(author)
        return json(
            AuthorSchema(id=author.id, name=author.name, biography=author.biography)
        )

    @delete("/{id}")
    async def delete_author(self, id):
        _ = models.Author().delete_by_id(id)
        return json({"details": "Delete successful"})

    @get("/{id}")
    async def get_author(self, id: int) -> AuthorSchema:
        author = models.Author().get_by_id(id)
        if author:
            return json(
                AuthorSchema(id=author.id, name=author.name, biography=author.biography)
            )
        return json({"details": "Not found."})

    @put("/{id}")
    async def update_author(self, id: int, data: BaseAuthorSchema) -> AuthorSchema:
        author = models.Author()
        author = author.update_by_id(id, data)

        return json(
            AuthorSchema(id=author.id, name=author.name, biography=author.biography)
        )

    # not working for partial update
    @patch("/{id}")
    async def partial_update_author(
        self, id: int, data: BaseAuthorSchema
    ) -> AuthorSchema:
        print(data)
        author = models.Author()
        author = author.update_by_id(id, data)

        return json(
            AuthorSchema(id=author.id, name=author.name, biography=author.biography)
        )


class CategoryController(Controller):
    @classmethod
    def route(cls) -> Optional[str]:
        return "/api/categories"

    @classmethod
    def class_name(cls) -> str:
        return "Category"

    @get("")
    async def get_authors(self, request) -> List[str]:
        return json(
            [
                BaseCategorySchema(
                    id=1, title="Python v3", description="this is python book."
                ),
            ]
        )

    @post("/")
    async def create_author(self, body: CategorySchema):
        return json(body)
