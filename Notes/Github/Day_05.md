## Starting Github and pushing the day till today

PS D:\AgenticAI_Journey> git config --global user.name "Lokesh Rajiv"
PS D:\AgenticAI_Journey> git config --global user.email "lokeshrajeev7864@gmail.com"
PS D:\AgenticAI_Journey> git config --list
diff.astextplain.textconv=astextplain
filter.lfs.clean=git-lfs clean -- %f
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
http.sslbackend=schannel
core.autocrlf=true
core.fscache=true
core.symlinks=false
pull.rebase=false
credential.helper=manager
credential.https://dev.azure.com.usehttppath=true
init.defaultbranch=master
PS D:\AgenticAI_Journey> git init
Initialized empty Git repository in D:/AgenticAI_Journey/.git/
PS D:\AgenticAI_Journey> git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        01_Python_Fundamentals/
        Notes/

nothing added to commit but untracked files present (use "git add" to track)
PS D:\AgenticAI_Journey> git add .
PS D:\AgenticAI_Journey> git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   01_Python_Fundamentals/Day01/hello.py
        new file:   01_Python_Fundamentals/Day01/practice.py
        new file:   01_Python_Fundamentals/Day02/practice.py
        new file:   01_Python_Fundamentals/Day02/variables.py
        new file:   Notes/AI_Foundations/Day01_AI_Basics.md
        new file:   Notes/PythonFoundations/Day02_Variables.md

PS D:\AgenticAI_Journey> git commit -m "Day 1 to Day 4 Python Fundamentals"
[master (root-commit) d2da3ac] Day 1 to Day 4 Python Fundamentals
 6 files changed, 84 insertions(+)
 create mode 100644 01_Python_Fundamentals/Day01/hello.py
 create mode 100644 01_Python_Fundamentals/Day01/practice.py
 create mode 100644 01_Python_Fundamentals/Day02/practice.py
 create mode 100644 01_Python_Fundamentals/Day02/variables.py
 create mode 100644 Notes/AI_Foundations/Day01_AI_Basics.md
 create mode 100644 Notes/PythonFoundations/Day02_Variables.md
PS D:\AgenticAI_Journey> git status                                        
On branch master
nothing to commit, working tree clean
PS D:\AgenticAI_Journey> git remote add origin https://github.com/lokesh888-code/AgenticAI-Journey.git
PS D:\AgenticAI_Journey> git remote -v
origin  https://github.com/lokesh888-code/AgenticAI-Journey.git (fetch)
origin  https://github.com/lokesh888-code/AgenticAI-Journey.git (push)
PS D:\AgenticAI_Journey> git push -u origin main
error: src refspec main does not match any
error: failed to push some refs to 'https://github.com/lokesh888-code/AgenticAI-Journey.git'
PS D:\AgenticAI_Journey> git branch -M main
PS D:\AgenticAI_Journey> git branch
* main
PS D:\AgenticAI_Journey> git push -u origin main
Enumerating objects: 12, done.
Counting objects: 100% (12/12), done.
Delta compression using up to 8 threads
Compressing objects: 100% (9/9), done.
Writing objects: 100% (12/12), 2.29 KiB | 782.00 KiB/s, done.
Total 12 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/lokesh888-code/AgenticAI-Journey.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
PS D:\AgenticAI_Journey> 