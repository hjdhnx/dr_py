const copyrightComponent = {
	template:`
<div class="container">
			<div class="row">
			<div class="stui-foot clearfix">
			<p class="text-center hidden-xs">本网站只提供web页面服务，并不提供资源存储，也不参与录制、上传<br>若本站收录的节目无意侵犯了贵司版权，请发邮件至5imv@protonmail.com （我们会在3个工作日内删除侵权内容，谢谢。）</p>
			<p class="text-center hidden-xs">
			t5imv.cc 版权所有 联系邮箱：<a href="mailto:{maccms:email}">5imv@protonmail.com</a></p>
			<p class="text-muted text-center visible-xs">Copyright © 2008-2023&nbsp;技术支持:<a :href="path" target="_blank">{[web_name]}</a>&nbsp;</p>
			<p class="text-muted text-center hidden-xs">
			<a class="fed-font-xiv" href="/rss.xml" target="_blank">RSS订阅</a>
			<span class="fed-font-xiv"> - </span>
			<a class="fed-font-xiv" href="/rss/baidu.xml" target="_blank">百度蜘蛛</a>
			<span class="fed-font-xiv"> - </span>
			<a class="fed-font-xiv" href="/rss/google.xml" target="_blank">谷歌地图</a>
			<span class="fed-font-xiv"> - </span>
			<a class="fed-font-xiv" href="/rss/sm.xml" target="_blank">神马爬虫</a>
			<span class="fed-font-xiv fed-hide-xs"> - </span>
			<a class="fed-font-xiv fed-hide-xs" href="/rss/sogou.xml" target="_blank">搜狗蜘蛛</a>
			<span class="fed-font-xiv fed-hide-xs"> - </span>
			<a class="fed-font-xiv fed-hide-xs" href="/rss/so.xml" target="_blank">奇虎地图</a>
			<span class="fed-font-xiv fed-hide-xs"> - </span>
			<a class="fed-font-xiv fed-hide-xs" href="/rss/bing.xml" target="_blank">必应爬虫</a>
			</p>
			</div>
			</div>
</div>
			`,
			setup(props, context) {
				console.log('copyright组件加载完毕');
				console.log(props);
			},
			props:{
				path:'',
				web_name:'',
			},  //配置需要传入的属性
			delimiters: ['{[', ']}'],//delimiters：改变默认的插值符号
};

const footbuttonComponent = {
	template: `
	<div class="fixed_right_bar">
		<div style="margin-top:3px;cursor: pointer;" class="copylink" >
		<img src="/web/cms/mxpro/img/show.png">
		</div>
		<div>
		<a  href="javascript:alert('暂无在线聊天功能')" >
		<img src="/web/cms/mxpro/img/help.png">
		</a>
		</div>
		<div class="ant-back-top">
		<img src="/web/cms/mxpro/img/back.png">
		</div>
	</div>	
	`,
	setup(props, context) {
		console.log('footbutton组件加载完毕');
		// console.log(props);
	},
	props:{},  //配置需要传入的属性
	delimiters: ['{[', ']}'],//delimiters：改变默认的插值符号
};

const notepopupComponent = {
	template: `
<div class="hide"></div>
<div class="popup" id="note" style="display: none;">
  <div class="popup-icon"><img src="/web/cms/mxpro/img/logo.png"></div>
  <div class="popup-header">
    <h3 class="popup-title"></h3>
  </div>
  <div class="popup-main">
    <p style="font-size:18px;color:red"><b>重要提示：</b></p>
    <p>近期，网站遭到不同程度的封锁屏蔽，导致部分地区无法访问。以下方式均可找到备用网址，强烈建议截屏/收藏保存。</p>
	<p>主用地址01：<a :href="path" style="color: #10AEFF;" target="_blank">👉 {[url]} 👈</a></p>
  	<p>截屏保存本提示</p>
	<p></p>
  </div>
  <div class="popup-footer"><span class="popup-btn" onclick="closeclick()">我记住啦</span></div>
</div>`,
	setup(props, context) {
		console.log('note-popup组件加载完毕');
		console.log(props);
	},
	props:{
		path:'',
		url:'',
	},  //配置需要传入的属性
	delimiters: ['{[', ']}'],//delimiters：改变默认的插值符号
};

