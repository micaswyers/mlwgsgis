import csv
import re

import phonenumbers


class GradYearMissingError(Exception):
    pass

class CSVMissingError(Exception):
    pass


def get_names_numbers(csvfile=None, grad_year=None):
    """Parses a CSV file and returns a list of (first_name, number) tuples"""

    if csvfile is None:
        raise CSVMissingError("No csv file specified.")
    if grad_year is None:
        raise GradYearMissingException("No grad year specified for texting alumni.")
    names_numbers_list = []
    with open(csvfile, 'rb') as readfile:
        donorlist = csv.reader(readfile, delimiter=',')
        for row in donorlist:
            if row[2] == str(grad_year):
                first_name = row[0].split()[0]
                number = row[4]
                if not number:
                    continue
                else:
                    number = "+1" + re.sub('[()-/\s]', '', number)
                    number_object = phonenumbers.parse(number, None)
                    if not phonenumbers.is_valid_number(number_object):
                        continue
                    names_numbers_list.append((first_name, number))
    return names_numbers_list

if __name__ == "__main__":
    print get_names_numbers('2004nondonors.csv', 2004)
