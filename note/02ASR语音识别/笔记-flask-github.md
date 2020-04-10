## 01 开始

在运行之前，需要通过设置`FLASK_APP`环境变量告诉Flask如何导入它：

```
(venv) $ export FLASK_APP=microblog.py
```

```
(venv) $ flask run
 * Serving Flask app "microblog"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

 `flask run`的输出表明服务器正在运行在IP地址127.0.0.1上，这是本机的回环IP地址，即*localhost*。 网络服务器监听在指定端口号等待连接。 部署在生产Web服务器上的应用程序通常会在端口443上进行监听，如果不执行加密，则有时会监听80，但启用这些端口需要root权限（非root用户不能使用1024以下端口 ）。由于此应用程序在开发环境中运行，因此Flask使用自由端口5000。

`Ctrl-C`来停止Web服务。

终端会话中直接设置的环境变量不会永久生效，因此你不得不在每次新开终端时设定 `FLASK_APP` 环境变量，Flask 允许你设置只会在运行`flask`命令时自动注册生效的环境变量，要实现这点，你需要安装 `python-dotenv`：

```
(venv) $ pip install python-dotenv
```

在项目的根目录下新建一个名为 `.flaskenv` 的文件，其内容是：

```
FLASK_APP=microblog.py
```

通过此项设置，`FLASK_APP`就可以自动加载了

## 02 模板

将应用程序的后台逻辑和网页布局划分开来，更容易组织管理。

模板有助于实现页面展现和业务逻辑之间的分离。 在Flask中，模板被编写为单独的文件，存储在应用程序包内的*templates*文件夹中。

*app/templates/index.html*中：`{{ ... }}`。`{{ ... }}`包含的内容是动态的，只有在运行时才知道具体表示成什么样子。

将模板转换为完整的HTML页面的操作称为*渲染*。 为了渲染模板，需要从Flask框架中导入一个名为`render_template()`的函数。 该函数需要传入模板文件名和模板参数的变量列表，并返回模板中所有占位符都用实际变量值替换后的字符串结果。

### 控制语句

在渲染过程中使用实际值替换占位符，只是Jinja2在模板文件中支持的诸多强大操作之一。 模板也支持在`{%...％}`块内使用控制语句。

```html
{% if title %}
<title>{{ title }} - Microblog</title>
{% else %}
<title>Welcome to Microblog!</title>
{% endif %}
```

```html
{% for post in posts %}
...
{% endfor %}
```

### 模板的继承

定义一个名为`base.html`的基本模板，其中包含一个简单的导航栏，以及我之前实现的标题逻辑。

 `extends`语句用来建立了两个模板之间的继承关系，这样Jinja2才知道当要求呈现`index.html`时，需要将其嵌入到`base.html`中。 而两个模板中匹配的`block`语句和其名称`content`，让Jinja2知道如何将这两个模板合并成在一起。 

## 03 Web表单

### 配置

使用类来存储配置变量，才是我真正的风格。我会将这个配置类存储到单独的Python模块，以保持良好的组织结构。

Flask及其一些扩展使用密钥的值作为加密密钥，用于生成签名或令牌。Flask-WTF插件使用它来保护网页表单免受名为[Cross-Site Request Forgery](http://en.wikipedia.org/wiki/Cross-site_request_forgery)或CSRF（发音为“seasurf”）的恶意攻击。

密钥被定义成由`or`运算符连接两个项的表达式。第一个项查找环境变量`SECRET_KEY`的值，第二个项是一个硬编码的字符串。这种首先检查环境变量中是否存在这个配置，找不到的情况下就使用硬编码字符串的配置变量的模式你将会反复看到。在开发阶段，安全性要求较低，因此可以直接使用硬编码字符串。但是，当应用部署到生产服务器上的时候，我将设置一个独一无二且难以揣摩的环境变量，这样，服务器就拥有了一个别人未知的安全密钥了。

`form.validate_on_submit()`实例方法会执行form校验的工作。

 `flash()`函数是向用户显示消息的有效途径。`redirect()`函数指引浏览器自动重定向到它的参数所关联的URL。

`with`结构在当前模板的上下文中来将`get_flashed_messages()`的结果赋值给变量`messages`。`get_flashed_messages()`是Flask中的一个函数，它返回用`flash()`注册过的消息列表。

## 04 数据库

[Flask-SQLAlchemy](http://packages.python.org/Flask-SQLAlchemy)，这个插件为流行的[SQLAlchemy](http://www.sqlalchemy.org/)包做了一层封装以便在Flask中调用更方便，ORM的工作就是将高级操作转换成数据库命令。SQLAlchemy不只是某一款数据库软件的ORM，而是支持包含[MySQL](https://www.mysql.com/)、[PostgreSQL](https://www.postgresql.org/)和[SQLite](https://www.sqlite.org/)在内的很多数据库软件

二个插件是[Flask-Migrate](https://github.com/miguelgrinberg/flask-migrate)。 这个插件是[Alembic](https://bitbucket.org/zzzeek/alembic)的一个Flask封装，是SQLAlchemy的一个数据库迁移框架。

```
(venv) $ pip install flask-sqlalchemy 
(venv) $ pip install flask-migrate
```

`SQLALCHEMY_DATABASE_URI`配置变量中获取应用的数据库的位置。 首先从环境变量获取配置变量，未获取到就使用默认值，这样做是一个好习惯。 本处，我从`DATABASE_URL`环境变量中获取数据库URL，如果没有定义，我将其配置为`basedir`变量表示的应用顶级目录下的一个名为*app.db*的文件路径。

`SQLALCHEMY_TRACK_MODIFICATIONS`配置项用于设置数据发生变更之后是否发送信号给应用，我不需要这项功能，因此将其设置为`False`。

在这个初始化脚本中我更改了三处。首先，我添加了一个`db`对象来表示数据库。然后，我又添加了数据库迁移引擎`migrate`。这种注册Flask插件的模式希望你了然于胸，因为大多数Flask插件都是这样初始化的。最后，我在底部导入了一个名为`models`的模块，这个模块将会用来定义数据库结构。

> bug `Instance of 'SQLAlchemy' has no 'Column' member`
>
> `pip install pylint-flask`
> VS code, please edit setting.json file as follows:(忽略报错警告)
> `"python.linting.pylintArgs": ["--load-plugins", "pylint-flask"]`

### 关系数据库

Post表

`User`类有一个新的`posts`字段，用`db.relationship`初始化。`db.relationship`的第一个参数表示代表关系“多”的类。 `backref`参数定义了代表“多”的类的实例反向调用“一”的时候的属性名称。这将会为用户动态添加一个属性`post.author`，调用它将返回给该用户动态的用户实例。 `lazy`参数定义了这种关系调用的数据库查询是如何执行的。

```
添加用户
>>> u = User(username='susan', email='susan@example.com')
>>> db.session.add(u)
添加动态
>>> u = User.query.get(1)
>>> p = Post(body='my first post!', author=u)
>>> db.session.add(p)
查询用户
>>> users = User.query.all()
>>> users
查询动态
>>> u = User.query.get(1)
>>> u
<User john>
>>> posts = u.posts.all()
>>> posts
删除用户
>>> users = User.query.all()
>>> for u in users:
...     db.session.delete(u)
提交
>>> db.session.commit()
取消修改
>>> db.session.rollback()
```

`flask shell`添加shell上下文处理器函数后，你无需导入就可以使用数据库实例：

## 05 登录界面

实现密码哈希的包是[Werkzeug](http://werkzeug.pocoo.org/)，它是Flask的一个核心依赖项。

```
from werkzeug.security import generate_password_hash check_password_hash
```

Flask插件[Flask-Login](https://flask-login.readthedocs.io/)。 该插件管理用户登录状态，以便用户可以登录到应用，然后用户在导航到该应用的其他页面时，应用会“记得”该用户已经登录。它还提供了“记住我”的功能，允许用户在关闭浏览器窗口后再次访问应用时保持登录状态。

三种可能的情况需要考虑，以确定成功登录后重定向的位置：

- 如果登录URL中不含`next`参数，那么将会重定向到本应用的主页。
- 如果登录URL中包含`next`参数，其值是一个相对路径（换句话说，该URL不含域名信息），那么将会重定向到本应用的这个相对路径。
- 如果登录URL中包含`next`参数，其值是一个包含域名的完整URL，那么重定向到本应用的主页。

前两种情况很好理解，第三种情况是为了使应用更安全。 攻击者可以在`next`参数中插入一个指向恶意站点的URL，因此应用仅在重定向URL是相对路径时才执行重定向，这可确保重定向与应用保持在同一站点中。 为了确定URL是相对的还是绝对的，我使用Werkzeug的`url_parse()`函数解析，然后检查`netloc`属性是否被设置。

### 用户注册

## 23 API

 应用程序编程接口（API），API是一组HTTP路由，被设计为应用程序中的低级入口点。API允许客户端直接使用应用程序的*资源*，从而决定如何通过客户端完全地向用户呈现信息。 这种路由的内容都以JSON格式编码，并在请求时使用`POST`方法。 此请求的响应也是JSON格式，服务器仅返回所请求的信息，客户端负责将此信息呈现给用户。构建不依赖于Web浏览器的API。

REST的六个定义特征。

> - 客户端－服务器原则：客户端和服务器的角色应该明确区分。 在实践中，这意味着客户端和服务器都是单独的进程，并在大多数情况下，使用基于TCP网络上的HTTP协议进行通信。
>- 分层系统原则是说当客户端需要与服务器通信时，它可能最终连接到代理服务器而不是实际的服务器。因为能够添加中间节点的这个特性，允许应用程序架构师使用负载均衡器，缓存，代理服务器等来设计满足大量请求的大型复杂网络。
> - 缓存原则扩展了分层系统，通过明确指出允许服务器或代理服务器缓存频繁且相同请求的响应内容以提高系统性能。 
>- 按需获取客户端代码
> - 在无状态API中，每个请求都需要包含服务器需要识别和验证客户端并执行请求的信息。这也意味着服务器无法在数据库或其他存储形式中存储与客户端连接有关的任何数据。主要原因是无状态服务器非常容易扩展，你只需在负载均衡器后面运行多个服务器实例即可。 
>- 统一接口的四个特性：唯一资源标识符，资源表示，自描述性消息和超媒体。唯一资源标识符是通过为每个资源分配唯一的URL来实现的。资源表示的使用JSON格式用于构建资源表示。自描述性消息意味着在客户端和服务器之间交换的请求和响应必须包含对方需要的所有信息， `GET`请求表示客户想要检索资源信息，`POST`请求表示客户想要创建新资源，`PUT`或`PATCH`请求定义对现有资源的修改，`DELETE` 表示删除资源的请求。超媒体需求是最具争议性的

*users.py*模块中。 下表总结了我要实现的路由：

| HTTP 方法 | 资源 URL                | 注释                       |
| --------- | ----------------------- | -------------------------- |
| `GET`     | */api/users/*           | 返回一个用户               |
| `GET`     | */api/users*            | 返回所有用户的集合         |
| `GET`     | */api/users//followers* | 返回某个用户的粉丝集合     |
| `GET`     | */api/users//followed*  | 返回某个用户关注的用户集合 |
| `POST`    | */api/users*            | 注册一个新用户             |
| `PUT`     | */api/users/*           | 修改某个用户               |

