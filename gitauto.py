import subprocess

# Function to read and update the counter from a file
def get_and_update_counter():
    try:
        with open('counter.txt', 'r') as file:
            counter = int(file.read())
    except FileNotFoundError:
        # If the file doesn't exist, start with counter value 0
        counter = 0

    # Increment the counter
    counter += 1

    # Save the updated counter to the file
    with open('counter.txt', 'w') as file:
        file.write(str(counter))

    return counter

# Function to perform the git operations
def perform_git_operations(task_number):
    subprocess.run(["git", "add", "."])
    commit_message = f"task {task_number}"
    subprocess.run(["git", "commit", "-m", commit_message])
    subprocess.run(["git", "push"])

# Example command
def example_command():
    print("This is an example command.")
    counter_value = get_and_update_counter()
    print("Counter:", counter_value)
    perform_git_operations(counter_value)

# Run the example command and perform git operations
example_command()