/**
 * @author Antonio
 */

webiopi().ready(init);
			
function init() {
	setInterval(updateUI, 500);	
}

function updateUI() {
	webiopi().callMacro("getStatus", "0", toggleRelay0Callback);
	webiopi().callMacro("getStatus", "1", toggleRelay1Callback);
	webiopi().callMacro("getStatus", "2", toggleRelay2Callback);
	webiopi().callMacro("getStatus", "3", toggleRelay3Callback);
	webiopi().callMacro("getStatus", "All", toggleAllCallback);	
}
					
function toggleRelay0() {
	webiopi().callMacro("toggleRelay", "0", toggleRelay0Callback);
}	
			
function toggleRelay1() {
	webiopi().callMacro("toggleRelay", "1", toggleRelay1Callback);
}	
	
function toggleRelay2() {
	webiopi().callMacro("toggleRelay", "2", toggleRelay2Callback);
}	
	
function toggleRelay3() {
	webiopi().callMacro("toggleRelay", "3", toggleRelay3Callback);
}

function toggleAll() {
	webiopi().callMacro("toggleRelay", "All", toggleAllCallback);
}	

function toggleAllCallback(macroName, args, data) {
		$("#bt_all_relay").text(data);
	if (data == "Off") {
		$("#bt_all_relay").attr("class", "offButton");
	}
	if (data == "Unknown") {
		$("#bt_all_relay").attr("class", "tristateButton");
	}
	if (data == "On") {
		$("#bt_all_relay").attr("class", "onButton");
	}
	
}	
	
function toggleRelay0Callback(macroName, args, data) {	
	$("#bt_relay0").text(data);
	if (data == "Off")
		$("#bt_relay0").attr("class", "offButton");
	if (data == "On")
		$("#bt_relay0").attr("class", "onButton");
}
	
function toggleRelay1Callback(macroName, args, data) {	
	$("#bt_relay1").text(data);
	if (data == "Off")
		$("#bt_relay1").attr("class", "offButton");
	if (data == "On")
		$("#bt_relay1").attr("class", "onButton");
}
	
function toggleRelay2Callback(macroName, args, data) {	
	$("#bt_relay2").text(data);
	if (data == "Off")
		$("#bt_relay2").attr("class", "offButton");
	if (data == "On")
		$("#bt_relay2").attr("class", "onButton");
}
	
function toggleRelay3Callback(macroName, args, data) {	
	$("#bt_relay3").text(data);
	if (data == "Off")
		$("#bt_relay3").attr("class", "offButton");
    if (data == "On")
		$("#bt_relay3").attr("class", "onButton");
}    
