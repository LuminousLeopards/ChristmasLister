FROM python:2-alpine3.6
USER nobody
ADD christmaslister/ /opt/christmaslister
#RUN pip install --no-cache-dir -r /opt/christmaslister/requirements.txt
EXPOSE 5000