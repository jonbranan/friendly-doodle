FROM python:alpine3.18
WORKDIR /
COPY . opt
RUN pip install requests
RUN pip install qbittorrent-api
RUN crontab /opt/crontab
RUN chmod +x /opt/entrypoint.sh
CMD ["/opt/entrypoint.sh"]