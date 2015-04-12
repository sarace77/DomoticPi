/**
 * @author Antonio
 */
webiopi().ready(init);
function init() {
	setInterval(updateUI, 1000);	
}

function updateUI() {
	webiopi().callMacro("getUptime", [], uptimeCallBack);
}   

function uptimeCallBack(macroName, args, data) {
	$("#bt_uptime").val(data);
}
