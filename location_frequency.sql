drop table if exists pickups_with_location;
create table pickups_with_location as (

    select
        t.pickup_datetime,
        t.passenger_count, 
        z1.borough as pickup_location,
        z2.borough as dropoff_location
    from yellow_tripdata_sample_2019_01 t
    left join taxi_zone_lookup z1 on t.pickup_location_id = z1.location_id
    left join taxi_zone_lookup z2 on t.dropoff_location_id = z2.location_id

);

drop table if exists location_frequency;

create table location_frequency as (
    select
        pickup_location,
        dropoff_location,
        count(*) as num_rides
    from pickups_with_location
    group by pickup_location, dropoff_location
    order by pickup_location, dropoff_location
);
