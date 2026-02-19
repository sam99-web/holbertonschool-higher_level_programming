from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionnaire des utilisateurs (stockage en mémoire)
users = {}


@app.route("/")
def home():
    """Endpoint principal."""
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """Retourne la liste de tous les usernames."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Retourne le statut de l'API."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Retourne les données d'un utilisateur spécifique."""
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Ajoute un nouvel utilisateur."""

    # Vérifier que le JSON est valide
    try:
        new_user = request.get_json(silent=True)
        if new_user is None:
            return jsonify({"error": "Invalid JSON"}), 400
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    # Vérifier que le username est présent
    if "username" not in new_user:
        return jsonify({"error": "Username is required"}), 400

    username = new_user["username"]

    # Vérifier que le username n'existe pas déjà
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Ajouter l'utilisateur
    users[username] = new_user

    return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run()