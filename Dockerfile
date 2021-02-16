FROM python:3
MAINTAINER Yang Hanlin <mattoncis@hotmail.com>
WORKDIR /app

ARG PYPI_MIRROR
COPY ./requirements.txt ./requirements.txt
RUN if [[ -n "$PYPI_MIRROR" ]]; then pip config set global.index-url "$PYPI_MIRROR"; fi
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
