# bernie-eats
文化祭用お好み焼き注文管理システム(Django版)

## 仮想環境の構築
```bash
$ export PIPENV_VENV_IN_PROJECT=true
$ pipenv --python 3.7
```

## インストールパッケージ
```bash
$ pipenv install django
```

## Djangoプロジェクトの作成
```bash
$ django-admin startproject config .
```

## Djangoアプリケーションの作成
```bash
$ django-admin startapp account
```