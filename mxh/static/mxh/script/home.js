document.addEventListener('DOMContentLoaded', function () {
    // Xử lý nút like
    document.querySelectorAll('.like-button').forEach(button => {
        button.addEventListener('click', function () {
            toggleLike(this);
        });
    });

    // Xử lý nút comment
    document.querySelectorAll('.comment-button').forEach(button => {
        button.addEventListener('click', function () {
            toggleComment(this);
        });
    });

    // Xử lý form report submit
    const reportForm = document.getElementById("report-form");
    if (reportForm) {
        reportForm.addEventListener("submit", function(event) {
            event.preventDefault();
            window.location.href = "/Trangchu.html";
        });
    }

});



// Toggle like

// Toggle comment input
function toggleComment(button) {
    const post = button.closest('.post');
    const commentInput = post ? post.querySelector('.comment-input') : null;
    if (commentInput) {
        const isVisible = commentInput.style.display === 'flex';
        commentInput.style.display = isVisible ? 'none' : 'flex';
        button.classList.toggle('active', !isVisible);
    }
}

// Tìm kiếm người dùng
document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('search-input');
    const searchButton = document.getElementById('search-button');

    // Gõ vào input thì tìm kiếm
    if (searchInput) {
        searchInput.addEventListener('input', function () {
            searchUsers(this.value);
        });
    }

    // Click nút tìm kiếm thì cũng tìm kiếm
    if (searchButton) {
        searchButton.addEventListener('click', function () {
            const query = searchInput.value;
            searchUsers(query);
        });
    }
});

// Hàm fetch kết quả
function searchUsers(query) {
    const resultsDiv = document.getElementById('search-results');

    if (!query.trim()) {
        resultsDiv.innerHTML = '';
        return;
    }

    fetch(`/search-users/?q=${encodeURIComponent(query)}`)
        .then(response => response.text())
        .then(html => {
            resultsDiv.innerHTML = html;
        })
        .catch(error => {
            console.error('Error fetching users:', error);
            resultsDiv.innerHTML = '<p>Có lỗi xảy ra khi tìm kiếm.</p>';
        });
}



