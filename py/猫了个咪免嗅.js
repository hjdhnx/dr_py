js:
// log(input);
let VID = input.split(';')[1];
let VURL = input.split(';')[0];
var fn = rc('maomi_aes.js');
let url = VURL + '?params='+fn.En('{"id":"' + VID + '"}');
// print(url);
input = JSON.parse(fn.De(request(url))).data.video_item[0].file;