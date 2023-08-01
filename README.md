
# Selenium LinkedIn Automation

This project uses the Selenium WebDriver for Python to automate the login and job application process on LinkedIn.

## Installation

To get started, you need to install selenium and python-dotenv. You can do this using pip:

```bash
pip install selenium python-dotenv
```

Also, you need to download the corresponding ChromeDriver for your version of Chrome from [here](https://sites.google.com/chromium.org/driver/) and place it in your system PATH.

# Setup

1. You will need to create a .env file in your project directory and add your LinkedIn username and password as environment variables:

```
LINKEDIN_EMAIL = your_email@example.com
LINKEDIN_PASSWORD = your_password
```

2. Replace 'URL' in the script with the URL of the job you want to apply to.

## Usage

The script automates the following:

1. Open LinkedIn and click the Sign in button.
2. Fill in the email and password fields and click on the submit button.
3. Click on the job's Apply button.

To run the script:

```python linkedin_auto_apply.py```

The script will output some information in the console, indicating the progress of the automation.

## Note

The script is sensitive to changes in LinkedIn's page structure. If LinkedIn updates their website, the script may stop working. 

## License

# This project is licensed under the terms of the MIT license.
