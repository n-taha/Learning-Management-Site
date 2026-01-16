document.addEventListener("DOMContentLoaded", function () {
    // Confirm delete pop-up
    document.querySelectorAll('a.deletelink').forEach(el => {
        el.addEventListener('click', function (e) {
            if (!confirm("Are you sure? This action cannot be undone!")) {
                e.preventDefault();
            }
        });
    });
});
