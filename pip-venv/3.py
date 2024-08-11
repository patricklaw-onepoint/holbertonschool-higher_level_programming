"""Playing with requirements in several environments"""

"""Create and activate a new fresh environment"""
# 	python -m venv testEnv
# 	    testEnv/Scripts/activate.bat
"""Install requests 2.30.0 and pandas 2.1.1"""
# 	pip install requests==2.30.0 pandas==2.1.1
"""Create a requirements.txt file with pip freeze command"""
# 	pip freeze > requirements.txt
"""Create and activate another new fresh environment"""
# 	deactivate
# 	python -m venv testEnv2
# 	    testEnv2/Scripts/activate.bat
"""Install the packages using the same requirements.txt file as step 2"""
# 	pip install -r requirements.txt
"""Upgrade requests."""
# 	pip install --upgrade requests
"""Have a good look at the command line output and see how pip identifies 
already satisfied dependencies"""
"""Check the list of packages"""
# 	pip list
"""Go back in the previous environment, and check the list of packages. 
See how we can have two different versions of requests!"""
# 	deactivate
# 	    python -m venv testEnv
# 	pip list
