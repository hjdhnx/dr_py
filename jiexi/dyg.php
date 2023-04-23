$DATA = curl('https://vip.lianfaka.com/vip/?url='.$_REQUEST['url']);
preg_match('/source src="(.*?)"/',$DATA,$url);
if (empty($url[1])) {
    $add['code'] = 404;
    $add['msg'] = '解析失败';
    $add['from'] = 'Q:2579949378';
    $add['name'] = '蓝莓';
} else {
    $add['code'] = 200;
    $add['msg'] = '解析成功';
    $add['from'] = 'Q:2579949378';
    $add['name'] = '蓝莓';
    $add['url'] = $url[1];
}
echo json_encode($add,456);
function curl($url, $cookie = '')
{
    // 初始化cURL\n        
    $curl = curl_init();// 设置网址
    curl_setopt($curl, CURLOPT_URL, $url);
    // 设置UA
    $header[] = 'Referer: https://www.dy6g.com';
    $header[] = 'User-Agent: Mozilla/5.0 (Linux; Android 6.0.1; OPPO R9s Plus Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36';    
    // 设置请求头
    curl_setopt($curl, CURLOPT_HTTPHEADER, $header);
    // 设置POST数据
    // 允许执行的最长秒数 超时时间
    curl_setopt($curl, CURLOPT_TIMEOUT, 30);
    // 过SSL验证证书
    curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false);
    // 将头部作为数据流输出
    curl_setopt($curl, CURLOPT_HEADER, false);
    // 设置以变量形式存储返回数据
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
    // 请求并存储数据
    $return = curl_exec($curl);
    // 分割头部和身体
    if (curl_getinfo($curl, CURLINFO_HTTP_CODE) == '200') {
        $return_header_size = curl_getinfo($curl, CURLINFO_HEADER_SIZE);
        $return_header = substr($return, 0, $return_header_size);
        $return_data = substr($return, $return_header_size);  
    }
    // 关闭cURL
    curl_close($curl);
    // 返回数据
    return $return;
}