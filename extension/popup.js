function activate() {
	chrome.tabs.executeScript({
	  file: 'method.js'
	}); 
  }
  
document.getElementById('generate_line_btn').addEventListener('click', activate);