// Xác nhận trước khi xóa
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll('.btn-delete').forEach(button => {
        button.addEventListener('click', function (event) {
            if (!confirm('Bạn có chắc muốn xoá công việc này?')) {
                event.preventDefault();
            }
        });
    });

    // Hiệu ứng highlight task mới nhất
    const tasks = document.querySelectorAll('.task-list li');
    if (tasks.length > 0) {
        const newest = tasks[0]; // Mặc định task mới nhất đầu danh sách
        const originalColor = getComputedStyle(newest).backgroundColor;
        newest.style.backgroundColor = "#e0f7fa";
        setTimeout(() => {
            newest.style.transition = "background-color 1s ease";
            newest.style.backgroundColor = originalColor;
        }, 300);
    }
});
