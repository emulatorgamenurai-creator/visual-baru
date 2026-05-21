/**
 * Returns true if the text cookie is set, false otherwise.
 */
function authFlowTestCookieSet() {
    return getCookie(AUTH_FLOW_TEST_COOKIE_NAME) === COOKIE_VALUE;
}

/**
 * Redirects to the return url. If autoClose is true, then the return url will be opened in a
 * new window, and it will be closed automatically when the page loads.
 */
async function redirectToReturnUrl(autoClose, storageAccessGranted = false) {
    const initialReturnUrl = new URLSearchParams(window.location.search).get('return_url');
    const returnUrl = initialReturnUrl ? new URL(initialReturnUrl) : null;

    if (returnUrl && returnUrl.protocol.toLowerCase() === 'javascript:') {
        console.error('Potentially malicious return URL blocked!');
        return;
    }

    if (storageAccessGranted) {
        returnUrl.searchParams.set('__storage_access_granted', '1');
    }

    if (autoClose) {
        returnUrl.searchParams.set('__auto_close', '1');
        const url = new URL(window.location.href);
        url.searchParams.set('return_url', returnUrl.toString());
        window.open(url.toString(), '_blank');
        const hasAccess = await document.hasStorageAccess();
        document.querySelector('#stepOne').classList.add('hidden');
        if (hasAccess) {
            document.querySelector('#stepThree').classList.remove('hidden');
        } else {
            window.location.reload();
        }
    } else {
        window.location.href = returnUrl.toString();
    }
}

/**
 * Grants the browser permission to set cookies.
 */
async function grantStorageAccess() {
    try {
        await document.requestStorageAccess();
        redirectToReturnUrl(false, /* storageAccessGranted= */ true);
    } catch (err) {
        console.log('Error after button click: ', err);
    }
}

/**
 * Verifies that the browser can set cookies.
 */
function verifyCanSetCookies() {
    if (authFlowTestCookieSet()) {
        const returnUrl = new URLSearchParams(window.location.search).get('return_url');
        const autoClose = new URL(returnUrl).searchParams.has('__auto_close');
        if (autoClose) {
            document.querySelector('#stepOne').classList.add('hidden');
            document.querySelector('#stepTwo').classList.remove('hidden');
        } else {
            redirectToReturnUrl(false);
            return;
        }
    }
    document.querySelector('.logo').classList.add('hidden');
    document.querySelector('.spinner').classList.add('hidden');
    document.querySelector('#errorUi').classList.remove('hidden');
}
