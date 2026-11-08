BEGIN;

-- 1. Xoa cot note khoi bang enrollment_events
ALTER TABLE enrollment_events
DROP COLUMN note;

-- 2. Xoa thong tin migration 002
DELETE FROM schema_migrations
WHERE version = '002';

COMMIT;
