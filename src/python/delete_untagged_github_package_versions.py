#!/usr/bin/python3 -B
# delete_untagged_github_package_versions.py

import os
import sys
import json
import requests
from requests.auth import HTTPBasicAuth


GH_TOKEN = os.environ['GH_TOKEN']

user = sys.argv[1]
package = sys.argv[2]

response = requests.get(f'https://api.github.com/user/packages/container/{package}/versions', auth=HTTPBasicAuth(user, GH_TOKEN))

(requests.delete(f'https://api.github.com/user/packages/container/{package}/versions/{package_version["id"]}', auth=HTTPBasicAuth(user, GH_TOKEN)) for package_version in json.loads(response.content) if not package_version['metadata']['container']['tags'])

