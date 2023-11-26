document.addEventListener('DOMContentLoaded', function() {
    var checkPageButton = document.getElementById('checkPage');
    checkPageButton.addEventListener('click', function() {
        // Query the current tab for the page URL
        chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
            var activeTab = tabs[0];
            chrome.tabs.sendMessage(activeTab.id, {"message": "start_scan"});
        });
    }, false);
}, false);

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.message === "scan_complete") {
        var resultText = request.result ? "Phishing links detected!" : "No phishing links detected.";
        document.getElementById('scanResult').textContent = resultText;
    }
});
