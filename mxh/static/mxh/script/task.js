function showTab(tabName) {
  document.querySelectorAll('.task-list').forEach(tabContent => {
    tabContent.style.display = 'none';
  });

  document.querySelectorAll('.task-tabs .tab').forEach(tabBtn => {
    tabBtn.classList.remove('active');
  });

  if (tabName === 'pending') {
    document.getElementById('pending-tasks').style.display = 'block';
  } else if (tabName === 'completed') {
    document.getElementById('completed-tasks').style.display = 'block';
  }

  document.querySelectorAll('.task-tabs .tab').forEach(tab => {
    if (
      (tabName === 'pending' && tab.textContent.includes('Chưa xong')) ||
      (tabName === 'completed' && tab.textContent.includes('Đã xong'))
    ) {
      tab.classList.add('active');
    }
  });
}

document.addEventListener('DOMContentLoaded', () => {
  showTab('pending');
});
