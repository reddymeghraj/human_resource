cur_frm.cscript.mobile=function(doc,cdt,cdn){
	var mobile=doc.mobile;
	var len=mobile.length;
	if(len!=10)
	{
		msgprint("Enter 10 Digit Mobile Number");
		cur_frm.set_value("mobile",'');
	}
}