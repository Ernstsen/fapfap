var clickedElement = null;

document.addEventListener("mousedown", function(event){
    //right click
    if (event.button == 2) {
        clickedElement = event.target;
        // findLowestChildTag();
        alert(clickedElement.type); 
    }
}, true);

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request == "idString") {
        // findLowestChildTag(); //TODO: RUN THROUGH SUCH THAT WE GET THE RIGHT ONE !!!! 
        
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                clickedElement.value = xhttp.responseText; 
                copyStringToClipboard(xhttp.responseText)
                alert("saved to clip board"); 
            }
        };
        xhttp.open("GET", "https://fapfap.e-software.dk/pickupline", true);
        xhttp.send();
    }
})

// NOTE: Function to find child elements for further work in regards to FB-injection
function findLowestChildTag(){
    document.getElementsByClassName(clickedElement.class); 
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