import pytest
from app.db.connection import Session
from app.db.models import Category as CategoryModel


@pytest.fixture(scope="function")
def db_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture(autouse=True)
def clean_db(db_session):
    yield
    db_session.query(CategoryModel).delete()
    db_session.commit()


@pytest.fixture(scope="function")
def categories_on_db(db_session):
    categories = [
        CategoryModel(name="Roupa", slug="roupa"),
        CategoryModel(name="Caixa", slug="caixa"),
        CategoryModel(name="Caixa de Limão", slug="caixa-de-limao"),
        CategoryModel(name="Limão", slug="limao"),
        CategoryModel(name="Itens de cozinha", slug="itens-de-cozinha"),
        CategoryModel(name="Decoracao", slug="decoracao"),
    ]

    for category in categories:
        db_session.add(category)
    db_session.commit()

    for category in categories:
        db_session.refresh(category)

    yield categories
