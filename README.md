# V2free自动签到

### 使用教程

1. 点击Fork按钮将项目Fork到自己仓库

2. 配置参数

    依次点击上栏【Setting】->【Security】->【Secrets】->【Actions】->【New repository secrets】 添加账号和密码，示例如下：

    |key |value                     |
    |:--:|:------------------------:|
    |USER|123@qq.com,567@outlook.com|
    |PWD |ccc,aaa                   |

### 说明

* 脚本会在00:07执行一次（Github定时任务会有20min左右延迟），或者自己点击star亦可手动执行一次（无延迟）。

* 支持多账号，账号之间与密码之间用**半角逗号**分隔，账号与密码的个数要对应。
