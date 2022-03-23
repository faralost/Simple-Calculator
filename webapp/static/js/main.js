async function onClick(event) {
    event.preventDefault()
    const a = parseInt(document.getElementById('A').value)
    const b = parseInt(document.getElementById('B').value)
    const data = {"A": a, "B": b}
    const url = event.target.dataset.url
    const settings = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json; charset=utf-8',
            "X-CSRFToken": getCookie("csrftoken")
        },
        body: JSON.stringify(data)
    };
    let alert = document.getElementById('alert')
    const response = await fetch(url, settings)
    let answer = await response.json()
    if (response.status === 400) {
        alert.innerText = answer.error
        alert.className = 'alert alert-danger mt-4'
    } else {
        alert.innerText = answer.answer
        alert.className = 'alert alert-success mt-4'
    }
}

function onLoad() {
    const buttons = document.querySelectorAll('.btn')
    buttons.forEach(function (currentBtn) {
        currentBtn.addEventListener('click', onClick)
    })
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

window.onload = onLoad