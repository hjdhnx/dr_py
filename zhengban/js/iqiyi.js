function i(e, t, n, i, a, o, s) {
    return r(t & n | ~t & i, e, t, a, o, s)
}

function a(e, t, n, i, a, o, s) {
    return r(t & i | n & ~i, e, t, a, o, s)
}

function o(e, t, n, i, a, o, s) {
    return r(t ^ n ^ i, e, t, a, o, s)
}

function r(e, t, n, r, i, a) {
    return c(function(e, t) {
        return e << t | e >>> 32 - t
    }(c(c(t, e), c(r, a)), i), n)
}
function c(e, t) {
    var n = (65535 & e) + (65535 & t);
    return (e >> 16) + (t >> 16) + (n >> 16) << 16 | 65535 & n
}

function s(e, t, n, i, a, o, s) {
    return r(n ^ (t | ~i), e, t, a, o, s)
}

function auth (e) {
    return function(e) {
        for (var t = "0123456789abcdef", n = "", r = 0; r < 4 * e.length; r++)
            n += t.charAt(e[r >> 2] >> r % 4 * 8 + 4 & 15) + t.charAt(e[r >> 2] >> r % 4 * 8 & 15);
        return n
    }(function(e, t) {
        e[t >> 5] |= 128 << t % 32,
        e[14 + (t + 64 >>> 9 << 4)] = t;
        for (var n = 1732584193, r = -271733879, u = -1732584194, d = 271733878, l = 0; l < e.length; l += 16) {
            var f = n
              , h = r
              , p = u
              , _ = d;
            n = i(n, r, u, d, e[l + 0], 7, -680876936),
            d = i(d, n, r, u, e[l + 1], 12, -389564586),
            u = i(u, d, n, r, e[l + 2], 17, 606105819),
            r = i(r, u, d, n, e[l + 3], 22, -1044525330),
            n = i(n, r, u, d, e[l + 4], 7, -176418897),
            d = i(d, n, r, u, e[l + 5], 12, 1200080426),
            u = i(u, d, n, r, e[l + 6], 17, -1473231341),
            r = i(r, u, d, n, e[l + 7], 22, -45705983),
            n = i(n, r, u, d, e[l + 8], 7, 1770035416),
            d = i(d, n, r, u, e[l + 9], 12, -1958414417),
            u = i(u, d, n, r, e[l + 10], 17, -42063),
            r = i(r, u, d, n, e[l + 11], 22, -1990404162),
            n = i(n, r, u, d, e[l + 12], 7, 1804603682),
            d = i(d, n, r, u, e[l + 13], 12, -40341101),
            u = i(u, d, n, r, e[l + 14], 17, -1502002290),
            n = a(n, r = i(r, u, d, n, e[l + 15], 22, 1236535329), u, d, e[l + 1], 5, -165796510),
            d = a(d, n, r, u, e[l + 6], 9, -1069501632),
            u = a(u, d, n, r, e[l + 11], 14, 643717713),
            r = a(r, u, d, n, e[l + 0], 20, -373897302),
            n = a(n, r, u, d, e[l + 5], 5, -701558691),
            d = a(d, n, r, u, e[l + 10], 9, 38016083),
            u = a(u, d, n, r, e[l + 15], 14, -660478335),
            r = a(r, u, d, n, e[l + 4], 20, -405537848),
            n = a(n, r, u, d, e[l + 9], 5, 568446438),
            d = a(d, n, r, u, e[l + 14], 9, -1019803690),
            u = a(u, d, n, r, e[l + 3], 14, -187363961),
            r = a(r, u, d, n, e[l + 8], 20, 1163531501),
            n = a(n, r, u, d, e[l + 13], 5, -1444681467),
            d = a(d, n, r, u, e[l + 2], 9, -51403784),
            u = a(u, d, n, r, e[l + 7], 14, 1735328473),
            n = o(n, r = a(r, u, d, n, e[l + 12], 20, -1926607734), u, d, e[l + 5], 4, -378558),
            d = o(d, n, r, u, e[l + 8], 11, -2022574463),
            u = o(u, d, n, r, e[l + 11], 16, 1839030562),
            r = o(r, u, d, n, e[l + 14], 23, -35309556),
            n = o(n, r, u, d, e[l + 1], 4, -1530992060),
            d = o(d, n, r, u, e[l + 4], 11, 1272893353),
            u = o(u, d, n, r, e[l + 7], 16, -155497632),
            r = o(r, u, d, n, e[l + 10], 23, -1094730640),
            n = o(n, r, u, d, e[l + 13], 4, 681279174),
            d = o(d, n, r, u, e[l + 0], 11, -358537222),
            u = o(u, d, n, r, e[l + 3], 16, -722521979),
            r = o(r, u, d, n, e[l + 6], 23, 76029189),
            n = o(n, r, u, d, e[l + 9], 4, -640364487),
            d = o(d, n, r, u, e[l + 12], 11, -421815835),
            u = o(u, d, n, r, e[l + 15], 16, 530742520),
            n = s(n, r = o(r, u, d, n, e[l + 2], 23, -995338651), u, d, e[l + 0], 6, -198630844),
            d = s(d, n, r, u, e[l + 7], 10, 1126891415),
            u = s(u, d, n, r, e[l + 14], 15, -1416354905),
            r = s(r, u, d, n, e[l + 5], 21, -57434055),
            n = s(n, r, u, d, e[l + 12], 6, 1700485571),
            d = s(d, n, r, u, e[l + 3], 10, -1894986606),
            u = s(u, d, n, r, e[l + 10], 15, -1051523),
            r = s(r, u, d, n, e[l + 1], 21, -2054922799),
            n = s(n, r, u, d, e[l + 8], 6, 1873313359),
            d = s(d, n, r, u, e[l + 15], 10, -30611744),
            u = s(u, d, n, r, e[l + 6], 15, -1560198380),
            r = s(r, u, d, n, e[l + 13], 21, 1309151649),
            n = s(n, r, u, d, e[l + 4], 6, -145523070),
            d = s(d, n, r, u, e[l + 11], 10, -1120210379),
            u = s(u, d, n, r, e[l + 2], 15, 718787259),
            r = s(r, u, d, n, e[l + 9], 21, -343485551),
            n = c(n, f),
            r = c(r, h),
            u = c(u, p),
            d = c(d, _)
        }
        return Array(n, r, u, d)
    }(function(e) {
        for (var t = Array(), n = 0; n < 8 * e.length; n += 8)
            t[n >> 5] |= (255 & e.charCodeAt(n / 8)) << n % 32;
        return t
    }(e), 8 * e.length))
}