/**
 * @author Antonio
 */

var tmp;
var pres;
webiopi().ready(init);
function init() {
	tmp = new Temperature("bmp");
	pres = new Pressure("bmp");	
	setInterval(updateUI, 5000);	
}

function updateUI() {
	tmp.getCelsius(temperatureCallback);
	pres.getHectoPascal(pressureCallBack);
	webiopi().callMacro("getHumidity", [], humidityCallBack);
	webiopi().callMacro("getUptime", [], uptimeCallBack);
}   

function humidityCallBack(macroName, args, data) {
	$("#bt_humidity").text(data);
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
