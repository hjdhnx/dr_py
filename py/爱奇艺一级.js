js:
let d = []; // 一级固定返回VODS变量,内置变量有 MY_CATE,detailUrl,setResult用法跟海阔相同
if(MY_CATE==='16'){//网络电影
    input = input.replace("channel_id=16", "channel_id=1").split("three_category_id")[0];
    input+= "three_category_id=27401";
    // input+= "three_category_id=27401;must,地区;must,类型;must,规格;must";
}else if(MY_CATE==='5'){//音乐
    input = input.replace("data_type=1", "data_type=2");
}
// let html = fetch(input,fetch_params);
let html = request(input);
let json = JSON.parse(html);
if (json.code === "A00003") {
    fetch_params.headers['user-agent'] = PC_UA;
    // print(fetch_params);
    json = JSON.parse(fetch(input,fetch_params));
}
// print(json);
json.data.list.forEach(function (data){
    if (data.channelId === 1) {
        desc = (data.hasOwnProperty("score") ? data.score + "分\t" : '');
    } else if (data.channelId === 2 || data.channelId === 4) {
        if (data.latestOrder === data.videoCount) {
            desc = (data.hasOwnProperty("score") ? data.score + "分\t" : '') + data.latestOrder + "集全";
        } else {
            if (data.videoCount) {
                desc = (data.hasOwnProperty("score") ? data.score + "分\t" : '') + data.latestOrder + "/" + data.videoCount + "集";
            } else {
                desc = "更新至 " + data.latestOrder + "集"
            }
        }
    } else if (data.channelId === 6) {
        desc = data.period + "期";
    } else if (data.channelId === 5) {
        desc = data.focus;
    } else {
        if (data.latestOrder) {
            desc = "更新至 第" + data.latestOrder + "期";
        } else if (data.period) {
            desc = data.period;
        } else {
            desc = data.focus;
        }
    }
     // url = "https://pcw-api.iqiyi.com/video/video/videoinfowithuser/" + data.albumId + "?agent_type=1&authcookie=&subkey=" + data.albumId + "&subscribe=1";
    url = MY_CATE +'$'+data.albumId;
    // d.push({
    //     vod_id:url,
    //     vod_name: data.name,
    //     vod_remarks: desc,
    //     vod_pic: data.imageUrl.replace('.jpg', '_390_520.jpg?caplist=jpg,webp'),
    // });
    d.push({
        url:url,
        title: data.name,
        desc: desc,
        pic_url: data.imageUrl.replace('.jpg', '_390_520.jpg?caplist=jpg,webp'),
    });
});
// VODS = d;
setResult(d);