import json


class TestDispatcher():
    """
    This is class for mapping the pytest file to the corresponding test config file
    """
    def __init__(self):
        """
        In this constructor method test selection and mapping file select_test.json is opened
        and json format is converted to python dict made as object attribute
        """
        with open("select_test.json") as f:
            self.test_config = json.load(f)

    def get_test_config(self, f_test_file):
        """
        :Algoritham
            1. separate out pytest file name without ".py"
            2. Traverse through the test selection and mapping data structure constructed in above method.
            3. Find the feature type and test config file required for a pytest file.
            4. Test config file is converted into dictionary
        :param f_test_file:
        :return: test_config
        """
        test_file = f_test_file.replace(".py", "")
        for feature, test_info in self.test_config.items():
            if test_file in test_info["test_files"]:
                test_config_file = test_info["test_conf"] + '.json'
                with open(test_config_file) as f:
                    test_config = json.load(f)
                return test_config
