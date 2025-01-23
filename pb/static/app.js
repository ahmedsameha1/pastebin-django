const confirmDialog = document.getElementById("confirmDialog");
const infoDialog = document.getElementById("infoDialog");
const confirmButton = document.getElementById("confirmButton");

function confirmDeletion() {
    confirmDialog.showModal();
}

confirmButton.addEventListener("click", () => {
    confirmDialog.close();
    infoDialog.showModal();
})