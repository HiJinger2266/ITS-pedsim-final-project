# Git

## basic

first thing first, clone the repo:  
```bash
cd <your_working_directory>
git clone
```

then, create a new branch:  
```bash
git checkout -b <branch_name>
```

push your branch to remote:  
```bash
git push -u origin <branch_name>
```

pull from remote: (always pull before you start working)
```bash
git pull
```

## commit & push 

add files to commit:  
```bash
git add <file_name>
```

commit:  
```bash
git commit -m "<commit_message>"
```

push:  
```bash
git push
```

## merge

add pull request on github, then merge it. (work later)

## flow

*ref: search github flow*

### branches

- master: the main branch, only merge from other branches
- gary_dev: gary's branch, mainly focus on ui
- yuquan_dev: yuquan's branch
- lolo_dev: lolo's branch

merge to master when there's a function done.

# Virtual Environment

use virtual environment to keep track of packages used in the project.

for example using conda:  
open anaconda prompt (press windows key and type anaconda prompt)  
use command:  
```bash
conda create -n <env_name> python=3.9
```
activate environment:  
```bash
conda activate <env_name>
```
install requirements:  
```bash
pip install -r requirements.txt
```

whenever installing new packages, update requirements.txt:  
```bash
pip freeze > requirements.txt
```

# MVC architecture

*ref:https://stackoverflow.com/questions/26698628/mvc-design-with-qt-designer-and-pyqt-pyside*

MVC means Model-View-Controller. It is a design pattern that separates the data from the user interface. The model is the data, the view is the window on the screen, and the controller is the glue between the two. The controller updates the model and the view when the user interacts with the view.

The tree view:
```
ITS-PEDSIM-FINAL-PROJECT/
    main.py              # main application with App class
    main_rc.py           # auto-generated resources file (using pyrcc.exe or equivalent)
    requirements.txt     # list of required packages
    controllers/
        main_ctrl.py        # main controller with MainController class
        other_ctrl.py
    model/
        model.py            # model with Model class
    resources/
        main.qrc         # Qt resources file
        main_view.ui        # Qt designer files
        other_view.ui
        img/
            icon.png
    views/
        main_view.py        # main view with MainView class
        main_view_ui.py     # auto-generated ui file (using pyuic.exe or equivalent)
        other_view.py
        other_view_ui.py
    utils/
        utils.py            # utility functions
```

# Pyinstaller

to pack:
```bash
pyinstaller -D -w -i resources/img/app_icon.ico main.py --clean
```

# resources

compile
```bash
pyrcc5 -o resource_rc.py resources/resource.qrc
```