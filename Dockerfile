FROM python:3.6-alpine
ADD christmaslister/ /opt/christmaslister
RUN pip install --no-cache-dir -r /opt/christmaslister/requirements.txt
EXPOSE 8000
CMD ["/usr/local/bin/python", "/opt/christmaslister/manage.py", "runserver", "0.0.0.0:8000"]