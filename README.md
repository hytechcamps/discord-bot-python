# Python Hy-Tech Camp
This course introduces programming using the [Python](https://www.python.org/) programming language. The intended audience is students who have not not had prior programming experience. The first day introduces some of the basic concepts used in Python, and the second day shows students how to create a [Discord](https://discordapp.com/developers/docs/intro) bot using Python.

## Overview
### Day One
- Icebreaker activity - Lines and Blobs
- Lecture - PowerPoint presentation with code examples
- Follow-Along Coding Activity
- Kahoot Quiz
- Individual Coding Exercises
- Challenges
- Show Discord Bot (briefly)

### Day Two
- Review Kahoot Quiz
- Setup Discord Bot
- Follow-Along Coding - Build from starter code
- Individual Coding Exercises - Continue building from starter code
- Challenges


## Software Requirements
- Python 3.5+
    - *note: during installation, the option should be set to add Python to the PATH variable*
- Visual Studio Code
- Python extension for VS Code: `ms-python.python`
- Code Runner extension for VS Code: `formulahendry.code-runner`
    - *note: this extension is not strictly necessary, but can be a useful utility*
- discord.py library for Python: `pip install discord.py`


## Getting Started
### 1. Cloning the Repository
- First, install Git from here: `\\onbase.net\shares\PublicApps\Applications\DeveloperApps\GIT`

>>>
**Note:** If this is the first time you've used GitLab, you may need to generate an SSH key. A guide can be found [here](https://gitlab.hylandqa.net/help/ssh/README). You should be able to access GitLab [here](https://gitlab.hylandqa.net/).
>>>

>>>
**Note:** You may need to use CMD as administrator in order to run these commands.
>>>

- Once you have Git installed, and your SSH key ready to go, open up Git Bash. Navigate to the folder where you want to clone the repository, and run the following command:

```bash
    git clone git@gitlab.hylandqa.net:tech-outreach/hy-tech-camps/python.git
```

Now all the content within the repository should be available locally!

### 2. Installing Python
- Install Python 3.6.1 from here: `\\onbase.net\shares\PublicApps\Applications\Python\3.6.1`

- Install `pip` using the `get-pip.py` script [here](https://bootstrap.pypa.io/get-pip.py):

```
    python get-pip.py
```

- Install the `discord.py` library with `pip` by running the following command:

```
    pip install discord.py
```

### 3. Using Visual Studio Code
- Install VS Code from here: `\\onbase.net\shares\PublicApps\Applications\DeveloperApps\Visual Studio Code\1.17.2`
- Open VS Code, and open the Extensions pane with `Ctrl+Shift+X`
- Find and install the Python extension (`ms-python.python`)
- File -> Open Folder and select the folder where the repository was cloned (should include a `.vscode` directory)

Now, you should be able to open a Python file in the editor, open the Debug pane, and click the "Start Debugging" button to run the file!

### 4. Making Changes
There are a few ways to make changes to the content in the repository.

#### Command Line
If you're a git pro, you can do everything the old-fashioned way.

#### VS Code Git Integration
If you open the SCM Pane, you can see all the changes currently saved in your local clone of the repository. Here, you should be able to view the diffs between your local version and the master version. You can then stage changes for a specific file using the plus button, enter a message, and commit those changes to your local repo using the checkmark button. To pull and push from the remote master repo, there is a "Synchronize Changes" button in the blue bar at the bottom right of VS Code. The image looks like a refresh icon. This will pull down the latest changes from the master repo, AND push up any local changes you have committed.

#### Web Interface
You can edit files right from the web! This is especially useful when swapping out versions of presentations, or updating markdown files (like this one!). It's fairly intuitive. 