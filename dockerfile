from python:3.7
RUN pip install --upgrade pip

run pip install virtualenv
ENV VIRTUAL_ENV = /venv 
run virtualenv venv 

WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt

COPY . /app

ENV PORT 8501

CMD streamlit run app.py 