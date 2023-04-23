js:
let bodys = {"keyword":KEY,"page":MY_PAGE};
var fn = rc('maomi_aes.js');
bodys = fn.En(stringify(bodys));
let url = input.split('#')[0];
print(url);
var html = JSON.parse(fn.De(request(url+bodys)));
let d = html.data.data.map(function (data){
    return {
        title: data.video_name,
        img: data.image,
        desc:data.rate,
        url: 'http://119.28.59.69:8089/api/video/detail?params=;'+fn.En('{"id":"'+data.video_id+'"}'),
    }
});
setResult(d);