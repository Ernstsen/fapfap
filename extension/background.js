// One-time event - create the context menu
chrome.runtime.onInstalled.addListener(function() {
    var contextMenu = {
        "id": "fapfap",
        "title": "Generate pickup line",
        "contexts": ["editable"]
    };
    chrome.contextMenus.create(contextMenu)
})

chrome.contextMenus.onClicked.addListener(function(info, tab) {
    if (info.menuItemId === "fapfap") { // here's where you'll need the ID
        mycallBack(info, tab)
    }
});

//This is our callback function
function mycallBack(info, tab) {
    chrome.tabs.sendMessage(tab.id, "idString")
    // , function(clickedElement){
    //     elt.value = clickedElement.value();
    // }); 
}
