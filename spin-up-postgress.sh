#!/bin/bash


# docker pull lilearningproject/big-star-postgres:latest

# docker run --name big-star-container-postgres -d -p 5432:5432 lilearningproject/big-star-postgres:latest

# docker exec -it big-star-container-postgres psql -U postgres -c "CREATE DATABASE bigstar;"

# docker exec -it big-star-container-postgres psql -U postgres -d big-star-db -c "\dt"
# docker exec -it big-star-container-postgres psql -U postgres -d big-star-db -c "ALTER SYSTEM SET wal_level = logical;"
# docker exec -it big-star-container-postgres psql -U postgres -d big-star-db -c "show wal_level"
# docker exec -it big-star-container-postgres psql -U postgres -d big-star-db -c "select * from orders;"
# docker exec -it big-star-container-postgres psql -U postgres -d big-star-db -c "select count(*) from orders;"

# docker exec -it big-star-container-postgres psql -U postgres -d big-star-db -c "ALTER TABLE customers REPLICA IDENTITY DEFAULT;"
# docker exec -it big-star-container-postgres psql -U postgres -d big-star-db -c "ALTER TABLE order_items REPLICA IDENTITY DEFAULT;"
# docker exec -it big-star-container-postgres psql -U postgres -d big-star-db -c "ALTER TABLE orders REPLICA IDENTITY DEFAULT;"
# docker exec -it big-star-container-postgres psql -U postgres -d big-star-db -c "ALTER TABLE products REPLICA IDENTITY DEFAULT;"

# docker exec -it big-star-container-postgres psql -U postgres -d big-star-db -c "select pg_create_logical_replication_slot('airbyte_slot', 'pgoutput');"
# docker exec -it big-star-container-postgres psql -U postgres -d big-star-db -c "CREATE PUBLICATION airbyte_publication FOR TABLE customers, order_items, orders, products;"



# docker exec -it big-star-container-postgres psql -U postgres -d big-star-db -c "insert into orders (order_id, customer_id, status, order_purchased_at, order_approved_at, order_delivered_at) values (10990, 100, 'delivered', '2022-01-01', '2022-01-01', '2022-01-01');"