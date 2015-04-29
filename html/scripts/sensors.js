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
	webiopi().callMacro("getLuminosity", [], luminosityCallBack);
	webiopi().callMacro("getUptime", [], uptimeCallBack);
}   

function humidityCallBack(macroName, args, data) {
	var item = document.getElementById("humidity");
	item.innerHTML = String("<h3>Umidità: </h3><i>") + String(data) + String("%</i>");
}

function luminosityCallBack(macroName, args, data) {
	var item = document.getElementById("luminosity");
}

function temperatureCallback(sensorName, data) {
	var item = document.getElementById("int_temperature");	
	item.innerHTML = String("<h3>Temperatura Interna: </h3><i>") + String(data) + String("°C</i>");
}					

function pressureCallBack(sensorName, data) {
	var item = document.getElementById("bar_pressure");
	item.innerHTML = String("<h3>Pressione Barometrica: </h3><i>") + String(data) + String("°C</i>");
}

function uptimeCallBack(macroName, args, data) {
	var item = document.getElementById("systemUpTime");
	item.innerHTML = String("<h3>Sistema acceso e funzionante da: </h3><i>") + String(data) + String("</i>");
}
