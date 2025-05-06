import logging
import time

# Configure logging to output to the console
logger = logging.getLogger("monitor_agent")
logger.setLevel(logging.INFO)

# Create a console handler with a specific format
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Log the start of the application
logger.info("Monitor Agent Application Started.")

# Provide a default name instead of waiting for user input
name = "AICICD"
logger.info(f"Default user name set to: {name}")

# Print a message to the console to simulate application output
print(f"Hello, {name}!")
logger.info("Greeted the user successfully.")

# Keep the application running a bit longer so logs can be captured
logger.info("Application will exit in 5 seconds...")
time.sleep(5)
logger.info("Monitor Agent Application Completed. Exiting now.")
