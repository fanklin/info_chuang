FROM python:3.8.1
WORKDIR /usr/local/python-example
COPY . /usr/local/python-example
RUN pip install -r requirements.txt
#在构建中可以使用DaoCloud内网的pip镜像加快构建速度使用以下命令安装依赖
#RUN pip install -i http://nexus.daocloud.io/repository/daocloud-pypi/simple  --trusted-host nexus.daocloud.io -r requirements.txt
EXPOSE 5000
CMD ["python", "run.py"]
