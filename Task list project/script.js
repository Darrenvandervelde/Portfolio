function addTask() {
    const newTask = document.querySelector("#taskForm").value;

    const newContent = document.createTextNode(newTask);
    const newElement = document.createElement("li");

    newElement.appendChild(newContent);

    const currentElement = document.querySelector("#list-id").lastElementChild.nextSibling;

    document.querySelector("#list-id").insertBefore(newElement, currentElement);
}