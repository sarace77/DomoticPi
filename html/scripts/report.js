/**
 * @author Antonio
 */
webiopi().ready(init);
function init() {
	setInterval(updateUI, 1000);	
}

function updateUI() {
	webiopi().callMacro("getTimerStatus","0",timer0StatusCallback);
	webiopi().callMacro("getTimerStatus","1",timer1StatusCallback);
	webiopi().callMacro("getTimerStatus","2",timer2StatusCallback);
	webiopi().callMacro("getTimerStatus","3",timer3StatusCallback);
	webiopi().callMacro("getUptime", [], uptimeCallBack);
}   

function uptimeCallBack(macroName, args, data) {
	$("#bt_uptime").val(data);
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


function brightLed(id) {
	var myLed = document.getElementById(id); 
  	myLed.setAttribute("class", "led-blue");
}

function darkLed(id) {
	var myLed = document.getElementById(id); 
  	myLed.setAttribute("class", "led-black");
}