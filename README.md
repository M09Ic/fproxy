# fproxy
a http proxy base on aliyun serverless function compute 

基于阿里云云函数的建议转发工具, 支持webshell转发, http请求等

## deploy
新建 python自定义函数, http触发器

## usage

如需使用改代理, 需要在url中添加 url=[targeturl] 或者在添加头X_FC_URL: [targeturl]

其余的header, request_method, body都会原样转发

