RUN apt-get update

RUN pip3 install --no-cache-dir -U -r requirements.txt

CMD bash start
