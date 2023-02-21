FROM public.ecr.aws/lambda/python:3.9
COPY ./models ${LAMBDA_TASK_ROOT}/models/
COPY .env ${LAMBDA_TASK_ROOT}
COPY post-book.py ${LAMBDA_TASK_ROOT}
COPY requirements.txt .
RUN pip install -r requirements.txt --target ${LAMBDA_TASK_ROOT}
CMD [ "post-book.lambda_handler" ]