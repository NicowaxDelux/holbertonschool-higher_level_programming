#!/usr/bin/python3
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

# Configura la clave secreta para JWT
app.config['JWT_SECRET_KEY'] = 'your_super_secret_key'  # Cambia esto a una clave más segura en producción

jwt = JWTManager(app)
basic_auth = HTTPBasicAuth()

# Diccionario de usuarios con contraseñas hasheadas y roles
users = {
    "admin": {"password": generate_password_hash("adminpassword"), "role": "admin"},
    "user1": {"password": generate_password_hash("password1"), "role": "user"},
    "user2": {"password": generate_password_hash("password2"), "role": "user"}
}

# Verificación de contraseña para Autenticación Básica
@basic_auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return False

# Ruta principal
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask API!"}), 200

# Ruta protegida con Autenticación Básica
@app.route('/basic-protected', methods=['GET'])
@basic_auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"}), 200

# Ruta de Login con JWT
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"msg": "Missing username or password"}), 400

    username = data.get('username')
    password = data.get('password')
    user = users.get(username)

    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity={'username': username, 'role': user['role']})
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad username or password"}), 401

# Ruta protegida con JWT
@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return jsonify({"message": "JWT Auth: Access Granted"})

# Decorador para control de acceso basado en roles
def role_required(role):
    def wrapper(fn):
        @jwt_required()
        def decorator(*args, **kwargs):
            current_user = get_jwt_identity()
            if current_user['role'] != role:
                return jsonify({"msg": "You do not have access to this resource"}), 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper

# Ruta solo para administradores
@app.route('/admin-only', methods=['GET'])
@role_required('admin')
def admin_only():
    return jsonify({"message": "Admin Access: Granted"})

# Manejadores de errores personalizados para JWT
@jwt.unauthorized_loader
def unauthorized_response(callback):
    return jsonify({
        "error": "Authorization required",
        "message": "Request does not contain an access token"
    }), 401

@jwt.invalid_token_loader
def invalid_token_response(callback):
    return jsonify({
        "error": "Invalid token",
        "message": "The token provided is invalid"
    }), 422

@jwt.expired_token_loader
def expired_token_response(callback):
    return jsonify({
        "error": "Token expired",
        "message": "The token has expired"
    }), 401

@jwt.needs_fresh_token_loader
def fresh_token_required_response(callback):
    return jsonify({
        "error": "Fresh token required",
        "message": "The token provided is not fresh"
    }), 401

@jwt.revoked_token_loader
def revoked_token_response(callback):
    return jsonify({
        "error": "Token revoked",
        "message": "The token has been revoked"
    }), 401

@jwt.token_verification_failed_loader
def user_claims_verification_failed_response(callback):
    return jsonify({
        "error": "User claims verification failed",
        "message": "User claims verification failed"
    }), 400

@jwt.revoked_token_loader
def wrong_token_response(callback):
    return jsonify({
        "error": "Wrong token",
        "message": "The token provided is the wrong type"
    }), 422

@jwt.user_identity_loader
def user_loader_error_response(callback):
    return jsonify({
        "error": "User loader error",
        "message": "Error loading the user"
    }), 401

if __name__ == '__main__':
    app.run(debug=True)
