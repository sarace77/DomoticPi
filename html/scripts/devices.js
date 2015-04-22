/**
 * @author Antonio
 */

/**
 * list of all Available Raspberri PI(2) pins
 */ 
var devices_pin = [  2,  3,  4, 17, 27, 22, 10,  9, 11,  5,  6, 13, 19, 
					26, 14, 15, 18, 23, 24, 25,  8,  7, 12, 16, 20, 21];

/**
 * Variable is used to store/retrieve pin status (true = connected to a device/ false = not connected)
 */
var devices_visibility = 	[false, false, false, false, false, false, false, false, false, false, false, false, false, 
							 false, false, false,  true,  true,  true,  true, false, false, false, false, false, false];

/**
 * insertMode is used to set if inputPin field is in "add" or "remove" pin mode.
 */							 
var insertMode = false;							 

/**
 * UI function: It hides inputPin field/buttons and shows add/del buttons 
 */
function discardChanges() {
	var editItem = document.getElementById("inputPinContainer");	
	editItem.style.display = "none";
	editItem = document.getElementById("editButtons");
	editItem.style.display = "block";
	editItem = document.getElementById("inputPin");
}


/**
 * Function used to initialize webiopi js module
 */
function init() {
	setInterval(updateUI, 500);	
}


/**
 * UI function: it hides add/del buttons and shows inputPin field/buttons (setting them in "add" or "remove" pin mode)
 */
function showInput(insMode) {
	insertMode = insMode;	
	var editItem = document.getElementById("inputPinContainer");	
	editItem.style.display = "block";
	editItem = document.getElementById("editButtons");
	editItem.style.display = "none";	 
}


/**
 * Used to toggle pin (device) status
 * TODO adding python script GPIO status support
 */
function toggle(id) {
	if (id.toString() != "-1") {
		var btn_id = String("gpio");
		if (id.toString().length == 2) {
			btn_id += id.toString();
		} else {
			btn_id += String("0") + id.toString();
		}
		var item = document.getElementById(btn_id);
		window.alert(item.className);
//		TODO uncomment the followng line		
//		webiopi().callMacro("toggleRelay", id.toString() , updateDeviceStatusCallBack);
	} else {
		var item = document.getElementById("bt_all_relay");
//		TODO uncomment the followng line		
//		webiopi().callMacro("toggleRelay", "All" , updateDeviceStatusCallBack);
		window.alert(item.id + item.className);
	}
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


/**
 * UI function: it show "available" (connected) pin, on page load and when a new pin is added or removed
 * TODO uncomment webiopi macro call 
 */
function updateDeviceList() {
	var placeholder = document.getElementById("devices");
	var items2remove = placeholder.children;
	while (items2remove.length > 0) {
		placeholder.removeChild(items2remove[0]);
		items2remove = placeholder.children;	
	}
	var elements = devices_pin;
	var states = devices_visibility;
	for (var i = 0, item; item = elements[i]; i++) {
		var str_id = "gpio";
		if (item.toString().length == 2) {
			str_id += item.toString();			
		} else {
			str_id += String("0") + item.toString();
		}
		if (states[i]){
			var h3 = document.createElement("h3"); 
			var btn = document.createElement("button");
			var txt = document.createTextNode(String("Unknown"));
			var pin = item;
			var name = String("gpio") + String(pin);
			var arg = [pin, name];
			btn.setAttribute("id", str_id);
			btn.setAttribute("class", "tristateButton");
			btn.setAttribute("onClick", String("toggle(") +  item.toString() + String(")"));
			btn.appendChild(txt);
			h3.innerHTML = String("Device ") + str_id + String(": ");
			h3.appendChild(btn);			
			placeholder.appendChild(h3);
			//TODO uncomment the following line
			//webiopi().callMacro("addRelay", arg, updateDeviceStatusCallBack);									
		}
	}
}


/**
 * callback for webiopi macro
 */
function updateDeviceStatusCallBack(macroname, args, data) {
	var pin = args[0];
	var str_id = "gpio";
	if (pin.toString() != "All")
	{
		if (pin.toString().length == 2) {
			str_id += pin.toString();
		} else {
			str_id += String("0") + pin.toString(); 
		}
	} else {
		str_id = "bt_all_relay";
	}
	var item = document.getElementById(str_id);
	window.alert(item.getAttribute("value"));
	item.setAttribute("value", data);
	if (data == "On") {
		item.setAttribute("class", "onButton");
	} else if (data == "Off") {
		item.setAttribute("class", "offButton");	
	} else {
		item.setAttribute("class", "tristateButton");
	}	
}


/**
 * Main Loop: update status of UI
 */
function updateUI() {
	var elements = devices_pin;
	var states = devices_visibility;
	for (var i = 0, item; item = elements[i]; i++) {
		if (states[i]) {
			webiopi().callMacro("getStatus", item.toString(), updateDeviceStatusCallBack);			
		}
	}
}


/**
 * Used to add/remove pin
 */
function validatePin() {
	var elements = devices_pin;
	var pin = document.getElementById("inputPin").value;
	var pinFound = false;
	for (var i = 0, item; item = elements[i]; i++) {
		if (String(pin) == String(item)) {
			devices_visibility[i] = insertMode;	
			updateDeviceList();
			var editItem = document.getElementById("inputPinContainer");	
			editItem.style.display = "none";	 
			editItem = document.getElementById("editButtons");
			editItem.style.display = "block";
			pinFound = true;
			var name = String("gpio") + String(pin);
			var arg = [Number(pin), name];
			if (insertMode) {
//				TODO uncomment the followng line						
//				webiopi().callMacro("addRelay", arg, []);									
			} else {
//				TODO remove Relay from python array
			}
			break;
		}
	}
	if (!pinFound){
		window.alert(String("Pin #") + String(pin) + String(" is not a valid pin!"));
	}
}


/**
 * Start of webio related functions
 */
webiopi().ready(init);


