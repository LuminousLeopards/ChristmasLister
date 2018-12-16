FROM centos:centos7.6.1810
USER santa
ADD christmaslister/ /opt/
EXPOSE 5000