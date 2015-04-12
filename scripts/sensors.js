/**
 * @author Antonio
 */

var tmp;
var pres;
webiopi().ready(init);
function init() {
	tmp = new Temperature("bmp");
	pres = new Pressure("bmp");
	setInterval(updateUI, 1000);	
}

function updateUI() {
	tmp.getCelsius(temperatureCallback);
	pres.getHectoPascal(pressureCallBack);
	webiopi().callMacro("getUptime", [], uptimeCallBack);
}   
	        
function temperatureCallback(sensorName, data) {
	$("#bt_temperature").text(data);
}					

function pressureCallBack(sensorName, data) {
	$("#bt_pressure").text(data);
}

function uptimeCallBack(macroName, args, data) {
	$("#bt_uptime").val(data);
}
