
# Git stats

This is a python script that can be used to determine quickly how much porcentage of the code in a repo was made by each memeber of the team.


## Demo

Insert gif or link to demo

```bash
$ gitstats

------------------------
Contributions by author:

ignacio de souza albores ---> ( 37.59% )
nicolasestefan ---> ( 30.25% )
santiago lopez de haro ---> ( 17.14% )
victoria firpo pessolano ---> ( 9.89% )
federico ---> ( 5.14% )
------------------------
```
## Define an alias for linux terminal

Clone the project

```bash
  git clone https://github.com/SantiagoLopezDeharo/git-stats.git
```

Go to the project directory

```bash
  cd git-stats
```

Install dependencies

```bash
  chmod -x gitstats.py
```

create the alias

For Bash:

```bash
echo 'alias gitstats="python3 ~/git-stats/gitstats.py"' >> ~/.bashrc
```
For Zsh:

```bash
echo 'alias git-contrib="python3 ~/git-stats/gitstats.py"' >> ~/.zshrc
```

close the terminal and open it again, and DONE !

For updates simply go back to the git-stats folder and ejecute "git pull", and the alias with update automatically.
