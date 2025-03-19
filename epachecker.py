import argparse

from requests_ntlm import HttpNtlmAuth
from utils import CustomHttpNtlmAuth, ntlm_auth

parser = argparse.ArgumentParser(description="EPAChecker")
parser.add_argument('-u', '--url', required=True, help='URL (e.g. https://<ca server>/certsrv/)')
parser.add_argument('-d', '--domain', required=True, help='domain')
parser.add_argument('-U', '--username', required=True, help='username')
parser.add_argument('-p', '--password', required=True, help='password')
args = parser.parse_args()

url = args.url
username = args.domain + "\\" + args.username
password = args.password

# arg check
if not url.startswith("https"):
    print("[-] url should be https!!")
    exit(0)

# main
# normal ntlm auth
ntlm_auth(url, HttpNtlmAuth(username, password))

# overwrite certificate_hash to check if EPA is enabled
# If EPA is enabled, auth should fail bacause of this overwrite
ntlm_auth(url, CustomHttpNtlmAuth(username, password))