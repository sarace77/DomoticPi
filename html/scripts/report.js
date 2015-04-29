/**
 * @author Antonio
 */
webiopi().ready(init);
function init() {
	var args = [18, "gpio18"];
	webiopi().callMacro("addRelay", args, updateLedCallBack);									
	args = [23, "gpio23"];
	webiopi().callMacro("addRelay", args, updateLedCallBack);									
	args = [24, "gpio24"];
	webiopi().callMacro("addRelay", args, updateLedCallBack);									
	args = [25, "gpio25"];
	webiopi().callMacro("addRelay", args, updateLedCallBack);									
	setInterval(updateUI, 500);	
}

function updateUI() {
	webiopi().callMacro("getLuminosity", [], luminosityCallBack);
}   

function brightLed(id) {
	var myLed = document.getElementById(id); 
  	myLed.setAttribute("class", "led-blue");
  	switch(id) {
  		case "led0Up":
  			webiopi().callMacro("switchOn", "18", updateLedCallBack);
  			break;
  		case "led1Up":
  			webiopi().callMacro("switchOn", "24", updateLedCallBack);
  			break;
  		case "led0Down":
  			webiopi().callMacro("switchOn", "23", updateLedCallBack);
  			break;
  		case "led1Down":
  			webiopi().callMacro("switchOn", "25", updateLedCallBack);
  			break;
  	}
}

function darkLed(id) {
	var myLed = document.getElementById(id); 
  	myLed.setAttribute("class", "led-black");
  	switch(id) {
  		case "led0Up":
  			webiopi().callMacro("switchOff", "18", updateLedCallBack);
  			break;
  		case "led1Up":
  			webiopi().callMacro("switchOff", "24", updateLedCallBack);
  			break;
  		case "led0Down":
  			webiopi().callMacro("switchOff", "23", updateLedCallBack);
  			break;
  		case "led1Down":
  			webiopi().callMacro("switchOff", "25", updateLedCallBack);
  			break;
  	}
}

function updateLedCallBack(macroname, args, data) {

}

function luminosityCallBack(macroName, args, data) {
	var lux = parseInt(data);
	var item = document.getElementById("luminosity");
	item.innerHTML = "<h3>" + lux + "</h3>"; 
	item = $('.progress-bar span');
	lux = lux /10;
	lux = lux.toString();
	item.css('width', lux + '%');
}

