# Imports

import pyperclip as pyclip
import pickle as pkl
from IEM import confirm, int_input


# File Data

name = "Reporte Erika"
author = "Geeky_Barista"
author_email = "rodrigo.mcuadrada@gmail.com"
description = "Pequeño archivo para elaborar reportes de ventas"


# Functions


def load_report():
    try:
        report = pkl.load(open('Report.data', 'rb'))
    except FileNotFoundError:
        report = []
        pkl.dump(report, open('Report.data', 'wb'))
    finally:
        return report


def save_report(report):
    pkl.dump(report, open("Report.data", "wb"))


def edit_report():
    """This Function will create a new report"""
    i = int_input("How many report items? ")
    report_items = [input("Report Item Name: ") for _ in range(i)]
    for report in report_items:
        print(report)
    if confirm():
        save_report(report_items)


def get_report():
    report = load_report()

    report_data = []
    for report_item in report:
        report_data.append(int_input("{}: ".format(report_item)))

    final_report = []
    for i, item in enumerate(report):
        final_report.append("*{}:* {}".format(item, report_data[i]))

    super_final_report = "Buenas Noches Reporte de *Centtral Interlomas*\n"
    super_final_report += "\n".join(final_report)

    pyclip.copy(super_final_report)
    print("Copied to Clipboard!")


def menu():
    while True:
        print("Please Select one of the following!")
        print("1. Edit Report\n2. Get Report")
        menu_selection = int_input("Select Option: ")
        if menu_selection == 1:
            edit_report()
        elif menu_selection == 2:
            get_report()
            break
        else:
            print("Invalid selection, please try again...")

# Main Code


menu()
