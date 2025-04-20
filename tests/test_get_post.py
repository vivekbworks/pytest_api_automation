import os

import pytest
from utils.data_reader import load_test_data

# Load test data from JSON
DATA_PATH = os.path.join("testdata", "post_payloads.json")
test_data = load_test_data(DATA_PATH)

@pytest.mark.usefixtures("client")
def test_get_single_post(client):
    response = client.get("/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
    assert isinstance(data["userId"], int)

def test_get_all_posts(client):
    response = client.get("/posts")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 100
    assert all("id" in post for post in data)

def test_filter_posts_by_user(client):
    response = client.get("/posts", params={"userId": 1})
    # response = client.get("/posts")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for post in data:
        assert post["userId"] == 1

def test_get_nested_comments(client):
    response = client.get("/posts/1/comments")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for comment in data:
        assert comment["postId"] == 1
        assert "email" in comment
        assert "body" in comment

def test_create_post(client):
    payload = test_data["create_post"]
    response = client.post("/posts", data=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data  # Faked ID returned

def test_update_post_put(client):
    payload = test_data["update_post_put"]
    response = client.put("/posts/1", data=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == payload["id"]
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

def test_partial_update_post_patch(client):
    payload = test_data["update_post_patch"]
    response = client.patch("/posts/1", data=payload)
    assert response.status_code == 200
    data = response.json()
    assert "title" in data
    assert data["title"] == payload["title"]

def test_delete_post(client):
    response = client.delete("/posts/1")
    assert response.status_code in [200, 204]
