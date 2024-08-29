# AzureImageProcessingFunction
A serverless function using Azure Functions to automatically resize images uploaded to Azure Blob Storage, showcasing cloud integration and image processing capabilities.

## Prerequisites
- **Python 3.9 or later** also need PIL or Pillow
- **Azure CLI**: To manage Azure resources from the command line.
- **Azure Functions Core Tools**: To develop and test Azure Functions locally.
- **Visual Studio Code**: (or any IDE) with the Azure Functions extension.
- **Azure Storage Explorer**: For local environment testing.
- **Git**: For version control.

## Setup Instructions
- Create an Azure account and install Azure CLI for command prompt bash commands.
- Create Azure Resource Group, Storage account, and input/output Blob containers with the same Storage Account Name via command prompt.
- Create Azure Function App through command prompt.
- Install Python, Azure Functions Core Tools, and Pillow (Python Package).
- Create new function project through VS code using Blob storage trigger.
- Update image processing logic in python program.
- Specify bindings in function.json
- Update local.settings.json AzureWebJobsStorage depending on if you are testing locally or through Azure with your storage connection string.
- Deploy the function to Azure and test by uploading image to your input container and making sure it is properly processed and output to your output container.
- Monitor the function with the Azure Portal Logs to evaluate any execution errors.

## Troubleshooting
- Resolved Python version compatibility issues by adjusting the Azure Function's runtime environment.
- Overcame dependency management challenges by correctly configuring the requirements.txt file and ensuring all necessary libraries, like Pillow, were installed.
- Addressed Git authentication errors by setting up Git with the correct user credentials and configuring the remote repository properly.
- Debugged Azure Function deployment issues by carefully managing environment variables and ensuring correct Azure Storage connection strings.

## Future Applications
While the current project focuses on basic image resizing, future enhancements could include:
- **Advanced Image Processing**: Add filters, format conversion, and image enhancement features.
- **Machine Learning Integration**: Implement image classification, face detection, or object recognition.
- **Dynamic User Input**: Allow users to specify image processing parameters via HTTP requests.
- **Scalability and Security**: Introduce queueing for high-volume processing, RBAC for security, and global deployment for high availability.
