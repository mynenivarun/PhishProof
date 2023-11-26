function getAllLinks() {
    return Array.from(document.links).map(link => link.href);
}

function highlightPhishingLinks(phishingLinks) {
    document.links.forEach(link => {
        if (phishingLinks.includes(link.href)) {
            link.style.border = '2px solid red';
            link.style.backgroundColor = 'yellow';
        }
    });
}

chrome.runtime.sendMessage({
    contentScriptQuery: "checkPhishingUrl",
    urls: getAllLinks()
}, response => {
    const phishingUrls = Object.entries(response.result).filter(([url, isPhishing]) => isPhishing).map(([url]) => url);
    if (phishingUrls.length > 0) {
        highlightPhishingLinks(phishingUrls);
    }
});
