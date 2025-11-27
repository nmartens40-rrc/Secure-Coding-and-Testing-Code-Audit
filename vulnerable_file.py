import subprocess
import pickle
import hashlib
import os

API_KEY = "12345-SECRET-KEY"

def run_ping(ip):
    subprocess.call(f"ping {ip}", shell=True)

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def load_data(data):
    return pickle.loads(data)

def save_temp(data):
    with open("/tmp/tempfile.txt", "w") as f:
        f.write(data)

def delete_file(path):
    os.system(f"rm {path}")

if __name__ == "__main__":
    run_ping("8.8.8.8")
    print(hash_password("password123"))
    print(load_data(b"cos\nsystem\n(S'echo dangerous'\ntR."))
    save_temp("test")
    delete_file("test.txt")
