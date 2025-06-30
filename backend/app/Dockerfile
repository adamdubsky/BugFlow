FROM python:3.12-slim

# set working directory
WORKDIR /app

# install Poetry and dependencies
COPY pyproject.toml poetry.lock* ./
RUN pip install poetry \
  && poetry config virtualenvs.create false \
  && poetry install --no-dev

# copy code
COPY . .

# run app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]