var array = [];

function addToArray() {
    const newNum = Number(document.querySelector("#numInput").value);
    array.push(newNum);
}

function printArray() {
    document.querySelector("#list-id").innerHTML = "";
    var sum = 0;

    for (let i = 0; i < array.length; i++) {
        const newElement = document.createElement("li");
        newElement.innerHTML = array[i];
        document.querySelector("#list-id").appendChild(newElement);

        sum = sum + array[i];
    }

    const average = Math.round(sum / array.length);
    document.querySelector("#average-id").innerHTML = "Your average is: " + average;
}