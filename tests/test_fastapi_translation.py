"""
The "big test": translate a non-trivial FastAPI application written in Pitão
(testcases/fastapi_app.pt) into Python and drive the real app with FastAPI's
TestClient.

This exercises Pitão end-to-end against a real third-party framework, not just
the self-contained example snippets. It also asserts that the generated Python
round-trips losslessly (py -> pt -> py), which guards the attribute-corruption
fix in pitao/parser.py.

FastAPI requires Python >= 3.10, so on older interpreters (and anywhere FastAPI
or httpx is not installed) these tests skip cleanly via importorskip.
"""

import importlib.util
import os

import pytest

from pitao.parser import translate_keywords

# Skip the whole module unless the FastAPI stack is importable.
pytest.importorskip("fastapi")
pytest.importorskip("httpx")

from fastapi.testclient import TestClient  # noqa: E402  (after importorskip)

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_PT = os.path.join(REPO_ROOT, "testcases", "fastapi_app.pt")


def _translate_app():
    """Translate the Pitão FastAPI app to Python source."""
    with open(APP_PT, "r", encoding="utf-8") as handle:
        pitao_source = handle.read()
    return translate_keywords(pitao_source, reverse=False)


@pytest.fixture(scope="module")
def app_module(tmp_path_factory):
    """Translate the .pt app, write it to a temp .py, import it."""
    python_source = _translate_app()
    out_dir = tmp_path_factory.mktemp("pitao_fastapi")
    out_path = out_dir / "fastapi_app.py"
    out_path.write_text(python_source, encoding="utf-8")

    spec = importlib.util.spec_from_file_location("pitao_fastapi_app", out_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client(app_module):
    """A fresh TestClient with an empty in-memory store per test."""
    app_module.itens_db.clear()
    return TestClient(app_module.app)


def test_translation_is_importable_fastapi_app(app_module):
    """The translated module exposes a real FastAPI instance with routes."""
    from fastapi import FastAPI

    assert isinstance(app_module.app, FastAPI)
    # root + list + get + post + put + delete (plus FastAPI's default docs routes)
    assert len(app_module.app.routes) >= 6


def test_health_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "total": 0}


def test_create_item(client):
    payload = {"nome": "Caneta", "preco": 2.5, "quantidade": 10}
    response = client.post("/itens/1", json=payload)
    assert response.status_code == 201
    body = response.json()
    assert body["item_id"] == 1
    assert body["item"] == payload


def test_create_conflict(client):
    payload = {"nome": "Caneta", "preco": 2.5, "quantidade": 10}
    assert client.post("/itens/1", json=payload).status_code == 201
    assert client.post("/itens/1", json=payload).status_code == 409


def test_get_item_roundtrips_body(client):
    payload = {"nome": "Lápis", "preco": 1.0, "quantidade": 3}
    client.post("/itens/7", json=payload)
    response = client.get("/itens/7")
    assert response.status_code == 200
    assert response.json() == payload


def test_get_missing_item_404(client):
    response = client.get("/itens/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item não encontrado"


def test_default_quantity(client):
    # 'quantidade' has a default of 0 in the pydantic model.
    client.post("/itens/3", json={"nome": "Borracha", "preco": 0.5})
    assert client.get("/itens/3").json()["quantidade"] == 0


def test_list_respects_query_limit(client):
    for item_id in range(1, 6):
        client.post(f"/itens/{item_id}", json={"nome": f"i{item_id}", "preco": 1.0})
    response = client.get("/itens", params={"limite": 2})
    assert response.status_code == 200
    body = response.json()
    assert len(body["itens"]) == 2
    assert body["total"] == 5


def test_query_validation_rejects_out_of_range(client):
    # Query(..., ge=1, le=100): a value above the bound is a 422.
    assert client.get("/itens", params={"limite": 1000}).status_code == 422


def test_update_item(client):
    client.post("/itens/1", json={"nome": "Caneta", "preco": 2.5, "quantidade": 10})
    updated = {"nome": "Caneta Azul", "preco": 3.0, "quantidade": 5}
    response = client.put("/itens/1", json=updated)
    assert response.status_code == 200
    assert response.json()["item"] == updated
    assert client.get("/itens/1").json() == updated


def test_update_missing_item_404(client):
    response = client.put("/itens/42", json={"nome": "x", "preco": 1.0})
    assert response.status_code == 404


def test_delete_item(client):
    client.post("/itens/1", json={"nome": "Caneta", "preco": 2.5, "quantidade": 10})
    response = client.delete("/itens/1")
    assert response.status_code == 200
    assert response.json()["item_id"] == 1
    # Deleting removes it: a subsequent GET is 404.
    assert client.get("/itens/1").status_code == 404


def test_delete_missing_item_404(client):
    assert client.delete("/itens/123").status_code == 404


def test_generated_python_is_roundtrip_lossless():
    """
    The demo app is authored to avoid the translator's inherent identifier
    collisions, so its generated Python must survive py -> pt -> py unchanged.
    This doubles as a regression test for the attribute-corruption fix.
    """
    python_source = _translate_app()
    round_tripped = translate_keywords(
        translate_keywords(python_source, reverse=True), reverse=False
    )
    assert round_tripped == python_source
