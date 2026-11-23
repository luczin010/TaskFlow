from flask import Flask, render_template, request, redirect, url_for
from pathlib import Path
import json

app = Flask(__name__)
DATA_FILE = Path(__file__).resolve().parent.parent / "tasks.json"

def load_tasks():
    if not DATA_FILE.exists():
        return []
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))

def save_tasks(tasks):
    DATA_FILE.write_text(json.dumps(tasks, ensure_ascii=False, indent=2), encoding="utf-8")

@app.route("/")
def index():
    tasks = load_tasks()
    columns = {"A Fazer": [], "Em Progresso": [], "Concluído": []}
    for task in tasks:
        columns.setdefault(task.get("status", "A Fazer"), []).append(task)
    return render_template("index.html", columns=columns)

@app.route("/tasks", methods=["POST"])
def create_task():
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    priority = request.form.get("priority", "Média")
    if title:
        tasks = load_tasks()
        tasks.append({
            "id": max([t["id"] for t in tasks], default=0) + 1,
            "title": title,
            "description": description,
            "priority": priority,
            "status": "A Fazer"
        })
        save_tasks(tasks)
    return redirect(url_for("index"))

@app.route("/tasks/<int:task_id>/status", methods=["POST"])
def update_status(task_id):
    status = request.form.get("status")
    allowed = {"A Fazer", "Em Progresso", "Concluído"}
    if status in allowed:
        tasks = load_tasks()
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = status
                break
        save_tasks(tasks)
    return redirect(url_for("index"))

@app.route("/tasks/<int:task_id>/delete", methods=["POST"])
def delete_task(task_id):
    tasks = [task for task in load_tasks() if task["id"] != task_id]
    save_tasks(tasks)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
