# Common Errors

These are some common errors that I came across in the testing process that you may encounter too.

### 1. Key Error

- Looks like `KeyError: 'results'`
- **Problem:** This error could be caused for a lot of reasons, but it usually resulted from the page ID not being integrated properly.
- **Solution:** Ensure that the page you’re trying to extract images from is connected with the integration you made. Go to the top right of your Notion page, click the three dots •••, and scroll down to “Connections”. Find your integration name in the dropdown, and click “Confirm”. Refer to step 5 of the README for more information.

### 2. Authorization Error

- Will look the same as key error, unless you print out JSON data, which then it will look like `{'object': 'error', 'status': 401, 'code': 'unauthorized', 'message': 'API token is invalid.', 'request_id'...}`
- **Description**: This error occurs when there are issues with the authorization process, typically due to incorrect or insufficient authentication credentials.
- **Solution**: Double-check the API token and ensure that it is correct and has the necessary permissions to access the Notion API. Verify that the token is properly formatted. Additionally, ensure that the API token has not expired and that it has the appropriate scope to perform the required actions. If necessary, regenerate the API token run the code with the new token.

### 3. Connection Error

- **Looks like `HTTPSConnectionPool(host='api.notion.com', port=443): Max retries exceeded with url`:**
- **Problem:** This error suggests a problem with establishing a connection to the Notion API. It might be due to network issues or problems with the API endpoint.
- **Solution**: Check your internet connection and ensure that the Notion API endpoint is accessible. You may also want to verify the API token and endpoint URL you entered into the prompt.
