"""Changing your python version"""

"""Install pyenv on your system."""
#   In CMD admin mode:
#   choco install pyenv-win
"""Using pyenv, check the current version of the global and local interpreter"""
#   Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
#   pyenv versions
"""No local version should be available!"""
"""Check the path to the interpreter with which python – You should see someshims!"""
#   where python
"""Check the version of python with python -V"""
#   python -V
"""How many different version of python can you install?"""
"""Tip: use the pipe operator and wc -l in your shell"""
"""The number should be north of 700"""
#   pyenv install --list | Measure-Object -line
"""Install python 3.5 (specifying 3.5 is enough for pyenv to download the latest 3.5 version, 3.5.10)"""
#       above doesn't work, and there is no 3.5.10
#       pyenv install -l | findstr 3.5
#   pyenv install 3.5.4
"""Create a new directory, move in, and specify a local 3.5 version for this directory"""
#   mkdir my_project
#   cd my_project
#   pyenv local 3.5.4
"""Check the local version of the interpreter again"""
#   python -V
"""run ls -a: you should have a .python-version file, which configures the interpreter 
for this directory. Read it (it’s short!)"""
#   echo 3.5.4 > .python-version
"""Check the output of python -V – it should be 3.5.10, and probably lower than what you 
got at step 2 (else, it is time to update your system!)."""
"""Within your new directory, create a virtual environment and activate it."""
#   python -m venv testEnv
#       testEnv/Scripts/activate.bat
"""Install pandas with pip"""
#   pip install pandas
"""List the packages. Given the previous tasks, what can you say about pandas and numpy, 
and by extension about other packages?"""
#   pip list
"""Using pip, force installing pandas 2.1.1. What happens?"""
#   pip install pandas==2.1.1
"""Deactivate your environment and remove the .python-version file and check the python version. 
It should match your system version."""
#       deactivate
#       del .python-version
#       python -V
"""Reactivate your environment. Check the python version. It should stay on 3.5.10! 
Your environment remembers the interpreter it was created with."""
#       myenv\Scripts\activate
#       python - V
"""Remark: Removing .python-version file in your project folder is not recommended - this is 
for illustration purpose only!"""
