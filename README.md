これはボウリングのスコアを記録するアプリです

開発サーバは以下で起動できます。
```bash
 export FLASK_APP=src.app
 flask run --debug
```

Docker起動方法
```bash
docker build -t test .
docker run -p 5000:5000  test
```