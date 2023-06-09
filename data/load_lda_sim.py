import gdown
import subprocess
url1="https://drive.google.com/uc?id=13goQQ5oE3iSLuFqsn1VMuu8qW1L78jvE"
gdown.download(url1,"csv_tar.tar")
subprocess.run(['tar','-xvf','csv_tar.tar'])
subprocess.run(['rm','csv_tar.tar'])
