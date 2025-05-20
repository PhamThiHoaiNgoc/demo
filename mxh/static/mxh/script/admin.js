document.addEventListener('DOMContentLoaded', function () {
    const imageInput = document.getElementById('id_image_url');
    if (imageInput) {
        imageInput.addEventListener('change', function () {
            const fileName = this.files[0] ? this.files[0].name : '';
            const fileNameDisplay = document.getElementById('file-name');
            if (fileNameDisplay) {
                fileNameDisplay.textContent = fileName;
            }
        });
    }

    document.getElementById('attachment').addEventListener('change', function() {
            const fileName = this.files[0] ? this.files[0].name : '';
            document.getElementById('file-name').textContent = fileName;
        });

    const recipientRadios = document.querySelectorAll('input[name="recipient_type"]');
    recipientRadios.forEach(radio => {
        radio.addEventListener('change', toggleDepartments);
    });

    function toggleDepartments() {
        const selected = document.querySelector('input[name="recipient_type"]:checked');
        const departmentsContainer = document.getElementById('departments-container');
        if (departmentsContainer && selected) {
            departmentsContainer.style.display = selected.value === 'department' ? 'block' : 'none';
        }
    }

    toggleDepartments();
});

function confirmDelete(id, title) {
    const modal = document.getElementById('delete-modal');
    const form = document.getElementById('delete-form');
    const titleSpan = document.getElementById('delete-title');

    if (form && modal && titleSpan) {
        form.action = `/admin_home/notifications/delete/${id}/`;
        titleSpan.textContent = title;
        modal.classList.add('show');
    }
}

function closeModal() {
    const modal = document.getElementById('delete-modal');
    if (modal) {
        modal.classList.remove('show');
    }
}