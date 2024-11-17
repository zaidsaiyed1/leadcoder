echo "Buid start"
#!/ env bash
pip install -r requirements.txt
python3.11 manage.py collectstatic --noinput --clear
python manage.py migrate

echo "Buid stop"