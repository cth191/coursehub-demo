- Migration 001: enrollment_events.
- Demo class: RACE-01, capacity = 1.
- POST /enrollments: lock class_sections bang FOR UPDATE.
- Concurrency test: 1 request 201, 1 request 409.
- Performance data: 100000 rows, dataset=performance.
- Index: idx_enrollment_events_dataset_student_time.
- Ghi lai scan type va Execution Time truoc/sau o day.

QUERY PLAN
Limit  (cost=2915.45..2915.58 rows=50 width=39) (actual time=4.804..4.809 rows=50.00 loops=1)
  Buffers: shared hit=1137
  ->  Sort  (cost=2915.45..2917.59 rows=855 width=39) (actual time=4.803..4.805 rows=50.00 loops=1)
        Sort Key: occurred_at DESC
        Sort Method: top-N heapsort  Memory: 31kB
        Buffers: shared hit=1137
        ->  Seq Scan on enrollment_events  (cost=0.00..2887.05 rows=855 width=39) (actual time=0.032..4.704 rows=820.00 loops=1)
              Filter: ((occurred_at >= '2025-12-20 00:00:00'::timestamp without time zone) AND ((dataset)::text = 'performance'::text) AND ((student_id)::text = '22000001'::text))
              Rows Removed by Filter: 99183
              Buffers: shared hit=1137
Planning:
  Buffers: shared hit=52 read=1
Planning Time: 1.239 ms
Execution Time: 4.826 ms