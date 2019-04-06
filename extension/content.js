// alert("Hello from your Chrome extension!");
// alert("val " + value.target);
//content script
var clickedElement = null;

document.addEventListener("mousedown", function(event){
    //right click
    // alert("Mousedown")
    if(event.button == 2) {
        alert("click event") 
        clickedElement = event.target;
        elemnt_id = clickedElement.id; 
        if(elemnt_id === null) {
            alert("Not able to find the ID of the input element. So the pickup line can't be returned\nThe line was...."); 
        }
        alert(clickedElement.id); 
    }
}, true);

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if(request == "idString") {
        alert("request was idString"); 
        // alert(sender); 
        // console.log("sender");
        // console.log(sender);
        // console.log("Reqeust");
        // console.log(request);
        // console.log("Response");
        // console.log(sendResponse); 
        // sendResponse({value: clickedElement});
        clickedElement.value = "HAHAHAHAH - Sune";   // TODO: Make AJAX call here... Only works for input-tags. 
        
    }
})