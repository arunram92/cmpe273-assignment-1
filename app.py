from flask import Flask
from github import Github
import base64
import sys

app = Flask(__name__)

@app.route('/')
def home():
    output = "Please use the format /v1/your file name"
    return output

@app.route('/v1/')
def v1():
    output = "Please use the format /v1/your file name"
    return output

@app.route('/v1/<fileName>')
def devenv(fileName):
    output = getDataFromGit(fileName)
    return output

def getDataFromGit(fileName):

    commandLineInput = ((sys.argv[1]).split("/"))
    commandLineInput.reverse()
    repositoryName = commandLineInput[0]
    userName = commandLineInput[1]
    print userName
    print repositoryName
    try:

        repo = Github().get_user(userName).get_repo(repositoryName)

        output = ""
        try:
            decodedJsonString = base64.b64decode(repo.get_contents(fileName).content)
            output = decodedJsonString
        except:
            output = "cannot find the config file '" +fileName+ "' in the repository '"+repositoryName+"'"
    except:
        output = "Cannot find the github repository"

    return output

if __name__ == '__main__':
    app.run()
