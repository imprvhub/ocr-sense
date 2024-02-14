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
    const dropArea = document.querySelector('.upload-container');
    const fileInput = document.querySelector('#image-input1');

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