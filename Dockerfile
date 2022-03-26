FROM kyyex/kyy-userbot:busterv2
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    curl \
    git \
    ffmpeg
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g npm
RUN git clone -b Joo-Userbot https://github.com/jookalem/Joo-Userbot /home/Joo-Userbot/ \
    && chmod 777 /home/Joo-Userbot \
    && mkdir /home/Joo-Userbot/bin/
WORKDIR /home/Joo-Userbot/
COPY ./sample_config.env ./config.env* /home/Joo-Userbot/
RUN pip install -r requirements.txt
CMD ["python3", "-m", "userbot"]
