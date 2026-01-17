{{ config(
    enabled=true
) }}

select *
from {{ ref('course__core') }}