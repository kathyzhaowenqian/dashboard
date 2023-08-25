FROM python:3.10
#声明这个变量，代表yml中写的build_arg的
ARG DJANGO_SECRET_KEY

LABEL version ="1.0"
LABEL maintainer="gouzigou"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#将上述ARG赋值给DJANGO_SECRET_KEY， 前面一个DJANGO_SECRET_KEY是可以自定义名称的， 后面的是用的上述的ARG后面的
ENV DJANGO_SECRET_KEY $DJANGO_SECRET_KEY


RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

RUN mkdir /anglissData
COPY .  /anglissData

WORKDIR /anglissData

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt 
CMD python manage.py runserver 0.0.0.0:8000  