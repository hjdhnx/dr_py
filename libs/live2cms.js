/**
 * live2cms.js
 * 配置设置 {"key":"Live2Mv","name":"直播转点播","type":3,"api":"http://drpy.nokia.press/libs/live2mv.js","searchable":2,"quickSearch":0,"filterable":0,"ext":"http://drpy.nokia.press/txt/json/live2mv_data.json"}
 * alist.json
[
{"name": "甜蜜",     "url": "http://zdir.kebedd69.repl.co/public/live.txt"},
{"name": "巧计",     "url": "https://ghproxy.net/https://raw.githubusercontent.com/dxawi/1/main/tvlive.txt"},
{"name": "星辰",     "url": "http://tvmvip.com/xclive.txt"},
{"name": "俊于",     "url": "http://home.jundie.top:81/Cat/tv/live.txt"},
{"name": "多多",     "url": "https://yydsys.top/duo/txt/v.txt"},
{"name": "菜妮丝",     "url": "http://xn--ihqu10cn4c.xn--z7x900a.love:63/TV/tvzb.txt"},
{"name": "乱世",     "url": "http://www.dmtv.ml/mao/live/m3u.txt"},
{"name": "吾爱",     "url": "http://52bsj.vip:81/api/v3/file/get/763/live.txt?sign=87BTGT1_6AOry7FPwy_uuxFTv2Wcb9aDMj46rDdRTD8%3D%3A0"},
{"name": "饭太硬",     "url": "http://ftyyy.tk/live.txt"}
]

 * 提示 ext文件格式为json列表,name,url参数
 *	取消加密,减少性能问题
 */
String.prototype.rstrip = function (chars) {
	let regex = new RegExp(chars + "$");
	return this.replace(regex, "");
};
const request_timeout = 5000;
const VERSION = 'live2cms 20230616';
const UA = 'Mozilla/5.0'; //默认请求ua
const __ext = {data_dict:{}};
/**
 * 打印日志
 * @param any 任意变量
 */
function print(any){
	any = any||'';
	if(typeof(any)=='object'&&Object.keys(any).length>0){
		try {
			any = JSON.stringify(any);
			console.log(any);
		}catch (e) {
			// console.log('print:'+e.message);
			console.log(typeof(any)+':'+any.length);
		}
	}else if(typeof(any)=='object'&&Object.keys(any).length<1){
		console.log('null object');
	}else{
		console.log(any);
	}
}

/*** js自封装的方法 ***/

/**
 * 获取链接的host(带http协议的完整链接)
 * @param url 任意一个正常完整的Url,自动提取根
 * @returns {string}
 */
function getHome(url){
	if(!url){
		return ''
	}
	let tmp = url.split('//');
	url = tmp[0] + '//' + tmp[1].split('/')[0];
	try {
		url = decodeURIComponent(url);
	}catch (e) {}
	return url
}

const http = function (url, options = {}) {
	if(options.method ==='POST' && options.data){
		options.body = JSON.stringify(options.data);
		options.headers = Object.assign({'content-type':'application/json'}, options.headers);
	}
	options.timeout = request_timeout;
	if(!options.headers){
		options.headers = {};
	}
	let keys = Object.keys(options.headers).map(it=>it.toLowerCase());
	if(!keys.includes('referer')){
		options.headers['Referer'] = getHome(url);
	}
	if(!keys.includes('user-agent')){
		options.headers['User-Agent'] = UA;
	}
	console.log(JSON.stringify(options.headers));
	try {
		const res = req(url, options);
		// if(options.headers['Authorization']){
		// 	console.log(res.content);
		// }
		res.json = () => res&&res.content ? JSON.parse(res.content) : null;
		res.text = () => res&&res.content ? res.content:'';
		return res
	}catch (e) {
		return {
			json() {
				return null
			}, text() {
				return ''
			}
		}
	}
};
["get", "post"].forEach(method => {
    http[method] = function (url, options = {}) {
        return http(url, Object.assign(options, {method: method.toUpperCase()}));
    }
});

