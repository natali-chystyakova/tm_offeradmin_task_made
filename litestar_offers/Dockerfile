FROM python:3.11

ENV PYTHONUNBUFFERED=1

ARG WORKDIR=/app
ARG USER=user

WORKDIR ${WORKDIR}

RUN useradd --system ${USER} && \
    chown --recursive ${USER} ${WORKDIR}

RUN apt update && apt upgrade -y

COPY --chown=${USER} requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install --requirement requirements.txt
COPY . .

COPY --chown=${USER} ./_main_.py _main_.py
COPY --chown=${USER} ./Makefile Makefile
COPY --chown=${USER} ./db_data db_data



USER ${USER}


#ENTRYPOINT ["uvicorn", "main_pet_project:app", "--host", "0.0.0.0", "--port", "8000"]

#CMD ["granian", "app:app", "--bind", "0.0.0.0:8000"]
#CMD ["granian", "app:app", "--bind", "0.0.0.0:5000"]
CMD ["granian", "app.application:build_app", "--factory", "--bind", "0.0.0.0:8000"]