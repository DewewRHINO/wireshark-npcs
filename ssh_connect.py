import paramiko
import sys

def ssh_login(host, username, password):
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(host, username=username, password=password)
        print(f"SSH login successful to {host}")
        ssh_client.close()
    except Exception as e:
        print(f"SSH Login Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python ssh_login.py SSH_HOST SSH_USER SSH_PASSWORD")
        sys.exit(1)

    ssh_host = sys.argv[1]
    ssh_user = sys.argv[2]
    ssh_password = sys.argv[3]

    ssh_login(ssh_host, ssh_user, ssh_password)
