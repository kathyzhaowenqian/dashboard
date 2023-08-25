FROM python:3.10
#声明这个变量，代表yml中写的build_arg的
ARG DJANGO_SECRET_KEY
ARG MYSQL_DATABASE_NAME
ARG MYSQL_USER
ARG MYSQL_PASSWORD
ARG MYSQL_HOST
ARG MYSQL_PORT



LABEL version ="1.0"
LABEL maintainer="gouzigou"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#将上述ARG赋值给DJANGO_SECRET_KEY， 前面一个DJANGO_SECRET_KEY是可以自定义名称的， 后面的是用的上述的ARG后面的
ENV DJANGO_SECRET_KEY $DJANGO_SECRET_KEY
ENV MYSQL_DATABASE_NAME  $MYSQL_DATABASE_NAME
ENV MYSQL_USER  $MYSQL_USER
ENV MYSQL_PASSWORD  $MYSQL_PASSWORD
ENV MYSQL_HOST  $MYSQL_HOST
ENV MYSQL_PORT  $MYSQL_PORT





RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

RUN mkdir /anglissData
COPY .  /anglissData
RUN mkdir /static  
WORKDIR /anglissData

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt 
#CMD python manage.py runserver 0.0.0.0:8000  
RUN python manage.py collectstatic 

CMD  uwsgi --ini  uwsgi.ini
