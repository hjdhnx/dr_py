js:
pd = jsp.pd;
let url=pd(html,".bookbutton&&a&&href");
log(url);
html = request(url);
let v=pd(html,'.booksite&&script&&Html');
var document={};
var VideoListJson;
// log(v);
VideoListJson=eval(v.split('VideoListJson=')[1].split(',urlinfo')[0]);
// 截取剔除eval代码js不兼容的部分 quickjs不支持没定义变量的情况下直接赋值!!!
// v = v.split('VideoListJson=')[1].split(',urlinfo')[0];
// eval(v);
log(typeof(VideoListJson));
let list1=VideoListJson[0][1];
LISTS=[list1];
log(LISTS);