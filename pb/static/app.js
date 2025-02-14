const confirmDialog = document.getElementById("confirmDialog");
const infoDialog = document.getElementById("infoDialog");
const confirmButton = document.getElementById("confirmButton");
const alreadyDeletedDialog = document.getElementById("alreadyDeletedDialog");

function confirmDeletion() {
    confirmDialog.showModal();
}

confirmButton.addEventListener("click", () => {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    window.fetch(window.location.href, {
        method: "DELETE", headers: { 'X-CSRFToken': csrftoken },
        mode: 'same-origin'
    }).then((response) => {
        confirmDialog.close();
        if (response.status === 204) {
            infoDialog.showModal();
        } else if (response.status === 404) {
            alreadyDeletedDialog.showModal();
        }
    });
});