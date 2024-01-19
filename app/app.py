from flask import Flask, render_template, request, redirect, url_for
import requests
import os


app = Flask(__name__)

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

# api = "http://api:5000/api/tasks"  # Docker Compose
api = "http://myapp-service:5000/api/tasks"  # Kubernetes


@app.route("/")
def home():
    try:
        response = requests.get(api, auth=(username, password))
        tasks = response.json().get("tasks")
        return render_template("index.html", tasks=tasks)
    except:
        return render_template("index.html", error=True)


@app.route("/", methods=["POST"])
def create_task():
    data = {"description": request.form.get("description")}
    requests.post(api, json=data, auth=(username, password))
    return redirect(url_for("home"))


@app.route("/edit/<int:task_id>")
def edit_task(task_id):
    requests.put(f"{api}/{task_id}", auth=(username, password))
    return redirect(url_for("home"))


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    requests.delete(f"{api}/{task_id}", auth=(username, password))
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
