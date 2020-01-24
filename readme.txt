
Dependency Modules:
-Python Version 3.6 
-pytest
-pytest-html
-requests
-re
-json
-logging
-os


Usage: 
python -m pytest --html=report_entries.html  test_entries.py
python -m pytest --html=report_random.html  test_random.py
python -m pytest --html=report_category.html  test_category.py
python -m pytest --html=report_categories.html  test_categories.py
python -m pytest --html=report_health.html  test_health.py


Execution Flow:
   1. Run any pytest file as shown in usage.
   2. Dependending on pytest file name, corresponding test config file picked from select_test.json file .
   3. According to the pytest file name, corresponding test config informations are picked.
   4. When all the test setup is done, test are executed according to pytest module.     



