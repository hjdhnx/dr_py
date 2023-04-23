eval(getCryptoJS());
var a = CryptoJS.enc.Utf8.parse("625222f9149e961d");
var t = CryptoJS.enc.Utf8.parse("5efdtf6060e2o330");
function De(word) {
  word = CryptoJS.enc.Hex.parse(word)
    return CryptoJS.AES.decrypt(CryptoJS.enc.Base64.stringify(word), a, {
        iv: t,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    }).toString(CryptoJS.enc.Utf8)
}
var En = function(word) {
    // print(a);
    // print(word);
    var Encrypted = CryptoJS.AES.encrypt(word, a, {
        iv: t,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    return Encrypted.ciphertext.toString();
}
$.exports = {
    De:De,
    En:En
}