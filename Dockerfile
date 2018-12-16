FROM python:2-alpine3.6
USER santa
ADD christmaslister/ /opt/
RUN pip install --no-cache-dir -r /opt/christmastlister/requirements.txt
EXPOSE 5000