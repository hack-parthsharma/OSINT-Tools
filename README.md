## Intelligence Gathering Tools

### This repo has 3 parts:
- Find Emails.
- Find Users.
- Extract Metadata.

### Find Emails
you can use this tool with the hunter API to download company's emails.

```
pip install pyhunter
python EmailsFinder.py microsoft.com {API_Key}
```

### Find Users
you can use this tool to find the company's social medial accounts.

```
pip install google
python SocialFinder.py microsoft.com 50
```

### Extract Metadata
you can use this tool to search for files related to the company, and then you can use tool like exiftool to extract the metadata from this files.

```
pip install google
python MetaAnalysis.py example.com pdf,doc,dot,docx,odp,ods,xls,xlt,xlsx,ppt,pot,pptx 20
```
