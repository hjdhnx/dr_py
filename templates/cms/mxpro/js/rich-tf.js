(function () {
    function IsPC() {
        var userAgentInfo = window.navigator.userAgent;
        var flag = true;
        if (userAgentInfo.indexOf('Mobile') != -1 || screen.width <= 750) {
            flag = false;
        }
        return flag;
    }
    var dom = document.getElementById('richid');
    var data = document.getElementById('richid').getAttribute('data')
    if (dom) {
        if (IsPC()) {
            var sp = document.createElement('script');
            sp.src = '//pc.stgowan.com/pc_w/m_rich.js';
            sp.id = 'richdata';
            sp.charset = 'utf-8';
            sp.setAttribute('data', data);
            if (data=='s=6871'||data=='s=7689'||data=='s=8227') {
                window.onload = function () {
                    document.body.appendChild(sp);
                }
            } else {
                document.body.appendChild(sp);
            }
        }
    }
})()