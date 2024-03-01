import subprocess

# Define a global variable
counter = 0

# Define a function to increment the counter by one
def increment_counter():
    global counter
    counter += 1
    return counter

# Function to perform the git operations
def perform_git_operations(task_number):
    subprocess.run(["git", "add", "."])
    commit_message = f"task {task_number}"
    subprocess.run(["git", "commit", "-m", commit_message])
    subprocess.run(["git", "push"])

# Example command
def example_command():
    global counter
    print("This is an example command.")
    counter_value = increment_counter()
    perform_git_operations(counter_value)

# Run the example command and perform git operations
example_command()