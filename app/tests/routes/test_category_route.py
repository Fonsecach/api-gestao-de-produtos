import pytest
from fastapi.testclient import TestClient
from fastapi import status
from app.main import app
from app.db.models import Category as CategoryModel
from app.tests.use_cases.conftest import categories_on_db, db_session

client = TestClient(app)


def test_add_category_route(db_session):
    body = {"name": "Roupa Nova", "slug": "roupa-nova"}

    response = client.post("/category/add", json=body)

    assert response.status_code == status.HTTP_201_CREATED

    categories_on_db = db_session.query(CategoryModel).all()
    assert len(categories_on_db) == 1

    added_category = categories_on_db[0]
    assert added_category.name == body["name"]
    assert added_category.slug == body["slug"]


def test_list_categories_route(db_session, categories_on_db):
    response = client.get("/category/list")

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    categories_in_db = db_session.query(CategoryModel).all()
    assert len(data) == len(categories_in_db)
    assert len(data) == len(categories_on_db)

    for db_category, response_category in zip(categories_on_db, data):
        assert response_category == {
            "id": db_category.id,
            "name": db_category.name,
            "slug": db_category.slug,
        }
