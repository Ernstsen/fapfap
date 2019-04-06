//content script
var clickedElement = null;

document.addEventListener("mousedown", function(event){
    //right click
    if(event.button == 2) {
        clickedElement = event.target;
        elemnt_id = clickedElement.id; 
        if(elemnt_id === null) {
            alert("Not able to find the ID of the input element. So the pickup line can't be returned\nThe line was...."); 
        }
    }
}, true);

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if(request == "idString") {
        // findLowestChildTag(); //TODO: RUN THROUGH SUCH THAT WE GET THE RIGHT ONE !!!! 
        
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                clickedElement.value = xhttp.responseText; 
            }
        };
        xhttp.open("GET", "http://fapfap.e-software.dk/pickupline", true);
        xhttp.send();
    }
})

// NOTE: Function to find child elements for further work in regards to FB-injection
// function findLowestChildTag(){
//     alert("FIND IT!"); 
//     clickedElement.childNodes(); 
//     while(clickedElement.childNodes.length > 0 ){
//         clickedElement = clickedElement.childNodes[0];
//     }
//     clickedElement.parent();
//     console.log("WOOOOOOOOOOORK!")
//     console.log("clicked element" + clickedElement)
//     alert(clickedElement.value); 

// }
