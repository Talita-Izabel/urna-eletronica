from ast import parse
import json
import os
from file import File

path = os.getcwd() + "/app/config/env.json"
env = File(path).readJSON()

print(env['password'])