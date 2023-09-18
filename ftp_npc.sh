#!/bin/bash

# FTP login details
FTP_HOST="your_ftp_host"
FTP_USER="your_ftp_user"
FTP_PASS="your_ftp_password"

# File to download
REMOTE_FILE="remote_file_to_download"
LOCAL_FILE="local_destination_file"

# FTP login and download
ftp -n $FTP_HOST <<END_SCRIPT
quote USER $FTP_USER
quote PASS $FTP_PASS
get $REMOTE_FILE $LOCAL_FILE
quit
END_SCRIPT
