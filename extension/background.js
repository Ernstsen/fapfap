// One-time event - create the context menu
//chrome.runtime.onInstalled.addListener(function() {
    
//})
var contextMenu = {
    "id": "fapfap",
    "title": "Generate pickup line",
    "contexts": ["editable"]
};
chrome.contextMenus.create(contextMenu)

chrome.contextMenus.onClicked.addListener(function(info, tab) {
    if (info.menuItemId === "fapfap") { // here's where you'll need the ID
        alert(info.menuItemId);
        alert(info.frameUrl);
        alert(info.frameId);
        getPickUpLine()
    }
});

getPickUpLine = function (){
    alert("Making pickup line")
}

// //This is our callback function
// mycallBack = function (info, tab) {
//     chrome.tabs.sendMessage(tab.id, "idString", function(clickedElement){
//         alert("in my call back"); 
//         // elt.value = clickedElement.value(); 
//         elt.value = "clickedElement.value()"; 
//     }); 
// }


// // chrome.contextMenus.onClicked.addListener(getPickUpLine)
// chrome.contextMenus.onClicked.addListener(test);

// getPickUpLine = function (){
//     alert("AJAX");
//     //     var xhttp = new XMLHttpRequest(); 
//     //     xhttp.onreadystatechange = function() {
//     //         if (this.readyState == 4 && this.status == 200){
//     //             alert("WE HAVE SUCCEEDED IN THE WAY OF MAKING OF AN AJAX CALL");  
//     //         }
//     //     }; 
        
//     //     xhttp.open("GET", "http://gooele.dk", true); // true makes sure that the rest of the html still works while do the back-end call asynchronous. 
//     //     xhttp.send();