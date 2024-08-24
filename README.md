# Profanity Checker Using Amazon Bedrock

## Overview

This repository contains a Streamlit application designed to detect and remove profane words from sentences. The application leverages Amazon Bedrock ( Claude 3 Sonnet model ) to provide accurate and efficient profanity filtering. Built with a serverless stack in mind, this solution can be deployed on AWS Lambda and API Gateway, making it scalable and easy to integrate with other applications.

## Use Cases

- **Content Moderation**: Automatically filter out profane words from user-generated content on websites, forums, and social media platforms.
- **Text Sanitization**: Ensure that text data used in applications or communications adheres to acceptable language standards by removing offensive terms.
- **Custom Filtering**: Adapt the profanity checker to specific needs by customizing the list of profane words or the sensitivity of the detection.

## Services Used

- **Streamlit**: A Python framework for building interactive web applications, used to create the user interface of the profanity checker.
- **Amazon Bedrock**: Provides foundational models and tools for natural language processing, utilized for the profanity detection capabilities.
- **AWS Lambda**: Serverless compute service that can be used to run the application backend without provisioning servers.
- **Amazon API Gateway**: Facilitates the creation and management of APIs for the profanity checker, enabling integration with other applications and services.

