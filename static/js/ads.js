// Google IMA SDK Integration
let adDisplayContainer;
let adsLoader;
let adsManager;
let videoContent;

function initializeIMA() {
    // Create the ad display container
    adDisplayContainer = new google.ima.AdDisplayContainer(
        document.getElementById('adContainer'),
        videoContent);

    // Initialize the container
    adDisplayContainer.initialize();

    // Create ads loader
    adsLoader = new google.ima.AdsLoader(adDisplayContainer);

    // Add event listeners
    adsLoader.addEventListener(
        google.ima.AdsManagerLoadedEvent.Type.ADS_MANAGER_LOADED,
        onAdsManagerLoaded,
        false);
    adsLoader.addEventListener(
        google.ima.AdErrorEvent.Type.AD_ERROR,
        onAdError,
        false);
}

function requestAds() {
    // Create ads request
    const adsRequest = new google.ima.AdsRequest();
    adsRequest.adTagUrl = 'YOUR_AD_TAG_URL'; // Replace with your ad tag URL

    // Specify the linear and nonlinear slot sizes
    adsRequest.linearAdSlotWidth = 640;
    adsRequest.linearAdSlotHeight = 400;
    adsRequest.nonLinearAdSlotWidth = 640;
    adsRequest.nonLinearAdSlotHeight = 150;

    // Make the request
    adsLoader.requestAds(adsRequest);
}

function onAdsManagerLoaded(adsManagerLoadedEvent) {
    // Get the ads manager
    const adsRenderingSettings = new google.ima.AdsRenderingSettings();
    adsRenderingSettings.restoreCustomPlaybackStateOnAdBreakComplete = true;
    adsManager = adsManagerLoadedEvent.getAdsManager(
        videoContent, adsRenderingSettings);

    // Add event listeners
    adsManager.addEventListener(
        google.ima.AdErrorEvent.Type.AD_ERROR,
        onAdError);
    adsManager.addEventListener(
        google.ima.AdEvent.Type.CONTENT_PAUSE_REQUESTED,
        onContentPauseRequested);
    adsManager.addEventListener(
        google.ima.AdEvent.Type.CONTENT_RESUME_REQUESTED,
        onContentResumeRequested);
    adsManager.addEventListener(
        google.ima.AdEvent.Type.ALL_ADS_COMPLETED,
        onAdEvent);

    try {
        // Initialize the ads manager and start playing ads
        adsManager.init(640, 360, google.ima.ViewMode.NORMAL);
        adsManager.start();
    } catch (adError) {
        // An error may be thrown if there was a problem with the VAST response
        console.error('AdsManager initialization failed:', adError);
    }
}

function onAdError(adErrorEvent) {
    console.error('Ad error:', adErrorEvent.getError());
    if (adsManager) {
        adsManager.destroy();
    }
}

function onContentPauseRequested() {
    // This function is called when the ad is about to play
    console.log('Content pause requested');
}

function onContentResumeRequested() {
    // This function is called when the ad is complete
    console.log('Content resume requested');
}

function onAdEvent(adEvent) {
    // Handle various ad events
    console.log('Ad event:', adEvent.type);
    
    if (adEvent.type === google.ima.AdEvent.Type.COMPLETE) {
        // Ad completed - notify the server
        fetch('/api/ads/claim', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                ad_type: 'video',
                impression_id: generateImpressionId()
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                showToast('success', `Earned ${data.credits} credits!`);
                updateCreditsDisplay(data.new_balance);
            } else {
                showToast('error', data.message || 'Failed to claim reward');
            }
        })
        .catch(error => {
            console.error('Error claiming reward:', error);
            showToast('error', 'Failed to claim reward');
        });
    }
}

function generateImpressionId() {
    return 'imp_' + Math.random().toString(36).substr(2, 9);
}

function showToast(type, message) {
    // Create toast element
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.innerHTML = `
        <i class="fas fa-${type === 'success' ? 'check-circle' : 'exclamation-circle'}"></i>
        <span>${message}</span>
    `;
    
    // Add to document
    document.body.appendChild(toast);
    
    // Trigger animation
    setTimeout(() => toast.classList.add('show'), 100);
    
    // Remove after delay
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

function updateCreditsDisplay(newBalance) {
    const creditsElement = document.getElementById('userCredits');
    if (creditsElement) {
        creditsElement.textContent = newBalance.toFixed(2);
    }
}

// Initialize IMA when the window loads
window.addEventListener('load', initializeIMA); 