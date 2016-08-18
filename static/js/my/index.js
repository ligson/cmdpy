/**
 * 
 */
function exeCmd() {
	var cmd = $("#cmd").val();
	if (cmd != null && cmd != "") {
		$.post("/exec.json", {
			cmd : cmd
		}, function(data) {
			$("#result").val(data.result);
		}, "json");
	}
}
$(function() {
	$("#exeBtn").click(function() {
		exeCmd();
	});
	$("#cmd").keydown(function(event){
		if(event.keyCode==13){
			exeCmd();
		}
	});
});