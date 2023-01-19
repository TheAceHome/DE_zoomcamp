
# cd  data-engineering-zoomcamp/cfg/postgres_cfg/
# docker build -t postgres:custom .
# docker run -it \
#   -e POSTGRES_USER="root" \
#   -e POSTGRES_PASSWORD="root" \
#   -e POSTGRES_DB="ny_taxi" \
#   -v C:/Users/U_M1E6D/PycharmProjects/data-engineering-zoomcamp/db/ny_taxi_postgres_data:/var/lib/postgresql/data \
#   -p 5432:5432 \
#   postgres:custom

# cd  data-engineering-zoomcamp/cfg/pyt_jup_cfg/
# docker build -t pyt_jup:custom .
# docker run -it pyt_jup:custom






