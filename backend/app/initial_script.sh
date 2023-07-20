#!/bin/bash

# Create table
alembic upgrade head
alembic revision --autogenerate
alembic upgrade head

# DB 체크
python3 app/initial_data.py
python3 app/backend_pre_start.py

# DB 데이터 생성
python3 input/exchange.py
python3 input/order_type.py
