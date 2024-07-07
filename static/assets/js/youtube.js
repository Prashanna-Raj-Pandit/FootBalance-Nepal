document.addEventListener('DOMContentLoaded', function() {
    var videoFacade = document.getElementById('video-facade');
    var videoContainer = document.getElementById('video-container');

    videoFacade.addEventListener('click', function() {
        var iframe = document.createElement('iframe');
        iframe.setAttribute('width', '100%');
        iframe.setAttribute('height', '100%');
        iframe.setAttribute('src', 'https://www.youtube.com/embed/YFHUTo3Zxk8?autoplay=1&rel=0');
        iframe.setAttribute('title', 'YouTube video player');
        iframe.setAttribute('frameborder', '0');
        iframe.setAttribute('allow', 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share');
        iframe.setAttribute('referrerpolicy', 'strict-origin-when-cross-origin');
        iframe.setAttribute('allowfullscreen', '');

        videoContainer.innerHTML = '';
        videoContainer.appendChild(iframe);
    });
});
