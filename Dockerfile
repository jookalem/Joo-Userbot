FROM kyyex/kyy-userbot:busterv2
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    curl \
    git \
    ffmpeg
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g npm
RUN git clone -b Joo-Userbot https://github.com/jookalem/Joo-Userbot /home/userbot/ \
    && chmod 777 /home/userbot \
    && mkdir /home/userbot/bin/
WORKDIR /home/userbot/
COPY ./sample_config.env ./config.env* /home/userbot/
RUN pip install -r requirements.txt
CMD ["python3", "-m", "userbot"]
