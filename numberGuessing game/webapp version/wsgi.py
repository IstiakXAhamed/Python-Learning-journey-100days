import sys
import os

# Add your project directory to the sys.path
project_home = '/home/sanim'
if project_home not in sys.path:
    sys.path.append(project_home)

# Import your Flask app
from app import app as application  # Ensure this matches your Flask app variable
