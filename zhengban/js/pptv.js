var CryptoJS = require("crypto-js");
// const msg = "type=mhpptv&appId=pptv.web.h5&appPlt=web&appVer=1.0.4&channel=sn.cultural&sdkVer=1.5.0&cid=23764751&allowFt=0,1,2,3&rf=0&ppi=302c393939&o=www.google.com&ahl_ver=1&ahl_random=56512723466a41555e402b327439736b&ahl_signa=9d6e29f58acde65886d26d364cb0c57145e57fcd8f430fdd3abea0795477937a&vvId=a88a33b5-5644-9435-6e95-b5f34b20c3d6&version=1&https=true&streamFormat=3"
// key = CryptoJS.enc.Hex.parse("3B4E7F4B13980C603A2936C5C3C304C85B823D8A581AA18A"); // key
// iv = CryptoJS.enc.Hex.parse("8C92E8813637F416");

function encrypted (msg, key, iv) {
    return CryptoJS.TripleDES.encrypt(msg, CryptoJS.enc.Hex.parse(key), {
        iv: CryptoJS.enc.Hex.parse(iv),
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    }).toString();
}

 function getRandomWithLen () {
    for (var t = "", i = 0; i < 16; i++) {
        var n = 93 * Math.random() + 33 >> 0;
        t += String.fromCharCode(n)
    }
    return t
}
function toHexStr (e) {
    for (var t = "", i = 0; i < e.length; i++)
        t += e.charCodeAt(i).toString(16);
    return t
}

//  function getSignatureWithKey(e){
//     var t = toHexStr(e);
//     console.log(t)
//     return stringify(t)
// }
//  function stringify(e){
//     for (var t = e.words, i = e.sigBytes, n = [], a = 0; a < i; a++) {
//         var r = t[a >>> 2] >>> 24 - a % 4 * 8 & 255;
//         n.push((r >>> 4).toString(16)),
//         n.push((15 & r).toString(16))
//     }
//     return n.join("")
// }
//  function parse(e){
//     for (var t = e.length, i = [], n = 0; n < t; n += 2)
//         i[n >>> 3] |= parseInt(e.substr(n, 2), 16) << 24 - n % 8 * 4;
//     return new s.init(i,t / 2)
// }
function get3rdKeyRandom(){
    var t = "mhpptv"
      , i = getRandomWithLen()
      , n = i;
    i += t + "-1V8oo0Or1f047NaiMTxK123LMFuINTNeI";
    var a = toHexStr(i);
    return {
        random_hex: encodeHex(n),
        signature_hex: a
    }
}
function encodeHex(e) {
    for (var t = "", i = e.length, n = 0; n < i; ++n) {
        var a = e.charCodeAt(n);
        t += "0123456789abcdef"[a >> 4],
        t += "0123456789abcdef"[15 & a]
    }
    return t
}

// const msg = "type=mhpptv&appId=pptv.web.h5&appPlt=web&appVer=1.0.4&channel=sn.cultural&sdkVer=1.5.0&cid=23764751&allowFt=0,1,2,3&rf=0&ppi=302c393939&o=www.google.com&ahl_ver=1&ahl_random=2c6944735c676e643244406266524a7c&ahl_signa=2c6944735c676e643244406266524a7c6d68707074762d3156386f6f304f7231663034374e61694d54784b3132334c4d4675494e544e6549&vvId=1ca862ac-d8eb-4ddd-86a3-daa958004eee&version=1&https=true&streamFormat=3"
// key = "3B4E7F4B13980C603A2936C5C3C304C85B823D8A581AA18A"
// iv = "8C92E8813637F416"
// console.log(encrypted(msg, key, iv).toString())
// console.log(get3rdKeyRandom())