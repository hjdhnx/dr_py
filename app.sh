#!/bin/bash
#kill -9 $(cat supervisord.pid) # 杀掉进程
msg='flask或0 ubuntu下自动识别gevent或普通启动flask\nsflask或1 ubuntu下gunicorn启动flask\ntermux或2 termux下自动识别gevent或普通启动flask\nstermux或3 termux下gunicorn启动flask\n'
case "$1" in
    flask)
        supervisord -c ./super/flask.conf
        ;;
    0)
      supervisord -c ./super/flask.conf
      ;;
    sflask)
        supervisord -c ./super/sflask.conf
        ;;
    1)
      supervisord -c ./super/sflask.conf
      ;;
    termux)
        supervisord -c ./super/termux.conf
        ;;
    2)
      supervisord -c ./super/termux.conf
      ;;
    stermux)
        supervisord -c ./super/stermux.conf
        ;;
    3)
        supervisord -c ./super/stermux.conf
        ;;
    *)
      echo -e $msg
      ;;
esac
# 保留一个 bash
/bin/bash