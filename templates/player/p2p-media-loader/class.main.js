/*###########################################
# xypaly 智能视频解析整合接口 by nohacks.cn#
# 官方网站: http://nohacks.cn");           #
# 源码获取：http://nohacks.taobao.com");   #
##########################################*/
/* global define, Base64, opera, java */


//base64加密 解密

/* //1.加密  
var result = Base64.encode('125中文');  //--> "MTI15Lit5paH"
  
//2.解密  
var result2 = Base64.decode(result); //--> '125中文'
*/

~(function(root, factory) {
  if (typeof define === "function" && define.amd) {
    define([], factory);
  } else if (typeof module === "object" && module.exports) {
    module.exports = factory();
  } else {
    root.Base64 = factory();
  }
}(this, function() {
    'use strict';   //严格模式
    function Base64() {
        // private property
        this._keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
    }
      //public method for encoding
        Base64.prototype.encode = function (input) {
        var output = "", chr1, chr2, chr3, enc1, enc2, enc3, enc4, i = 0;
        input = this._utf8_encode(input);
        while (i < input.length) {
            chr1 = input.charCodeAt(i++);
            chr2 = input.charCodeAt(i++);
            chr3 = input.charCodeAt(i++);
            enc1 = chr1 >> 2;
            enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
            enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
            enc4 = chr3 & 63;
            if (isNaN(chr2)) {
                enc3 = enc4 = 64;
            } else if (isNaN(chr3)) {
                enc4 = 64;
            }
            output = output +
            this._keyStr.charAt(enc1) + this._keyStr.charAt(enc2) +
            this._keyStr.charAt(enc3) + this._keyStr.charAt(enc4);
        }
        return output;
    };

    // public method for decoding
    Base64.prototype.decode = function (input) {
        var output = "", chr1, chr2, chr3, enc1, enc2, enc3, enc4, i = 0;
        input = input.replace(/[^A-Za-z0-9\+\/\=]/g, "");
        while (i < input.length) {
            enc1 = this._keyStr.indexOf(input.charAt(i++));
            enc2 = this._keyStr.indexOf(input.charAt(i++));
            enc3 = this._keyStr.indexOf(input.charAt(i++));
            enc4 = this._keyStr.indexOf(input.charAt(i++));
            chr1 = (enc1 << 2) | (enc2 >> 4);
            chr2 = ((enc2 & 15) << 4) | (enc3 >> 2);
            chr3 = ((enc3 & 3) << 6) | enc4;
            output = output + String.fromCharCode(chr1);
            if (enc3 !== 64) {
                output = output + String.fromCharCode(chr2);
            }
            if (enc4 !== 64) {
                output = output + String.fromCharCode(chr3);
            }
        }
        output = this._utf8_decode(output);
        return output;
    };

    // private method for UTF-8 encoding
    Base64.prototype._utf8_encode = function (string) {
        string = string.replace(/\r\n/g,"\n");
        var utftext = "";
        for (var n = 0; n < string.length; n++) {
            var c = string.charCodeAt(n);
            if (c < 128) {
                utftext += String.fromCharCode(c);
            } else if((c > 127) && (c < 2048)) {
                utftext += String.fromCharCode((c >> 6) | 192);
                utftext += String.fromCharCode((c & 63) | 128);
            } else {
                utftext += String.fromCharCode((c >> 12) | 224);
                utftext += String.fromCharCode(((c >> 6) & 63) | 128);
                utftext += String.fromCharCode((c & 63) | 128);
            }
    
        }
        return utftext;
    };

    // private method for UTF-8 decoding
    Base64.prototype._utf8_decode = function (utftext) {
        var string = "", i = 0, c = 0, c1 = 0, c2 = 0, c3 = 0;
        while ( i < utftext.length ) {
            c = utftext.charCodeAt(i);
            if (c < 128) {
                string += String.fromCharCode(c);
                i++;
            } else if((c > 191) && (c < 224)) {
                c2 = utftext.charCodeAt(i+1);
                string += String.fromCharCode(((c & 31) << 6) | (c2 & 63));
                i += 2;
            } else {
                c2 = utftext.charCodeAt(i+1);
                c3 = utftext.charCodeAt(i+2);
                string += String.fromCharCode(((c & 15) << 12) | ((c2 & 63) << 6) | (c3 & 63));
                i += 3;
            }
        }
        return string;
    };
    
    var Base64 = new Base64();
    
    return Base64;
}));


