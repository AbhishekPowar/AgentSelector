form = document.getElementById('customerForm');
form.addEventListener('submit', async (e) => {
	e.preventDefault();

	params = '?';

	mode = document.getElementById('Mode').value;
	params += `Mode=${mode}`;
	roles = document.getElementsByName('roles');
	vaildRoles = [];
	for (const box of roles) {
		if (box.checked) vaildRoles.push(box.value);
	}
	params += `&&roles=${vaildRoles.join('-')}`;
	res = await fetch('customerReg' + params);
	json = await res.json();
	console.log(json);
	output = '';
	for (const key of [ 'mode', 'roles' ]) {
		output += `<div class="Jbox">
                    <div class="key">${key}</div>
                    <div class="value">${json[key]}</div>
                </div>`;
	}
	if (json['error'] != '0') {
		output += `<div class="Jbox">
                    <div class="key">Response</div>
                    <div class="value">${json['error']}</div>
                </div>`;
	} else {
		for (const key of Object.keys(json['response'])) {
			output += `<div class="card JboxRes">
                    <div class="key">${key}</div>
                    <div class="value">${json['response'][key]}</div>
                </div>`;
		}
	}

	//JSON.stringify(json)
	document.getElementById('output').innerHTML = output;
});

document.addEventListener('DOMContentLoaded', function() {
	var elems = document.querySelectorAll('select');
	var instances = M.FormSelect.init(elems, options);
});
