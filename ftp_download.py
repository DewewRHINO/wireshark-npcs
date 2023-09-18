from ftplib import FTP
import os
import sys

def ftp_download_dir(ftp, remote_dir, local_dir):
    try:
        # Create local directory if it doesn't exist
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)

        # Change remote directory
        ftp.cwd(remote_dir)

        # List files and directories in the current remote directory
        remote_items = ftp.nlst()

        for item in remote_items:
            local_item = os.path.join(local_dir, item)

            if ftp.nlst(item) == []:
                # If it's a file, download it
                with open(local_item, "wb") as f:
                    ftp.retrbinary("RETR " + item, f.write)
                print(f"Downloaded {item} to {local_item}")
            else:
                # If it's a directory, recurse into it
                ftp_download_dir(ftp, item, local_item)

        # Go back up one level in the remote directory hierarchy
        ftp.cwd("..")

    except Exception as e:
        print(f"FTP Download Error: {str(e)}")

def main():
    if len(sys.argv) != 6:
        print("Usage: python ftp_download_dir.py FTP_HOST FTP_USER FTP_PASS FTP_REMOTE_DIR FTP_LOCAL_DIR")
        sys.exit(1)

    ftp_host = sys.argv[1]
    ftp_user = sys.argv[2]
    ftp_pass = sys.argv[3]
    ftp_remote_dir = sys.argv[4]
    ftp_local_dir = sys.argv[5]

    try:
        ftp = FTP(ftp_host)
        ftp.login(ftp_user, ftp_pass)
        ftp_download_dir(ftp, ftp_remote_dir, ftp_local_dir)
        ftp.quit()
    except Exception as e:
        print(f"FTP Connection Error: {str(e)}")

if __name__ == "__main__":
    main()
