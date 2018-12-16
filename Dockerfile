FROM python:2-alpine3.6
USER nobody
ADD christmaslister/ /opt/christmaslister
RUN pip install --no-cache-dir -r /opt/christmaslister/requirements.txt
EXPOSE 8000
ENTRYPOINT ["python /opt/christmaslister/web/manage.py runserver"]