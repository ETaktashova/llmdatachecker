FROM python:3.9-slim-bookworm
RUN apt update && apt -y upgrade
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt


COPY ./src /src
COPY ./xdata /xdata
WORKDIR /src
ENTRYPOINT ["python", "-m", "src.main.py"]

# docker run gigachat python main.py -c ./data/classes.xlsx -s ./data/example.xlxs - для запуска через докер (добавить автоключ)
# docker run -it 2bfe4106ec86 /bin/bash - посмотреть содержимое образа
# /home/elizaveta/GitProjects/gigachat/data/classes.xlsx
# /home/elizaveta/GitProjects/gigachat/data/strings.xlsx