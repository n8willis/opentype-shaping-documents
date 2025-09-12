function toggleColor(elementId) {
    demoImage = document.getElementById(elementId);
    console.log(elementId);
    
    if (demoImage.classList.contains("shaping-demo")) {
	if (demoImage.classList.contains("greyscale-svg")) {
	    
	    demoImage.classList.add("color-svg");
	    demoImage.classList.remove("greyscale-svg");
	    
	} else {
	    if (demoImage.classList.contains("color-svg")) {

		demoImage.classList.add("greyscale-svg");
		demoImage.classList.remove("color-svg");
	      
	    }
	}
    }
    else {
	console.log("toggleColor called on element that is not .shaping-demo class");
    }
}

