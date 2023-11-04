#!/bin/bash
banip_run(){
	# https://help.baidu.com/search?keywords=hiker.nokia.press  访问这个直接dd
	nginx_home=/usr/sbin/nginx
	log_path=/var/log/nginx
	nginx_etc=/etc/nginx/conf.d
	maxcn=3000
	history=50000
	cat /dev/null >  $log_path/ban_ip_tmp.txt
	tail -n$history $log_path/access.log \
		|awk '{print $1,$12}' \
		|grep -i -v -E "google|yahoo|baidu|msnbot|FeedSky|sogou" \
		|awk '{print $1}'|sort|uniq -c|sort -rn \
		|awk '{if($1>'$maxcn')print "deny "$2";"}' >$log_path/ban_ip_tmp.txt
	spiders=`awk 'END{print NR}' $log_path/ban_ip_tmp.txt`
	now_time=$(date "+%Y-%m-%d %H:%M:%S")
	if [ $spiders -gt 0 ]
	then
		cat $log_path/ban_ip_tmp.txt > $nginx_etc/ban_ip.conf
		blacks=`cat $log_path/ban_ip_tmp.txt`
		echo "$now_time  本次封禁以下$spiders个IP:$blacks"
		service nginx reload
		echo "nginx重载完毕"
		#docker restart hiker
	docker exec hiker odoo restart
	echo "道长仓库重载完毕"
else
	    echo "$now_time  很棒,本次检测未发现恶意访问的ip"
	        hiker_test
	fi
}
hiker_test(){
	httpcode=`curl -I localhost:8025 -w "%{http_code}\n" -o /dev/null -s`
	#  httpcode=`curl -I -s localhost:8025|head -1|cut -d " " -f2`
	if [ "$httpcode" == "200" ];then
		echo "hiker服务运行正常"
	else
		echo "hiker服务已经异常,返回$httpcode,开始重启服务"
	docker exec hiker odoo restart
	echo "道长仓库重载完毕"
fi
}

banip_num(){
	  # 500000 10000
	  log_path=/var/log/nginx
	  tail -n$1 $log_path/access.log \
		  |awk '{print $1,$12}' \
		  |grep -i -v -E "google|yahoo|baidu|msnbot|FeedSky|sogou" \
		  |awk '{print $1}'|sort|uniq -c|sort -rn \
		  |awk '{if($1>'$2')print ""$2""}' >$log_path/ban_ip_tmps.txt
	  cat $log_path/ban_ip_tmps.txt
  }

  banip_kill(){
	    log_path=/var/log/nginx
	      for line in `cat $log_path/ban_ip_tmps.txt`
	      do
		       iptables -I INPUT -s $line -j DROP
		        echo '封禁了:'$line
		done
	}

	ipkill(){
		 iptables -I INPUT -s $1 -j DROP
		  echo '封禁了:'$1
	  }
	  ipallow(){
		    iptables -D INPUT -s $1 -j DROP
		      echo '解封了:'$1
	      }
	      ipshow(){
		      #  iptables --list
		        iptables -L
		}
		log(){
			  log_path=/var/log/nginx
			    tail -f $log_path/access.log
		    }

		    banip_log(){
			      awk '{print $1}' /var/log/nginx/access.log |sort |uniq -c|sort -n
		      }

		      banip_clear(){
			        cat /dev/null > ban_ip.conf
			}

			banip_show(){
				  nginx_etc=/etc/nginx/conf.d
				    cat $nginx_etc/ban_ip.conf
			    }
			    # cat /dev/null > banips.sh
			    #ln -s /etc/nginx/conf.d/banips.sh /usr/local/bin/banips
			    #rm -rf /usr/local/bin/banips
			    #crontab -e
			    #15分钟执行一次封ip
			    # */15 * * * * banips run >> /etc/nginx/conf.d/banips.log  2>&1
			    # iptables -L -n --line-numbers
			    # iptables -I INPUT -s 168.138.198.222 -j DROP
			    # cat /var/log/nginx/access.log | grep HEAD
			    msg='run 启动ip封杀\nlog 打印访问ip记录\nshow 显示被封的ip\nclear 清空封禁列表\nlogs 显示nginx实时日志\nnum输出异常ip到文本\nkills 封禁文本异常ip\nipkill 手动封单ip\nipshow 显示规则\nipallow 解封ip'
			    case "$1" in
				        run)
                  banip_run
                  ;;
                log)
                  banip_log
                  ;;
                logs)
                  log
                  ;;
                  num)
                banip_num $2 $3
                    ;;
                kills)
                    banip_kill
                        ;;
                show)
                  banip_show
                    ;;
                clear)
                banip_clear
                  ;;
                ipkill)
                    ipkill $2
                  ;;
                ipallow)
                  ipallow $2
                    ;;
                ipshow)
                    ipshow
                      ;;
                    *)
            echo -e $msg
            ;;
        esac