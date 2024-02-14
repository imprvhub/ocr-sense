window.updateFileName = function (input) {
    const fileNameContainer = document.getElementById('file-name-container');
    const fileName = input.files[0].name;
    fileNameContainer.textContent = `Selected file: ${fileName}`;
};
