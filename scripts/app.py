from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
from datetime import datetime, timedelta
import json
import os

app = Flask(__name__)

# ---- CONFIG ----
app.config["JWT_SECRET_KEY"] = "supersecretkey123"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
jwt = JWTManager(app)

# ---- BASE DE DONNEES SIMULEE ----
users = [
    {"id": 1, "username": "admin", "password": "admin123", "role": "admin"},
    {"id": 2, "username": "alice", "password": "alice123", "role": "user"},
    {"id": 3, "username": "bob", "password": "bob123", "role": "user"},
]

devices = [
    {"id": 1, "name": "PC0", "ip": "192.168.1.10", "status": "online"},
    {"id": 2, "name": "PC1", "ip": "192.168.1.11", "status": "online"},
    {"id": 3, "name": "PC2", "ip": "192.168.1.12", "status": "offline"},
]

# ---- LOGGING ----
LOG_FILE = "../Logs/api_logs.json"
os.makedirs("../Logs", exist_ok=True)

def log_request(endpoint, method, ip, status, user=None, error=None):
    log = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "endpoint": endpoint,
        "method": method,
        "ip": ip,
        "status": status,
        "user": user,
        "error": error
    }
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            try:
                logs = json.load(f)
            except:
                logs = []
    logs.append(log)
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

# ---- AUTH ----
@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = next((u for u in users if u["username"] == username and u["password"] == password), None)

    if not user:
        log_request("/api/login", "POST", request.remote_addr, 401, error="Invalid credentials")
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity=username, additional_claims={"role": user["role"]})
    log_request("/api/login", "POST", request.remote_addr, 200, user=username)
    return jsonify({"token": token, "role": user["role"]}), 200

# ---- DEVICES CRUD ----
@app.route("/api/devices", methods=["GET"])
@jwt_required()
def get_devices():
    user = get_jwt_identity()
    log_request("/api/devices", "GET", request.remote_addr, 200, user=user)
    return jsonify(devices), 200

@app.route("/api/devices/<int:device_id>", methods=["GET"])
@jwt_required()
def get_device(device_id):
    user = get_jwt_identity()
    device = next((d for d in devices if d["id"] == device_id), None)
    if not device:
        log_request(f"/api/devices/{device_id}", "GET", request.remote_addr, 404, user=user, error="Device not found")
        return jsonify({"error": "Device not found"}), 404
    log_request(f"/api/devices/{device_id}", "GET", request.remote_addr, 200, user=user)
    return jsonify(device), 200

@app.route("/api/devices", methods=["POST"])
@jwt_required()
def create_device():
    user = get_jwt_identity()
    claims = get_jwt()
    if claims.get("role") != "admin":
        log_request("/api/devices", "POST", request.remote_addr, 403, user=user, error="Admin only")
        return jsonify({"error": "Admin access required"}), 403
    data = request.get_json()
    new_device = {
        "id": len(devices) + 1,
        "name": data.get("name"),
        "ip": data.get("ip"),
        "status": data.get("status", "online")
    }
    devices.append(new_device)
    log_request("/api/devices", "POST", request.remote_addr, 201, user=user)
    return jsonify(new_device), 201

@app.route("/api/devices/<int:device_id>", methods=["PUT"])
@jwt_required()
def update_device(device_id):
    user = get_jwt_identity()
    claims = get_jwt()
    if claims.get("role") != "admin":
        log_request(f"/api/devices/{device_id}", "PUT", request.remote_addr, 403, user=user, error="Admin only")
        return jsonify({"error": "Admin access required"}), 403
    device = next((d for d in devices if d["id"] == device_id), None)
    if not device:
        return jsonify({"error": "Device not found"}), 404
    data = request.get_json()
    device.update(data)
    log_request(f"/api/devices/{device_id}", "PUT", request.remote_addr, 200, user=user)
    return jsonify(device), 200

@app.route("/api/devices/<int:device_id>", methods=["DELETE"])
@jwt_required()
def delete_device(device_id):
    user = get_jwt_identity()
    claims = get_jwt()
    if claims.get("role") != "admin":
        log_request(f"/api/devices/{device_id}", "DELETE", request.remote_addr, 403, user=user, error="Admin only")
        return jsonify({"error": "Admin access required"}), 403
    global devices
    device = next((d for d in devices if d["id"] == device_id), None)
    if not device:
        return jsonify({"error": "Device not found"}), 404
    devices = [d for d in devices if d["id"] != device_id]
    log_request(f"/api/devices/{device_id}", "DELETE", request.remote_addr, 200, user=user)
    return jsonify({"message": "Device deleted"}), 200

# ---- LOGS DASHBOARD ----
@app.route("/api/logs", methods=["GET"])
@jwt_required()
def get_logs():
    user = get_jwt_identity()
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    else:
        logs = []
    return jsonify(logs), 200

# ---- MAIN ----
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000, ssl_context=("scripts/cert.pem", "scripts/key.pem"))