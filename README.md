## Setup

```
git clone {this repo}
cd {this repo}
mv .env.example .env
docker compose up
```

### Note
- Docker will create admin user with username:password = admin:admin (see photos/management/commands/init_admin.py for the reference)
- To make it simple: filtering by geo implemented without postgis or similar libraries (see photos/utils)

Explore http://localhost:8000/api/swagger/


