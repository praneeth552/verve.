$(document).ready(function() {
    $(".loader").fadeOut("slow");
});

document.querySelectorAll('.like-button').forEach(button => {
    button.addEventListener('click', function() {
        const postId = this.getAttribute('data-post-id');
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        fetch(`/like/${postId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.is_liked) {
                this.textContent = `Unlike (${data.total_likes})`;
            } else {
                this.textContent = `Like (${data.total_likes})`;
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});

