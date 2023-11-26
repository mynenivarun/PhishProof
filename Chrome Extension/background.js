chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.contentScriptQuery === "checkPhishingUrl") {
        fetch('http://127.0.0.1:1234/check_url', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({urls: request.urls})
        })
        .then(response => response.json())
        .then(data => sendResponse({result: data}))
        .catch(error => console.error('Error:', error));
        return true;  // Will respond asynchronously
    }
});
