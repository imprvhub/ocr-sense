window.updateFileName = function (input) {
    const fileNameContainer = document.getElementById('file-name-container');
    const fileName = input.files[0].name;
    fileNameContainer.textContent = `Selected file: ${fileName}`;
};


function handleDrop(event) {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
  }
  

  document.addEventListener("dragover", function (event) {
    event.preventDefault();
  });
  
  document.addEventListener("drop", handleDrop);


  window.addEventListener('DOMContentLoaded', () => {
    const dropArea = document.querySelector('#upload-form');
    const fileInput = document.querySelector('#pdf-input');

    dropArea.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropArea.classList.add('drag-over');
    });

    dropArea.addEventListener('dragleave', () => {
        dropArea.classList.remove('drag-over');
    });

    dropArea.addEventListener('drop', (e) => {
        e.preventDefault();
        dropArea.classList.remove('drag-over');
        const file = e.dataTransfer.files[0];
        fileInput.files = e.dataTransfer.files;
        updateFileName(fileInput);
    });

    fileInput.addEventListener('change', () => {
        updateFileName(fileInput);
    });
});

function updateFileName(input) {
    const fileNameContainer = document.getElementById('file-name-container');
    const fileName = input.files[0].name;
    fileNameContainer.textContent = `File: ${fileName}`;
}


function validateFileSize() {
    var input = document.getElementById('pdf-input');
    var fileSize = input.files[0].size;
    var maxSize = 1024 * 1024; // 1MB

    if (fileSize > maxSize) {
        document.getElementById('file-size-error').style.display = 'block';
        return false; // Evitar el envío del formulario si el tamaño excede el límite
    } else {
        document.getElementById('file-size-error').style.display = 'none';
        return true; // Permite el envío del formulario si el tamaño está dentro del límite
    }
}
