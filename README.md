# speech-synthesizer
Give me English text. You get English speeches in various accents.

## Authentication

speech-synthesizer requires you to have authentication setup. Refer to the
[Authentication Getting Started Guide](https://cloud.google.com/docs/authentication/getting-started) for instructions on setting up
credentials for applications.

credentials.json


## Deploying speech-synthesizer

1. Download the [Google App Engine Python SDK](https://cloud.google.com/appengine/downloads) for your platform.
2. Use `gcloud` to deploy the sample, you will need to specify your Project ID and a version number:

        gcloud app deploy --project your-app-id -v your-version

3. Visit `https://[your-app-id].appspot.com` to view your application.

## Additional resources

For more information on App Engine:

> https://cloud.google.com/appengine

For more information on Python on App Engine:

> https://cloud.google.com/appengine/docs/python