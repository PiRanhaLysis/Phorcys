# Example with Yara rules applied on binary file
Generate a dummy file
```commandline
echo "{\"title\": \"Hello world\"}" | gzip -c | base64 > example
```
write your rules
```
# rules.yar
rule r: dummy_rule
{
    strings:
        $my_text_string = "hello world" nocase
    condition:
        $my_text_string
}
```
then run *Phorcys*
```commandline
phorcys_decode.py -b example -y rules.yar
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
              "id": "352631c2-3517-4d8f-9a50-54d809fbde56",
              "length": 11,
              "matching_rules": [
                {
                  "count": 1,
                  "rule": "r",
                  "tags": [
                    "dummy_rule"
                  ]
                }
              ],
              "name": "text",
              "text": [
                "Hello world"
              ]
            }
          ],
          "headers": [],
          "human_readable": true,
          "id": "50b42506-7679-4b89-8a2a-553e22b2a9b5",
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
      "id": "9d3a96e7-7db3-4034-9345-ff2f659465f2",
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
  "id": "482c3bab-860c-4c16-bdcb-6cc7db4efa4f",
  "length": 65,
  "matching_rules": [],
  "name": "base64",
  "text": [
    "b'H4sIAFeqS1sAA6tWKsksyUlVslJQ8kjNyclXKM8vyklRquUCACkrZhkZAAAA\\n",
    "'"
  ]
}
```