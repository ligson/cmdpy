# coding=UTF-8
'''
Created on 2016年8月18日

@author: trq
'''
import web;
import json;
import os;
urls = (
        "/", "index"
        , "/exec.json", "Exec"
    )
render = web.template.render("views")
class Exec:
    def POST(self):
        cmd = web.input().cmd;
        print cmd;
        web.header('Content-Type', 'text/json; charset=utf-8', unique=True)
        
        r = os.popen(cmd)  # 执行该命令
        info = r.readlines()  # 读取命令行的输出到一个list
        infos = "";
        for line in info:  # 按行遍历
            infos = infos + line + "\n\r"
        
        print infos.decode("gbk")
        result = {"result":infos.decode("gbk")};
        return json.dumps(result);
class index:
    def GET(self):
        return render.index();
if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
