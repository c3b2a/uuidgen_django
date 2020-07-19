<h1 style="font-family: sans-serif;">UUID 生成器 ( Django )</h1>

<h2>1、获取源码</h2>

```bash
git clone https://github.com/c3b2a/uuidgen_django.git
cd uuidgen_django
```

<h2>2、安装依赖</h2>

```bash
pip3 install django
```

<h2>3、运行程序</h2>

```bash
python3 manage.py runserver 0.0.0.0:8000
```
<p>8000 为端口号</p>

<h2>4、域名访问</h2>

<h3>1、Cloudflare</h3>
<p>使用 Cloudflare 的 CDN，将 SSL/TLS 加密模式改为灵活</p>

<h3>2、反向代理</h3>
<p>安装 Nginx 或其他反向代理工具，将 http://127.0.0.1:8000 反代</p>