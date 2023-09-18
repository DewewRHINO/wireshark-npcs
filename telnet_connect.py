import telnetlib
import sys

def telnet_connect(host, port):
    try:
        tn = telnetlib.Telnet(host, port, timeout=10)
        print(f"Connected to {host}:{port}")
        return tn
    except Exception as e:
        print(f"Telnet Connection Error: {str(e)}")
        return None

def telnet_login(tn, username, password):
    try:
        tn.read_until(b"login: ")
        tn.write(username.encode('ascii') + b"\n")
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
        response = tn.read_until(b"$", timeout=10)
        if b"Last login" in response:
            print("Telnet login successful")
        else:
            print("Telnet login failed")
        return tn
    except Exception as e:
        print(f"Telnet Login Error: {str(e)}")
        return None

def main():
    if len(sys.argv) != 4:
        print("Usage: python telnet_connect.py HOST PORT USERNAME PASSWORD")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    username = sys.argv[3]
    password = sys.argv[4]

    tn = telnet_connect(host, port)
    if tn:
        telnet_login(tn, username, password)
        # You can perform other Telnet operations here if needed.

if __name__ == "__main__":
    main()
