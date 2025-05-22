// Video player controls and error handling
document.addEventListener('DOMContentLoaded', function() {
    const videos = document.querySelectorAll('video');
    
    videos.forEach(video => {
        // Add controls attribute if not present
        video.controls = true;
        
        // Create close button container
        const closeContainer = document.createElement('div');
        closeContainer.className = 'video-close-container';
        closeContainer.style.position = 'absolute';
        closeContainer.style.top = '10px';
        closeContainer.style.right = '10px';
        closeContainer.style.zIndex = '1000';
        
        // Create close button
        const closeButton = document.createElement('button');
        closeButton.innerHTML = '×';
        closeButton.className = 'video-close-btn';
        closeButton.style.padding = '5px 10px';
        closeButton.style.background = 'rgba(0, 0, 0, 0.5)';
        closeButton.style.color = 'white';
        closeButton.style.border = 'none';
        closeButton.style.borderRadius = '50%';
        closeButton.style.cursor = 'pointer';
        closeButton.style.fontSize = '20px';
        
        // Add hover effect
        closeButton.onmouseover = () => closeButton.style.background = 'rgba(0, 0, 0, 0.8)';
        closeButton.onmouseout = () => closeButton.style.background = 'rgba(0, 0, 0, 0.5)';
        
        // Close button click handler
        closeButton.onclick = () => {
            video.pause();
            const container = video.closest('.video-container') || video.parentElement;
            container.style.display = 'none';
        };
        
        // Add close button to container
        closeContainer.appendChild(closeButton);
        
        // Add container next to video
        const container = video.closest('.video-container') || video.parentElement;
        container.style.position = 'relative';
        container.insertBefore(closeContainer, video);
        
        // Error handling
        video.addEventListener('error', function(e) {
            console.error('Video error:', e);
            const container = video.closest('.video-container') || video.parentElement;
            container.innerHTML += '<div class="video-error">Error loading video. Please try refreshing the page.</div>';
        });
        
        // Handle connection errors
        video.addEventListener('stalled', function() {
            console.warn('Video connection stalled');
            video.load(); // Attempt to reload the video
        });
    });
}); 