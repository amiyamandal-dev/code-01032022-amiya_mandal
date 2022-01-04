FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
RUN pip install uvicorn[standard]
EXPOSE 8000
RUN pytest
CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8000"]
