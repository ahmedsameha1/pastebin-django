const confirmDialog = document.getElementById("confirmDialog");
const infoDialog = document.getElementById("infoDialog");
const confirmButton = document.getElementById("confirmButton");

function confirmDeletion() {
    confirmDialog.showModal();
}

confirmButton.addEventListener("click", () => {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    window.fetch(window.location.href, {
        method: "DELETE", headers: { 'X-CSRFToken': csrftoken },
        mode: 'same-origin'
    });
    confirmDialog.close();
    infoDialog.showModal();
});