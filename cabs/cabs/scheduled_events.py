import frappe

from frapppe.utils import today, add_days 


def send_insurance_remainder():
    three_days_ahead = add_days(today(),3)
    insurance_renewals = frappe.get_all("Vehicle",filters={"insurance_expiry": three_days_ahead},filters={"insurance_expiry": three_days_ahead},fields=["name","make"])


    for vehicle in insurance_renewals:
        frappe.sendmail(
            recipients=["komalbahade22@navgurukul.org"],
            subject=("Insurance Renewal Remainder"),
            message=("Insurance for {0} expires on {1}").format(vehicle.make, three_days_ahead)

        )
