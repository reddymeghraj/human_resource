cur_frm.cscript.salary_date=function(doc,cdt,cdn)
{
	var d=doc.salary_month;
	var arr=d.split("-");
	var month=arr[1];
	var year=arr[0];
	var salary=new Date(d);
	var last_day  = new Date(salary.getFullYear(), salary.getMonth()+1, 0);
	var d1=doc.salary_date;
	var sdate=new Date(d1);
	if(last_day<sdate)
	{
		var emp=doc.engineer;
		frappe.call({
			method:"human_resource.human_resource.doctype.salary_slipdetails.salary_slipdetails.get_attendance",
			args:{emp1:emp,month:month,year:year},
			callback:function(r){
				var doclist = frappe.model.sync(r.message);
				cur_frm.set_value("present_days",doclist[0]);
				cur_frm.set_value("absent_days",doclist[1]);
				cur_frm.set_value("paid_leave",doclist[2]);
				cur_frm.set_value("unpaid_leave",doclist[3]);
				cur_frm.set_value("basic_salary",doclist[4]);
				cur_frm.set_value("salary_of_month",doclist[7]);
				cur_frm.set_value("advance_expense",doclist[6]);
				cur_frm.set_value("expense",doclist[5]);
				cur_frm.set_value("net_salary",doclist[8]);
			}	
		})

	}	
	else
	{
		alert("Salary Sleep Can not be generated");
	}
}