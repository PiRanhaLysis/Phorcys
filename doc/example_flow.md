# Example with a `.flow` file
To analyze your file, give it to *Phorcys*. You can also specify a Yara rule file with the `-y` option
```commandline
phorcys_decode.py -f run.flow
```
and get the result. The generated JSON is largely inspired by the [HAR format](https://en.wikipedia.org/wiki/.har).
```json
[
{
    "startedDateTime": "2018-02-08T20:44:35.533261+00:00",
    "time": 405,
    "id": "252132dd-dcb1-41c0-930d-db44658ad73e",
    "request": {
      "method": "GET",
      "url": "https://app-measurement.com/config/app/1%3A150559058554%3Aandroid%3A5dbd678b1d742f47?app_instance_id=01914e98bb770111efaed194dbe437ef&platform=android&gmp_version=11975",
      "httpVersion": "HTTP/1.1",
      "host": "app-measurement.com",
      "cookies": [],
      "headers": [
        {
          "name": "User-Agent",
          "value": "Dalvik/1.6.0 (Linux; U; Android 4.4.2; V7A Build/KOT49H)"
        },
        {
          "name": "Host",
          "value": "app-measurement.com"
        },
        {
          "name": "Connection",
          "value": "Keep-Alive"
        },
        {
          "name": "Accept-Encoding",
          "value": "gzip"
        }
      ],
      "queryString": [
        {
          "name": "app_instance_id",
          "value": "01914e98bb770111efaed194dbe437ef"
        },
        {
          "name": "platform",
          "value": "android"
        },
        {
          "name": "gmp_version",
          "value": "11975"
        }
      ],
      "headersSize": 183,
      "bodySize": 0,
      "content": ""
    },
    "response": {
      "status": 200,
      "statusText": "OK",
      "httpVersion": "HTTP/1.1",
      "cookies": [],
      "headers": [
        {
          "name": "Accept-Ranges",
          "value": "bytes"
        },
        {
          "name": "Vary",
          "value": "Accept-Encoding"
        },
        {
          "name": "Content-Encoding",
          "value": "gzip"
        },
        {
          "name": "Content-Type",
          "value": "application/x-protobuf"
        },
        {
          "name": "Access-Control-Allow-Origin",
          "value": "*"
        },
        {
          "name": "Content-Length",
          "value": "72"
        },
        {
          "name": "Date",
          "value": "Thu, 08 Feb 2018 20:44:35 GMT"
        }
      ],
      "content": "CMDhjqP+29UCEicxOjE1MDU1OTA1ODU1NDphbmRyb2lkOjVkYmQ2NzhiMWQ3NDJmNDcYAQ==",
      "redirectURL": "",
      "headersSize": 669,
      "bodySize": 72
    },
    "cache": {},
    "timings": {
      "send": 10,
      "receive": 8,
      "wait": 225,
      "connect": 73,
      "ssl": 89
    },
    "inspection": {
      "url": {
        "layers": {
          "id": "f06e0a0c-07ec-41f3-8988-5de79bcfbdc1",
          "name": "urlencoded",
          "human_readable": true,
          "matching_rules": [],
          "headers": [],
          "children": [
            {
              "id": "3c2a9a00-195b-4010-bac5-92d74a78bb7e",
              "name": "text",
              "human_readable": true,
              "matching_rules": [],
              "headers": [
                {
                  "length": 24
                }
              ],
              "children": [],
              "length": 32,
              "text": [
                "01914e98bb770111efaed194dbe437ef"
              ]
            },
            {
              "id": "1b9e73d6-af82-4d29-a85a-21b82c97b0ea",
              "name": "platform",
              "human_readable": true,
              "matching_rules": [],
              "headers": [],
              "children": [],
              "length": 7,
              "text": [
                "android"
              ]
            },
            {
              "id": "1c62d84d-5a66-41e0-b13b-ff73518b399b",
              "name": "gmp_version",
              "human_readable": true,
              "matching_rules": [],
              "headers": [],
              "children": [],
              "length": 5,
              "text": [
                "11975"
              ]
            }
          ],
          "length": 168,
          "text": [
            "https://app-measurement.com/config/app/1:150559058554:android:5dbd678b1d742f47?app_instance_id=01914e98bb770111efaed194dbe437ef",
            "platform=android",
            "gmp_version=11975"
          ]
        },
        "clues": 0
      },
      "response": {
        "layers": {
          "id": "d5e0eb1b-1686-47ac-aac2-f9e34a7b2759",
          "name": "protobuf",
          "human_readable": true,
          "matching_rules": [],
          "headers": [],
          "children": [
            {
              "id": "272bf916-e432-482c-bb1a-ebbdc9fa8a78",
              "name": "text",
              "human_readable": true,
              "matching_rules": [],
              "headers": [
                {
                  "length": 19
                }
              ],
              "children": [],
              "length": 19,
              "text": [
                ";1=1502894492987584"
              ]
            },
            {
              "id": "5ea3de7a-6412-4812-a8a7-64d9cb5282ab",
              "name": "text",
              "human_readable": true,
              "matching_rules": [],
              "headers": [
                {
                  "length": 44
                }
              ],
              "children": [],
              "length": 44,
              "text": [
                ";2=\"1:150559058554:android:5dbd678b1d742f47\""
              ]
            },
            {
              "id": "b157d876-6eb4-419d-b7c2-efd035285f3a",
              "name": "text",
              "human_readable": true,
              "matching_rules": [],
              "headers": [
                {
                  "length": 4
                }
              ],
              "children": [],
              "length": 4,
              "text": [
                ";3=1"
              ]
            }
          ],
          "length": 70,
          "text": [
            "1: 1502894492987584",
            "2: \"1:150559058554:android:5dbd678b1d742f47\"",
            "3: 1"
          ]
        },
        "clues": 0
      },
      "rules": {},
      "clues": 0,
      "tags": []
    }
  }
]
```