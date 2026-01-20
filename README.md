# dez-homework-1
Homework 1: Docker, SQL and Terraform for Data Engineering Zoomcamp 2026


## Question 1. Understanding Docker images

```bash
docker pull python:3.13

docker run -it --rm python:3.13 bash

python -m pip -V # 25.3
```


## Question 3. Counting short trips

```sql
select count(*) 
from public.green_taxi_data
where lpep_pickup_datetime >= '2025-11-01' and lpep_pickup_datetime < '2025-12-01'
and trip_distance <= 1;
-- 8007
```


## Question 4. Longest trip for each day

```sql
select lpep_pickup_datetime::date, max(trip_distance)
from public.green_taxi_data
where trip_distance < 100
group by lpep_pickup_datetime::date
order by max(trip_distance) desc;
-- 2025-11-14 - 88.03
```


## Question 5. Biggest pickup zone

```sql
select z."Zone", sum(t.total_amount)
from public.green_taxi_data t
join public.zones z on z."LocationID" = t."PULocationID"
where lpep_pickup_datetime::date = '2025-11-18'
group by z."Zone"
order by sum(t.total_amount) desc;
-- East Harlem North - 9281.919999999991
```


## Question 6. Largest tip

```sql
select doz."Zone", max(t.tip_amount)
from public.green_taxi_data t
join public.zones puz on puz."LocationID" = t."PULocationID"
join public.zones doz on doz."LocationID" = t."DOLocationID"
where puz."Zone" = 'East Harlem North' 
	and EXTRACT(YEAR FROM t.lpep_pickup_datetime) = 2025
	and EXTRACT(MONTH FROM t.lpep_pickup_datetime) = 11
group by doz."Zone"
order by max(t.tip_amount) desc;
-- Yorkville West - 81.89
```


## Question 7. Terraform Workflow

```bash
terraform init

terraform plan

terraform apply

terraform destroy
```


