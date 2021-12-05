from opensuse/tumbleweed
RUN zypper -n in python38-pip python38
EXPOSE 3000/tcp
COPY app.py requirements.txt /opt
WORKDIR /opt
RUN pip install -r requirements.txt
CMD /usr/bin/python3 app.py
