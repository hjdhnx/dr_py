js:
log(TABS);
LISTS=[];
TABS.forEach(function (tab){
    if(/边下边播/.test(tab)){
    let ftp = html.data.new_ftp_list;
    let d = ftp.map(function (it){
       return it.title+'$'+(/m3u8/.test(it.url)?play_url+it.url:'tvbox-xg:'+it.url)
    });
    LISTS.push(d);
    }else if(/在线点播/.test(tab)){
    let m3u = html.data.new_m3u8_list;
    let d=m3u.map(function (it){
        return it.title+'$'+(/m3u8/.test(it.url)?play_url+it.url:'tvbox-xg:'+it.url);
    });
    LISTS.push(d);
    }
});