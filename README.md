# aviary-tools
Utilities for working with Aviary

# Set up

1. Clone this repository
   ```
   git clone https://github.com/awoods/aviary-tools.git
   cd aviary-tools
   ```
1. Install dependencies
   ```
   pip install -r requirements.txt
   ```
1. Set up Aviary credentials
   - Copy `.creds-example` to `.creds` and populate with Aviary username and password
1. Generate access token and `.env`
   ```
   ./auth.sh
   ```
1. Log into the Aviary web console and create an empty media-file resource
   - Find the "Aviary Resource ID" for the new media-file resource in the list of resources for the relevant Aviary Collection
1. Upload an A/V file that is larger than 100MB
   ```
   python upload-media-chunked.py -f <local-av-filename> -r <aviary-resource-id>
   # For example:
   # clear;date; time python upload-media-chunked.py -f keystone.mp4 -r 84607
   ```

