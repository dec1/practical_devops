make sure aws (cli or sdk) is [configured](../../../../../aws/config/profile/profile.md)

- `docker-compose up -d`

- `docker logs -f localstack`

- `docker logs -f dynamodb-admin`

- `docker-compose down`

- interact with localstack
    - [s3](../../../../../aws/infrastructure/s3.md)
    - [dynamo](../../../../../aws/infrastructure/dynamo.md)