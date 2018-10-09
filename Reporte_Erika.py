# Imports

import pyperclip as pyclip
import pickle as pkl
from IEM import confirm, UEIP


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
    """This Function will create a new report """
    i = int(input("How many report items? "))
    report_items = []
    while i > 0:
        report_items.append(input("Report Item Name: "))
        i -= 1
    for report in report_items:
        print(report)
    if confirm():
        save_report(report_items)


def get_report():
    report = load_report()
    report_data = []
    final_report = []
    for report_item in report:
        report_data.append(int(input("{}: ".format(report_item))))
    i = 0
    for item in report:
        x = ("*{}:* {}".format(item, report_data[i]))
        i += 1
        final_report.append(x)
    super_final_report = "Buenas Noches Reporte de *Centtral Interlomas*"
    for report in final_report:
        super_final_report += "\n{}".format(report)
    pyclip.copy(super_final_report)
    print("Copied to Clipboard!")


def menu():
    while True:
        print("Please Select one of the following!")
        print("1.Edit Report\n2.Get Report")
        menu_selection = UEIP("Select Option: ", 0)
        if menu_selection == 1:
            edit_report()
        else:
            get_report()
            break

# Main Code


menu()
