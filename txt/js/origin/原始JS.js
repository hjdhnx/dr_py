function init(ext) {
    console.log('init');
}

function home(filter) {
    console.log("home");
    let classes = [];
    classes.push({
    'type_id': 'test',
    'type_name': '测试分类'
    });
    let res = {
        'class': classes
    };
    return JSON.stringify(res);
}

function homeVod(params) {
    console.log("homeVod");
    let d = [];
    d.push({
        vod_name:'测试',
        vod_id:'index.html',
        vod_pic:'https://gitee.com/CherishRx/imagewarehouse/raw/master/image/13096725fe56ce9cf643a0e4cd0c159c.gif',
        vod_remarks:'原始JS',
    });
    return JSON.stringify({
        list:d
    })
}

function category(tid, pg, filter, extend) {
    console.log("category");
    let d = [];
    d.push({
        vod_name:'测试',
        vod_id:'index.html',
        vod_pic:'https://gitee.com/CherishRx/imagewarehouse/raw/master/image/13096725fe56ce9cf643a0e4cd0c159c.gif',
        vod_remarks:'类型:'+tid,
    });
    return JSON.stringify({
        list:d
    })
}

function detail(vod_url) {
    console.log("detail");
    let vod = {
      // vod_id:id,
      vod_name:'测试二级',
      type_name:vod_url,
      vod_pic:'https://gitee.com/CherishRx/imagewarehouse/raw/master/image/13096725fe56ce9cf643a0e4cd0c159c.gif',
      vod_content:'这是一个原始js的测试案例',
      vod_play_from:'测试线路1$$$测试线路2',
      vod_play_url:'选集播放1$1.mp4#选集播放2$2.mp4$$$选集播放3$3.mp4#选集播放4$4.mp4',
    };
    return JSON.stringify({
        list: [vod]
    })
}

function play(flag, id, flags) {
    console.log("play");
    return '{}'
}

function search(wd, quick) {
    console.log("search");
    let yzm_url = 'http://192.168.10.99:5705/static/img/yzm.png';
    console.log('测试验证码地址:',yzm_url);
    let img_base64 = req(yzm_url,{buffer:2}).content;
    console.log(img_base64);
    const res = req('http://drpy.nokia.press:8028/ocr/drpy/text', {data:{img:img_base64},method:'POST'});
    console.log('验证码识别结果:',res.content);
    let d = [];
    d.push({
        vod_name:wd,
        vod_id:'index.html',
        vod_pic:'https://gitee.com/CherishRx/imagewarehouse/raw/master/image/13096725fe56ce9cf643a0e4cd0c159c.gif',
        vod_remarks:'测试搜索',
    });
    return JSON.stringify({
        list:d
    })
}

// 导出函数对象
export default {
    init: init,
    home: home,
    homeVod: homeVod,
    category: category,
    detail: detail,
    play: play,
    search: search,
}