js:
let d = [];
let bodys = {
  "access_token": "",
  "cate_id": MY_CATE,
  "identifier": "ffffffff-c67a-899b-ffff-ffffef05ac4a",
  "page": MY_PAGE,
  "region": 0,
  "type_id": 0,
  "vip": 0,
  "year": ""
};
// print(input);
// print(bodys);
var fn = rc('maomi_aes.js');
bodys = fn.En(stringify(bodys));
// print(bodys);
let obj = {
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
    },
    method: 'POST',
    // body: 'params=' + bodys + '&version=26&sign=' + CryptoJS.MD5('QEBBQADSwrXIXaNqBmMofjfRY/8Sxaxgparams' + bodys + 'version26QEBBQADSwrXIXaNqBmMofjfRY/8Sxaxg')
    body: 'params=' + bodys + '&version=26&sign=' + md5('QEBBQADSwrXIXaNqBmMofjfRY/8Sxaxgparams' + bodys + 'version26QEBBQADSwrXIXaNqBmMofjfRY/8Sxaxg')
};
// print(obj);
let api = input.split('#')[0];
let html = JSON.parse(fn.De(request(api, obj)));
// print(html);
html.data.data.forEach(function (it){
    d.push({
        title:it.name,
        img:it.image,
        desc:it.rate,
        url:api.replace('index','detail')+';'+it.id
    });
});
setResult(d);