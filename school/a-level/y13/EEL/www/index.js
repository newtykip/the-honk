const UNIT_CONVERT = /(?<quantity>\d+) (?<base>.*)(?:s)? (?:in|to) (?<target>.*)(?:s)?/;
const FUEL_TRAVEL = /fuel to travel (?<quantity>\d+) mile(?:s)?/;
const SURFACE_AREA = /surface area of field with diameter (?<value>\d+).*/;

eel.expose(read)

function update_response(text) {
	const response = document.getElementById("response");
	response.innerText = text;
}

function submit() {
	const textbox = document.getElementById("box");
	const { value } = textbox;

	// unit conversion
	if (UNIT_CONVERT.test(value)) {
		let { quantity, target, base } = UNIT_CONVERT.exec(value).groups;

		try {
			quantity = parseFloat(quantity);
		} catch {
			update_response("Quantity is not a valid number");
		}

		eel.convert_units(base, target, quantity)().then(update_response);
	} else if (FUEL_TRAVEL.test(value)) {
		let { quantity } = FUEL_TRAVEL.exec(value).groups;

		try {
			quantity = parseFloat(quantity);
		} catch {
			update_response("Quantity is not a valid number");
		}

		eel.calculate_fuel(quantity)().then(update_response);
	} else if (SURFACE_AREA.test(value)) {
		let { value } = SURFACE_AREA.exec(value).groups;

		try {
			value = parseFloat(value);
		} catch {
			update_response("Diameter is not a valid number");
		}

		eel.surface_area(value)().then(update_response);
	}
}

function save() {
	const { innerText: content } = document.getElementById("response");
	const save_response = document.getElementById("save_result");
	
	eel.save(content)().then(file_id => {
		save_response.innerText = `You can find the response at out/${file_id}.txt ${blob}`;

		setTimeout(() => save_response.innerText = "", 5000);
	});
}