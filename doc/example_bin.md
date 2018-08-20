# Example with binary file
Generate a dummy file
```commandline
echo "{\"title\": \"Hello world\"}" | gzip -c | base64 > example
```
then decode it
```commandline
phorcys_decode.py -b example
```
and get the result
```json
{
  "children": [
    {
      "children": [
        {
          "children": [
            {
              "children": [],
              "headers": [
                {
                  "length": 11
                }
              ],
              "human_readable": true,
              "id": "4a8e27fe-5824-4379-92b7-af057cd837b9",
              "length": 11,
              "matching_rules": [],
              "name": "text",
              "text": [
                "Hello world"
              ]
            }
          ],
          "headers": [],
          "human_readable": true,
          "id": "436b71fc-0499-45f1-b49a-2db32cc14e88",
          "length": 29,
          "matching_rules": [],
          "name": "json",
          "text": [
            "{",
            "  \"data\": {",
            "    \"title\": \"Hello world\"",
            "  }",
            "}"
          ]
        }
      ],
      "headers": [
        {
          "length": 25
        }
      ],
      "human_readable": false,
      "id": "f1448d1c-3e47-421e-92c9-0d0dbbdc4e1b",
      "length": 126,
      "matching_rules": [],
      "name": "gzip",
      "text": [
        "0000000000 7b 22 74 69 74 6c 65 22 3a 20 22 48 65 6c 6c 6f {\"title\": \"Hello",
        "0000000010 20 77 6f 72 6c 64 22 7d 0a                       world\"}."
      ]
    }
  ],
  "headers": [
    {
      "length": 45
    }
  ],
  "human_readable": false,
  "id": "ad96afa3-243e-4054-82ec-4105f948da69",
  "length": 65,
  "matching_rules": [],
  "name": "base64",
  "text": [
    "b'H4sIAFeqS1sAA6tWKsksyUlVslJQ8kjNyclXKM8vyklRquUCACkrZhkZAAAA\\n",
    "'"
  ]
}
```