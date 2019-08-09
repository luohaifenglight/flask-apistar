# The base image
# FROM your base image base centos
WORKDIR /code

COPY src /code

WORKDIR /code/clannad

RUN pip install -r requirements.txt



ENV IS_ONLINE true

# Set entrypoint
ENTRYPOINT ["uwsgi", "--http-socket", ":80", "--gevent", "50", "--processes", "3", "--wsgi-file", "app.py", "--callable", "server", "--need-app", "--lazy", "--die-on-term"]
