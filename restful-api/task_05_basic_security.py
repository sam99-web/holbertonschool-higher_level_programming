from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configuration JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-in-production"

# Initialisation des extensions
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# --------------------------------------------------------
# Données utilisateurs en mémoire
# --------------------------------------------------------
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# --------------------------------------------------------
# Basic Authentication
# --------------------------------------------------------
@auth.verify_password
def verify_password(username, password):
    """Vérifie le username et le mot de passe hashé."""
    if username in users and check_password_hash(
            users[username]["password"], password):
        return username
    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Route protégée par Basic Auth."""
    return "Basic Auth: Access Granted"


# --------------------------------------------------------
# JWT Authentication
# --------------------------------------------------------
@app.route("/login", methods=["POST"])
def login():
    """Connexion : retourne un token JWT si les credentials sont valides."""
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    if username not in users or not check_password_hash(
            users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Inclure le rôle dans le token
    access_token = create_access_token(
        identity=username,
        additional_claims={"role": users[username]["role"]}
    )
    return jsonify({"access_token": access_token}), 200


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Route protégée par JWT."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Route accessible uniquement aux admins."""
    from flask_jwt_extended import get_jwt
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


# --------------------------------------------------------
# Gestionnaires d'erreurs JWT (retournent tous 401)
# --------------------------------------------------------
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_data):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_data):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_data):
    return jsonify({"error": "Fresh token required"}), 401


# --------------------------------------------------------
if __name__ == "__main__":
    app.run()