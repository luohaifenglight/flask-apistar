## clannad---an clann as dango---团子大家族

flask-apistar基于flask, flask_restplus,使用Django集中路由管理的思想

### 一些说明
1. src/clannad模块下可以建立业务模块，其中simple是一个模块样例
```
# models 提供模型
# repository 业务逻辑层
# service 提供服务
# tests 单元测试
# urls 子路由映射
```
2. src/clannad/clannad下urls里添加主路由和蓝图模块配置
3. src/clannad/settings里添加配置项 如果有基于微服务的模块配置需要而配置文件加上
4. 客户端天加lint 检查基于flake8,需要先安装 添加文件.git/hooks/pre-commit 加入以下内容
```
# #!/usr/bin/env bash
# flake8 .
```
5. settings添加配置，数据使用的mongo的例子，可以添加其他
6. 如果使用Docker 需要在首行添加基础镜像地址一般centos
7. deploy.json 是部署配置，如果建立微服务使用持续集成的话需要配置
8. python app.py 可以本地调试
9. python manage.py shell 进入REPL模式,也可以自定义命令
10. .gitlab-ci.yml可以添加gitlab构建触发规则，持续集成使用