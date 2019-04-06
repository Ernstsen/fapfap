var clickedElement = null;

document.addEventListener("mousedown", function(event){
    //right click
    if (event.button == 2) {
        clickedElement = event.target;
    }
}, true);

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request == "idString") {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                clickedElement.value = xhttp.responseText; 
                copyStringToClipboard(xhttp.responseText)
            }
        };
        xhttp.open("GET", "https://fapfap.e-software.dk/pickupline", true);
        xhttp.send();
    }
})

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