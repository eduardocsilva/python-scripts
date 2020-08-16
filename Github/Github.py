#!/usr/bin/env python3


import sys
import os
import subprocess
import datetime
import json
import github


"""
    Loads the script configuration object from the corresponding file.
"""
def load_config(config_file_path):
    with open(os.path.dirname(os.path.abspath(__file__)) + "/" + config_file_path, "r") as config_file:
        config_file_data = config_file.read()

    return json.loads(config_file_data)


"""
    Loads the script configuration object with the repository files' content.
    Since this content is generated within the script, I've decided that they
    aren't placed in the configuration JSON file, but that can change in the future.
"""
def load_repo_files_content(config):
    config["readme"] = f"# {repo_name}\n#### {config['description']}\n{config['readme-content']}"

    config["license"] = f"""MIT License

Copyright (c) {datetime.datetime.now().year} {config['username']}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""


"""
    Creates an empty local repository.
"""
def create_local_repo(repo_name, config):
    try:
        subprocess.check_output(["mkdir", repo_name],
                                stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        print("ERROR - A folder with the repository name already exists in the current folder...")
        exit(1)

    os.chdir(f"./{repo_name}")
    os.system("git init >/dev/null 2>&1")
    os.system(f"echo \"{config['readme']}\" >> README.md")
    os.system(f"echo \"{config['license']}\" >> LICENSE")
    os.system("git add . >/dev/null 2>&1")
    os.system("git commit -m \"Initial Commit\" >/dev/null 2>&1")


"""
    Authenticates with the Github API and returns the user object.
"""
def auth_github(config):
    g = github.Github(config["token"])
    return g.get_user()


"""
    Creates the remote repository on Github.
"""
def create_github_repo(repo_name, config):
    try:
        user.create_repo(repo_name,
                         allow_rebase_merge=True,
                         auto_init=False,
                         description=config['description'],
                         has_issues=True,
                         has_projects=False,
                         has_wiki=True,
                         private=True)

    except github.GithubException as ex:
        print(
            f"ERROR - {ex.data['message']} ({ex.data['errors'][0]['message']})")
        exit(1)


"""
    Links the local repository to the created Github repository.
"""
def link_local_repo_to_github(config):
    os.system(f"git remote add origin https://{config['username']}:{config['token']}@github.com" +
              f"/{config['username']}/{repo_name}.git >/dev/null 2>&1")
    os.system("git push -u origin master >/dev/null 2>&1")


if __name__ == "__main__":

    # The script requires the name of the repo as an argument
    if len(sys.argv) != 2:
        print("ERROR - Invalid number of arguments...")
        exit(1)

    repo_name = sys.argv[1]
    config = load_config("config.json")
    load_repo_files_content(config)
    create_local_repo(repo_name, config)
    user = auth_github(config)
    create_github_repo(repo_name, config)
    link_local_repo_to_github(config)

    print("Repository successfully created and linked to Github!")