/*   代码加密        */  
  function encode(code){
	 'use strict';   //严格模式
     var c= String.fromCharCode(code.charCodeAt(0)+code.length);
	 for(var i=1;i<code.length;i++){	     
	   c+=String.fromCharCode(code.charCodeAt(i)+code.charCodeAt(i-1));		 
     }
       return escape(c);
   
  }

 /*   代码解密         */  
  function decode(code){	  
	  'use strict';   //严格模式
	   code=unescape(code);
	   var c= String.fromCharCode(code.charCodeAt(0)-code.length);
	   for(var i=1;i<code.length;i++){	     
	   c+=String.fromCharCode(code.charCodeAt(i)-code.charCodeAt(i-1));		 
     }
      return c ;
   } 
	  
 /*   文本加解密         */ 
 function strdecode(string,encode,key){
	   'use strict';   //严格模式
	   encode=encode||false; key=key||'xyplay';
	   var len=key.length; var code=''; var k='';
	   if(encode){string=Base64.encode(string);}else{string=Base64.decode(string);};
	   for(var i=0;i<string.length;i++){		   
	      k=i % len;  
		 code+= String.fromCharCode(string.charCodeAt(i)^key.charCodeAt(k));		   
	   };
	   if(encode){return Base64.encode(code);}else{return Base64.decode(code);};
    }

//取网址参数
function _GET(name,isurl) { 
    isurl=isurl || false;
	var word="(^|&)" + name + "=([^&]*)(&|$)";
	if(isurl){word="(^|&)" + name + "=(.*?)$";}	
	var reg = new RegExp(word, "i");
    var r = window.location.search.substr(1).match(reg);
    if (r !== null) {
        return decodeURI(r[2]);
    };
    return "";
}

 function removeHTMLTag(str,all){      
             var str=str.replace(/&quot;/g, '"');  //引号html编码转换
             str=str.replace(/\+/g," ");//恢复转码的"+"为空格            
            str = str.replace(/[ | ]*\n/g,'\n'); //去除行尾空白
            str = str.replace(/\n[\s| | ]*\r/g,'\n'); //去除多余空行 	
            //str=str.replace(/ /ig,'');//去掉所有空格      
            if(all){str = str.replace(/<\/?.*?$/g,'');}else{str.replace(/<[^>]+>/g,"");}
            return str;
    };

//搜索有分割符的字符串否在指定文本中存在,成功返回真，失败返回假。
//参数：搜索字符串，待搜索文本,分隔符,默认"|"
function isurl(flag, word,split) {
    if (!flag || !word) {
        return false;
    }
    var strs = new Array();	
	spli=!split ? "|":split;
	strs = flag.split(split);
    for (var i = 0; i < strs.length; i++) {
        if (word.indexOf(strs[i]) > -1) {
            return true;
        }
    }
    return false;
};



//设置浏览器缓存项值，参数：项名,值,有效时间(小时)
function setCookie(c_name, value, expireHours) {
    var exdate = new Date();
    exdate.setHours(exdate.getHours() + expireHours);
    document.cookie = c_name + "=" + escape(value) + ((expireHours === null) ? "" : ";expires=" + exdate.toGMTString());
}
//获取浏览器缓存项值，参数：项名
function getCookie(c_name) {
    if (document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start !== -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end === -1) {
                c_end = document.cookie.length;
            };
            return unescape(document.cookie.substring(c_start, c_end));
        }
    }
    return '';
}

//判断设备类型
function is_mobile() {
    var regex_match = /(nokia|iphone|android|motorola|micromessenger|^mot-|softbank|foma|docomo|kddi|up.browser|up.link|htc|dopod|blazer|netfront|helio|hosin|huawei|novarra|CoolPad|webos|techfaith|palmsource|blackberry|alcatel|amoi|ktouch|nexian|samsung|^sam-|s[cg]h|^lge|ericsson|philips|sagem|wellcom|bunjalloo|maui|symbian|smartphone|midp|wap|phone|windows ce|iemobile|^spice|^bird|^zte-|longcos|pantech|gionee|^sie-|portalmmm|jigs browser|hiptop|^benq|haier|^lct|operas*mobi|opera*mini|320x320|240x320|176x220)/i;
    var u = navigator.userAgent;
    if (null === u) {
        return true;
    }
    var result = regex_match.exec(u);
    if (null === result) {
        return false;
    } else {
        return true;
    }
};

