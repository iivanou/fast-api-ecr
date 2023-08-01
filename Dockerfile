FROM public.ecr.aws/lambda/python:3.10
COPY ./app ${LAMBDA_TASK_ROOT}
COPY requirements.txt .
COPY .env ${LAMBDA_TASK_ROOT}
RUN --mount=type=cache,target=/root/.cache/pip pip3 install -r requirements.txt -t "${LAMBDA_TASK_ROOT}"
CMD [ "main.handler" ]