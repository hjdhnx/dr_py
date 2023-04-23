js:
let body = input.split('#')[1];
let t = Math.round(new Date() / 1000).toString();
let key = md5("DS"+t+"DCC147D11943AF75");
let url = input.split('#')[0];
body=body+'&time='+t+'&key='+key;
print(body);
fetch_params.body = body;
let html = post(url,fetch_params);
// print(html);
let data = JSON.parse(html);
VODS = data.list;