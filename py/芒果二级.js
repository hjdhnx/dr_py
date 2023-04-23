js:
// log(input);
fetch_params.headers.Referer = 'https://www.mgtv.com';
fetch_params.headers['User-Agent'] = UA;
pdfh = jsp.pdfh;
pdfa = jsp.pdfa;
pd = jsp.pd;
VOD = {};
let d = [];
let html = request(input);
let json = JSON.parse(html);
let host = 'https://www.mgtv.com';
let ourl = json.data.list.length>0?json.data.list[0].url:json.data.series[0].url;
if(!/^http/.test(ourl)){
    ourl = host+ourl
}
// print(ourl);
fetch_params.headers['User-Agent'] = MOBILE_UA;
html = request(ourl);
if(html.includes('window.location =')){
    print('开始获取ourl');
    ourl = pdfh(html,'meta[http-equiv=refresh]&&content').split('url=')[1];
    print('获取到ourl:'+ourl);
    html = request(ourl);
}
//影片信息
try{
    // print(html);
    let details = pdfh(html, '.m-details&&Html').replace(/h1>/,'h6>').replace(/div/g, 'br');//详情网页
    print(details);
    let actor='',director='',time='';
    if (/播出时间/.test(details)) {
        actor = pdfh(html, 'p:eq(5)&&Text').substr(0,25);
        director = pdfh(html, 'p:eq(4)&&Text');
        time = pdfh(html, 'p:eq(3)&&Text');
    }else{
        actor = pdfh(html, 'p:eq(4)&&Text').substr(0,25);
        director = pdfh(html, 'p:eq(3)&&Text');
        time = '已完结';
    }
    let _img = pd(html,'.video-img&&img&&src');
    let JJ = pdfh(html,'.desc&&Text').split("简介：")[1];//简介
    let _desc = time;//更新，时间

     VOD.vod_name = pdfh(html, '.vt-txt&&Text');
     VOD.type_name = pdfh(html, 'p:eq(0)&&Text').substr(0,6);
     VOD.vod_area = pdfh(html, 'p:eq(1)&&Text');
     VOD.vod_actor = actor;
     VOD.vod_director = director;
     VOD.vod_remarks = _desc;
     VOD.vod_pic = _img;
     VOD.vod_content = JJ;
}catch(e){
    log('获取影片信息发生错误:'+e.message);
}
// print(VOD);
function getRjpg(imgUrl,xs){
    xs = xs||3;
    let picSize = /jpg_/.test(imgUrl)?imgUrl.split('jpg_')[1].split('.')[0]:false;
    let rjpg = false;
    if(picSize){
        let a = parseInt(picSize.split('x')[0])*xs;
        let b = parseInt(picSize.split('x')[1])*xs;
        rjpg = a+'x'+b+'.jpg';
    }
    let img = /jpg_/.test(imgUrl)&&rjpg?imgUrl.replace(imgUrl.split('jpg_')[1],rjpg):imgUrl;
    return img
}
// log(json.data.total+","+json.data.list.length);
if (json.data.total === 1 && json.data.list.length===1) {
    let data= json.data.list[0];
    let url = 'https://www.mgtv.com' + data.url;
    d.push({
        title: data.t4,
        desc: data.t2,
        pic_url:getRjpg(data.img),
        url: url,
    });
} else if(json.data.list.length>1){
    for (let i = 1; i <= json.data.total_page; i++) {
        if (i > 1) {
            json = JSON.parse(fetch(input.replace('page=1', 'page=' + i), {}));
        }
        json.data.list.forEach(function (data){
            let url = 'https://www.mgtv.com' + data.url;
            if (data.isIntact == '1') {
                d.push({
                    title: data.t4,
                    desc: data.t2,
                    pic_url: getRjpg(data.img),
                    url: url,
                });
            }
        });
    }
}else{
    print(input+'暂无片源');
}
VOD.vod_play_from = 'mgtv';
VOD.vod_play_url = d.map(function (it){
    return it.title + '$' + it.url;
}).join('#');
setResult(d);