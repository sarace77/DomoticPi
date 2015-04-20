/**
 * @author Antonio
 */

var devices_pin = [  2,  3,  4, 17, 27, 22, 10,  9, 11, 5, 6, 
					13, 19, 26, 14, 15, 18, 23, 24, 25, 8, 7, 
					12, 16, 20, 21];

var devices_visibility = 	[false, false, false, false, false, false, false, false, false, false, false, 
							 false, false, false, false, false,  true,  true,  true,  true, false, false, 
							 false, false, false, false];

function updateDeviceList() {
	var placeholder = document.getElementById("devices");
	var elements = devices_pin;
	var states = devices_visibility;
	for (var i = 0, item; item = elements[i]; i++) {
		var str_id = "gpio"+ item.toString();
		if (states[i]){
			var h3 = document.createElement("h3"); 
			var btn = document.createElement("button");
			var txt = document.createTextNode(str_id + String(": Unknown"));
			btn.setAttribute("id", str_id);
			btn.setAttribute("class", "tristateButton");
			btn.setAttribute("onClick", String("toggle(#bt_") +  item.toString() + String(")"));
			btn.appendChild(txt);
			h3.appendChild(btn);			
			placeholder.appendChild(h3);
		}
	}
}

function showDevice(id, status) {
	var divelement = document.getElementById(id);
	if (String(status) == "true") {		
		divelement.style.display = 'block'; 
	} else {
		divelement.style.display = 'none'; 
	}
}

function toggle(id) {
	
}

webiopi().ready(init);

function init() {
	var pins = devices_pin;
	var elements = devices_visibility;
	for (var i = 0, item; item = elements[i]; i++) {
		if (item) {
			var pin = pins[i];
			var name = String("gpio") + String(pin);
			var arg = [pin, name];
			webiopi().callMacro("addRelay", arg, []);									
		}		
	}

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