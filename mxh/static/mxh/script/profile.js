document.addEventListener("DOMContentLoaded", () => {
  // Tab switching
  const postsTab = document.getElementById("posts-tab")
  const infoTab = document.getElementById("info-tab")
  const postsContent = document.getElementById("posts-content")
  const infoContent = document.getElementById("info-content")

  postsTab.addEventListener("click", () => {
    postsTab.classList.add("active")
    infoTab.classList.remove("active")
    postsContent.classList.remove("hidden")
    infoContent.classList.add("hidden")
  })

  infoTab.addEventListener("click", () => {
    infoTab.classList.add("active")
    postsTab.classList.remove("active")
    infoContent.classList.remove("hidden")
    postsContent.classList.add("hidden")
  })

  // Post menu dropdown
  const menuButtons = document.querySelectorAll(".menu-button")
  menuButtons.forEach((button) => {
    button.addEventListener("click", function (e) {
      e.stopPropagation()
      const dropdown = this.nextElementSibling
      dropdown.classList.toggle("show")
    })
  })

  // Close dropdowns when clicking outside
  document.addEventListener("click", () => {
    const dropdowns = document.querySelectorAll(".dropdown-menu")
    dropdowns.forEach((dropdown) => {
      dropdown.classList.remove("show")
    })
  })

  // Edit post modal
  const editPostLinks = document.querySelectorAll(".edit-post")
  const editPostModal = document.getElementById("edit-post-modal")
  const closeModalButton = document.querySelector(".close-button")

  editPostLinks.forEach((link) => {
    link.addEventListener("click", (e) => {
      e.preventDefault()
      editPostModal.classList.add("show")
    })
  })

  closeModalButton.addEventListener("click", () => {
    editPostModal.classList.remove("show")
  })

  // Close modal when clicking outside
  editPostModal.addEventListener("click", (e) => {
    if (e.target === editPostModal) {
      editPostModal.classList.remove("show")
    }
  })

  // Remove image from post preview
  const removeImageButton = document.querySelector(".remove-image-button")
  const postImagePreview = document.querySelector(".post-image-preview")

  if (removeImageButton && postImagePreview) {
    removeImageButton.addEventListener("click", () => {
      postImagePreview.style.display = "none"
    })
  }
})