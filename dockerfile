from python:3.7

run pip install virtualenv
ENV VIRTUAL_ENV = /venv 
run virtualenv venv -p python3 

WORKDIR .
ADD . .

run pip install -r requirements.txt 

COPY . /app

ENV PORT 8501

CMD streamlit run app.py 