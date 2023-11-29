eel.expose(read_text_box)

function read_text_box() {
	var textbox = document.getElementById("box");
	return textbox.value;
}

function send_message() {
	var textbox = document.getElementById("box");
	eel.send(textbox.value)(process_acknowledgement);
}

function process_acknowledgement(result) {
	if (result == "ok") {
		var textbox = document.getElementById("box");
		textbox.value = "";
	}
}
