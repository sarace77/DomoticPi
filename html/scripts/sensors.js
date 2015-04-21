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
	webiopi().callMacro("getHumidity", [], humidityCallBack);
	webiopi().callMacro("getUptime", [], uptimeCallBack);
}   

function humidityCallBack(macroName, args, data) {
	var item = document.getElementById("humidity");
	item.innerHTML = String("<b>Umidità: </b><i>") + String(data) + String("%</i>");
}
function temperatureCallback(sensorName, data) {
	var item = document.getElementById("int_temperature");	
	item.innerHTML = String("<b>Temperatura Interna: </b><i>") + String(data) + String("°C</i>");
}					

function pressureCallBack(sensorName, data) {
	var item = document.getElementById("bar_pressure");
	item.innerHTML(String("<b>Pressione Barometrica: </b><i>") + String(data) + String("°C</i>"));
}

function uptimeCallBack(macroName, args, data) {
	var item = document.getElementById("systemUpTime");
	item.innerHTML(String("<b>Sistema acceso e funzionante da: </b><i>") + String(data) + String("</i>"));
}
