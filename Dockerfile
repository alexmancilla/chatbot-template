FROM public.ecr.aws/lambda/python:3.12

# Copy requierements file
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install Python dependencies
RUN pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy files
COPY . ${LAMBDA_TASK_ROOT}

# Set the entrypoint
CMD [ "run.main" ]