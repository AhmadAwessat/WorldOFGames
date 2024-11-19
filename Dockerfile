FROM python:3.12

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Set the working directory inside the container
WORKDIR /WorldofGames

# Copy the rest of your application code into the container
COPY . /WorldofGames

# Run the MainScores.py script when the container starts
CMD ["python", "MainScores.py"]
