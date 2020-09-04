window.deleteItem = function (url, token) {
    if (!confirm('are u sure?')) {
        return;
    }
    return fetch(url, {
        method: 'delete',
        headers: {
            'csrfmiddlewaretoken' : token
        }
    }).then((response) => {
        response.json()
        window.location.reload()
    })
}
