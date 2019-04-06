var clickedElement = null;

document.addEventListener("mousedown", function(event){
    //right click
    if (event.button == 2) {
        clickedElement = event.target;
    }
}, true);

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request == "idString") {
        clickedElement.value = "HAHAHAHAH - Sune";   // TODO: Make AJAX call here... Only works for input-tags.       
    }
})