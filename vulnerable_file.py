import subprocess
import pickle
import hashlib
import os

# Hardcoded secret (will trigger B105)
API_KEY = "12345-SECRET-KEY"

# Use of subprocess with shell=True (will trigger B602/B603)
def run_ping(ip):
    subprocess.call(f"ping {ip}", shell=True)

# Use of insecure hash algorithm MD5 (will trigger B303)
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# Loading pickle from untrusted data (will trigger B301)
def load_data(data):
    return pickle.loads(data)

# Use of /tmp insecure temporary file (will trigger B108)
def save_temp(data):
    with open("/tmp/tempfile.txt", "w") as f:
        f.write(data)

# Use of os.system (will trigger B605)
def delete_file(path):
    os.system(f"rm {path}")

if __name__ == "__main__":
    run_ping("8.8.8.8")
    print(hash_password("password123"))
    print(load_data(b"cos\nsystem\n(S'echo dangerous'\ntR."))
    save_temp("test")
    delete_file("test.txt")
