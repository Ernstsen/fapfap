/* alert("Hello from your Chrome extension!")

alert(value.target);

//content script
var clickedElement = null;

document.addEventListener("mousedown", function(event){
    //right click
    alert("Mousedown")
    if(event.button == 2) {
        alert("click event") 
        clickedElement = event.target;
    }
}, true);

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if(request == "idString") {
        sendResponse({value: clickedElement.value});
    }
}) */