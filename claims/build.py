"""Builds index.html (served by GitHub Pages) from claims/template.html and claims/verdicts.json.
Run from the repo root after claims/verify.py. Fonts and colour tokens come from claims/base_style.html (shared with the Rate Call Tracker)."""
import json
base = open("claims/base_style.html").read()
head = base[:base.index("</style>") + len("</style>")].replace("<title>Rate Call Tracker</title>", "<title>Fed Claim Catalog</title>")
body = open("claims/template.html").read().replace("/*VERDICTS*/", json.dumps(json.load(open("claims/verdicts.json"))))
extra_style, body = body.split("</style>", 1)
open("index.html", "w").write('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
    + head + "\n" + extra_style + "</style>\n</head>\n<body>" + body + "\n</body>\n</html>\n")
print("built index.html")
