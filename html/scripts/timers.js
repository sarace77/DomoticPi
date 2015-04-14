/**
 * @author Antonio
 */

webiopi().ready(updateUI);
			
function updateUI() {
	webiopi().callMacro("getTimerOff","0",timer0OffCallback);
	webiopi().callMacro("getTimerOff","1",timer1OffCallback);
	webiopi().callMacro("getTimerOff","2",timer2OffCallback);
	webiopi().callMacro("getTimerOff","3",timer3OffCallback);

	webiopi().callMacro("getTimerOn","0",timer0OnCallback);
	webiopi().callMacro("getTimerOn","1",timer1OnCallback);
	webiopi().callMacro("getTimerOn","2",timer2OnCallback);
	webiopi().callMacro("getTimerOn","3",timer3OnCallback);

	webiopi().callMacro("getTimerStatus","0",timer0StatusCallback);
	webiopi().callMacro("getTimerStatus","1",timer1StatusCallback);
	webiopi().callMacro("getTimerStatus","2",timer2StatusCallback);
	webiopi().callMacro("getTimerStatus","3",timer3StatusCallback);
}


function timer0OffCallback(macroName, args, data) {
	var hh = parseInt(data / 3600);
	var mm = parseInt((data - hh * 3600) /60);
	var ss = parseInt(data - hh * 3600 - mm * 60);
	$("#input_hh_timer0_off").val(hh); 
	$("#input_mm_timer0_off").val(mm); 
	$("#input_ss_timer0_off").val(ss); 
}

function timer1OffCallback(macroName, args, data) {
	var hh = parseInt(data / 3600);
	var mm = parseInt((data - hh * 3600) /60);
	var ss = parseInt(data - hh * 3600 - mm * 60);
	$("#input_hh_timer1_off").val(hh); 
	$("#input_mm_timer1_off").val(mm); 
	$("#input_ss_timer1_off").val(ss); 
}

function timer2OffCallback(macroName, args, data) {
	var hh = parseInt(data / 3600);
	var mm = parseInt((data - hh * 3600) /60);
	var ss = parseInt(data - hh * 3600 - mm * 60);
	$("#input_hh_timer2_off").val(hh); 
	$("#input_mm_timer2_off").val(mm); 
	$("#input_ss_timer2_off").val(ss); 
}


function timer3OffCallback(macroName, args, data) {
	var hh = parseInt(data / 3600);
	var mm = parseInt((data - hh * 3600) /60);
	var ss = parseInt(data - hh * 3600 - mm * 60);
	$("#input_hh_timer3_off").val(hh); 
	$("#input_mm_timer3_off").val(mm); 
	$("#input_ss_timer3_off").val(ss); 
}




function timer0OnCallback(macroName, args, data) {
	var hh = parseInt(data / 3600);
	var mm = parseInt((data - hh * 3600) /60);
	var ss = parseInt(data - hh * 3600 - mm * 60);
	$("#input_hh_timer0_on").val(hh); 
	$("#input_mm_timer0_on").val(mm); 
	$("#input_ss_timer0_on").val(ss); 	
}

function timer1OnCallback(macroName, args, data) {
	var hh = parseInt(data / 3600);
	var mm = parseInt((data - hh * 3600) /60);
	var ss = parseInt(data - hh * 3600 - mm * 60);
	$("#input_hh_timer1_on").val(hh); 
	$("#input_mm_timer1_on").val(mm); 
	$("#input_ss_timer1_on").val(ss); 	
}

function timer2OnCallback(macroName, args, data) {
	var hh = parseInt(data / 3600);
	var mm = parseInt((data - hh * 3600) /60);
	var ss = parseInt(data - hh * 3600 - mm * 60);
	$("#input_hh_timer2_on").val(hh); 
	$("#input_mm_timer2_on").val(mm); 
	$("#input_ss_timer2_on").val(ss); 	
}

function timer3OnCallback(macroName, args, data) {
	var hh = parseInt(data / 3600);
	var mm = parseInt((data - hh * 3600) /60);
	var ss = parseInt(data - hh * 3600 - mm * 60);
	$("#input_hh_timer3_on").val(hh); 
	$("#input_mm_timer3_on").val(mm); 
	$("#input_ss_timer3_on").val(ss); 	
}






function timer0StatusCallback(macroName, args, data) {
	$("#bt_timer0").text(data);
	if (data == "Off") {
		$("#bt_timer0").attr("class", "offButton");
	}
	if (data == "Unknown") {
		$("#bt_timer0").attr("class", "tristateButton");
	}
	if (data == "On") {
		$("#bt_timer0").attr("class", "onButton");
	}
}

function timer1StatusCallback(macroName, args, data) {
	$("#bt_timer1").text(data);
	if (data == "Off") {
		$("#bt_timer1").attr("class", "offButton");
	}
	if (data == "Unknown") {
		$("#bt_timer1").attr("class", "tristateButton");
	}
	if (data == "On") {
		$("#bt_timer1").attr("class", "onButton");
	}
}