function init(ext) {
	console.log("当前版本号:"+VERSION);
	let data;
	if (typeof ext == 'object'){
		data = ext;
		print('live ext:object');
	} else if (typeof ext == 'string') {
		if (ext.startsWith('http')) {
			let ext_paramas = ext.split(';');
			let data_url = ext_paramas[0];
			print(data_url);
			data = http.get(data_url).json();
			print('live ext:json string');
			data = JSON.parse(ext);
		}
	}
    print(data);
    __ext.data = data;
	print('init执行完毕');
}

function home(filter) {
	let classes = __ext.data.map(it => ({
		type_id: it.url,
		type_name: it.name,
	}));
	print("----home----");
	print(classes);
	return JSON.stringify({ 'class': classes});
}

function homeVod(params) {
	let _get_url = __ext.data[0].url;
	let html = http.get(_get_url).text();
    let arr = html.match(/.*?,#[\s\S].*?#/g);
	let _list = [];
	try {
		arr.forEach(it=>{
			_list.push({
				vod_name:it.split(',')[0],
				vod_id:_get_url+'$'+it.split(',')[0],
				// vod_pic:'https://avatars.githubusercontent.com/u/97389433?s=120&v=4',
				vod_remarks:it.split(',')[1],
			});
		});
	}catch (e) {
		print('Live2mv获取首页推荐发送错误:'+e.message);
	}
	return JSON.stringify({ 'list': _list });
}

function category(tid, pg, filter, extend) {
    let _get_url = tid;
    let html;
    if(__ext.data_dict[_get_url]){
        html = __ext.data_dict[_get_url];
    }else{
        html = http.get(_get_url).text();
        __ext.data_dict[_get_url] = html;
    }
    let arr = html.match(/.*?,#[\s\S].*?#/g);
    let _list = [];
	try {
		arr.forEach(it=>{
			_list.push({
				vod_name:it.split(',')[0],
				vod_id:_get_url+'$'+it.split(',')[0],
				// vod_pic:'https://avatars.githubusercontent.com/u/97389433?s=120&v=4',
				vod_remarks:it.split(',')[1],
			});
		});
	}catch (e) {
		print('Live2mv获取首页推荐发送错误:'+e.message);
	}

	return JSON.stringify({
		'page': 1,
		'pagecount': 1,
		'limit': _list.length,
		'total': _list.length,
		'list': _list,
	});
}

function detail(tid) { // ⛵  港•澳•台
    let _get_url = tid.split('$')[0];
    let _tab = tid.split('$')[1];
    let html;
    if(__ext.data_dict[_get_url]){
        html = __ext.data_dict[_get_url];
    }else{
        html = http.get(_get_url).text();
        __ext.data_dict[_get_url] = html;
    }
    let a = new RegExp(`.*?${_tab},#[\\s\\S].*?#`);
    let b = html.match(a)[0];
    let c = html.split(b)[1];
    if(c.match(/.*?,#[\s\S].*?#/)){
        let d = c.match(/.*?,#[\s\S].*?#/)[0];
        c = c.split(d)[0];
    }
    let arr = c.trim().split('\n');
    let _list = [];
    arr.forEach((it)=>{
        if(it.trim()){
            let t = it.trim().split(',')[0];
            let u = it.trim().split(',')[1];
            _list.push(t+'$'+u);
        }
    });
    let vod_name = __ext.data.find(x=>x.url===_get_url).name;
    let vod_play_url = _list.join('#');
    let vod = {
        vod_id: tid,
        vod_name: _tab,
        type_name: "直播列表",
        vod_pic: "https://avatars.githubusercontent.com/u/97389433?s=120&v=4",
        vod_content: tid,
        vod_play_from: vod_name,
        vod_play_url: vod_play_url,
        vod_remarks: `道长直播转点播js-当前版本${VERSION}`,
    };

    return JSON.stringify({
        list: [vod]
    });
}

function play(flag, id, flags) {
    let vod = {
		'parse': /m3u8/.test(id)?0:1,
		'playUrl': '',
		'url': id
	};
    print(vod);
	return JSON.stringify(vod);
}

function search(wd, quick) {
	return JSON.stringify({
			'list': []
    });
}

// 导出函数对象
export default {
	init: init,
	home: home,
	homeVod: homeVod,
	category: category,
	detail: detail,
	play: play,
	search: search
}