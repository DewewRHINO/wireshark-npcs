from ftplib import FTP
import sys

def ftp_download(host, username, password, remote_file, local_file):
    try:
        ftp = FTP(host)
        ftp.login(username, password)
        ftp.retrbinary("RETR " + remote_file, open(local_file, "wb").write)
        ftp.quit()
        print(f"Downloaded {remote_file} to {local_file}")
    except Exception as e:
        print(f"FTP Download Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python ftp_download.py FTP_HOST FTP_USER FTP_PASS FTP_REMOTE_FILE FTP_LOCAL_FILE")
        sys.exit(1)

    ftp_host = sys.argv[1]
    ftp_user = sys.argv[2]
    ftp_pass = sys.argv[3]
    ftp_remote_file = sys.argv[4]
    ftp_local_file = sys.argv[5]

    ftp_download(ftp_host, ftp_user, ftp_pass, ftp_remote_file, ftp_local_file)
