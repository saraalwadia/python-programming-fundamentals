###########################################################
# Virtual Environments and pip in Python
###########################################################


"""
Python allows us to install external packages.

A package is a collection of Python code
created to help us perform specific tasks.

Examples:

- numpy
- pandas
- requests

pip is used to install and manage packages.

Virtual environments allow each project
to have its own packages and dependencies.
"""


# ===========================================================
# PART 1: What is pip?
# ===========================================================


"""
pip is Python's package manager.

We use pip to:

- Install packages
- Remove packages
- View installed packages
- Manage dependencies
"""


# Check pip version:

# pip --version


# ===========================================================
# PART 2: Install a Package
# ===========================================================


"""
To install a package, use:

pip install package_name
"""


# Example:

# pip install numpy


# Another example:

# pip install pandas


# ===========================================================
# PART 3: Import an Installed Package
# ===========================================================


"""
After installing a package,
we can import it into our Python program.
"""


# Example:

import math


print(math.sqrt(25))


# Note:
#
# math is a built-in module.
#
# It does not need pip install.



# ===========================================================
# PART 4: View Installed Packages
# ===========================================================


"""
To see all installed packages:

pip list
"""


# Command:

# pip list



# ===========================================================
# PART 5: Check Package Information
# ===========================================================


"""
To see information about a package:

pip show package_name
"""


# Example:

# pip show numpy



# ===========================================================
# PART 6: Upgrade a Package
# ===========================================================


"""
To upgrade an installed package:

pip install --upgrade package_name
"""


# Example:

# pip install --upgrade numpy



# ===========================================================
# PART 7: Uninstall a Package
# ===========================================================


"""
To remove a package:

pip uninstall package_name
"""


# Example:

# pip uninstall numpy



# ===========================================================
# PART 8: What is a Virtual Environment?
# ===========================================================


"""
A virtual environment is an isolated
Python environment for a project.

Each project can have:

- Its own packages
- Its own package versions
- Its own dependencies


Example:

Project A:

numpy version 1.x


Project B:

numpy version 2.x


Virtual environments allow both projects
to work independently.
"""


# ===========================================================
# PART 9: Create a Virtual Environment
# ===========================================================


"""
Open the terminal inside your project folder.

Create a virtual environment using:
"""


# Windows:

# python -m venv .venv


# The name ".venv" is commonly used
# for the virtual environment folder.



# ===========================================================
# PART 10: Activate Virtual Environment
# ===========================================================


"""
Before installing packages,
activate the virtual environment.
"""


# Windows PowerShell:

# .\.venv\Scripts\Activate.ps1


# Windows Command Prompt:

# .venv\Scripts\activate


# macOS / Linux:

# source .venv/bin/activate



# ===========================================================
# PART 11: Deactivate Virtual Environment
# ===========================================================


"""
To leave the virtual environment:

deactivate
"""


# Command:

# deactivate



# ===========================================================
# PART 12: Install Packages Inside venv
# ===========================================================


"""
After activating the virtual environment,
install packages normally.
"""


# Example:

# pip install numpy


# Example:

# pip install pandas



# ===========================================================
# PART 13: Check Python Environment
# ===========================================================


"""
After activating the environment,
check which Python version is being used.
"""


# Windows:

# where python


# macOS / Linux:

# which python



# ===========================================================
# PART 14: requirements.txt
# ===========================================================


"""
requirements.txt stores the packages
required for a project.

This makes it easier for another developer
to install the same dependencies.
"""


# Create requirements.txt:

# pip freeze > requirements.txt



# Install packages from requirements.txt:

# pip install -r requirements.txt



# ===========================================================
# PART 15: Typical Project Structure
# ===========================================================


"""
my_project/

│
├── .venv/
│
├── main.py
│
├── requirements.txt
│
└── README.md
"""


# ===========================================================
# PART 16: Important .gitignore File
# ===========================================================


"""
Do NOT upload the virtual environment
folder to GitHub.

Instead, add it to .gitignore.
"""


# Add this to .gitignore:

# .venv/


# ===========================================================
# PART 17: Complete Workflow
# ===========================================================


"""
1. Create a project folder.

2. Open the folder in VS Code.

3. Create virtual environment:

    python -m venv .venv

4. Activate the environment.

    Windows PowerShell:

    .\.venv\Scripts\Activate.ps1

5. Install packages.

    pip install package_name

6. Create requirements.txt.

    pip freeze > requirements.txt

7. Add .venv/ to .gitignore.

8. Upload project files to GitHub.
"""


# ===========================================================
# PART 18: Useful Commands Summary
# ===========================================================


"""
Check pip version:

pip --version


Install package:

pip install package_name


List packages:

pip list


Show package information:

pip show package_name


Upgrade package:

pip install --upgrade package_name


Uninstall package:

pip uninstall package_name


Create virtual environment:

python -m venv .venv


Activate PowerShell:

.\.venv\Scripts\Activate.ps1


Deactivate:

deactivate


Save dependencies:

pip freeze > requirements.txt


Install dependencies:

pip install -r requirements.txt
"""


# ===========================================================
# PART 19: Practice Exercises
# ===========================================================


"""
Exercise 1:

Create a new folder called:

python_project


Create a virtual environment inside it.


-----------------------------------------------------------


Exercise 2:

Activate the virtual environment.


Install:

numpy


Check that numpy is installed using:

pip list


-----------------------------------------------------------


Exercise 3:

Create a requirements.txt file.

Use:

pip freeze > requirements.txt


-----------------------------------------------------------


Exercise 4:

Create a .gitignore file.

Add:

.venv/


-----------------------------------------------------------


Exercise 5:

Deactivate the virtual environment.
"""


###########################################################
# END OF VIRTUAL ENVIRONMENTS AND PIP
###########################################################
