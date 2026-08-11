console.log("hello again");

function changeText() {
    let element = document.getElementById("button_header");

    if (element.innerHTML == "Look it changed!") {
        element.innerHTML = "It changed again!";
        element.style.backgroundColor = "yellow";
    } else if (element.innerHTML == "It changed again!") {
        element.innerHTML = "Hello! This is program where you click this button and things change! Go click it";
        element.style.backgroundColor = "black";
        element.style.border = "none";
    } else {
        element.innerHTML = "Look it changed!";
        element.style.border = "solid";
        element.style.borderRadius = "10px";
    }
}

function elementCreator() {
    const newSection = document.createElement("section");
    const newContent = document.createTextNode("Surprise! I'm here!");

    newSection.appendChild(newContent);

    const currentSection = document.querySelector("section-id");

    document.body.insertBefore(newSection, currentSection);
}

const headContainer = document.querySelector("#header-id");

function changeToBlue(e) {
    e.target.classList.toggle("blue");
}

headContainer.addEventListener("click", function () {
    this.target.classList.toggle("blue");
});

