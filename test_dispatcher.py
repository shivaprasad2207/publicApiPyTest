import json


class TestDispatcher():
    def __init__(self):
        with open("select_test.json") as f:
            self.test_config = json.load(f)

    def get_test_config(self, f_test_file):
        test_file = f_test_file.replace(".py", "")
        for feature, test_info in self.test_config.items():
            if test_file in test_info["test_files"]:
                test_config_file = test_info["test_conf"] + '.json'
                with open(test_config_file) as f:
                    test_config = json.load(f)
                return test_config
