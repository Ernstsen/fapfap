window.onload = generateLine; 


function generateLine() {
    var div = document.getElementById("pickup_line");
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			div.innerHTML = "<b> Pickup line: </b> <br> " + xhttp.responseText;
			div.style.color = "black"
			copyStringToClipboard(xhttp.responseText)                                                                                
		} else { // Make this less general - alert is being displayed several times????
			console.log("Server API is not responding")
		}
	};
	xhttp.open("GET", "https://fapfap.e-software.dk/pickupline", true);
	xhttp.send(); 
}

function copyStringToClipboard (str) {
	// Create new element
	var el = document.createElement('textarea');
	// Set value (string to be copied)
	el.value = str;
	// Set non-editable to avoid focus and move outside of view
	el.setAttribute('readonly', '');
	el.style = {position: 'absolute', left: '-9999px'};
	document.body.appendChild(el);
	// Select text inside element
	el.select();
	// Copy text to clipboard
	document.execCommand('copy');
	// Remove temporary element
	document.body.removeChild(el);
}
