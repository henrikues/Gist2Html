# Gist2HTML

One day I was curious if I could make a simple website to work right off a gist and I can. 

This project was built using azure functions simply because I already had everythign installed for it. 

## Usage
When you run the app in vs code, you'll get a url generated based on your preferences. Mine is "http://localhost:7071/api/" for example. 

Using that URL, call the gist2html endpoint and pass your gist ID to it as the "gistId" querry string param. Like this: 

```xml
<Your Function URL>/gist2html?gistId=<Your Gist ID>
```

Like this:

```css
http://localhost:7071/api/gist2html?gistId=9a32625e802957edcba5bb67b70ec7cc
```
