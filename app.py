from flask import Flask
from github import Github
import base64
import json
import sys

app = Flask(__name__)

@app.route('/')
def devenv():
    output = getDataFromGit("dev")
    return output

@app.route('/test')
def testenv():
    output = getDataFromGit("test")
    return output

def getDataFromGit(env):

    commandLineInput = ((sys.argv[1]).split("/"))
    commandLineInput.reverse()
    repositoryName = commandLineInput[0]
    userName = commandLineInput[1]

    try:

        repo = Github().get_user(userName).get_repo(repositoryName)

        fileName = env + "-config.json"
        output = ""
        try:
            decodedJsonString = base64.b64decode(repo.get_contents(fileName).content)
            config = json.loads(decodedJsonString)
            try:
                first_number = config["first_number"]
                second_number = config["second_number"]
                operation = config["operation"]

                output += "message : " + config["welcome_message"] + "<br />"
                output += "first_number : " + str(first_number) + "<br />"
                output += "second_number : " + str(second_number) + "<br />"
                output += "operation : '" + operation + "'<br />"
                output += "result : " + str(operations(first_number, second_number, operation)) + "<br />"
            except:
                output = "One or more values needed for calculator app was not found in the json file.<br/> Required Values : welcome_message,first_number,second_number,operation"
        except:
            output = "cannot find the config json in the repository"
    except:
        output = "Cannot find the github repository"

    return output

def operations(x,y,op):
    if(op=='+'):
        return x+y
    elif(op=='-'):
        return x-y
    elif (op == '*'):
        return x*y
    else:
        return x/y

if __name__ == '__main__':
    app.run()