const stuheaderComponent = {
	template: `
<header class="stui-header clearfix">
 <div class="container"> 
  <div class="row">
   <ul class="stui_header__user">
    <li>
     <a href="javascript:;"><i class="iconfont icon-search"></i></a>
     <div class="dropdown search">
      <div class="item">
             <form id="search" name="search" method="GET" action="" onsubmit="return notnull()">
           <input type="text" id="wd" name="wd" class="form-control" value="" placeholder="请输入关键词..."/>
        <button class="submit" id="searchbutton" type="submit"><i class="icon iconfont icon-search"></i></button>
       </form>
        </div>
        <ul>
         <li v-for="item in hotsuggs.data">
       <a :href="ctx.path+'?wd='+item.title">{[item.title]}</a>
      </li>
        </ul>
     </div>
    </li>
    <li>
     <a href="javascript:;"><i class="iconfont icon-viewgallery"></i></a>
     <ul class="dropdown type clearfix">
      <li class="active"><a :href="ctx.path">首页</a></li>
      <li v-for="item in items.class">
       <a :href="ctx.path+'?tid='+item.type_id">{[item.type_name]}</a>
      </li>
     </ul>
    </li>
    <li>
     <a href="javascript:;"><i class="iconfont icon-clock"></i></a>
     <div class="dropdown history">
      <div class="head">
       <a class="historyclean pull-right" href="">清空</a>
       <h5>播放记录</h5>
      </div>
      <ul class="clearfix" id="stui_history">
      </ul>
     </div>
    </li>
    <li>
     <a  href="#"><i class="icon iconfont icon-account"></i> </a>
    </li>
    <li>
     <a href="#"><i>公告</i></a>
    </li>

   </ul>

   <div class="stui-header__logo">
    <a class="logo" :href="ctx.path"></a>
   </div>
   <ul class="stui-header__menu">
    <li class="active"><a :href="ctx.path">首页</a></li>
    <li v-for="item in items.class">
     <a :href="ctx.path+'?tid='+item.type_id">{[item.type_name]}</a>
    </li>
   </ul>
   
  </div>              
 </div>
</header>
	
	`,
	setup(props, context) {
		console.log('stuheader组件加载完毕');
		console.log(props);
	},
	props:{
		ctx:{},
		items:{class:[],list:[]},
		hotsuggs:{data:[]},
	},  //配置需要传入的属性
	delimiters: ['{[', ']}'],//delimiters：改变默认的插值符号
};

const stubannerComponent = {
	template:`
<div class="stui-pannel__bd">
    <div class="carousel carousel_default flickity-page">
     <div class="stui-banner__item">
      <a href="/v/85190/" class="stui-vodlist__thumb banner" title="疾速追杀4" style="background: url(https://t1.szrtcpa.com/2023/03/25/8ab97553a4fbc.jpg) no-repeat; background-position:50% 50%; background-size: cover;">
       <span class="pic-text text-center">疾速追杀4</span>
      </a>
     </div>
     <div class="stui-banner__item">
      <a href="/v/47715/" class="stui-vodlist__thumb banner" title="进击的巨人最终季完结篇前篇" style="background: url(https://t1.szrtcpa.com/2023/03/06/e33f67297d1a2.jpg) no-repeat; background-position:50% 50%; background-size: cover;">
       <span class="pic-text text-center">进击的巨人最终季完结篇前篇</span>
      </a>
     </div>
     <div class="stui-banner__item">
      <a href="/v/84935/" class="stui-vodlist__thumb banner" title="铃芽之旅" style="background: url(https://t1.szrtcpa.com/2023/03/27/5ec1282101423.jpg) no-repeat; background-position:50% 50%; background-size: cover;">
       <span class="pic-text text-center">铃芽之旅</span>
      </a>
     </div>

    </div>
</div>
	
	`,
	setup(props, context) {
		console.log('stubanner组件加载完毕');
		console.log(props);
	},
	props:{
		ctx:{},
		items:{class:[],list:[]},
		hotsuggs:{data:[]},
	},  //配置需要传入的属性
	delimiters: ['{[', ']}'],//delimiters：改变默认的插值符号
}

//下面的注册组件方法无法使用,需要在app里去注册
// Vue.component('copy-right', copyrightComponent);
// Vue.component('foot-button', footbuttonComponent);
// Vue.component('note-popup', notepopupComponent);
// Vue.component('stu-header', stuheaderComponent);
// Vue.component('stu-banner', stubannerComponent);