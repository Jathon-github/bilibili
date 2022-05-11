# bilibili

这是一个使用 Scrapy 爬虫框架实现爬取哔站视频合集功能的程序。

## 内容列表

- [背景](#背景)
- [安装](#安装)
- [使用说明](#使用说明)
- [版本更新](#版本更新)
- [法律声明](#法律声明)

## 背景

这段时间想转岗做开发，所以在网上比较盲目的看了很多开发相关的视频，有关于 Python 的，也有关于容器技术的，等等杂七杂八的知识点。但是感觉缺乏动手实践，于是自己想了这么一个爬取哔站视频的需求想把所学实践一下。

## 安装

这个项目的其他依赖都已用 Docker 进行打包，请确保你本地安装 Docker 和 docker-compose。可以使用 git 拉取本项目。

```sh
$ git clone https://github.com/Jathon-github/bilibili.git
```

## 使用说明

1. 修改 ./bilibili/setting.py 配置文件中的 VIDEO_AID 参数，该参数表示待爬取视频的 AID，即 url 中 video 后面的一部分，拿[”Python爬虫实战——哔哩哔哩视频抓取”](https://www.bilibili.com/video/BV1uQ4y1k7G4)举例，url 是 https://www.bilibili.com/video/BV1uQ4y1k7G4，AID 即为 BV1uQ4y1k7G4，如果不做修改，本项目默认爬取的就是该视频合集。
2. 在项目根目录下执行命令 `docker-compose up --build --abort-on-container-exit` 进行镜像的构建并启动。第一次启动会去下载各种依赖有点慢，依赖安装好之后就快了。
3. 当程序执行完成，步骤 2 中的命令会使所有容器关闭。此时在项目根目录下会产生一个 output 文件夹即为视频输出文件夹。里面包含了视频音频素材文件夹和视频音频合成之后的文件。

## 版本更新

1. 修复视频标题中带空格时合成失败的 bug
2. 取消 Scrapy 的日志显示
3. 将 Dockerfile 中换源和下载 ffmpeg 的操作合并成一条语句

## 法律声明

本项目仅用于个人学习练手。请支持哔站版权，若用于违法行为，后果自负。
