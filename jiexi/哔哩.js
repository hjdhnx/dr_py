// print(env);
// vipUrl = 'https://www.bilibili.com/bangumi/play/ep704873';
fetch_params.headers = {
        'User-Agent':PC_UA,
        "Referer": "https://www.bilibili.com",
        "Cookie":env.bili_cookie||''
};
let appkey = env.appkey||'';
let access_key = env.access_key||'';
// print(fetch_params);

function getEpUrl(ssUrl){
let html = request(ssUrl);
let short_link = html.match(/short_link(.*?),/)[1];
short_link = short_link.split(':').slice(1,-1).join('"').split('"')[1];
let epUrl = unescape(short_link);
return epUrl
}

function getCidEid(vipUrl){
// print(vipUrl);
let url = vipUrl.split('?')[0];
// print(url);
if(url.endsWith('/')){
url = url.slice(0,-1);
}
if(url.includes('bilibili.com/video/')){
let r = request(vipUrl);
try{
let mtext = r.match(/window\.__INITIAL_STATE__=(.*?);\(function/)[1];
mtext = JSON.parse(mtext);
let avid = mtext['aid'];
let bvid = mtext['bvid'];
let cid = mtext['videoData']['cid'];
return [cid,avid,bvid]
} catch (e) {
return null
}

}else if(url.includes('/ep')){
let epid = url.split('ep')[1];
let data_url = 'https://api.bilibili.com/pgc/view/web/season?ep_id='+epid;
let r = JSON.parse(request(data_url));
if(r.code === 0){
let episodes = r['result']['episodes'];
let furl = url.replace('https://m.bilibili.com', 'https://www.bilibili.com');
let now_ep = episodes.filter(function (it){
return [it['short_link'], it['share_url'],it['link']].includes(furl)
})[0];
let avid = now_ep['aid'];
let cid = now_ep['cid'];
return [cid,avid,null];
}else{
return null
}
}else if(url.includes('/ss')){
let epUrl = getEpUrl(vipUrl);
return getCid(epUrl)
}else{
return null
}
}
if(!/bilibili/.test(vipUrl)){
   realUrl = vipUrl;
}else {
        try {
// print(vipUrl);
                let ids = getCidEid(vipUrl);
                if (Array.isArray(ids)) {
                        print(ids);
                        let cid = ids[0];
                        let avid = ids[1];
                        let rurl = "https://api.bilibili.com/x/player/playurl?avid=" + avid + "&cid=" + cid + "&qn=120&type=&128=128&otype=json&fnver=&fourk=1&mid=&appkey=" + appkey + "&access_key=" + access_key;
                        print(rurl);
                        try {
                                let r = JSON.parse(request(rurl));
                                print(r);
                                let purl = r['data']['durl'][0]['url'];
                                print('purl:' + purl);
                                // realUrl = purl;
                                // https://upos-szbyjkm8g1.bilivideo.com
                                realUrl = purl.replace(/.*bilivideo.*?\/(.*)/,'https://upos-szbyjkm8g1.bilivideo.com/$1');

                        } catch (e) {
                                print(e.message);
                                realUrl = vipUrl;
                        }
                } else {
                        realUrl = vipUrl;
                }
        } catch (e) {
                print(e.message);
        }
}