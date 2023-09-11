function closeclick() {
    document.getElementById('note').style.display = 'none';
    setSessionStorage("note", 1)
}
function clickclose() {
    noteStatus = getSessionStorage('note')
    console.log(noteStatus);
    if (noteStatus && Number(noteStatus) == 1) {
        document.getElementById('note').style.display = 'none';
    } else {
        document.getElementById('note').style.display = 'block';
    }

}
function setSessionStorage(key, val) {
    window.sessionStorage.setItem(key, val);
}
function getSessionStorage(key) {
    return window.sessionStorage.getItem(key);
}
// window.onload = clickclose;