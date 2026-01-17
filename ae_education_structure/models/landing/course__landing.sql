{{ config(
    enabled=true 
) }}


select *
from {{ ref('course_seed') }}