//时间文本到微妙时间
function is_time(time){
      if("undefined" !==typeof time && time!==null){
       var r = (/^(\d+)(.*?)$/i).exec(time);
       if(!r|| r.length < 2){return 0;}
       switch(r[2]){ 
          case "d":                   
            return r[1]*24*60*60*1000;
           case "h":                   
            return r[1]*60*60*1000; 
          case "m":                   
             return r[1]*60*1000;
          case "s":                   
             return r[1]*1000;       
          case "ms":                   
             return r[1];        
         default:  
              return r[1]*1000;  
       }    
      
        }else{
           return -1; 
       }
      
  }
//取随机数
function random(min, max) {
     min = Math.ceil(min);
     max = Math.floor(max);
     return Math.floor(Math.random() * (max - min + 1)) + min;
 }

//取随机颜色
 function random_rgb(min,max){
	 min=min||0;
	 max=max||256;
     var r=random(min,max);
     var g=random(min,max);
     var b=random(min,max);
     return "rgb("+r+','+g+','+b+")";
    }
//调试输出兼容代码
function log(message,off) {

  if (typeof console === 'object') {
    console.log(message);
  } else if (typeof opera === 'object') {
    opera.postError(message);
  } else if (typeof java === 'object' && typeof java.lang === 'object') {
    java.lang.System.out.println(message);
  }
}


function open_without_referrer(link){
document.body.appendChild(document.createElement('iframe')).src='javascript:"<script>top.location.replace(\''+link+'\')<\/script>"';
}

//出错友好提示
 function fnErrorTrap(msg,url,line){

       errinfo={type:"xyplay_error",msg:msg,url:url,line:line,ua:navigator.userAgent}; 

       document.write('<div style="margin-top:90px;text-align:center;"><font color=\'#ff0000\'>哎呀，这是彩蛋，BUG君被你发现了！&nbsp;&nbsp;<a  href="javascript:;" onClick="copy_errinfo()" >来抓我</a>');
 }
 
     //复制内容到剪切板
       function copy_errinfo ()
      {
        var oInput = document.createElement('input');
        oInput.value = JSON.stringify(errinfo);
        document.body.appendChild(oInput);
        oInput.select(); // 选择对象
        document.execCommand("Copy"); // 执行浏览器复制命令
        oInput.className = 'oInput';
        oInput.style.display='none';
        alert('成功捕获野生BUG君，粘贴打包给它主人有奖励哟!');
     };


// 反调试函数,参数：开关，执行代码
function endebug(off,code){
if (off==="0") {
    ! function(e) {
        function n(e) {
            function n() {
                return u;
            }

            function o() {
               
		window.Firebug && window.Firebug.chrome && window.Firebug.chrome.isInitialized ? t("on") : (a = "off", console.log(d), ("undefined"!==typeof console.clear) && console.clear(),t(a));
            }

            function t(e) {
                u !== e && (u = e, "function" === typeof c.onchange && c.onchange(e));
            }

            function r() {
                l || (l = !0, window.removeEventListener("resize", o), clearInterval(f));
            }
            "function" === typeof e && (e = {
                onchange: e
            });
            var i = (e = e || {}).delay || 500,
                c = {};
            c.onchange = e.onchange;
            var a, d = new Image;
            d.__defineGetter__("id", function() {
                a = "on";
            });
            var u = "unknown";
            c.getStatus = n;
            var f = setInterval(o, i);
            window.addEventListener("resize", o);
            var l;
            return c.free = r, c;
        }
        var o = o || {};
        o.create = n, "function" === typeof define ? (define.amd || define.cmd) && define(function() {
            return o;
        }) : "undefined" !== typeof module && module.exports ? module.exports = o : window.jdetects = o;
    }(), jdetects.create(function(e) {
        var a = 0;
        var n = setInterval(function() {
            if ("on" === e) {
                setTimeout(function() {
                    if (a ===0) {
                        a = 1;						                   						 
			 setTimeout(Base64.decode(code));											
                    }
                }, 200);
            }
        }, 100);
    });
};
}



   
   