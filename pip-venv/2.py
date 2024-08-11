"""Manipulating package versions"""

"""Create a virtual environment and activate it."""
# 	python -m venv testEnv
# 	    testEnv/Scripts/activate.bat
"""Install the old 0.21.1 version of dotenv."""
# 	pip install python-dotenv==0.21.1
"""Upgrade dotenv."""
# 	pip install --upgrade python-dotenv
"""Upgrage pip itself!"""
# 	pip install --upgrade pip
"""Install the last version of numpy 1.23.x using == and the character *"""
# 	pip install 'numpy==1.23.*'
"""Ensure you get the version 1.23.5"""
# 	pip list
"""Upgrade numpy to any version after 1.24 , and before 1.26 using only > and <."""
"""You may need to use single quotes if your terminal complains while reading the command!"""
# 	pip install 'numpy>1.24,<1.26'
"""Ensure you get the version 1.25.2"""
# 	pip list
"""Upgrade to the last version of numpy"""
#   pip install --upgrade numpy
"""Deactivate your environment"""
# 	    deactivate
