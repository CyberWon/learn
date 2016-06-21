#!/usr/bin/python
#coding:utf-8
import jinja2
def firstDemo(var):
    template=jinja2.Template('Hello,{{ var }}')
    return template.render(var=var)
def NginxPHP(obj):
    nginx_template='''server {
    listen {{ obj.port }};
    server_name {{ obj.server_name }};
    index {{ obj.index_file }};
    root {{ obj.root }};
     location ~ \.php$ {
            fastcgi_pass   127.0.0.1:9000;
            fastcgi_index  index.php;
            fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
            include        fastcgi_params;
        }
}'''
    template=jinja2.Template(nginx_template)
    return template.render(obj=obj)
if __name__=='__main__':
    obj={'port':80,'index_file':'index.php','root':'/var/www/html','server_name':'test.demo.com'}
    print NginxPHP(obj)
    obj={'port':82,'index_file':'index.php','root':'/var/www/html','server_name':'localhost'}
    print NginxPHP(obj)