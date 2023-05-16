const copyRightComponent = {
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
				console.log('copyRight组件加载完毕');
				// console.log(props);
			},
			props:{
				path:'',
				web_name:'',
			},  //配置需要传入的属性
			delimiters: ['{[', ']}'],//delimiters：改变默认的插值符号
};

const footButtonComponent = {
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
		console.log('footButton组件加载完毕');
		// console.log(props);
	},
	props:{},  //配置需要传入的属性
	delimiters: ['{[', ']}'],//delimiters：改变默认的插值符号
};

const notePopup = {
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
		console.log('notePopup组件加载完毕');
		// console.log(props);
	},
	props:{
		path:'',
		url:'',
	},  //配置需要传入的属性
	delimiters: ['{[', ']}'],//delimiters：改变默认的插值符号
};

const stuHeaderComponent = {
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
      <li :class="{ active: !!is_home && !tid }"><a :href="ctx.path">首页</a></li>
      <li v-for="item in items.class" :class="{ active: tid == item.type_id }">
       <a :href="ctx.path+'?tid='+item.type_id+'&tname='+item.type_name">{[item.type_name]}</a>
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
    <li :class="{ active: !!is_home }"><a :href="ctx.path">首页</a></li>
    <li v-for="item in items.class" :class="{ active: tid == item.type_id }">
     <a :href="ctx.path+'?tid='+item.type_id+'&tname='+item.type_name">{[item.type_name]}</a>
    </li>
   </ul>
   
  </div>              
 </div>
</header>
	
	`,
	setup(props, context) {
		console.log('stuHeader组件加载完毕');
		// console.log(props);
	},
	props:{
		ctx:{},
		items:{class:[],list:[]},
		hotsuggs:{data:[]},
		tid:String,
		is_home:Boolean,
	},  //配置需要传入的属性
	delimiters: ['{[', ']}'],//delimiters：改变默认的插值符号
};

const stuCategoryComponent = {
	template: `
	<div v-for="item in items.class">
	<div class="stui-vodlist__head">
      <a class="pull-right" :href="ctx.path+'?tid='+item.type_id+'&tname='+item.type_name">更多 <i class="iconfont icon-more"></i></a>
      <p>
            </p>
      <h3><a :href="ctx.path+'?tid='+item.type_id+'&tname='+item.type_name"><i class="iconfont icon-all"></i>  {[item.type_name]}</a></h3>
     </div>
     <ul class="stui-vodlist clearfix">
      <li style="display: none">
       <div class="stui-vodlist__box">
       <a class="stui-vodlist__thumb lazyload" href="/v/107952/" title="侠盗之簪花乱" data-original="">
        <span class="play hidden-xs"></span>
        <span class="pic-text1 text-right"><b>电影</b></span>
        <span class="pic-text text-right"><b>HD国语</b></span>
       </a>
       <div class="stui-vodlist__detail">
        <h4 class="title text-overflow"><a href="/v/107952/" title="侠盗之簪花乱">侠盗之簪花乱</a></h4>
        <p class="text text-overflow text-muted hidden-xs">冯建宇林妍柔</p>
       </div>
       </div>
      </li>
     </ul>
     </div>
	`,
	setup(props, context) {
		console.log('stuCategory组件加载完毕');
		// console.log(props);
	},
	props:{
		ctx:{},
		items:{class:[],list:[]},
	},  //配置需要传入的属性
	delimiters: ['{[', ']}'],//delimiters：改变默认的插值符号
};

const stuBannerComponent = {
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
		console.log('stuBanner组件加载完毕');
		// console.log(props);
	},
	props:{
		ctx:{},
		items:{class:[],list:[]},
		hotsuggs:{data:[]},
	},  //配置需要传入的属性
	delimiters: ['{[', ']}'],//delimiters：改变默认的插值符号
};

const stuFilterComponent = {
	template:`
	<div class="item" id="screenbox" style="display: none;">
       <!-- 筛选 -->
       <ul class="clearfix" v-for="filters in now_filters">
        <li>
         <span>按{[filters.name]}-{[filters.key]}：</span>
        </li>

        <li v-for="obj in filters.value" :class="{ active: tellActive(obj,filters) }">
         <a  :href="ctx.path+'?tid='+item.type_id+'&tname='+item.type_name+'&filter='+obj.v" @click.prevent="openFilterUrl(item,obj,filters)">{[obj.n]}</a>
        </li>

       </ul>
       <!-- end 筛选 -->
      </div>
	`,
	setup(props, context) {
		console.log('stuFilter组件加载完毕');
		// console.log(props);
		const items = props.items;
		const tid = props.tid;
		const ctx = props.ctx;
		const now_filters = computed(() => {
			// console.log('计算now_filters');
			// items.value.class.find(it=>it.type_id===tid);
			let now_filters = items&&items.filters? items.filters[tid]:[];
			// console.log(now_filters);
			return now_filters
		});
		let p = new URLSearchParams(location.href.split('?')[1]);
		let dict = Object.fromEntries(p.entries());
		let f = dict.f || '{}';
		try {
			f = JSON.parse(f);
		}catch (e) {

		}
		const methods = {
			openFilterUrl(item,obj,filters){
				// let url = ctx.path+'?tid='+item.type_id+'&tname='+item.type_name+'&filter='+obj.v;
				// let p = new URLSearchParams(location.href.split('?')[1]);
				// let dict = Object.fromEntries(p.entries());
				// let f = dict.f || '{}';
				try {
					// f = JSON.parse(f);
					f[filters.key] = obj.v;
					f = JSON.stringify(f);
					dict.f = f;
					let new_p = new URLSearchParams(dict);
					let url = ctx.path+'?'+new_p;
					// console.log(url);
					location.href = url;
				}catch (e) {
					console.log(`筛选发生错误:${e.message}`);
				}
			},
			tellActive(obj,filters){
				return f[filters.key] === obj.v;
			}
		}
		return {
			...methods,
			now_filters
		}
	},
	props:{
		items:{},
		now_filters:[],
		tid:String,
		ctx:{},
		item:{},
	},  //配置需要传入的属性
	delimiters: ['{[', ']}'],//delimiters：改变默认的插值符号
};


const stuTopicComponent = {
	template:`
	<div class="stui-vodlist__head">
      <h3><a :href="link"><i class="iconfont icon-all"></i> 最新专题</a></h3>
 	</div>
     <ul class="stui-vodlist clearfix">
     </ul>
	`,
	setup(props, context) {
		console.log('stuTopic组件加载完毕');
		// console.log(props);
	},
	props:{
		link:'',
	},  //配置需要传入的属性
	delimiters: ['{[', ']}'],//delimiters：改变默认的插值符号
};

const stuLinksComponent = {
	template:`
	<ul class="stui-link__text clearfix">
      <li><span>友情链接：</span>
       <a v-for='link in links' :href="link.url" class="links" target="_blank">{[link.name]}</a>
      </li>
     </ul>
	`,
	setup(props, context) {
		console.log('stuLinks组件加载完毕');
		// console.log(props);
	},
	props:{
		links:Array,
	},  //配置需要传入的属性
	delimiters: ['{[', ']}'],//delimiters：改变默认的插值符号
};

const StuImageComponent = {
	template:`
	<div v-show="visible" @click="closeImage" class="showPhoto">
    	<img class="img" :src="url" alt="图片加载失败" />
  	</div>
	`,
	setup(props, context) {
		console.log('StuImage组件加载完毕');
		const methods = {
			closeImage(e) {
			  //子组件可以使用 context.emit 触发父组件的自定义事件
				// console.log(context.emit);
				// console.log('调用父组件 closeImage');
				context.emit('close_image');
			},
		};
		return {
			...methods,
			// visible
		}
	},
	props: {
		url: {
			type: String,
			default: "",
		},
		visible: {
			type: Boolean,
			default: false,
		},
	},//配置需要传入的属性
	emits :['close_image'],
	delimiters: ['{[', ']}'],//delimiters：改变默认的插值符号
};

const StuPagerComponent = {
	template:`
	<div class="stui-pannel__ft">
    <ul class="stui-page__item text-center clearfix">
     <li><a :href="ctx.path+'?tid='+ctx.tid+'&tname='+ctx.tname+'&pg=1'">首页</a></li>
     <li><a :href="ctx.path+'?tid='+ctx.tid+'&tname='+ctx.tname+'&pg='+last_page">上一页</a></li>
<!--     <span v-for="n in 10">{{ n }}</span>-->
     <li class="hidden-xs" :class="{ active: n == ctx.pg }" v-for="n in now_pages">
      <a :href="ctx.path+'?tid='+ctx.tid+'&tname='+ctx.tname+'&pg='+n">{[n]}</a>
     </li>

     <li class="active num"><a>{[pg]}/{[pagecount]}</a></li>
     <li><a :href="ctx.path+'?tid='+ctx.tid+'&tname='+ctx.tname+'&pg='+next_page">下一页</a></li>
     <li><a :href="ctx.path+'?tid='+ctx.tid+'&tname='+ctx.tname+'&pg=99'">尾页</a></li>
    </ul>

   </div>
	`,
	setup(props, context) {
		console.log('StuPager组件加载完毕');
		let pg = props.pg; //pg非ref变量,直接就可以拿到，不需要.value
		// console.log('pg:',pg);
		const last_page = ref(Number(pg)-1>0?Number(pg)-1:1);
		const next_page = ref(Number(pg)+1>0?Number(pg)+1:1);
		const now_pages = computed(() => {
			// console.log('计算now_pages：',(Number(pg)+10));
			let start = (Number(pg)-5)>0?(Number(pg)-5):1;
			let end = (Number(pg)+5) > start+10?start+10:(Number(pg)+5);
			let rangeArr = Array.from({ length: end - start + 1 }, (_, i) => start + i);
			// console.log(rangeArr);
			return rangeArr
		});

		const methods = {
			// closeImage(e) {
			// 	context.emit('close_image');
			// },
		};
		return {
			...methods,
			last_page,
			next_page,
			now_pages,
		}
	},
	props: ['ctx','pg','pagecount'],
	delimiters: ['{[', ']}'],//delimiters：改变默认的插值符号
};

//下面的注册组件方法无法使用,需要在app里去注册
// Vue.component('copy-right',  copyRightComponent);
// Vue.component('foot-button', footButtonComponent);
// Vue.component('note-popup',  notePopup);
// Vue.component('stu-header', stuHeaderComponent);
// Vue.component('stu-banner', stuBannerComponent);

/*注意事项
封装组件过程中传递属性名称一定不能含有大写,比如isHome会被强制识别为is-home，所以应该传递为is_home
 */