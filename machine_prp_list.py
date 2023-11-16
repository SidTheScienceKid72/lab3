# ECOR 1042 Lab 3 - Template


# Update
__author__ = "Siddarth Jain"
__student_number__ = "101304051"
__team__ = "T040"

#==========================================#
# Place your machine_prp_list function after this line

import string


def machine_prp_list(filename: str, prp: int) -> list[dict]:
    """Return a list of dictionaries containing a list of machines and their
    specifications in key-value pairs. If no prp value is given, the function
    returns an empty list.

    >>> machine_prp_list('machine.csv', 198)
    [ {'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256,
    ...'MMAX': 6000, 'CACH': 256, 'ERP': 199} ]

    >>> machine_prp_list('machine.csv', 220)
    [ {'Vendor': 'amdahl', 'Model': '470v/7a', 'MYCT': 29, 'MMIN': 8000,
    ...'MMAX': 32000, 'CACH': 32, 'ERP': 253} ]

    >>> machine_prp_list('machine.csv', 38)
    [ {'Vendor': 'apollo', 'Model': 'dn320', 'MYCT': 400, 'MMIN': 1000,
    ...'MMAX': 3000, 'CACH': 0, 'ERP': 23} ]
    """
    infile = open(filename, "r")
    final_list = []

    first_line = infile.readline().split(',')
    index = first_line.index('PRP')

    for line in infile:
        split_line = line.split(',')
        if int(split_line[6]) >= prp:
            dic = {first_line[0]: split_line[0], first_line[1]: split_line[1], first_line[2]: int(split_line[2]), first_line[3]: int(
                split_line[3]), first_line[4]: int(split_line[4]), first_line[5]: int(split_line[5]), first_line[7].replace("\n", ""): int(split_line[7])}
            final_list.append(dic)

    infile.close()
    return final_list


# Do not include a main script