function timer2StatusCallback(macroName, args, data) {
	$("#bt_timer2").text(data);
	if (data == "Off") {
		$("#bt_timer2").attr("class", "offButton");
	}
	if (data == "Unknown") {
		$("#bt_timer2").attr("class", "tristateButton");
	}
	if (data == "On") {
		$("#bt_timer2").attr("class", "onButton");
	}
}


function timer3StatusCallback(macroName, args, data) {
	$("#bt_timer3").text(data);
	if (data == "Off") {
		$("#bt_timer3").attr("class", "offButton");
	}
	if (data == "Unknown") {
		$("#bt_timer3").attr("class", "tristateButton");
	}
	if (data == "On") {
		$("#bt_timer3").attr("class", "onButton");
	}
}



function toggleTimer0() {
	var hh, mm, ss, timerOn, timerOff, enable;	
	hh = parseInt($("#input_hh_timer0_on").val());
	mm = parseInt($("#input_mm_timer0_on").val());
	ss = parseInt($("#input_ss_timer0_on").val());
	if ( (hh >= 0 && hh < 24) && (mm >= 0 && mm < 60) && (ss >=0 && ss < 60)) {
		timerOn = hh * 3600 + mm * 60 + ss;	
	}
	hh = parseInt($("#input_hh_timer0_off").val());
	mm = parseInt($("#input_mm_timer0_off").val());
	ss = parseInt($("#input_ss_timer0_off").val());
	if ( hh >= 0 && hh < 24 && mm >= 0 && mm < 60 && ss >=0 && ss < 60) {
		timerOff = hh * 3600 + mm * 60 + ss;	
	}
	if ($("#bt_timer0").text() == "On") {
		enable = "False";
	}		
	else {
		enable = "True";
	}
	var args = new Array("0", "0", timerOn, timerOff, enable);
	webiopi().callMacro("editTimer", args, []);
	updateUI();
}

function toggleTimer1() {
	var hh, mm, ss, timerOn, timerOff, enable;	
	hh = parseInt($("#input_hh_timer1_on").val());
	mm = parseInt($("#input_mm_timer1_on").val());
	ss = parseInt($("#input_ss_timer1_on").val());
	if ( (hh >= 0 && hh < 24) && (mm >= 0 && mm < 60) && (ss >=0 && ss < 60)) {
		timerOn = hh * 3600 + mm * 60 + ss;	
	}
	hh = parseInt($("#input_hh_timer1_off").val());
	mm = parseInt($("#input_mm_timer1_off").val());
	ss = parseInt($("#input_ss_timer1_off").val());
	if ( hh >= 0 && hh < 24 && mm >= 0 && mm < 60 && ss >=0 && ss < 60) {
		timerOff = hh * 3600 + mm * 60 + ss;	
	}
	if ($("#bt_timer1").text() == "On") {
		enable = "False";
	}		
	else {
		enable = "True";
	}
	var args = new Array("1", "1", timerOn, timerOff, enable);
	webiopi().callMacro("editTimer", args, []);
	updateUI();
}

function toggleTimer2() {
	var hh, mm, ss, timerOn, timerOff, enable;	
	hh = parseInt($("#input_hh_timer2_on").val());
	mm = parseInt($("#input_mm_timer2_on").val());
	ss = parseInt($("#input_ss_timer2_on").val());
	if ( (hh >= 0 && hh < 24) && (mm >= 0 && mm < 60) && (ss >=0 && ss < 60)) {
		timerOn = hh * 3600 + mm * 60 + ss;	
	}
	hh = parseInt($("#input_hh_timer2_off").val());
	mm = parseInt($("#input_mm_timer2_off").val());
	ss = parseInt($("#input_ss_timer2_off").val());
	if ( hh >= 0 && hh < 24 && mm >= 0 && mm < 60 && ss >=0 && ss < 60) {
		timerOff = hh * 3600 + mm * 60 + ss;	
	}
	if ($("#bt_timer2").text() == "On") {
		enable = "False";
	}		
	else {
		enable = "True";
	}
	var args = new Array("2", "2", timerOn, timerOff, enable);
	webiopi().callMacro("editTimer", args, []);
	updateUI();
}

function toggleTimer3() {
	var hh, mm, ss, timerOn, timerOff, enable;	
	hh = parseInt($("#input_hh_timer3_on").val());
	mm = parseInt($("#input_mm_timer3_on").val());
	ss = parseInt($("#input_ss_timer3_on").val());
	if ( (hh >= 0 && hh < 24) && (mm >= 0 && mm < 60) && (ss >=0 && ss < 60)) {
		timerOn = hh * 3600 + mm * 60 + ss;	
	}
	hh = parseInt($("#input_hh_timer3_off").val());
	mm = parseInt($("#input_mm_timer3_off").val());
	ss = parseInt($("#input_ss_timer3_off").val());
	if ( hh >= 0 && hh < 24 && mm >= 0 && mm < 60 && ss >=0 && ss < 60) {
		timerOff = hh * 3600 + mm * 60 + ss;	
	}
	if ($("#bt_timer3").text() == "On") {
		enable = "False";
	}		
	else {
		enable = "True";
	}
	var args = new Array("3", "3", timerOn, timerOff, enable);
	webiopi().callMacro("editTimer", args, []);
	updateUI();
}
