import yaml
import os
import csv
import pandas as pd



def ymls_l(self):
    DetectionLibrary = []
    for file in os.listdir(self):
        if file.endswith(('.yaml', '.yml')):
            detections = os.path.join(self, file)
            with open(detections, 'r') as rules:
                yaml_data = yaml.safe_load_all(rules)
                for data in yaml_data:
                    DetectionLibrary.append(data)
        else:
            raise TypeError('not yaml file.')
    return DetectionLibrary  # list object with dict: rules yamls
def ymls_w(self):
    with open('test.csv', 'w') as file:
        self = csv.writer(file, delimiter=',')
        new_file = self
        return new_file


class Detections:
    # need to pass yamls into Yml_Loader first.

    def __init__(self, rule_list=None):
        self.rule_list = rule_list
        return

    def key_parser(self, _index):
        # _index = input('which field would you like to search (must be a string):')
        if isinstance(_index, str):
            for i in self.rule_list:
                for key, value in i.items():
                    if _index == key:
                        self.search = value
                        return print(f"self.search is currently: {self.search}")
        else: raise TypeError('input needs to be a string.')

    def add_detection(self, file):
            new_rule = yml_l(file)
            for i in new_rule and i in self:
                if new_rule[i] != self.rule_list[i]: # need to test this.
                    self.rule_list.append(new_rule)
            return self.rule_list

    def pop_detection(self):
        # not ready.
        # end = len(self.rule_list) - 1 # this just pops of however many - 1.
        self.rule_list = self.rule_list.pop()
        return self.rule_list
        # pass

    def rules_to_pandas(self):
        data = pd.DataFrame(self.rule_list)
        return  data

    def show_rules(self):
        for i in self.rule_list:
            print(f'rule: {i}')
        return

    def search_by_type(self, _type):
        if isinstance(_type, str):
            for i in self.rule_list:
                if i['Type'] == _type:
                    result = i
                    return result
                    break
        else: raise TypeError('not a string.')

    def query_by_rule(self):
        pass