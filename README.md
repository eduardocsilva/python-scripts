# Python Scripts

This repository contains a small collection of Python scripts that I've developed.

Feel free to use, fix or suggest improvements for any of them.

### Github

This script, at the moment, allows a user to automate the process of a repository setup in Github (i.e. creating a local repository, creating a Github repository, linking them up and initializing a README and LICENSE files).

In order for this script to work, a **_config.json_** file should be setup in the same directory as the script, so each user can configure their credentials and other information, containing the following structure:

|Field|Description|
|:-|-:|
|**username**|Github username. |
|**token**|Github access token<br>([here's a tutorial on how to create one](https://docs.github.com/en/enterprise/2.15/user/articles/creating-a-personal-access-token-for-the-command-line)).|
|**description**|Repository description.|
|**readme-content**|README content, besides the repository name and <br>description which will be included in the README header.|

**Example:**

```json
{
    "username": "steve_jobs",
    "token": "j7uyhs3urxqngqe8eb9ephwhn3k9uya10l83bazh",
    "description": "Repository created using a Python script.",
    "readme-content": "Further information should be added later."
}
```

### Tree

This is a simple script, that mimics the well-known **_Tree_** command, displaying the directory structure of the current path (i.e. files and directories).

**Example:**

```
- Tree
    - PyTree.py
- LICENSE
- README.md
- Github
    - config.json
    - Github.py
```
