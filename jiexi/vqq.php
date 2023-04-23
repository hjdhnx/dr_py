<?php
error_reporting(0);
if (!file_exists('Cache/qq')) {mkdir('Cache/qq', 0777, true);}
$url = $_GET["url"];
echo json_encode(VQQ::parse($url));
class VQQ
{
    public static function parse($url) {
        $content = file_get_contents($url);
        
        preg_match('#"drm":(0|1|2),#iU',$content,$isdrm);
        preg_match('#<title>(.*?)<\/title>#iU',$content,$name);
        $drm = $isdrm[1];

        preg_match('#cid=(\w+)&vid=(\w+)["|&]#',$content,$id);
        $cid = empty($id[1])? 0 :$id[1];
        $vid = $id[2];
        if (!$vid) {
            preg_match('#&vid=(\w+)["|&]#',$content,$id);
            $vid = $id[1];
            $cid = '';
           }
  
        $ep_file= 'Cache/qq/'.$vid.'.m3u8';
        if (!file_exists($ep_file)||filemtime($ep_file)+10800 < time()){
            if ($drm != 0) { //是否付费
                $cookie = file_get_contents("qqck.txt");;//这里写你的cookie
                return self::h5($vid,$cookie);
            } else{
                $cookie = file_get_contents("qqck.txt");;//这里写你的cookie
                return self::h5($vid,$cookie);
            }
        }else{
            $vurl = 'http://'.$_SERVER['HTTP_HOST'].'/'.$ep_file;
            $videoinfo['code'] = 200;
    	    $videoinfo['success'] = 1;
		    $videoinfo['url'] = $vurl;
		    $videoinfo['type'] = 'hls';
		    $videoinfo['player'] = "dplayer";
		    $videoinfo['cache'] = "1";
        }

        return $videoinfo;
    }
	public static function h5($vid,$cookie){
        $api = 'https://h5vv6.video.qq.com/getinfo?encver=2&defn=fhd&platform=10801&otype=ojson&sdtfrom=v4138&appVer=7&dtype=3&vid='.$vid.'&newnettype=4';
        
        $body = self::gh5($api,$cookie);

        
        $data = json_decode($body,true);
        
        $vi = $data["vl"]["vi"][0];
        $ui = $vi["ul"]["ui"];
       
        $url = $ui[3]["url"];
        
        $hls = $ui[3]['hls']['pt'];
        $vurl = $url.$hls;
        if($vurl ==''||$vurl ==null){ return ['code' => '404','url' => 'null'];	}
        $data = file_get_contents($vurl);
        $lines = preg_split('/[\r\n]+/s', $data);//按行进行分割字符串
    	$durations = array();
    	$urls = array();
    	$bool = true;
    	$targetduration = "";
    	foreach ($lines as $value) {
    		if(!empty(strstr($value,"#EXT-X-TARGETDURATION:"))){//多码率
    			$targetduration = $value;
    		}else if(!empty(strstr($value,"#EXTINF:"))){//单码率
    			$durations[count($durations)] = $value;
    			$bool = true;
    		}else if(!empty($value)&&substr($value,0,1)!="#"){	
    			if($bool){
    				$urls[count($urls)] = $value;
    			}
		    }
    	}
    	  
        $url =  preg_replace('/(http:\/\/(.*?)\/(.*?)\/(.*?)\/)/i','https://omts.tc.qq.com/',$url);
    	$m3u8 = "#EXTM3U\n#EXT-X-VERSION:3\n";
    	$m3u8 .= empty($targetduration)?"#EXT-X-TARGETDURATION:7200\n" : $targetduration."\n";
    	foreach ($durations as $key => $value) {
    		$m3u8 .= $value."\n".$url.$urls[$key]."\n";
    	}
		$m3u8 = str_replace('&ver=4','',$m3u8);
    	$m3u8 .="#EXT-X-ENDLIST";
		$ep_file= 'Cache/qq/'.$vid.'.m3u8';
    	file_put_contents($ep_file, $m3u8);
    	$vvurl = 'http://'.$_SERVER['HTTP_HOST'].'/'.$ep_file;
    	$videoinfo['success'] = 1;
		$videoinfo['code'] = 200;
		$videoinfo['url'] = $vvurl;
		$videoinfo['type'] = 'hls';
		$videoinfo['player'] = "dplayer";
	
		return $videoinfo;
    }
    
	public static function gh5($url,$cookie){
        $header = array(
            'Host: h5vv6.video.qq.com',
            'Accept: */*',
            'Content-Type: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Connection: keep-alive',
            'Cookie: '.$cookie,
            'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
            'Referer: https://servicewechat.com/wxa75efa648b60994b/69/page-frame.html',
            'Accept-Language: zh-CN,zh;q=0.9',
        );
        $curl = curl_init();
        //初始化 curl
        curl_setopt($curl, CURLOPT_URL, $url);
        //要访问网页 URL 地址
        curl_setopt($curl, CURLOPT_HTTPHEADER, $header);//设定是否输出页面内容
        curl_setopt($curl, CURLOPT_REFERER,$url) ;
        //伪装网页来源 URL
        curl_setopt($curl, CURLOPT_AUTOREFERER, 1);
        //当Location:重定向时，自动设置header中的Referer:信息
        curl_setopt($curl, CURLOPT_TIMEOUT, 10);
        //数据传输的最大允许时间
        curl_setopt($curl, CURLOPT_HEADER, 0);
        //不返回 header 部分
        curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
        //返回字符串，而非直接输出到屏幕上
        curl_setopt($curl, CURLOPT_FOLLOWLOCATION,1);
        //跟踪爬取重定向页面
        curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, '0');
        //不检查 SSL 证书来源
        curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, '0');
        //不检查 证书中 SSL 加密算法是否存在
        curl_setopt($curl, CURLOPT_ENCODING, '');
        //解决网页乱码问题
        //curl_setopt($curl, CURLOPT_COOKIE, '');
        //从字符串传参来提交cookies
        $data = curl_exec($curl);
        //运行 curl，请求网页并返回结果
        curl_close($curl);
        //关闭 curl
        return $data;
    }
}
?>
