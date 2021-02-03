# Flask

```bash
pip install -r requirements.txt
python hello.py

curl -XGET 'http://localhost:8080/get'
{
  "first_name": "taiyo",
  "last_name": "tamura"
}

curl -XPOST http://localhost:8080/post \
     -H "Content-type:application/json" \
     -d '{"first_name": "tarou"}'
{
  "first_name": "tarou",
  "last_name": "tamura"
}
```