## create todo

```
curl --location --request DELETE 'http://127.0.0.1:8000/api/todos/1' \
--header 'Content-Type: application/json' \
--data '{
    "title":"hello",
    "discription":"sample description",
    "is_completed": true
}'
```