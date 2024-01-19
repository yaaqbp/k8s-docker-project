from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

auth = HTTPBasicAuth()
expected_username = os.getenv("USERNAME")
expected_password = os.getenv("PASSWORD")


@auth.verify_password
def verify_password(username, password):
    if username == expected_username and password == expected_password:
        return username


app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:////data/tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    done = db.Column(db.Boolean, default=False)

    def serialize(self):
        return {
            "id": self.id,
            "description": self.description,
            "done": self.done,
        }


with app.app_context():
    db.create_all()


@app.route("/api/tasks", methods=["GET", "POST"])
@auth.login_required
def get_post_task():
    try:
        if request.method == "GET":
            tasks = Task.query.all()
            return jsonify({"tasks": [t.serialize() for t in tasks]}), 200

        if request.method == "POST":
            task = Task(description=request.json.get("description"))
            db.session.add(task)
            db.session.commit()
            return jsonify({"task": task.description}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/tasks/<int:task_id>", methods=["PUT", "DELETE"])
@auth.login_required
def edit_delete_task(task_id):
    try:
        if request.method == "PUT":
            task = Task.query.get(task_id)
            task.done = not task.done
            db.session.commit()
            return jsonify({"task": task.description}), 200

        if request.method == "DELETE":
            task = Task.query.get(task_id)
            db.session.delete(task)
            db.session.commit()
            return jsonify({"task": task.description}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
