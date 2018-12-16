FROM python:3.6-alpine
ADD christmaslister/ /opt/christmaslister
RUN pip install --no-cache-dir -r /opt/christmaslister/requirements.txt
EXPOSE 8000
ENTRYPOINT ["python /opt/christmaslister/web/manage.py runserver"]