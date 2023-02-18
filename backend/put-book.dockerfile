FROM public.ecr.aws/lambda/python:3.9
COPY ./models ${LAMBDA_TASK_ROOT}/models/
COPY put-book.py ${LAMBDA_TASK_ROOT}
COPY requirements.txt .
RUN pip install -r requirements.txt --target ${LAMBDA_TASK_ROOT}
CMD [ "put-book.lambda_handler" ]