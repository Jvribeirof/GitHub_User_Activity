import urllib.request
import json
from sys import argv
import os

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    url = f'https://api.github.com/users/{argv[1]}/events'
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            json_data = json.loads(data)
    except:
        print('ERROR: Please, select a correct user repository')
    listed_actions = {
        'PushEvent': pushEvent,
        'CreateEvent': createEvent,
        'ForkEvent': forkEvent,
        'IssuesEvent': issueEvent,
        'WatchEvent': watchEvent,
        'DeleteEvent': deleteEvent,
        'PullRequestEvent': pullRequestEvent
    }

    for action in json_data:
        try:
            listed_actions[action['type']](action)
        except:
            print(f"-> {action['type']} in {action['repo']['name']}")
def pushEvent(json_data):
    print(f"-> Pushed {len(json_data['payload']['commits'])} commits in {json_data['repo']['name'][11:]}")
def createEvent(json_data):
    print(f"-> {json_data['payload']['ref_type'].upper()}({json_data['payload']['ref']}) was created in {json_data['repo']['name'][11:]}")
def issueEvent(json_data):
    print(f"-> Issue created in {json_data['repo']['name'][11:]}")
def forkEvent(json_data):
    print(f"-> Forking {json_data['repo']['name'][11:]}")
def watchEvent(json_data):
    print(f"-> Watching {json_data['repo']['name'][11:]}")
def deleteEvent(json_data):
    print(f"-> {json_data['payload']['ref_type'].upper()}({json_data['payload']['ref']}) was deleted in {json_data['repo']['name'][11:]}")
def pullRequestEvent(json_data):
    print(f"-> Pull Request({json_data['payload']['pull_request']['title']}) in {json_data['repo']['name'][11:]}")

if __name__ == '__main__':
    main()