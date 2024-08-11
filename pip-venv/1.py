"""Playing with pip in a virtual environment"""

"""Create a virtual environment with the system interpreter"""
# 	python -m venv testEnv
"""Activate the environment and list the available packages with pip"""
# 	    testEnv/Scripts/activate.bat
"""Install the package for dotenv"""
"""Go on PyPi and search for dotenv. The first result is probably not what you want. Look at the last udpate dates."""
"""warning the name of the python’s module (‘dotenv’) does not always match the name of the PyPi package!"""
"""warning always go on PyPi and check what you are downloading!"""
"""Looking at the results, install python-dotenv"""
# 	pip install python-dotenv
"""List the available packages"""
# 	pip list
"""Install flask and list available packages. See how flask’s dependencies have been pulled in."""
# 	pip install flask
# 	pip list
"""Uninstall both dotenv and flask. List the packages. What happened ?!"""
# 	pip uninstall python-dotenv flask -y
"""Get the frozen list of package from pip. Compare it to the list of all available packages (you should have 2 less packages in it!)"""
# 	pip freeze > requirements.txt
"""Tip: use a shell redirection with > to create a file"""
"""Uninstall all the packages from the frozen list using the -r flag of pip"""
# 	pip uninstall -r requirements.txt -y
"""List the available packages. It should be the same as step 2."""
# 	pip list
"""Deactivate the environment"""
# 	    deactivate
