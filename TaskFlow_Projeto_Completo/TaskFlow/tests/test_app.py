import json
import pytest
from src.app import app, DATA_FILE

@pytest.fixture
def client(tmp_path, monkeypatch):
    test_file = tmp_path / "tasks.json"
    monkeypatch.setattr("src.app.DATA_FILE", test_file)
    app.config["TESTING"] = True
    return app.test_client(), test_file

def test_home_page_loads(client):
    web, _ = client
    response = web.get("/")
    assert response.status_code == 200
    assert b"TaskFlow" in response.data

def test_create_task(client):
    web, file = client
    response = web.post("/tasks", data={"title": "Teste", "description": "Desc", "priority": "Alta"})
    assert response.status_code == 302
    tasks = json.loads(file.read_text())
    assert tasks[0]["title"] == "Teste"
    assert tasks[0]["priority"] == "Alta"

def test_update_task_status(client):
    web, file = client
    file.write_text(json.dumps([{"id": 1, "title": "Task", "description": "", "priority": "Média", "status": "A Fazer"}]))
    web.post("/tasks/1/status", data={"status": "Concluído"})
    assert json.loads(file.read_text())[0]["status"] == "Concluído"

def test_delete_task(client):
    web, file = client
    file.write_text(json.dumps([{"id": 1, "title": "Task", "description": "", "priority": "Média", "status": "A Fazer"}]))
    web.post("/tasks/1/delete")
    assert json.loads(file.read_text()) == []
