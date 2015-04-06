# Copyright (c) 2013, wayzontech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class SalarySlipdetails(Document):
	pass
@frappe.whitelist()
def get_attendance(emp1,month,year):
	query=frappe.db.sql("""select count(d.status) as present_days from `tabAttendance Sheet` a ,`tabAttendance Details` d where a.name=d.parent and employee=%s  and MONTH(d.date)=%s and YEAR(d.date)=%s and d.status='Present' """,(emp1,month,year))
	query1=frappe.db.sql("""select count(d.status) from `tabAttendance Sheet`a ,`tabAttendance Details` d where a.name=d.parent and employee=%s and MONTH(d.date)=%s and YEAR(d.date)=%s and d.status='Absent'""",(emp1,month,year))
	query2=frappe.db.sql("""select count(d.status) from `tabAttendance Sheet`a ,`tabAttendance Details` d where a.name=d.parent and employee=%s and MONTH(d.date)=%s and YEAR(d.date)=%s and d.status='Paid Leave'""",(emp1,month,year))
	query3=frappe.db.sql("""select count(d.status) from `tabAttendance Sheet`a ,`tabAttendance Details` d where a.name=d.parent and employee=%s and MONTH(d.date)=%s and YEAR(d.date)=%s and d.status='Unpaid Leave'""",(emp1,month,year))
	query4=frappe.db.sql("""select basic_salary from `tabEmployee` where name=%s""",emp1)
	query5=frappe.db.sql("""select sum(daily_charges),sum(advance_amount),sum(other_expenses) from `tabDaily Report` where engineer=%s and MONTH(date)=%s and YEAR(date)=%s""",(emp1,month,year))
	if query5[0][0]:
		exp=int(query5[0][0])+int(query5[0][2])
		aexp=int(query5[0][1])
	else:	
		exp=0
		aexp=0
	query6=frappe.db.sql("""select sum(daily_charges),sum(advance_amount),sum(other_expences) from `tabCustomer` where engineer_name=%s and MONTH(date)=%s and YEAR(date)=%s""",(emp1,month,year))
	if query6[0][0]:
		exp1=query6[0][0]+query6[0][2]
		aexp1=query6[0][1]
	else:
		exp1=0
		aexp1=0	
	expenses=exp+exp1
	advnce_expence=aexp+aexp1
	pdsal=query4[0][0]/26
	sal=pdsal*(query[0][0]+query2[0][0])
	salary=sal+(expenses-advnce_expence)
	options = list()
	options.append(query[0][0])
	options.append(query1[0][0])
	options.append(query2[0][0])
	options.append(query3[0][0])
	options.append(query4[0][0])
	options.append(expenses)
	options.append(advnce_expence)
	options.append(sal)
	options.append(salary)
	return options