import json

# some JSON:
x = '{"Requirements":"_Noresponse_","Entrypoint":"demo.py","Type":"PythonScript(Default)","Whatyourcodedoes?":"Somemagicisgoinghappened!","Models":"_Noresponse_","Images":"_Noresponse_","Logs":"_Noresponse_","CodeofConduct":"-[X]IagreetofollowthisprojectCodeofConduct"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
if y["Requirements"] == "_Noresponse_":
    req="requirements.txt"
    print("::set-output name=reqs::{" + req + "}")
else:
    print("::set-output name=reqs::{" + y["Requirements"] + "}")
if y["Entrypoint"] == "_No response_":
    ent="main.py"
    print("::set-output name=entrypoint::{" + ent + "}")
else:
    print("::set-output name=entrypoint::{" + y["Entrypoint"] + "}")

