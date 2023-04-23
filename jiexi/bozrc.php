<?php

header('Content-Type:application/json');
$DATA = httpget("https://jx.bozrc.com:4433/aliplayer/?url=".$_REQUEST['url']);
preg_match('/source:"(.*)",width:"100%",height:"100%",/',$DATA,$url);
	if ($url[1] != null) {
		$add['code'] = 200;
		$add['msg'] = '解析成功，免费解析请加群：905111367';
		$add["success"]="1";
		$add['type'] = 'hls';
		$add['url'] = $url[1];
	}
    else {
		$add['code'] = 404;
		$add['msg'] = '解析失败';
	}
	echo json_encode($add,JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES);
function httpget($url) {
$curl = curl_init();
$header = array(
"X-FORWARDED-FOR:".rand_ip(),
"CLIENT-IP:".rand_ip(),
"X-Real-IP:".rand_ip(),
"referer:https://jx.bozrc.com:4433/",//模拟来路访问
"Connection: Keep-Alive",//可持久连接、连接重用。。。避免了重新建立连接
"User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
//"Content-Length: 326",
"Accept: application/json, text/javascript, */*; q=0.01",
"Accept-Language: zh-CN,zh;q=0.9",
);
curl_setopt($curl, CURLOPT_URL, $url);
curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, FALSE);
curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, FALSE);
curl_setopt($curl, CURLOPT_RETURNTRANSFER,true);
curl_setopt($curl, CURLOPT_HTTPHEADER, $header);//读头部数据
curl_setopt($curl, CURLOPT_FOLLOWLOCATION,1);//重定向处理
curl_setopt($curl, CURLOPT_HEADER,0); //显示头部数据为1 不显示为0
curl_setopt($curl, CURLOPT_CONNECTTIMEOUT, 10);// 在尝试连接时等待的秒数
curl_setopt($curl, CURLOPT_TIMEOUT, 10);// 最大执行时间
$content = curl_exec($curl); //抓取URL并把它传递给浏览器
curl_close($curl);//释放curl句柄
return $content;
}
function rand_ip(){
$ip_long = array(
array('607649792', '608174079'), //36.56.0.0-36.63.255.255
array('975044608', '977272831'), //58.30.0.0-58.63.255.255
array('999751680', '999784447'), //59.151.0.0-59.151.127.255
array('1019346944', '1019478015'), //60.194.0.0-60.195.255.255
array('1038614528', '1039007743'), //61.232.0.0-61.237.255.255
array('1783627776', '1784676351'), //106.80.0.0-106.95.255.255
array('1947009024', '1947074559'), //116.13.0.0-116.13.255.255
array('1987051520', '1988034559'), //118.112.0.0-118.126.255.255
array('2035023872', '2035154943'), //121.76.0.0-121.77.255.255
array('2078801920', '2079064063'), //123.232.0.0-123.235.255.255
array('-1950089216', '-1948778497'), //139.196.0.0-139.215.255.255
array('-1425539072', '-1425014785'), //171.8.0.0-171.15.255.255
array('-1236271104', '-1235419137'), //182.80.0.0-182.92.255.255
array('-770113536', '-768606209'), //210.25.0.0-210.47.255.255
array('-569376768', '-564133889'), //222.16.0.0-222.95.255.255
);
$rand_key = mt_rand(0, 14);
$huoduan_ip= long2ip(mt_rand($ip_long[$rand_key][0], $ip_long[$rand_key][1]));
return $huoduan_ip;
}